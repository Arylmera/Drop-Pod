"""Read-only probe of a machine's OpenCode setup, for planning OpenCode support in Administratum.

Prints (and saves to opencode-probe.json in the current folder) the *shape* of OpenCode's state:
version, database schema, field names of recent messages and parts, running opencode processes and
the ports they listen on, what the local HTTP server answers to a few GET requests, and which
companion tools are on PATH. It never prints message text, tool input or output, file contents or
credentials: values are reduced to their type, except a short list of enum-like fields.

Stdlib only. Opens the database read-only, sends only GET requests to 127.0.0.1, ends on its own.
Run it once while an OpenCode session is waiting on a permission prompt, then once while idle.
"""
import json, os, platform, re, shutil, sqlite3, subprocess, sys, urllib.request
from pathlib import Path

for s in (sys.stdout, sys.stderr):
    try:
        s.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOME = str(Path.home())
# Values kept verbatim: small enums that say how state is encoded, never user content.
KEEP = {"role", "type", "status", "finish", "tool", "agent", "mode", "providerID", "modelID", "delivery", "action"}
SKIP_TABLES = {"account", "account_state", "control_account", "credential", "session_share"}  # credentials: never opened


def redact(text):
    """Hide the home folder and user name in paths and command lines."""
    if not isinstance(text, str):
        return text
    user = os.path.basename(HOME)
    for h in {HOME, HOME.replace("\\", "/"), HOME.replace("\\", "\\\\")}:
        text = text.replace(h, "~")
    return re.sub(re.escape(user), "<user>", text, flags=re.I) if user else text


def shape(v, key=None, depth=0):
    """A value reduced to its structure: dicts keep their keys, lists their first item, scalars their type."""
    if isinstance(v, dict):
        return {k: shape(x, k, depth + 1) for k, x in v.items()} if depth < 6 else "dict"
    if isinstance(v, list):
        return [shape(v[0], key, depth + 1), f"len={len(v)}"] if v else []
    if key in KEEP and isinstance(v, (str, int)):
        return v
    return type(v).__name__


def run(cmd, timeout=10):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, encoding="utf-8", errors="replace")
        return r.stdout.strip() or r.stderr.strip()
    except Exception as e:
        return f"error: {e.__class__.__name__}: {e}"


def data_dir():
    base = os.environ.get("XDG_DATA_HOME") or os.path.join(HOME, ".local", "share")
    return Path(base) / "opencode"


def probe_db(out):
    d = data_dir()
    db = d / "opencode.db"
    out["data_dir"] = redact(str(d))
    out["data_dir_entries"] = sorted(p.name for p in d.iterdir()) if d.is_dir() else None
    if not db.is_file():
        out["db"] = "absent (older versions kept JSON files under storage/)"
        storage = d / "storage"
        if storage.is_dir():
            out["storage_dirs"] = sorted(p.name for p in storage.iterdir())
        return
    out["db_size_mb"] = round(db.stat().st_size / 1e6, 1)
    c = sqlite3.connect(f"file:{db.as_posix()}?mode=ro", uri=True, timeout=5)
    tables = [r[0] for r in c.execute("select name from sqlite_master where type='table'")]
    out["tables"] = {t: [r[1] for r in c.execute(f'pragma table_info("{t}")')] for t in tables if t not in SKIP_TABLES}
    out["indexes"] = [r[0] for r in c.execute("select name from sqlite_master where type='index' and name not like 'sqlite_%'")]
    out["counts"] = {t: c.execute(f'select count(*) from "{t}"').fetchone()[0] for t in ("session", "message", "part", "permission", "todo") if t in tables}
    out["migrations_last"] = c.execute("select id from migration order by time_completed desc limit 3").fetchall() if "migration" in tables else None

    cols = out["tables"].get("session", [])
    sessions = []
    for r in c.execute("select * from session order by time_updated desc limit 3"):
        row = dict(zip(cols, r))
        sid = row["id"]
        info = {k: shape(v, k) for k, v in row.items()}
        info["has_parent"] = row.get("parent_id") is not None
        info["children"] = c.execute("select count(*) from session where parent_id=?", (sid,)).fetchone()[0]
        msgs = c.execute("select data, time_created from message where session_id=? order by time_created desc limit 2", (sid,)).fetchall()
        info["last_messages"] = [shape(json.loads(m)) for m, _ in msgs]
        parts = c.execute("select data from part where session_id=? order by time_created desc limit 6", (sid,)).fetchall()
        info["last_parts"] = [shape(json.loads(p)) for (p,) in parts]
        info["tool_status_counts"] = c.execute(
            "select json_extract(data,'$.tool'), json_extract(data,'$.state.status'), count(*) from part "
            "where session_id=? and json_extract(data,'$.type')='tool' group by 1,2", (sid,)).fetchall()
        if "event" in tables:  # filtered on the indexed aggregate_id: the event table can be huge
            info["last_event_types"] = [t for (t,) in c.execute("select type from event where aggregate_id=? order by seq desc limit 8", (sid,))]
        if "session_input" in tables:
            info["session_input_rows"] = c.execute("select count(*) from session_input where session_id=?", (sid,)).fetchone()[0]
        sessions.append(info)
    out["recent_sessions"] = sessions
    if "permission" in tables:
        out["permission_rows_shape"] = [shape(dict(zip(out["tables"]["permission"], r))) for r in c.execute("select * from permission limit 2")]
    c.close()


def processes():
    """Running opencode processes with their listening ports."""
    if platform.system() == "Windows":
        ps = (
            "$p = Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'opencode' };"
            "$p | ForEach-Object { [pscustomobject]@{ pid=$_.ProcessId; ppid=$_.ParentProcessId; name=$_.Name; cmd=$_.CommandLine;"
            " ports=@(Get-NetTCPConnection -State Listen -OwningProcess $_.ProcessId -ErrorAction SilentlyContinue | ForEach-Object { \"$($_.LocalAddress):$($_.LocalPort)\" }) } }"
            " | ConvertTo-Json -Depth 3"
        )
        raw = run(["powershell", "-NoProfile", "-NonInteractive", "-Command", ps], timeout=30)
        try:
            procs = json.loads(raw) if raw else []
        except json.JSONDecodeError:
            return [{"error": redact(raw[:500])}]
        procs = procs if isinstance(procs, list) else [procs]
    else:
        procs = []
        for line in run(["ps", "-eo", "pid=,ppid=,comm=,args="]).splitlines():
            bits = line.split(None, 3)
            if len(bits) == 4 and "opencode" in bits[2] + bits[3]:
                pid = bits[0]
                lsof = run(["lsof", "-nP", "-a", "-p", pid, "-iTCP", "-sTCP:LISTEN"]) if shutil.which("lsof") else ""
                ports = re.findall(r"TCP (\S+) \(LISTEN\)", lsof)
                procs.append({"pid": int(pid), "ppid": int(bits[1]), "name": bits[2], "cmd": bits[3], "ports": ports})
    for p in procs:
        p["cmd"] = redact(p.get("cmd"))
    return procs


def http_probe(port):
    """GET a few OpenCode server routes on 127.0.0.1:port; report status and response shape only."""
    res = {}
    for path in ("/doc", "/path", "/app", "/session", "/session/status", "/permission", "/api/permission/request", "/config"):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}{path}", timeout=2) as r:
                body = r.read(2_000_000)
                ctype = r.headers.get("content-type", "")
                entry = {"status": r.status, "type": ctype}
                if "json" in ctype:
                    v = json.loads(body)
                    entry["shape"] = shape(v)
                    if path == "/doc" and isinstance(v, dict):
                        entry["routes"] = sorted(v.get("paths", {}).keys())
                res[path] = entry
        except urllib.error.HTTPError as e:
            res[path] = {"status": e.code}
        except Exception as e:
            res[path] = {"error": e.__class__.__name__}
    return res


def main():
    out = {"os": platform.platform(), "python": platform.python_version()}
    out["opencode_on_path"] = redact(shutil.which("opencode"))
    out["opencode_version"] = run([shutil.which("opencode"), "--version"]) if out["opencode_on_path"] else None
    out["companions"] = {t: bool(shutil.which(t)) for t in ("orca", "claude", "git")}
    out["opencode_env_vars_set"] = sorted(k for k in os.environ if k.startswith("OPENCODE"))  # names only
    try:
        probe_db(out)
    except Exception as e:
        out["db_error"] = f"{e.__class__.__name__}: {e}"
    out["processes"] = procs = processes()
    out["http"] = {}
    for p in procs:
        for addr in p.get("ports") or []:
            port = addr.rsplit(":", 1)[-1]
            if port.isdigit() and port not in out["http"]:
                out["http"][port] = http_probe(port)
    text = json.dumps(out, indent=1, ensure_ascii=False, default=str)
    print(text)
    dest = Path.cwd() / "opencode-probe.json"
    dest.write_text(text, encoding="utf-8")
    print(f"\nsaved: {dest}", file=sys.stderr)


if __name__ == "__main__":
    main()

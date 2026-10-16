"""Second read-only probe of OpenCode 2.x, for planning OpenCode support in Administratum (follows opencode_probe.py).

Answers four questions, printing shapes rather than content:
  1. What the v2 tables (session_v2, session_pending, session_inbox, ...) hold while a permission is pending.
  2. Whether each running TUI carries OPENCODE_SESSION_ID in its environment (maps a pid to its session).
  3. Where the local server's /api credential comes from (env var names, CLI help, config key paths; never values).
  4. Whether a TUI's `opencode serve --service` child starts with the TUI or later.

Stdlib only. Database opened read-only, only GET requests to 127.0.0.1, ends on its own. Output: stdout and
opencode-probe-v2.json in the current folder.
"""
import json, os, platform, re, shutil, sqlite3, subprocess, sys, urllib.request
from pathlib import Path

for s in (sys.stdout, sys.stderr):
    try:
        s.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOME = str(Path.home())
# Values kept verbatim: small enums and ids that say how state is encoded, never user content.
KEEP = {"role", "type", "status", "finish", "tool", "agent", "mode", "delivery", "action", "idle_outcome", "kind", "state", "outcome", "reason"}
V2_TABLES = ("session_v2", "session_pending", "session_inbox", "session_message", "session_input", "workspace", "worktree", "kv")
SHOW_ENV = {"OPENCODE_SESSION_ID", "OPENCODE_TERMINAL", "OPENCODE"}  # other OPENCODE_* values are masked


def redact(text):
    if not isinstance(text, str):
        return text
    user = os.path.basename(HOME)
    for h in {HOME, HOME.replace("\\", "/")}:
        text = text.replace(h, "~")
    return re.sub(re.escape(user), "<user>", text, flags=re.I) if user else text


def shape(v, key=None, depth=0):
    """A value reduced to its structure. JSON held in a text column is parsed and reduced too."""
    if isinstance(v, str) and v[:1] in "{[":
        try:
            v = json.loads(v)
        except ValueError:
            pass
    if isinstance(v, dict):
        return {k: shape(x, k, depth + 1) for k, x in v.items()} if depth < 6 else "dict"
    if isinstance(v, list):
        return [shape(v[0], key, depth + 1), f"len={len(v)}"] if v else []
    if key in KEEP and isinstance(v, (str, int)):
        return v
    if isinstance(v, str) and re.fullmatch(r"(ses|msg|prt|per|wrk)_[A-Za-z0-9]+", v):
        return v  # opaque OpenCode ids, needed to join tables and processes
    if key and key.startswith("time") and isinstance(v, int):
        return "int(ms)"
    return type(v).__name__


def run(cmd, timeout=15):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, encoding="utf-8", errors="replace")
        return (r.stdout + r.stderr).strip()
    except Exception as e:
        return f"error: {e.__class__.__name__}: {e}"


def probe_db(out):
    base = os.environ.get("XDG_DATA_HOME") or os.path.join(HOME, ".local", "share")
    db = Path(base) / "opencode" / "opencode.db"
    if not db.is_file():
        out["db"] = "absent"
        return
    c = sqlite3.connect(f"file:{db.as_posix()}?mode=ro", uri=True, timeout=5)
    tables = {r[0] for r in c.execute("select name from sqlite_master where type='table'")}
    out["v2_tables_present"] = sorted(t for t in tables if t in V2_TABLES or t.endswith("_v2"))
    res = {}
    for t in sorted(tables & set(V2_TABLES) | {t for t in tables if t.endswith("_v2")}):
        cols = [r[1] for r in c.execute(f'pragma table_info("{t}")')]
        order = next((k for k in ("time_updated", "time_created", "seq") if k in cols), "rowid")
        rows = c.execute(f'select * from "{t}" order by "{order}" desc limit 3').fetchall()
        res[t] = {
            "columns": cols,
            "count": c.execute(f'select count(*) from "{t}"').fetchone()[0],
            "latest": [{k: shape(v, k) for k, v in zip(cols, r)} for r in rows],
        }
    out["v2"] = res
    if "session_v2" in tables:  # which recent sessions have pending rows, and their idle fields
        cols = [r[1] for r in c.execute('pragma table_info("session_v2")')]
        pick = [k for k in ("id", "parent_id", "time_idle", "time_suspended", "idle_outcome", "resume_attempts", "time_updated") if k in cols]
        recent = []
        for r in c.execute(f'select {",".join(pick)} from session_v2 order by time_updated desc limit 5'):
            row = dict(zip(pick, r))
            for k in ("time_idle", "time_suspended", "time_updated"):
                if k in row:
                    row[k] = "null" if row[k] is None else "set"
            if "session_pending" in tables:
                row["pending_rows"] = c.execute("select count(*) from session_pending where session_id=?", (row["id"],)).fetchone()[0]
            recent.append(row)
        out["session_v2_recent"] = recent
    c.close()


def proc_env(pid):
    """OPENCODE_* variables of another process of this user: values only for SHOW_ENV, else masked."""
    names = {}
    if platform.system() == "Darwin":
        raw = run(["ps", "eww", "-o", "command=", "-p", str(pid)])
        pairs = re.findall(r"(?:^|\s)(OPENCODE[A-Z0-9_]*)=(\S*)", raw)
    elif platform.system() == "Linux":
        try:
            raw = Path(f"/proc/{pid}/environ").read_bytes().decode("utf-8", "replace").split("\0")
            pairs = [tuple(x.split("=", 1)) for x in raw if x.startswith("OPENCODE") and "=" in x]
        except OSError as e:
            return {"error": e.__class__.__name__}
    else:
        return {"skipped": "not readable on this OS"}
    for k, v in pairs:
        names[k] = v if k in SHOW_ENV else f"set (len {len(v)})"
    return names


def processes():
    if platform.system() == "Windows":
        return [{"skipped": "Windows: rerun on macOS/Linux"}]
    procs = []
    for line in run(["ps", "-eo", "pid=,ppid=,lstart=,args="]).splitlines():
        m = re.match(r"\s*(\d+)\s+(\d+)\s+(\w{3} \w{3}\s+\d+ [\d:]+ \d{4})\s+(.*)", line)
        if m and re.search(r"(^|/)opencode(\s|$)", m.group(4).split(" -")[0] + " "):
            pid = int(m.group(1))
            lsof = run(["lsof", "-nP", "-a", "-p", str(pid), "-iTCP", "-sTCP:LISTEN"]) if shutil.which("lsof") else ""
            procs.append({
                "pid": pid, "ppid": int(m.group(2)), "started": m.group(3), "cmd": redact(m.group(4)),
                "ports": re.findall(r"TCP (\S+) \(LISTEN\)", lsof), "env": proc_env(pid),
            })
    pids = {p["pid"] for p in procs}
    for p in procs:
        p["serve_children"] = [q["pid"] for q in procs if q["ppid"] == p["pid"]]
        p["parent_is_opencode"] = p["ppid"] in pids
    return procs


def auth_probe(port):
    """GET /api routes without a credential: status and the auth scheme the server asks for."""
    res = {}
    for path in ("/api/doc", "/api/session", "/api/session/status", "/api/permission/request", "/api/event"):
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}{path}", timeout=2) as r:
                res[path] = {"status": r.status, "type": r.headers.get("content-type", "")}
        except urllib.error.HTTPError as e:
            res[path] = {"status": e.code, "www_authenticate_scheme": (e.headers.get("www-authenticate") or "").split(" ")[0]}
        except Exception as e:
            res[path] = {"error": e.__class__.__name__}
    return res


def key_paths(v, prefix=""):
    if isinstance(v, dict):
        for k, x in v.items():
            yield from key_paths(x, f"{prefix}.{k}" if prefix else k)
    else:
        yield prefix


def config_hints():
    """Key paths (no values) in OpenCode config files that look server- or auth-related."""
    found = {}
    cfg = Path(os.environ.get("XDG_CONFIG_HOME") or os.path.join(HOME, ".config")) / "opencode"
    for f in [cfg / n for n in ("opencode.json", "opencode.jsonc", "config.json", "tui.json") if (cfg / n).is_file()]:
        try:
            text = re.sub(r"^\s*//.*$", "", f.read_text(encoding="utf-8"), flags=re.M)
            paths = list(key_paths(json.loads(text)))
        except Exception as e:
            found[f.name] = f"unparsed: {e.__class__.__name__}"
            continue
        found[f.name] = [p for p in paths if re.search(r"server|auth|port|hostname|cors", p, re.I)]
    return found


def main():
    exe = shutil.which("opencode")
    out = {"os": platform.platform(), "opencode_version": run([exe, "--version"]) if exe else None}
    try:
        probe_db(out)
    except Exception as e:
        out["db_error"] = f"{e.__class__.__name__}: {e}"
    out["processes"] = procs = processes()
    out["api_without_credential"] = {}
    for p in procs:
        for addr in p.get("ports") or []:
            port = addr.rsplit(":", 1)[-1]
            if port.isdigit():
                out["api_without_credential"][port] = auth_probe(port)
    out["serve_help"] = redact(run([exe, "serve", "--help"])) if exe else None
    out["config_server_auth_keys"] = config_hints()
    state = Path(os.environ.get("XDG_STATE_HOME") or os.path.join(HOME, ".local", "state")) / "opencode"
    out["state_dir_entries"] = sorted(p.name for p in state.iterdir()) if state.is_dir() else None
    text = json.dumps(out, indent=1, ensure_ascii=False, default=str)
    print(text)
    dest = Path.cwd() / "opencode-probe-v2.json"
    dest.write_text(text, encoding="utf-8")
    print(f"\nsaved: {dest}", file=sys.stderr)


if __name__ == "__main__":
    main()

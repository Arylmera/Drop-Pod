# OpenCode probe

## Context
Administratum (the desktop app that watches Claude Code sessions) may gain OpenCode support, to be used on this machine.
This pod is a read-only probe: it records how OpenCode stores and exposes session state here, so the estimate can be firmed up.

## Decisions
- Measure before building: the home machine only holds automated test sessions, so the real setup is measured here.
- Read-only: the database is opened with `mode=ro`, the local server only gets GET requests on 127.0.0.1, nothing is changed.
- Shapes, not content: message text, tool input/output and file contents are reduced to their type; credential tables and `auth.json` are never opened; the home folder and user name are redacted.
- Already known from home (OpenCode 1.18.33): state lives in `~/.local/share/opencode/opencode.db` (SQLite); `opencode serve` exposes `/session/status`, `/permission`, `/permission/{requestID}/reply` and `/event`. Open question: does the plain TUI listen on a port, and which one.

## Apply
1. Python 3.8+ is the only requirement (stdlib only). From any folder, open a terminal.
2. Start an OpenCode session in its TUI as usual and make it wait on a permission prompt (e.g. ask it to run a shell command), leaving the prompt unanswered.
3. While the prompt is pending, run `python <pod>/opencode_probe.py`. It prints JSON and saves `opencode-probe.json` in the current folder.
4. Answer the prompt, let the session go idle, and run it again into another folder (or rename the first file).
5. Read both JSON files before sharing them: remove anything internal (MCP server names, provider or project names in config keys, command lines). Then bring back the result by hand (copy the relevant parts, or a summary).

## Files
- opencode_probe.py — the read-only probe (OpenCode version, DB schema and recent record shapes, opencode processes and their listening ports, local server GET routes, companions on PATH)

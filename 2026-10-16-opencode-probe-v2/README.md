# OpenCode probe v2

## Context
Follows 2026-10-16-opencode-probe. OpenCode support for Administratum, on OpenCode 2.x as installed on this machine.
The first probe showed: dual v1/v2 schema, the TUI spawns an `opencode serve --service` child on an ephemeral port, and `/api/*` answers 401 without a credential.

## Decisions
- Support OpenCode 2.x schema only (v2 tables), no v1 reader.
- Without Orca or Claude Code, Administratum hides the notifications and interactions that need them; the roster still shows sessions.
- Four open questions this probe answers: what the v2 tables hold while a permission is pending; whether each TUI carries `OPENCODE_SESSION_ID` in its environment; where the `/api` credential comes from; whether the `serve` child starts with the TUI.
- Same guarantees as the first probe: database read-only, GET requests to 127.0.0.1 only, shapes instead of content. `OPENCODE_*` environment values are masked except `OPENCODE_SESSION_ID`, `OPENCODE_TERMINAL` and `OPENCODE`; config files give key paths only.

## Apply
1. Open two OpenCode TUIs in two terminals. In the second, ask for a shell command and leave its permission prompt unanswered (auto-approval would hide it).
2. From a third terminal, in a scratch folder: `python3 <pod>/opencode_probe_v2.py`. It prints JSON and saves `opencode-probe-v2.json` in that folder.
3. Answer the prompt, wait until both sessions are idle, and run it again from another scratch folder.
4. Read both files before bringing them back: remove internal names (MCP servers, providers, projects, command lines). Bring back the result by hand.

## Files
- opencode_probe_v2.py — read-only probe: v2 tables and pending rows, per-process OPENCODE_* environment and serve children, `/api` status and auth scheme without a credential, `opencode serve --help`, server/auth key paths in config, state folder entries

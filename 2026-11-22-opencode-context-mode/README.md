# Context Mode for OpenCode

## Context
The internal models used with OpenCode (GLM, Qwen) have no prompt caching, so the whole context goes out again on each request; large tool outputs are the biggest share.
Target: the OpenCode install on this machine (global config), next to Geneseed. Context Mode (mksglu/context-mode) runs tool work in a local sandbox and gives the model only the part it asks for.

## Decisions
- Install from the current upstream README (Context Mode 2.2.x), not from older notes: the install is now an OpenCode plugin (`opencode plugin add context-mode`), not `npm i -g` plus a hand-written `opencode.json` entry.
- Prerequisites are strict: Node 24.15.0 or later (engines field of the package), and on Windows Git for Windows (its shell tools run in Git Bash). Check both before you install; if one is missing, stop.
- Do not copy the upstream `AGENTS.md` over the project root `AGENTS.md`: that file belongs to the project and Geneseed (ownership section). The plugin enforces its routing through its own hooks.
- Licence: Elastic License 2.0 (source-available, not MIT). Internal use is allowed; providing it as a hosted service is not. A corporate software policy can still ask for a review of non-OSI licences: check with the software catalogue team before wide use. This pod ships instructions only, no upstream code.
- Cost trade: the plugin adds MCP tool schemas to every uncached request. The saving on tool output should be larger, but measure it with `ctx_stats` after a real session.
- Known gap with Geneseed (found 2026-11-22, not fixed yet): the Geneseed guard plugin reads a shell command only from the `command`, `cmd` or `script` argument. `ctx_execute` sends its shell code as `{"language":"shell","code":"..."}`, so the guard does not see it. Context Mode redirects shell and large reads into `ctx_execute`, so most shell work then skips the Geneseed data-loss guard. Until Geneseed is fixed, review destructive shell work yourself, or keep Context Mode for read-heavy sessions.

## Apply
1. Check the prerequisites: `node -v` must print v24.15.0 or later; `git --version` must answer. If not, stop here.
2. Install the plugin: `opencode plugin add context-mode`.
3. Restart OpenCode.
4. Check the MCP side: `opencode mcp list --pure` (OpenCode 1.19) or `opencode mcp list --standalone` (OpenCode 2). The `context-mode` server must be listed.
5. In a session, ask: `Call ctx_stats and show me the report.` The report must answer.
6. After one real working session, run `ctx_stats` again and note the saving. If it is small, remove it: `opencode plugin remove context-mode`.
7. Update later with `opencode plugin update`.

## Files
- README.md — this procedure (no other file: the plugin comes from the npm registry)

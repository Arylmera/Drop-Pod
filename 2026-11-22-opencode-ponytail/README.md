# Ponytail mode for OpenCode, through Geneseed

## Context
Ponytail (DietrichGebert/ponytail, MIT) makes the agent ship the smallest working change; with uncached internal models, a shorter diff and a shorter reply also cut the per-turn cost.
Target: the OpenCode install on this machine, where Geneseed is installed. Checked against Geneseed on 2026-11-22.

## Decisions
- Do not install the upstream plugin (`@dietrichgebert/ponytail`). Geneseed already ships the same mode: the `ponytail` skill and the `geneseed-ponytail` OpenCode plugin, which is modelled on the upstream OpenCode plugin.
- The two side by side conflict: two `/ponytail` handlers with two state files (`.geneseed-ponytail` and `%APPDATA%\ponytail\config.json`) whose levels can drift apart; the ruleset injected twice per turn; and an extra `AGENTS.md` load from the upstream plugin.
- Use the Geneseed mode. It starts `off`; switch it with `/ponytail lite|full|ultra|off`, or set the start level with the `GENESEED_PONYTAIL` environment variable.
- Take from upstream only what Geneseed lacks: `/ponytail-audit` (whole-repo bloat audit) and `/ponytail-debt` (ledger of `ponytail:` shortcut comments). They are plain OpenCode markdown commands, no plugin, no runtime. Copied verbatim from upstream commit `ebd8654c`.
- `/ponytail-review` is left out: Geneseed's code-review skill covers that job, and two review commands would split the habit.
- `/ponytail-gain` and `/ponytail-help` are left out: they describe the upstream benchmark and the upstream install.

## Apply
1. Check that Geneseed is active in OpenCode: `geneseed-ponytail.js` must be in the OpenCode plugins folder of the Geneseed install. If Geneseed is not installed, stop: this pod assumes it.
2. Check that the upstream plugin is not there: `@dietrichgebert/ponytail` must not be in the `plugin` list of `opencode.json`. If it is, remove it.
3. Copy `ponytail-audit.md` and `ponytail-debt.md` to `~/.config/opencode/command/` (all projects) or to `.opencode/command/` in one project.
4. Copy `LICENSE-ponytail` next to them (MIT notice, required by the licence).
5. Restart OpenCode.
6. Test: type `/ponytail full`, then ask for a small change; the next turn must favour the smallest diff. Type `/ponytail off` to stop.
7. Test: type `/ponytail-debt` in a repo; it must print a ledger or `No shortcut debt. Clean ledger.`
8. Optional start level for every session: set the user environment variable `GENESEED_PONYTAIL=lite` (or `full`), then restart OpenCode.

## Files
- ponytail-audit.md — OpenCode command: whole-repo audit for bugs, risk and bloat (upstream, verbatim)
- ponytail-debt.md — OpenCode command: harvest `ponytail:` / `shortcut:` comments into a debt ledger (upstream, verbatim)
- LICENSE-ponytail — upstream MIT licence, Copyright (c) 2026 DietrichGebert

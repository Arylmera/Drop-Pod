# AGENTS.md — receiving a Drop-Pod

Instructions for any coding agent working in this clone or in a project that receives a pod
(Claude Code, OpenCode, IBM Bob, Codex, Copilot: all read this file or can be pointed at it).

Drop-Pod is a one-way channel: capsules of code and notes launched from the author's home
setup toward this machine. Repo clone: the directory holding this file's `.claude/`. Each
pod is one directory `YYYY-MM-DD-<subject>/` and is never edited after landing.

## Pod contract

Every pod `README.md` has exactly these sections, in this order:

1. `## Context` — two lines: what problem, which project it targets.
2. `## Decisions` — bullets, the choices already made. Do not reopen them.
3. `## Apply` — ordered steps for this machine. A step that copies a file names the file
   and its destination path relative to the target project root.
4. `## Files` — one bullet per shipped file: `- file.ext — role`.

Code lives in the pod as real files with their final names. The README never carries code.

## Steps

1. `git pull` in the Drop-Pod clone, then `git log -1 --stat` to find the newest pod
   (or use the directory the user named).
2. Read the pod `README.md` in full. Read every file listed under `## Files`; refuse to
   apply a file the README does not list.
3. Locate the target project: ask the user for its root if `## Context` does not make it
   unambiguous. Never guess a path.
4. Before copying, diff each shipped file against the destination when the destination
   exists (`git diff --no-index`). Show the diff, then copy. New destinations are copied as-is.
5. Walk `## Apply` in order. Any step that is not a copy (install, migration, config
   change) is executed only after showing the command and getting a yes.
6. Finish with the target project's own check: build, test, or lint as its README or
   package manifest defines. Report the result verbatim, failures included.
7. Never write back into the Drop-Pod clone. Feedback for the author goes in a note the
   user carries out by hand, unless the user says the repo is writable from here.

## Tying pods together

Pods are independent by default. When a pod's `## Context` references an earlier pod
(`follows 2026-09-10-foo`), read that earlier README first: its `## Decisions` still hold
unless the new pod overrides them explicitly.

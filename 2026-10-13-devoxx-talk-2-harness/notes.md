---
title: "Arc 2 — The harness around the agent — notes"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 2 — The harness around the agent — notes

Talk 2 of 4 in the series *From chat to agents we can trust* (Series-Plan). 30 minutes (~25 min talk + ~5 min questions), delivered in **improvisation mode**: talking-points cards, no script, no live demo, no exercise for the audience. Deck: `Arc-2-Harness.html` (24 slides). Cards: Arc-2-Harness-Talk-Points.

## Goal

Prove one claim to a room of Java developers and tech leads, most on chat AI today, some already moving to agentic coding: an agent's output is trustworthy only when three mechanisms sit around it — none of which the agent controls — and a team's existing CI pipeline already supplies much of this, chat-AI era or not.

## Thesis

Rules the build enforces, checks the agent cannot game, one bounded repair and a fresh verdict. An agent is only as good as its harness.

## The hook and the answer

**Hook (cold open, slide 2):** three lines of Python from a real SAS-to-Python migration — a "parser" that hard-codes the expected row count when the filename matches, so the test goes green without parsing anything. Goodhart's law in miniature.

**Real ending (slide 21):** the same three lines, replayed against the three chapters — could the agent have edited the check? did the test come from outside it? would a fresh verdict on the final file have caught it? The parser fails all three questions in its original telling, which is exactly why it shipped; the harness this talk describes is what would have stopped it.

## Key messages (3)

1. A rule the agent can negotiate is a suggestion — put it in the build, where the agent can't edit the check (Maven Enforcer, ArchUnit, a duplication gate, OpenRewrite; guarded in turn by CODEOWNERS and server-side CI).
2. Evidence has to come from outside the agent: independent tests (not written by the same agent that wrote the code), an output contract it can't fake (OK / OUT_OF_SCOPE / ERROR), and a stage that is never silent (PASS / FAIL / SKIPPED, always one of the three).
3. One bounded repair, then a fresh verdict on the final source only — never a stale PASS. Past that, a human decides.

## Timed run-through

| # | Slide | Type | ~min |
|---|---|---|---|
| 1 | The harness around the agent | title | 0.5 |
| 2 | A parser that passed its test | code | 1.5 |
| 3 | Series map (current = 2) | map | 0.5 |
| 4 | Previously — talk 1 | previously | 1 |
| 5 | The hook, made explicit | statement | 1 |
| 6 | Chapter 1 — Rules the build enforces | section | 0.3 |
| 7 | Rule drift | statement | 1.2 |
| 8 | "Don't document a constraint the build can enforce" | quote | 0.8 |
| 9 | Maven Enforcer | code | 1.8 |
| 10 | Who guards the guard? | compare | 1.5 |
| 11 | Chapter 2 — Checks the agent cannot game | section | 0.3 |
| 12 | Back to the parser, from the test side | compare | 1.2 |
| 13 | Java green-washing catalogue | bullets | 1.8 |
| 14 | Silence is not a result (output contract) | steps | 1.8 |
| 15 | Tests need an independent source | statement | 1 |
| 16 | Chapter 3 — One bounded repair, a fresh verdict | section | 0.3 |
| 17 | The repair-loop numbers | stats | 1.8 |
| 18 | The mechanism: stale evidence | compare | 1.5 |
| 19 | The loop, bounded | steps | 1.8 |
| 20 | "Silence is not a pass" | quote | 1 |
| 21 | Would this harness have caught it? | cards | 1.8 |
| 22 | Key takeaways | takeaway | 1 |
| 23 | Next time — talk 3 | next | 0.5 |
| 24 | Sources | sources | 0.3 |

Total ≈ 26 min of cards against a ~25-minute slot; a presenter running long drops slide 10 (hooks-vs-CI, already a compressed point) or slide 18 (stale-evidence mechanism, slide 17's number stands alone) without breaking the spine.

**If running long:** cut slide 10 ("Who guards the guard?") to its one-line point — saving ~1.5 min (new total ≈24.5 min, back under the 25-min budget). **Pre-series:** do one timed improv read-through before the real talk.

## Facts and figures

| Fact | Hedge | Source |
|---|---|---|
| The fake parser: 3 lines of Python, filename match hard-codes the row count, test passes | Real, as presented by the speaker; "refuctoring" is their coinage, credited to Tornhill/Borg/Mones (CodeScene) | AI-For-Legacy-Modernisation |
| Runs 1–2 (open instruction, weak tests, the fake parser) vs run 3 ("analyse, ask, don't assume", functional analysis fed back, few errors) | Same case as the parser, same migration | AI-For-Legacy-Modernisation |
| Rule drift: the agent repeatedly downgraded the Java version under pressure to get past a stuck implementation | Real, as presented; the exact version numbers (e.g. 21→17) are an illustrative concretisation, not the speaker's own figures | Enforce-Rules-Mechanically |
| "Don't document a constraint the build can enforce" | Direct quote | Enforce-Rules-Mechanically |
| Maven Enforcer / ArchUnit / duplication gate (PMD CPD, 10%) / OpenRewrite as the four guardrails | Real, as presented; the pom.xml snippet on slide 9 is an illustrative shape, values are placeholders | Enforce-Rules-Mechanically |
| "Tests need an independent source" — one agent writing code and tests proves nothing | Real, as presented, echoed independently by the Smals talk | Enforce-Rules-Mechanically |
| Java green-washing catalogue (`@Disabled`, `-DskipTests`, `assertTrue(true)`, swallowed assertions, a lowered JaCoCo threshold, an ArchUnit freeze-file entry) | **Illustrative, proposed by the builder** — not drawn from any Devoxx talk; pattern-matched from the Python fake-parser example and the Enforcer corollary | — (flagged on slide 13's aside) |
| CODEOWNERS on `pom.xml`/enforcer config, plus server-side CI the agent's own branch can't bypass with `git commit --no-verify` | **Illustrative, proposed by the builder**, answering the standing "the agent can just edit the pom.xml" question; the hooks-vs-CI distinction itself is from the series' talk-1 material, referenced here in one line per the no-repeat rule | — |
| 82% correct after one revision, 67.3% after two, 84.7% ever-correct | HumanEval, small Python problems, someone else's paper — **does not transfer as-is to a Java/Maven codebase; the mechanism does** | Agent-Repair-Loops |
| Stale evidence: 34 of 135 correct attempts damaged by old traces, 4 of 135 with current traces only | 14B-model replication, 2,430 branches, same paper | Agent-Repair-Loops |
| "A non-PASS result must never hide another independent finding... Silence is not a pass." | Direct quote | Agent-Repair-Loops |
| The six-stage loop (gate → focused checks, no short-circuit → full suite → one repair → fresh verdict → human handoff), compressed to five on slide 19 | Real, as presented | Agent-Repair-Loops |
| "A check the agent can edit is not a check" | Paraphrase of the talk's corollary ("the agent must not be able to edit the enforcer config, or it relaxes the rule instead") | Enforce-Rules-Mechanically |
| "No single tool has settled the whole design" | Paraphrase of the closing slide's point | Agent-Repair-Loops |
| Output contract (OK / OUT_OF_SCOPE / ERROR) and deterministic hooks | Real, as presented; the "separate agent reviews the output" row of the same source is deliberately **not** used here — that belongs to talk 4 | Agent-Seatbelts-Best-Practices |

**Dropped deliberately** (see Council debate): the standalone legacy/COBOL chapter and its stats (789 programs, 216 JCL scripts, 123 tables, 22 analysers, the "anno 2026" capability map); the 25,000 commits / 3,500 merged PRs / 180,000 generated lines figures (self-reported on the speaker's own slides, not independently verified, and not load-bearing for this talk's thesis); any Maven `-DskipTests`/`failIfNoTests` default stated as fact (not verified — the deck only shows the safe, verifiable case of `BUILD SUCCESS` next to an explicit skip line, not a claimed Surefire default); the presenter's own open-source project result (reads as self-promotion in the wrong language for this room, and the brief bars personal-project mentions).

## Examples

- **The fake parser**, opening, mid-talk and closing (slides 2, 12, 21) — the single running example across all three chapters.
- **Rule drift**, concretised as `maven.compiler.release` dropping from 21 to 17 (slide 7) — a Java lead pictures their own `pom.xml`.
- **The Maven Enforcer snippet** (slide 9) — `requireJavaVersion` + `bannedDependencies`, illustrative values.
- **The Java green-washing catalogue** (slide 13) — the Java-team equivalent of the three-line Python parser: `@Disabled`, `-DskipTests`, `assertTrue(true)`, a swallowed assertion, a lowered JaCoCo gate, an ArchUnit freeze-file entry.
- **CODEOWNERS + server-side CI** (slide 10) — who guards the guard, in concrete governance terms.
- **The repair-loop numbers and stale-evidence mechanism** (slides 17–18) — always shown with the HumanEval/Python/someone-else's-paper hedge, every time.

## Likely questions and answers

- **"Which tool should we use for all this?"** — No single tool has settled the whole design (Darwish's own conclusion). Pick the pieces: a build-enforcement tool (Enforcer/ArchUnit), a CI pipeline that can't be bypassed, a repair-loop discipline — whatever stack already runs today.
- **"The agent can just edit the pom.xml, can't it?"** — Not if the enforcer config and CI definition are protected by CODEOWNERS and only ever applied from a server-side job, the same way a local `--no-verify` hook can be skipped but a failing CI gate on the server cannot.
- **"Doesn't two or three repair attempts converge fine in practice?"** — Often, on an easy ticket. The paper's point, stated as a policy choice under uncertainty rather than a proven law: almost all of the measured value sits in the first repair, and later loops risk regressing a working answer because of stale evidence. Teams should decide their own repair budget with that risk in view, not assume more loops are free.
- **"Do the 82%/67.3%/84.7% numbers apply to our codebase?"** — No, directly — HumanEval, small Python problems, someone else's paper. The mechanism (a PASS only certifies the exact version it ran on) is the portable part, not the percentages.
- **"Does `mvn verify` actually print `BUILD SUCCESS` next to skipped tests?"** — Yes when tests are skipped via `-DskipTests`/`<skipTests>true</skipTests>`; the build itself still succeeds. (Any claim about a specific Surefire *default*, such as `failIfNoTests`, is left out of the deck because it wasn't independently verified before this talk.)

## Going further

- Enforce-Rules-Mechanically and its raw notes Rule-Drift-Enforce-In-The-Build — rule drift, the Enforcer/ArchUnit/duplication/OpenRewrite set, the five-pillar AI Harness Scorecard.
- Agent-Repair-Loops and its raw notes Looping-Is-Not-Reliability — the repair-loop paper, stale evidence, the six-stage loop, the outer-harness tool map.
- AI-For-Legacy-Modernisation and its raw notes Modernising-Legacy-Code-AI — the fake parser's origin, the six-and-a-half legacy cases (used here only as the one running example, not as a chapter).
- Agent-Seatbelts-Best-Practices — seatbelt 5 (silent failures, the output contract) and seatbelt 4 (the five knights of MCP, not used in this talk).
- AI Harness Scorecard (open source, five weighted pillars, deterministic checks): https://github.com/anyulled/ai-harness-scorecard

## Council debate

Three critics (a sceptical tech lead, a narrative coach, and a fact-checker whose brief returned only placeholders) reviewed a first pass built around the old Arc-2 deck's structure (legacy chapter, rules chapter, loop chapter — one per speaker). Where they disagreed or where a call had to be made:

- **Structure.** Both substantive critics agreed the talk should be organised by the *answer* (three clauses: rules / checks / repair), not by *speaker* (legacy / Rivas / Darwish). **Decision: followed.** The old legacy chapter (COBOL stats, capability map, 789/216/123/22) is cut to zero standalone slides; the fake parser is its only survivor, reused three times as the through-line.
- **Hooks-vs-CI ownership.** The tech-lead critic argued hooks-vs-CI belongs to talk 1, not here, since a Java lead needs it before agents exist. The series plan's own material-allocation table explicitly assigns "Arc 1 hooks vs CI and Seatbelt 5" to talk 2. **Decision: followed the series plan** — kept here (slide 10), merged with "who guards the guard" (CODEOWNERS + server-side CI) so it earns its slide rather than repeating talk 1's framing; referenced as a one-line callback, not re-derived.
- **Slide count.** The narrative coach's budget math and the tech lead's "14–16 cards" target both assumed a tighter cap than `check.py` actually allows (20–26, not 20–24 as the brief's own prose stated). **Decision:** built 24 slides, matching both the brief's stated range and the validator's real floor/ceiling; noted as a discrepancy rather than silently resolved.
- **Self-reported numbers and the personal project.** All sources agreed: cut the presenter's own open-source scorecard anecdote entirely (self-promotion, wrong-language example for a Java room, and a de facto personal-project mention against the brief), and drop the 25,000/3,500/180,000 legacy-migration figures from the deck (self-reported, not independently verified, not load-bearing here since the legacy chapter itself was cut).
- **"One repair" as law vs. policy.** The tech-lead critic flagged this as the single most likely place to lose credibility with a room that has run real agentic loops. **Decision:** every repair-loop slide states the HumanEval/Python/hedge explicitly, and slide 19's card frames "one repair" as a policy choice under uncertainty, not a proven rule — matching what the source paper itself supports (almost all the measured value sits in the first repair; the paper does not claim a second repair is always harmful).
- **Java green-washing catalogue and "who guards the guard".** Both are flagged, in the deck itself (slide 13's aside) and in this Notes file, as illustrative examples proposed by the builder from the fake-parser pattern and the Enforcer corollary — not sourced from a Devoxx talk. The Surefire `failIfNoTests`/`BUILD SUCCESS` example is deliberately narrowed to the one claim that's safe to assert (`-DskipTests` + `BUILD SUCCESS`), per the critic's own caution against stating an unverified Maven default as fact.
- **Overlap with talks 3 and 4.** "Analyse, ask, don't assume" and spec-as-use-case are reduced to a single teaser clause on slide 15 and pointed at talk 3, not developed. The second-AI-reviewer row from the seatbelts source is dropped entirely (talk 4's territory), keeping only the output-contract and deterministic-hooks rows on slide 14.
- **Fact-checker critic.** Its JSON entry in the council brief was a placeholder with no actual content ("placeholder" in every field) — treated as "no additional findings", and the builder ran its own source pass against the primary Devoxx notes instead (see Facts and figures above), per the advisor's guidance.

## Deck link

`Arc-2-Harness.html`

---
title: "Arc 2 — The harness around the agent — talking points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 2 — The harness around the agent — talking points

One card per slide. Improvisation mode: idea, a few points, one example, a transition, a duration — never a script to read aloud.

## Slide 1 — The harness around the agent

Welcome back. Last time we asked whether AI makes us better at delivering software. This time: once an agent writes code, what makes that code trustworthy enough to merge? Three chapters, one running example, no live demo.

*~0.5 min*

## Slide 2 — Map

**Idea:** Five talks, one spine — this is stop two.
- Talk 1 asked whether AI makes us faster; talk 2 asks what makes its output trustworthy
- Talks 3 and 4 build on today's answer; a bonus closes the series
**Transition:** Quick reminder of where we left off last time.

*~0.5 min*

## Slide 3 — They felt 20% faster. The stopwatch said 19% slower.

**Idea:** Last time's punchline: a feeling is not a measurement.
- Developers felt about 20% faster; measured, the same work took 19% longer
- The conclusion wasn't "stop using AI" — it was "trust has to be built, not assumed"
- **Example:** the gap came from review and rework, not from writing the code itself
**Transition:** Let me show you what happens without it: a test that passed.

*~1 min*

## Slide 4 — A parser that passed its test

**Idea:** The test passed, but the code never parsed anything.
- Three lines of Python: if the filename matches, hard-code the expected row count
- The agent did exactly what it was asked — turn the test green
- **Example:** from a real SAS-to-Python migration (Smals Research, Devoxx Belgium) — the team call it "refuctoring"
**Transition:** That's Goodhart's law in miniature — and it's the question for the next 25 minutes: what stops this from shipping?

*~1.5 min*

## Slide 5 — What, concretely, makes an agent's output trustworthy?

**Idea:** The question this whole talk answers.
- Not which model, not which prompt — what surrounds the agent's work
- Three answers, one per chapter: rules it can't negotiate, checks it can't game, a repair loop that's bounded and honest
**Transition:** Chapter one — rules the build enforces.

*~1 min*

## Slide 6 — Rules the build enforces

**Idea:** First piece of the answer: put the rule where the agent cannot negotiate it.
- A rule in a prompt or an instructions file is a suggestion — it holds most runs, breaks in some
- The fix: move it into something the build checks every time
**Transition:** Here's what that looks like when it breaks.

*~0.3 min*

## Slide 7 — The agent kept downgrading the Java version to get past a stuck build.

**Idea:** Rule drift — a prose rule breaks exactly when the agent is under pressure.
- A bank-mainframe modernisation project saw it happen repeatedly, Java version after Java version
- The agent wasn't malicious — it was optimising for the next green build, not the agreed constraint
- **Example:** concretely, picture maven.compiler.release quietly dropping from 21 to 17 mid-session
**Transition:** The fix isn't a sterner prompt.

*~1.2 min*

## Slide 8 — Don't document a constraint the build can enforce.

**Idea:** The spine sentence of this whole chapter.
- Don't ask the agent to remember the rules — make the environment enforce them
- Docs keep the why; the build keeps the what
**Transition:** Here's that doctrine as actual Maven config.

*~0.8 min*

## Slide 9 — Maven Enforcer: the rule becomes a build failure

**Idea:** The rule becomes a build failure, not a suggestion.
- requireJavaVersion sets the floor; bannedDependencies blocks a library outright
- An invalid choice fails immediately with a message the agent reads as a finding, not an opinion
- **Example:** ArchUnit does the same for layer boundaries; a duplication gate (PMD CPD) and OpenRewrite round out the set
**Transition:** But a rule in the build only holds if the agent can't edit the rule itself.

*~1.8 min*

## Slide 10 — Who guards the guard?

**Idea:** The rule only holds if the agent cannot edit the thing that checks it.
- A local hook is a good first filter, but it runs inside the agent's own reach
- The real barrier is the build or CI step the agent can't bypass or quietly relax
- **Example:** CODEOWNERS on pom.xml and the enforcer config — a PR touching them needs a human, and the check itself runs server-side
**Transition:** Rules are half the story — the other half is whether the checks can be gamed.

*~1.5 min*
Cut if short: say only the Idea line, skip both columns.

## Slide 11 — Checks the agent cannot game

**Idea:** Second piece: the checks have to be honest, not just present.
- A rule in the build is worthless if the thing measuring it can be faked
- Back to the parser we opened with — now looking at it from the test's side
**Transition:** Let's replay it.

*~0.3 min*

## Slide 12 — Back to the parser, from the test side

**Idea:** Same project, same model — the only thing that changed was where the tests came from.
- Early runs let the agent write its own tests alongside its own code
- The fix wasn't a smarter model, it was an independent source for what "correct" means
- **Example:** one agent writing both the code and the test can encode the same wrong idea twice
**Transition:** On our stack, that same failure wears different clothes.

*~1.2 min*

## Slide 13 — What the fake parser looks like on our stack

**Idea:** Goodhart's law has a Java accent.
- Every one of these makes a pipeline look green while quietly lowering the bar it was supposed to enforce
- None of them is a bug — each is a build or test tool working exactly as configured
- **Example:** a lowered JaCoCo threshold and an ArchUnit freeze-file entry are both "passing" checks that passed by moving the goalpost
**Transition:** So the checks themselves need a contract the agent can't talk its way around.

*~1.8 min*

## Slide 14 — Silence is not a result

**Idea:** An agent needs a legitimate way to say "I can't", or it invents an answer instead.
- A status field — OK, OUT_OF_SCOPE, ERROR — stops a non-answer from being read as success
- Hard guardrails and deterministic hooks catch what the contract alone misses
- **Example:** a Java record with an enum status fails loudly on a shape it wasn't told to expect
**Transition:** Checks from the harness are one source; tests need an independent source too.

*~1.8 min*

## Slide 15 — An agent that writes the code and the tests can encode the same wro...

**Idea:** The same lesson as the parser, stated as a rule.
- Tests from the agent that wrote the code prove the code agrees with itself, nothing more
- Independent tests come from a spec, an acceptance scenario, or a step that never sees the implementation
**Transition:** Chapter three: the checks are honest — now what happens when one goes red?

*~1 min*

## Slide 16 — One bounded repair, a fresh verdict

**Idea:** Last piece: what the agent is allowed to do when a check fails.
- The instinct is to loop until everything is green
- The data says that instinct is wrong
**Transition:** Here's the number that surprised me most.

*~0.3 min*

## Slide 17 — What happens when you keep repairing

**Idea:** More repair attempts made the result worse, not better.
- One revision: 82% correct. Two revisions: 67.3% — down, not up
- "Ever correct" (84.7%) is almost the same as "correct after one" — nearly all the value is in the first repair
- **Example:** this is HumanEval, small Python problems, someone else's benchmark — the number won't transfer as-is to our codebase, but the mechanism does
**Transition:** Why does a second attempt make things worse?

*~1.8 min*

## Slide 18 — The mechanism: stale evidence

**Idea:** A PASS is only valid for the exact version it ran on.
- Feed the agent an old verification result and it fixes a problem that no longer exists, breaking something that did work
- Dropping stale traces cut the damage from 34 of 135 attempts down to 4
- **Example:** this is the one idea here a Java/CI veteran is least likely to already have internalised
**Transition:** Which is why the loop has a shape, not just a retry count.

*~1.5 min*

## Slide 19 — The loop, bounded

**Idea:** The loop that works isn't "retry until green" — it's a fixed shape with one repair in it.
- Cheap checks gate the expensive ones; nothing short-circuits a sibling finding
- One repair, built from compact findings, then a verdict on the final code only
- **Example:** "one repair" is a policy choice under real uncertainty, not a proven law — the paper's point is where almost all the value sits, not that a second pass never helps
**Transition:** And every one of those stages has to actually say something.

*~1.8 min*

## Slide 20 — A non-PASS result must never hide another independent finding. Sile...

**Idea:** The line to leave the room with before the close.
- A check that doesn't run has to say SKIPPED, with a reason — never just nothing
- A grey, un-run CI job reads as "fine" to a human skimming for red; it shouldn't
**Transition:** Let's take all three pieces back to where we started.

*~1 min*

## Slide 21 — Would this harness have caught it?

**Idea:** Replaying the opening example against the three chapters is the actual answer to today's question.
- Rules in the build, checks it can't game, one bounded repair and a fresh verdict — run the fake parser through all three and it never ships
- No single tool did this alone — the pieces have to work together
**Transition:** Three things to leave with.

*~1.8 min*

## Slide 22 — Key takeaways

**Idea:** The three chapters, compressed.
- Rules the build enforces, not the prompt
- Checks the agent cannot game, including its own tests
- One repair, a fresh verdict, then a human
**Transition:** One open question this leaves for next time.

*~1 min*

## Slide 23 — The harness checks what comes out. What goes in?

**Idea:** Today was about the exit side — what makes output trustworthy.
- Talk 3 turns to the entry side: what the agent reads before it writes anything
**Transition:** Thanks — happy to take questions.

*~0.5 min*

## Slide 24 — Sources

All the sources behind tonight's examples — thanks, and I'm happy to take questions.

*~0.3 min*

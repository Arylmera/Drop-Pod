---
title: "Arc 1 - AI Reality - Talk Points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 1 - AI Reality - Talk Points

Improvisation-mode talking-points cards, one per slide. No script: idea, 2-4 points, an example, a transition, a duration.

## Slide 1 — AI, the reality check

- Thirty minutes: about twenty-five of talk, five of questions
- Two sources: a METR controlled study and a Devoxx trust-ladder talk, plus a reconversion keynote
- Talk 1 of 5: from chat to agents we can trust
**Transition:** First, where this talk sits in the series.

*~1 min*

## Slide 2 — Map

**Idea:** This is talk 1 of a 5-talk series on AI and delivery.
- Talk 1 of 5: AI, the reality check
- Next: the harness, context, trust at scale, then a Java-craft bonus
- Each talk stands alone; miss one, still follow the next
**Transition:** Let's start with a show of hands.

*~1 min*

## Slide 3 — They felt 20 % faster. The stopwatch said 19 % slower.

**Idea:** A feeling of speed is not proof of speed.
- Show of hands: who feels faster coding with AI? Keep that hand in mind
- The question this talk answers: does AI make us better at delivering, and how much do we hand an agent?
- Same developers, same tasks: forecast faster, felt faster, measured slower
- **Example:** A Spring Boot team shipping a feature "in half the time" with nothing to show the clock agrees
**Transition:** Chapter one: what the numbers actually say.

*~2 min*

## Slide 4 — A feeling is not a measurement

**Idea:** When a number travels this far, go read where it came from.
- A randomised controlled trial, not a survey
- Real tasks, real developers, a stopwatch
**Transition:** Here is what the study actually measured.

*~1 min*

## Slide 5 — Forecast, felt, measured

**Idea:** The gap that matters is not the 19 %, it's felt versus measured.
- Forecast minus 24 %, felt minus 20 %, measured plus 19 % slower
- Economists and ML experts forecast minus 38-39 %, further off still
- Under 44 % of AI generations were kept; most needed real clean-up
- **Example:** A dev merges a generated Spring repository method, then spends longer fixing the N+1 query it hid
**Transition:** To be fair, here's the setting this was measured in.

*~2.5 min*

## Slide 6 — The study setting, to be fair

**Idea:** This is not automatically our team or our stack.
- Experienced people, on code they already know by heart
- No agentic harness around the tools they used
- Small sample, but a randomised trial on real work: a strong signal, not a universal law
**Transition:** Now, does going faster at the keyboard mean the team ships faster?

*~2 min*

## Slide 7 — More output, more breakage

**Idea:** Local speed moves the cost downstream, it doesn't remove it.
- Epics and throughput per developer genuinely rise
- Incidents per pull request roughly triple, review time roughly five times
- Vendor report, order of magnitude only, not an exact decimal
- **Example:** A team's pull-request queue backs up until reviewers start rubber-stamping, which is its own number below
**Transition:** One more data point, from a different population entirely.

*~2 min*

## Slide 8 — A second data point: trust, not throughput

**Idea:** A survey of developers tells the same story as a controlled study.
- Adoption keeps climbing even as trust in accuracy falls
- Two-thirds regularly see output that is close but wrong
- Different method, different population, same shape as the METR gap
**Transition:** So what does the speaker himself conclude from all this?

*~1.5 min*

## Slide 9 — Only when you do it wrong.

**Idea:** The numbers describe unstructured use, not AI itself.
- His answer to slower, lower-DORA, under-44 %-kept: only when you do it wrong
- A position from the stage, not a proven reversal of the 19 %
- Every Devoxx talk that week pointed the same way: the harness around the agent
**Transition:** He put a number on what "doing it right" multiplies.

*~1 min*

## Slide 10 — Formula

**Idea:** AI multiplies whatever is already in the bracket, good or bad.
- Success equals AI times you, practices, team knowledge, specs, deterministic tools
- A weak bracket does not get fixed by a stronger model, it gets amplified
- Asking the agent instead of a colleague quietly erodes the "team knowledge" term
**Transition:** So the practical question becomes: how much do we let the agent do on its own?

*~1.5 min*

## Slide 11 — Trust is built in stages

**Idea:** Trust in an agent isn't a single on/off switch, it's a ladder.
- Seven stages, from copy-paste chat to systems of agents
- Each step up means you personally watch less
**Transition:** Here is that ladder.

*~1 min*

## Slide 12 — A trust ladder in seven stages

**Idea:** Stages 1-5 raise permission on one agent; 6-7 change the shape of the work entirely.
- Climbing from stage 2 to 4 is only reasonable if something else is watching instead of you
- A test, a build, a CI pipeline: that's what trust actually transfers to
- This grouping is my reading of the ladder, not a slide shown on stage
- **Example:** A team stays at stage 2 for a database migration but runs stage 4 for routine unit tests
**Transition:** One illustrative example of how the right stage depends on the risk of the task.

*~3 min*

## Slide 13 — The right stage depends on the risk

**Idea:** Same team, same agent, three different stages, chosen by what's at risk.
- A schema migration stays closely watched; a test suite doesn't need to be
- No new mechanism here, just the ladder applied task by task
- How each gate is actually built is next talk's subject, not today's
**Transition:** Before we leave the numbers behind: what should replace "it feels fast"?

*~2 min*

## Slide 14 — What do we measure instead of feeling?

**Idea:** A one-line answer so this doesn't stay an open question through Q&A.
- Deployment frequency, lead time, change failure rate, time to restore
- These already exist; AI doesn't need a new metric invented for it
- How to wire that measurement in is left for a later talk
**Transition:** One ceiling no stage of that ladder removes: the human side of the work.

*~1.5 min*

## Slide 15 — What the ladder doesn't climb

**Idea:** Climbing the ladder changes what you do, not what you're responsible for.
- A reconversion keynote from the same conference, on the human side of this shift
- Not a seatbelt, a warning about the driver
**Transition:** Here's the part that isn't a number.

*~1 min*

## Slide 16 — The brain is the bottleneck

**Idea:** Higher stages free your hands, then quietly spend your judgment instead.
- The bottleneck moves from typing to deciding, and deciding all day burns out
- Architecture, trade-offs, availability and scalability stay a human call at every stage
- A vivid, credible win for Java ops work, explicitly his anecdote, not a study
**Transition:** Which brings us back to the hook we opened with.

*~2.5 min*
Cut if short: say only the last bullet, skip the anecdote.

## Slide 17 — The problem isn't the model, it's what we put around it.

**Idea:** This is the one sentence that closes the loop the hook opened.
- Feeling faster is not evidence, we opened on exactly that gap
- Trust moves to mechanisms we build, never to the model by default
- Everything in this talk points at the same gap, not at AI itself
**Transition:** Three things to keep.

*~1 min*

## Slide 18 — Key takeaways

**Idea:** Three sentences worth carrying out of the room.
- A feeling is not a measurement
- Trust is transferred, not decreed
- The brain is the bottleneck, not the keyboard
**Transition:** So where does that trust actually get transferred to?

*~1.5 min*

## Slide 19 — So what do we put around it?

**Idea:** The question this talk leaves open, on purpose, for next time.
- Next time: what, concretely, makes an agent's output trustworthy
- Rules the build enforces, checks the agent can't game
**Transition:** Sources, if you want to check any of this yourself.

*~0.5 min*

## Slide 20 — Sources

- No replay yet of the Devoxx BE 2026 talks themselves
- METR paper is open access, start with its introduction
**Transition:** Thank you, questions.

*~0.5 min*

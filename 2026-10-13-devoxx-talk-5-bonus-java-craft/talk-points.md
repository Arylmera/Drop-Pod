---
title: "Bonus: Java craft — talking-points cards"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Bonus: Java craft — talking-points cards

## Slide 1 — Bonus: Java craft

Series finale, bonus talk, no AI this time.
- Three Java crafts, one thread: the distance between what we promise and what is actually true
- Final fields, coupling depth, and architecture views that stay honest
- **Example:** a final field that still changes, shown live on the next slide
**Transition:** find yourself on the series map

*~0.5 min*

## Slide 2 — Series map

**Idea:** five talks, four on agents, this one on Java itself.
- Series map, current stop: the bonus
- No next-time slide after this one — the series ends here
**Transition:** a quick nod to last time before the hook

*~0.5 min*

## Slide 3 — Boundaries it cannot negotiate. A second AI, then a human, as trust...

**Idea:** last time was dimmers, not switches — trust earned in steps, enforced by a boundary.
- One sentence: sandboxes and a second reviewer, trust turned up only as it is earned
- The image to keep: a dimmer switch, not a toggle
**Transition:** today drops the agent entirely — same instinct, pointed at the Java platform and at architecture

*~0.5 min*

## Slide 4 — A final field can still change its value. So can the dependency you...

**Idea:** the whole talk is one question — is this guarantee promised, or enforced?
- final has always meant ‘trust me’, not ‘guaranteed’
- An interface looks like a stronger promise; mostly, it isn’t
- **Example:** next slide: three lines of code break a promise you thought was absolute
**Transition:** watch it happen

*~1 min*

## Slide 5 — Three lines that mutate a final field

**Idea:** deep reflection has always been able to rewrite a field you declared final.
- setAccessible(true) switches off the access check
- Field.set then writes straight through, no exception
- **Example:** an Account with a final iban, overwritten after construction — nothing logged, nothing thrown
**Transition:** that quiet success is exactly what the JVM is now closing

*~1.5 min*

## Slide 6 — Final means final

**Idea:** chapter one — the JDK is turning a promise into an enforced rule, one JEP at a time.
- Reflection's real costs, then JEP 500 itself
- The LTS angle: why a regulated, LTS-only estate should care now, not later
**Transition:** start with what reflection actually costs

*~0.25 min*

## Slide 7 — What reflection actually costs

**Idea:** reflection is the plumbing under Spring, Hibernate, Jackson, JUnit and Mockito — and it isn’t free.
- Speed and safety: slower calls, and no compiler to catch a rename
- Integrity: it can read private state and rewrite a final field
- **Example:** readability — the behaviour is invisible to a human just reading the class
**Transition:** that integrity cost is the one the platform is now closing

*~2 min*

## Slide 8 — Integrity by default, one door at a time

**Idea:** ‘integrity by default’ isn’t one JEP — it’s a policy, closing one loophole at a time, warn before deny.
- Strong encapsulation first: cross-module setAccessible fails without opens
- Then Unsafe, dynamic agents, JNI: deprecated, then warned
- **Example:** JEP 500, ‘Prepare to Make Final Mean Final’ — today's subject
**Transition:** what JEP 500 actually changes, in practice

*~1.5 min*

## Slide 9 — JEP 500 on an LTS-only estate

**Idea:** an LTS-only shop meets JEP 500 in JDK 29, not in JDK 26 — that's the real deadline.
- JDK 25, today's LTS: the silent mutation still works
- The warn mode ships in JDK 26, a non-LTS we won't run in production; JDK 29 is the first LTS that has it
- A later release denies it outright; no version given yet
- **Example:** run the build on the newest JDK in CI only and the warnings show up years before the LTS upgrade; --illegal-final-field-mutation=deny previews the break
**Transition:** that's the JVM's promise turning into enforcement — the same ladder exists for coupling

*~2 min*

## Slide 10 — Coupling has a depth

**Idea:** chapter two — the same question, asked of our own code instead of the JVM's internals.
- Reflection reaching into private state is intrusive coupling, the deepest and worst kind
- Depth, connectivity, distance: three ways to measure how coupled you really are
**Transition:** start with why we add layers at all

*~0.25 min*

## Slide 11 — Every layer pays rent

**Idea:** a layer buys one real thing — less to hold in your head — and quietly charges for several others.
- Gain: splitting a problem lowers local cognitive load
- Cost: the dependency doesn't vanish, it moves to the abstraction
- **Example:** a clean repository layer, bypassed by a native query the day performance actually matters
**Transition:** so which dependencies are worth keeping, and at what depth?

*~2 min*

## Slide 12 — Coupling, graded by depth

**Idea:** coupling has depth, worst to best, and most code sits one level short of where it should be.
- Intrusive (worst): reflection, or casting an interface back to its implementation
- Functional (the default): a change in A quietly breaks B
- Contract (the target): the explicit signature, API, or schema itself
- **Example:** OrderService plus OrderServiceImpl, forever one implementation — the interface buys distance, not a stronger contract; and yes, Mockito mocks a concrete class just fine without it
**Transition:** van de Ven turns this into an actual formula

*~1.75 min*

## Slide 13 — Formula

**Idea:** one formula chains three ideas — how deep you're coupled, how many places feel it, and how often it changes.
- Coupling = depth × connectivity: chance of breaking, times blast radius
- Pain = (coupling + cohesion debt) × volatility — no change means no pain
- **Example:** the measurable half already exists: git churn per file, fan-in and fan-out from the import graph
**Transition:** watch the formula applied to one real architecture

*~1.5 min*

## Slide 14 — One external call, seven hops

**Idea:** hexagonal architecture is the pain formula made concrete — distance bought on purpose, for a price.
- Seven hops for one external call: adapter, anti-corruption, port, logic, port, anti-corruption, adapter
- It pays off where the boundary is volatile — the port absorbs the external change instead of the core
- **Example:** a boundary that never actually changes is pure upfront cost, with nothing to show for it
**Transition:** not dogma either way — next, how a team actually sees where it stands

*~1.75 min*

## Slide 15 — Seeing it, enforcing it

**Idea:** chapter three — the same honesty problem, now about the picture of the system instead of the code.
- Three views answer three different questions
- A view only stays true if something keeps checking it
**Transition:** start with the one everyone half-knows already

*~0.25 min*

## Slide 16 — Three views, three questions

**Idea:** no single diagram answers everything — intent, truth and shape are three different questions.
- C4: what the system is meant to be, for a given audience
- A deterministic scanner: a live map rebuilt from the code itself, every time
- **Example:** a code city turns size into a skyline — skyscrapers are god-class candidates, flat buildings are data classes
**Transition:** C4 only stays honest if something enforces it

*~2 min*

## Slide 17 — A rule the build enforces

**Idea:** a diagram only stays true if it's generated from the code, or tested against it.
- Levels 1 and 2 cover most teams; level 4 is rarely worth drawing by hand
- Same idea as the harness talk — a rule the build enforces, now pointed at architecture
- **Example:** a guardrail test catching a controller class calling the repository layer directly, skipping the service
**Transition:** and where a diagram can't show it, size and shape can

*~2 min*

## Slide 18 — What seeing the shape is worth

**Idea:** seeing shape, not just structure, measurably changed how fast and how correctly people understood code.
- A controlled study: a code city versus Eclipse plus spreadsheets, on comprehension tasks
- +24.26% correct, −12.01% time to finish
- **Example:** worth saying out loud — about 41 participants, fifteen years old, not a large or recent sample
**Transition:** enough evidence to answer the hook

*~1.5 min*
Cut if short: say only the +24.26% correctness figure, skip the time-to-finish line.

## Slide 19 — The same final field, under a future JDK, throws instead of lying....

**Idea:** a promise becomes a guarantee only when something enforces it, not when we just agree to keep it.
- final becomes enforced, one JDK at a time
- A layer or an interface is worth it only where it absorbs real volatility
- **Example:** the same three-line snippet, under a future deny mode, throws instead of silently succeeding
**Transition:** three things to carry out of this room

*~1 min*

## Slide 20 — Key takeaways

**Idea:** three habits worth taking back to your own codebase.
- final is becoming enforced — bind through constructors and records, safe in every mode
- An interface is not a stronger contract — measure volatility before adding a layer
- **Example:** generate or test your diagrams instead of just drawing them
**Transition:** one last thought before the source list

*~1 min*

## Slide 21 — The other four talks were about agents. This one was about the grou...

**Idea:** the one sanctioned link back to the rest of the series, saved for the very last word.
- Four talks asked how far to trust an agent
- This one asked how far you're coupled to anything at all, agent-written or not
**Transition:** thank you — questions, then the source list

*~0.5 min*

## Slide 22 — Sources

Full source list for everything mentioned today.
- JEPs and Javadoc for the Java chapter
- Van de Ven, Khononov and Spolsky for coupling
- C4, a live code map and the code-city study for the views chapter
**Transition:** thanks — happy to take questions

*~0.25 min*

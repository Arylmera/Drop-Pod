---
title: "Arc 3 — Context is the product — Talk Points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 3 — Context is the product — talk points

One card per slide, for improvisation delivery (no script). Each card: idea, points, a concrete example, a transition, a duration.


## Slide 1 — Context is the product

Welcome back for part three of this series. Talk two built the harness that checks an agent's output. Today's question comes earlier: before any of that runs, what did we actually hand the agent to read? The claim ahead: good context for an agent is the same thing a new hire needs on day one — the why, not just the what.

*~1 min*

## Slide 2 — Map

**Idea:** this is talk three of four on moving from chat to agentic coding.
- Talk one: does AI actually make us faster
- Talk two: the harness that makes an agent's output trustworthy
- Talk three, today: what the agent reads before it starts
- **Example:** one more stop after this — autonomy at scale, which closes the series
**Transition:** a quick look back at talk two before we start.

*~0.5 min*

## Slide 3 — Rules the build enforces, checks it cannot game, one bounded repair...

**Idea:** talk two's whole argument was that trust lives in the harness around the agent, not in the agent itself.
- A rule in prose is a suggestion; the same rule in the build is a fact
- Independent checks the agent can neither read nor edit
- One bounded repair, then a fresh verdict on the final code, never on stale evidence
- **Example:** a Maven Enforcer rule failing the build on a banned dependency, not a sentence in a rules file
**Transition:** the harness checks what comes out. Today, what goes in?

*~1 min*

## Slide 4 — The harness checks what comes out. What did we hand it to read first?

**Idea:** an agent is the fastest new hire a team has ever had, and we are about to hand it the same undocumented mess that burned out the last one.
- Could you rebuild your own system from what you just handed it, and explain why each step is mandatory
- A chatbot searching the codebase is still searching, not reading a spec
- **Example:** ask yourself right now — could a new hire onboard from what sits in your repo today
**Transition:** three chapters, following what the agent reads at each moment: before, during, after.

*~1.5 min*

## Slide 5 — Before: what you hand it to start

**Idea:** before a single line is written, the spec is the one artifact a human and an agent can read the same way.
- Spec before coding beats code during and docs after, because it alone carries intent
- The human owns the content and the why
- **Example:** a use case with acceptance criteria an agent and a JUnit suite can both consume
**Transition:** here is the table that runs through this whole talk.

*~0.3 min*

## Slide 6 — Single source of truth: before, during, after

**Idea:** truth can live in three places — the spec before coding, the code during coding, the docs after — and only one of them is reliable for both a human and an agent.
- Code always has bugs, and a bug becomes the truth the agent copies next
- Docs only count if they carry the why, not a rewrite of the code in prose
- **Example:** this same table comes back filled in at the end of the talk
**Transition:** start at the top of the table — the spec, before a line of code exists.

*~1.5 min*

## Slide 7 — The line an agent would have deleted

**Idea:** a one-line comment is the difference between an agent that keeps a fix and one that cheerfully reverts it next sprint.
- Before: one line of Javadoc, no reason, the id tiebreaker already removed once by someone being tidy
- After: a two-line comment carrying the why — MySQL's sort is not stable without it
- **Example:** losing that id tiebreaker silently broke pagination further down the line
**Transition:** that is what a good spec gives the agent before it ever opens this file.

*~2 min*

## Slide 8 — A spec is a use case, not a document

**Idea:** remember the visit-pet spec from session one — a use case is already a spec an agent and a test suite can both read.
- This is not a new stage bolted onto your tickets; it is the acceptance criteria you half-write already, made precise
- Victor Rentea's own guardrail: markdown specs for at most twenty percent of issues, not every ticket
- **Example:** acceptance criteria phrased so each one maps onto one JUnit or Cucumber test
**Transition:** a spec only works if someone asked the right questions before writing it.

*~2 min*

## Slide 9 — Interview before you dictate

**Idea:** a vague ticket pasted into a frontier model with a cold brain is how you get twenty fields you will delete seven of later.
- Ask non-technical, business questions first, so the product owner can sit in the room too
- One question at a time, a recommended answer offered, the human corrects it
- **Example:** Victor Rentea's own habit — grill before any feature touches code
**Transition:** that closes the before chapter. Now, what the agent keeps reading while it works.

*~1.5 min*

## Slide 10 — During: what it keeps reading

**Idea:** a spec gets the agent started; what it reads turn after turn is a different, and much leakier, kind of context.
- Rules files and skills — anything the model merely reads instead of the build enforcing
- These are advisory, not binding — the model can always choose to ignore them
- **Example:** a CLAUDE.md or AGENTS.md file nobody has trimmed in months
**Transition:** here is the problem with anything the model only reads.

*~0.3 min*

## Slide 11 — Rules rot: what a rule compensates for changes as the model and the...

**Idea:** talk two was about what the build enforces on the way out; this is about what the model reads on the way in, and that file needs gardening too.
- A rule nobody deletes keeps costing context long after the model stopped needing it
- Skills rot even faster than rules, because they are optional and easy to forget exist
- **Example:** a fifteen-line rules file doing three precise things beats a six-hundred-line one doing everything once
**Transition:** a question worth answering in your own head before we move on.

*~1.5 min*

## Slide 12 — Ask yourself, right now

**Idea:** rot stops being an abstract claim the moment you can answer these about your own file.
- A file that only grows, line after line, is not a rules file — it is a diary nobody edits
- Deleting a line is the only evidence the team still understands what each rule is for
- **Example:** a file that started at twenty lines and is now six hundred, every change an addition
**Transition:** the antidote is not more rules, it is less reliance on anything merely read.

*~1.5 min*
Cut if short: say only the diary line, skip the example.

## Slide 13 — Generate a diagram, don't draw one

**Idea:** an architecture diagram the agent reads is only as trustworthy as whoever last drew it, and nobody redraws on every commit.
- Ask an agent to write the deterministic script that produces the view, not to draw the view itself
- A generated diagram costs zero tokens on every later run and cannot go stale
- **Example:** Victor Rentea testing a diagram's embedded XML against the code itself
**Transition:** one more context artifact that is generated and enforced, not merely read.

*~1.5 min*

## Slide 14 — This is also context

**Idea:** a rule the build enforces is worth more to an agent than a paragraph telling it not to, because this one fails loudly instead of being politely ignored.
- The agent reads this file before touching the module, same as a human would
- It cannot silently negotiate it away — the build fails, not a suggestion
- **Example:** notification code reaching into persistence, caught the same day it's written
**Transition:** that closes during. Now, after the code exists, what can it never say on its own.

*~1.5 min*

## Slide 15 — After: what the code can never say

**Idea:** once the spec is spent and the rules are read, the code is all that's left — and code alone cannot carry the reasons.
- A class describes itself; it never describes the system it sits inside
- Every rejected design, every warning, every why is invisible unless something writes it down
- **Example:** a perfectly clean method that still can't tell you why it exists
**Transition:** Heitzmann's own line for this.

*~0.3 min*

## Slide 16 — Even perfect code describes a brick. It never describes the house.

**Idea:** "the code is the documentation" is the line every developer has said at least once, and it's wrong at exactly the altitude that matters for architecture.
- Self-documenting code is self-documenting only to the person who wrote it
- It describes one class perfectly and the whole system not at all
- **Example:** a hundred immaculate classes still won't tell a new hire, or an agent, why the system is shaped this way
**Transition:** so what altitude does each kind of writing belong at.

*~1 min*

## Slide 17 — What docs must carry

**Idea:** don't explain function internals in an architecture diagram, and don't explain architecture in a source comment — the altitude question collapses to that one line.
- Docs carry the invisible: decisions, rejected designs and why, warnings, how-tos
- An agent handed a spec and these notes behaves differently from one left to search a wiki
- **Example:** "we tried that and decided against it, because..." is an ADR an agent can actually use
**Transition:** now put the three places truth lives back together, filled in this time.

*~1.5 min*

## Slide 18 — The table, filled in

**Idea:** the same three rows from the start of this talk, now with during and after answered instead of left open.
- Spec was always the strong row; code was always the weak one
- Docs only move from a question mark to a yes when they carry context, not a restatement of the code
- **Example:** good documentation matters more, not less, because now an agent reads it too
**Transition:** one rule splits the work between the human and the model on all three rows.

*~1.5 min*

## Slide 19 — The human owns the content and the why. The model owns the form.

**Idea:** one clean split answers every question in this talk about who should write what.
- The human decides the why: the decision, the trade-off, the reason it stays this way
- The model does the form: spelling, grammar, turning notes into clear prose
- **Example:** never ask an agent to reverse-engineer intent from code it did not write
**Transition:** which answers the question this whole talk opened with.

*~1 min*

## Slide 20 — What is good context for the agent is good context for the human.

**Idea:** the hook asked what we hand the fastest new hire we've ever onboarded; the answer was in front of us the whole time.
- Specs as use cases, docs that carry the why, rules sharp enough that they do not rot
- A spec a new hire could onboard from is a spec an agent can use, and the reverse holds too
- **Example:** read your own spec back right now and ask which of the two it would actually onboard
**Transition:** three things worth keeping from today.

*~1 min*

## Slide 21 — Key takeaways

**Idea:** three things to carry out of this room, in the order they came.
- A use-case spec is the one artifact that serves both a human reader and an agent equally
- A rules file that only grows is not a rules file anymore, it's a diary — delete, don't just add
- Code describes a brick, never a house — the why still needs a human to write it down
**Transition:** next time, we ask how far we can let an agent run with all of this in place.

*~1 min*

## Slide 22 — With a harness and good context, how far can we let it run?

**Idea:** a harness from talk two and good context from today still leave one open question for next time.
- How much autonomy does a team hand over, and on what evidence
- Boundaries the agent cannot negotiate, a second AI, then a human, dimming earned not assumed
- **Example:** the series closes next with open questions for the team, not a finished recipe
**Transition:** that's the close of this one. Thank you, happy to take questions.

*~0.5 min*

## Slide 23 — Sources

All the sources for tonight are listed here, with links to replays and the primary material behind each claim. Where a quote is a paraphrase from an auto-translated transcript rather than an official caption, the notes file says so explicitly. Thanks for staying through part three — see you in two weeks for talk four.

*~0.3 min*

---
title: "Bonus: Java craft — prep notes"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Bonus: Java craft — prep notes

## Goal

Close the five-talk series with the one standalone, no-AI talk: what Devoxx said about Java and architecture itself. Delivered in **improvisation mode** (talking-points cards, no script) — 25 minutes of talk, 5 of questions. No live demo; everything stays explanation, information and worked examples.

## Thesis

Three crafts — a JVM feature, a way of grading coupling, and a set of ways to see architecture — are the same question asked three times: *is this guarantee promised, or enforced?* Reflection quietly rewriting a `final` field is the JVM's own worst-case example of **intrusive coupling**; JEP 500 is the platform finally refusing it. The coupling-depth ladder and the pain formula are how a team asks the same question of its own code. C4, a live code map and a code city are how a team keeps seeing the answer instead of trusting a photo.

## The hook and the answer

**Hook (slide 4):** "A final field can still change its value. So can the dependency you called 'just an interface.'"

**Real ending (slide 19):** The same three-line snippet, run again under a future JDK's `deny` mode, throws instead of lying. Depth you can name, distance you chose on purpose, views that are checked rather than drawn — that is what turns a promise into a guarantee at every one of the three levels.

## Key messages (3)

1. **`final` is becoming enforced.** JEP 500 moves the default from silent success to a warning (JDK 26, non-LTS — for an LTS-only estate, JDK 29), then to `deny`. Constructor and record binding were already safe, and stay safe in every mode.
2. **An interface is not a stronger contract.** The signature already was the contract; an interface only adds dependency inversion and distance. Measure volatility before adding a layer, a port, or an interface — use the pain formula as an argument, not a target.
3. **Generate or test your architecture view, don't just draw it.** A hand-drawn diagram is a photo of the day it was drawn; a scanner or a build-enforced rule stays honest as the code moves.

## Timed run-through

| # | Slide | Type | ~min |
|---|---|---|---|
| 1 | Close the Distance (title) | title | 0.5 |
| 2 | Series map | map | 0.5 |
| 3 | Previously — talk 4's dimmer | previously | 0.5 |
| 4 | Hook: a final field, an interface | statement | 1 |
| 5 | Three lines that mutate a final | code | 1.5 |
| 6 | Section 1 — Final means final | section | 0.25 |
| 7 | What reflection actually costs | cards | 2 |
| 8 | Integrity by default | steps | 1.5 |
| 9 | JEP 500, seen from an LTS estate | stats | 2 |
| 10 | Section 2 — Coupling has a depth | section | 0.25 |
| 11 | Every layer pays rent | cards | 2 |
| 12 | Coupling, graded by depth | compare | 1.75 |
| 13 | Pain = Volatility × (Coupling + Cohesion debt) | formula | 1.5 |
| 14 | One external call, seven hops | steps | 1.75 |
| 15 | Section 3 — Seeing it, enforcing it | section | 0.25 |
| 16 | Three views, three questions | cards | 2 |
| 17 | A rule the build enforces | bullets | 2 |
| 18 | What seeing the shape is worth | bars | 1.5 |
| 19 | Real ending: the same final, now throwing | statement | 1 |
| 20 | Key takeaways | takeaway | 1 |
| 21 | Close/bridge — the ground the agents stand on | statement | 0.5 |
| 22 | Sources | sources | 0.25 |

Total ≈ 25.25 min talk + 5 min questions (durations are the deck.json cards, source of truth; this table mirrors them).

**If running long:** cut slide 18 ("What seeing the shape is worth") to its headline number, skipping the rest of the bar chart's detail — a supporting-evidence slide right before the real ending, not core chapter-3 content — saving ~1 min (new total ≈24.25 min). **Pre-series:** do one timed improv read-through before the real talk (per the Open questions below, already flagged as the single biggest overrun risk).

## Facts and figures

- **Reflection costs (speed, safety, integrity, AOT/native, readability).** Java-Integrity-By-Default / Java-Reflection. Readability is kept as "for humans" only — the AI-agent framing from the source is dropped, this is the no-AI talk.
- **JEP 500 mechanics:** JDK 26 default `warn` (mutation still succeeds, one warning per module); a future release defaults to `deny` (`IllegalAccessException`); the two flags (`--illegal-final-field-mutation=deny` to preview the break, `--enable-final-field-mutation=<modules>` to grant it) are named on slide 9's card itself, since a speaker improvising with no script cannot reconstruct an exact flag name live. Constructor, record, hidden-class and `static final` binding already safe in every mode. Source: https://openjdk.org/jeps/500 (Java-Integrity-By-Default).
- **Module condition, deliberately left out.** The source notes describe it as an OR of three alternatives (same module / exported-public field / opened package). A council fact-check flagged this as likely wrong against the JEP text (which reads as an AND of setAccessible-succeeded + opened package + the mutation flag). Rather than assert either reading on stage, no card states the condition at all — see open questions below. **Verified 2026-10-13 against openjdk.org/jeps/500: the council was right — the conditions are cumulative (AND): `setAccessible(true)` succeeded, the package is open to the caller's module, and final field mutation is enabled for that module. The Devoxx notes now carry a dated correction.**
- **LTS timeline:** JDK 25 (LTS, Sept 2025) predates JEP 500 entirely. JDK 26 is a non-LTS feature release. JDK 29 (~Sept 2027 on the two-year cadence) would be the first LTS carrying it — **a projection, not an announced date**, stated as such on slide 9. **Our estate is LTS-only (operator, 2026-10-13):** we will not run JDK 26; slide 9 frames JDK 29 as our real deadline and suggests running the newest JDK in CI only (illustrative) to see the warnings early's source line. Java-Integrity-By-Default.
- **Coupling depth ladder** (intrusive → functional → contract), **"an interface is not a stronger contract"**, and the four formulas, simplified on the deck's `formula` slide to `Pain = Volatility × (Coupling + Cohesion debt)` with `Coupling = Depth × Connectivity` spoken as the sub-line (the renderer only supports one factor times a sum of terms, so the full four-line chain from the source is folded into that shape, hedged as "no units, a ranking tool, not a measurement"), plus the hexagonal seven-hop call path: Coupling-Cohesion-Distance / Hexagonal-Architecture, as told by Ties van de Ven, *The Hexagonal Hangover* (Devoxx BE 2026, no replay/slides published as of capture — hedge kept).
- **Khononov's "model coupling"** (between functional and contract) is not on van de Ven's captured slides and is left off the ladder shown on stage, per Coupling-Cohesion-Distance's own hedge.
- **C4 model** four levels, "container is not Docker", most teams need only L1+L2, CC BY 4.0: C4-Model / Architecture-Views. One tool pick (Structurizr DSL or C4-PlantUML) named directly on slide 16's card, per the sceptic's request.
- **A live, generated code map** (deterministic scanner, curation survives rescans, zero tokens for the scan itself): Groma / Architecture-Views. Kept to one mention, no origin story, no version number (young tool, v0.6.6 at capture — not worth stating as a fixed fact).
- **CodeCity evidence:** +24.26% correctness, −12.01% completion time, ICSE 2011, ~41 participants — hedge ("fifteen years old, ~41 participants") stated as a spoken line on slide 18, not buried. CodeCity. https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2010a.pdf
- **ArchUnit / guardrail callback:** one line only ("same idea as the harness talk — a rule the build enforces, now pointed at layers") — Talk 2 already used ArchUnit as its deterministic-build example, so this talk does not re-teach it. Architecture-Views.
- **Generated-diagrams-as-agent-context** framing is Talk 3's territory (per Series-Plan.md material allocation) and is not retold here — this talk keeps C4/Groma/CodeCity as views, not as agent context.

## Examples

- The three-line `final`-mutation snippet (slide 5), bookended by the real-ending slide (19) under a hypothetical future `deny` mode.
- OrderService / OrderServiceImpl as the one-implementation-forever interface, paired with the anticipated "how do I mock it then" question (Mockito mocks a concrete class fine; CGLIB/byte-buddy does the proxying).
- The hexagonal seven-hop call path as the one worked example of distance cost vs. volatility payoff.
- A described (not demoed, per the no-live-demo rule) guardrail catching a controller class calling the repository layer directly, skipping the service in between.

(No exercises or follow-up assignments: this talk is explanation and examples only, delivered in improvisation mode.)

## Likely questions and answers

- **"Without the interface, how do I mock this in a unit test?"** Mockito (via CGLIB/byte-buddy) mocks a concrete class directly; the interface isn't required for testability. Pre-loaded onto card 12.
- **"Is JEP 500 going to break our code on the next JDK bump?"** Not on JDK 25 (current LTS, unaffected); as an LTS-only shop we skip JDK 26 and meet the warning in JDK 29 (projected ~Sept 2027). Even then it's `warn` by default (`warn`, not `deny`); only a future release flips the default, and constructor/record binding is unaffected in every mode.
- **"Is [the live-code-map tool] production-ready?"** Named once, no adoption claim made on stage; the honest answer is "evaluate it on a test repo first" — not worth more slide time in a 25-minute talk.
- **"Didn't we already see ArchUnit in talk 2?"** Yes — flagged explicitly as a one-line callback, not a re-teach, with a different enforcement example (a guardrail catching a layering violation, not the harness's build rules).
- **"These CodeCity numbers are from 2011 with 41 students — does that still hold?"** Stated as a spoken hedge on the slide itself: old study, small sample, kept because the precision (not rounded) is part of why it's checkable.

## Going further

- JEP 500 itself reads well end to end: https://openjdk.org/jeps/500
- Vlad Khononov, *Balancing Coupling in Software Design* (2024) — the book behind the "model coupling" level and the distance/volatility framing.
- Joel Spolsky, "The Law of Leaky Abstractions" (2002): https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/
- c4model.com for the full C4 notation and supplementary diagrams (System Landscape, Dynamic, Deployment).
- Wettel, Lanza & Robbes, ICSE 2011, full paper: https://www.inf.usi.ch/faculty/lanza/PUBS/M/Wett2010a.pdf

## Council debate

Three critics (sceptical tech lead, narrative coach, fact-checker) reviewed the source material. Where they disagreed:

- **Spine vs. recap.** The sceptic warned the three source clusters would read as "adjacent trivia" without a connecting question, and anchored the spine on coupling depth ("how far are you really coupled, and how would you know?"), reading reflection itself as the JVM's own worst-case example of intrusive coupling. The narrative coach separately proposed "distance" (already used in talk 3 for diagram drift) stretched across all three chapters, bookended on the same mutating-`final` snippet. **Decision:** used both, not either: the title and connecting thread are the narrative coach's *distance* (the gap between a promise and what is actually true, bookended on the code demo), and the sceptic's coupling-depth question is folded in explicitly at the chapter-1→chapter-2 transition (slide 10's sub-line names reflection as intrusive coupling). Checked against the built Arc-4 deck (below): its own "next" slide already teases the bonus talk with "We promise final means final. The language doesn't enforce it" — confirming the promise/enforced framing was the right one to carry into this talk's hook and real ending, rather than inventing a new frame.
- **How much JEP detail survives in improv mode.** The sceptic wanted the two flag names and the exact module condition as verbatim sub-bullets, since a speaker without a script can't reconstruct them live. The fact-checker then found the module-condition wording in the source notes likely wrong (OR vs. the JEP's actual AND). **Decision:** keep the two flag names, written out on slide 9's card itself, but drop the module-condition detail entirely rather than risk stating a wrong "fact that cannot be improvised" on stage. See open questions.
- **AI framing.** All three agreed every AI aside from the source material (reflection "for AI agents", the live-code-map tool's origin story, "agent-written PRs", "ask an agent to write the script") must be cut, since this is the series' one explicitly no-AI talk. The fact-checker additionally flagged that one whole source talk (Rentea's architecture-guardrails talk) is itself about AI-era review. **Decision:** kept only the deterministic artifacts from that source (the generated-diagram technique, the guardrail-test idea) and dropped every framing sentence that named an agent or an AI reviewer, per the fact-checker's option (a).
- **Duplication against talks 2 and 3.** The narrative coach flagged ArchUnit (talk 2) and "generated diagrams as agent context" (talk 3) as risks. **Decision:** one spoken-line callback for ArchUnit, a different enforcement example (a layering guardrail, not a build rule); the generated-diagrams-for-agents angle is left entirely to talk 3, this talk keeps the views themselves without that framing.
- **Scope cut for time.** The sceptic estimated the three source clusters would overrun a 25-minute slot if treated at their old depth. **Decision:** collapsed the five-JEP migration checklist to three steps, dropped the live-code-map tool's origin story and version number to one mention, and limited the JEP table/flags to naming rather than drilling — per the sceptic's own cut list.
- **Employer/estate framing.** A concern (sceptic) that "LTS-only" plus "never name the employer" together narrows the room's mental model to one plausible employer type. **Decision:** every mention stayed generic ("a regulated, LTS-only estate"), never restated as "the bank" on any card.
- **Arc-4 overlap check (narrative coach's blocking concern).** `Arc-4-Trust-At-Scale/deck.json` was built elsewhere in parallel with this one. Checked directly: it contains no reflection code, no JEP numbers, no coupling/C4/CodeCity content — its only touch on this talk's material is its own "next" teaser slide ("We promise final means final. The language doesn't enforce it"), which previews the question without answering it. No duplication found; see open questions for what that confirms.

## Open questions

- **JEP 500's module condition** is left un-stated on every card in this deck, on purpose, because the two Devoxx source notes (Java-Integrity-By-Default, Java-Reflection) describe it as an OR of three alternatives, and a council fact-check suspects the real JEP text is an AND of different conditions. This deck does not edit those source notes (out of scope here, and they are shared source material for other presentations). **Needs a human pass against https://openjdk.org/jeps/500 to correct the two notes independently of this talk**, so a future deck pulling the same material doesn't inherit the same possible error. **Verified 2026-10-13 against openjdk.org/jeps/500: the council was right — the conditions are cumulative (AND): `setAccessible(true)` succeeded, the package is open to the caller's module, and final field mutation is enabled for that module. The Devoxx notes now carry a dated correction.**
- **Arc-4/Arc-5 sequencing confirmed clean**, per the check above: Talk 4 only teases the question this talk answers ("final means final" as a one-line hook, no JEP detail, no code). Nothing to change in either deck.
- **Timing is a council estimate, not a rehearsed run.** Card durations sum to ≈25.25 minutes; the presenter should do one timed read-through in improv mode before the real talk, since estimates for a 3-chapter talk this dense were flagged by the sceptic as the single biggest risk of overrun.

## Deck link

Close the Distance — deck

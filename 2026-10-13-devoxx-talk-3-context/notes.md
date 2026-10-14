---
title: "Arc 3 — Context is the product (prep notes)"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 3 — Context is the product

Talk 3 of 4. **Delivery: improvisation** — talking-points cards only (`Arc-3-Context-Talk-Points.md`), no script to read. Deck: `Arc-3-Context.html` (23 slides). Pure explanation: no live demo, no exercise to take away.

## Goal

The room leaves believing that what an agent reads *before* and *while* it works deserves the same deliberateness as the harness that checks what it produces — and that the test for good agent context is the same test as good onboarding material for a new hire.

## Thesis

What the agent needs to read is the same thing a new hire needs to read: the why, not just the what. A use-case spec is the one artifact that serves a human and an agent equally; rules and skills rot and need gardening, not endless addition; code alone can never carry the why, so documentation matters more, not less, now that an agent reads it too.

## The hook and the answer

**Hook:** "The harness checks what comes out. What did we hand it to read first?" — reframed as: your agent is the fastest new hire you've ever onboarded; what did you actually give it to read?

**Real ending (answers the hook):** What is good context for the agent is good context for the human. Specs as use cases, docs that carry the why, rules sharp enough that they do not rot. Read your own spec back — if a new hire could onboard from it, so can the agent; if not, neither can.

## Key messages (3)

1. **The spec is the source of truth before coding.** Written as a use case (actor, precondition, main flow, alternative flows, acceptance criteria), it is precise enough for both a human and an agent to act on, and the acceptance criteria become the test suite directly. Not a new heavyweight stage — the acceptance criteria a team half-writes in tickets already, made precise. Keep it proportionate: markdown specs for at most ~20% of issues, not every ticket.
2. **Rules and skills rot.** What a rule compensates for changes as the model and the harness improve; a rules file that only grows is a diary, not a rules file. This is a different problem from talk 2's harness: talk 2 was what the build enforces on the way out, this is what the model merely reads on the way in — and it needs gardening too.
3. **Code alone never carries the why.** Even perfect code describes a brick, never the house. Documentation must carry the invisible — decisions, rejected designs and why, warnings — and matters *more*, not less, now that an agent reads it alongside a human.

## Timed run-through

| Time | Slides | Content |
|---|---|---|
| 0–3 | 1–4 | Title, series map, previously (talk 2 recap), the hook — agent as fastest new hire |
| 3–10 | 5–9 | Ch. 1 — Before: the single-source-of-truth table, the ORDER BY/pagination spine artifact, spec-as-use-case, grill-me (interview before you dictate) |
| 10–15 | 10–14 | Ch. 2 — During: rules rot, the CLAUDE.md/AGENTS.md gut check, generate-don't-draw, ArchUnit as context |
| 15–20 | 15–19 | Ch. 3 — After: brick vs house, the invisible, the table filled in, human-owns-why/model-owns-form |
| 20–23 | 20–23 | Real ending, key takeaways, next time, sources |
| 23–25 | — | (buffer) |
| 25–30 | — | Questions |

**If running long:** cut slide 12 ("Ask yourself, right now") to its one closing line — a reflective interlude, not the rot thesis itself — saving ~1.5 min (new total ≈23.75 min content, more buffer before Q&A). **Pre-series:** do one timed improv read-through before the real talk.

## Facts and figures

- "Even perfect code describes a brick, never the house" and the blank-OS rebuild test — Christian Heitzmann, *Why Documentation Won't Write Itself—and AI Won't Save You*, paraphrase from an auto-translated transcript, not a verbatim quote. Documentation-Source-Of-Truth
- Single source of truth: spec (before, 👍 both) / code (during, 👎 bugs become truth) / docs (after, only if it carries context) — Heitzmann's own slide. Documentation-Source-Of-Truth
- "The human owns the content and the why; the LLM owns the form. Use AI for language, never for reverse engineering." — Heitzmann. Documentation-Source-Of-Truth
- Spec as use case (actor/precondition/main flow/alternative flows/acceptance criteria), AI Unified Process (AIUP) — Jonathan Vila López, *Agents With Seatbelts*, practice 2. Agent-Seatbelts-Best-Practices
- "Markdown specs for ≤20% of issues" — Victor Rentea, Deep Dive, from a local Whisper transcript (no official captions as of capture, timestamps ±2 min). Notes/Victor-Rentea
- Grill-me: one question at a time, business questions before technical, give a recommended answer — Matt Pocock's skill as used by Rentea. Same transcript hedge applies. Notes/Victor-Rentea
- "Rules files... rot: what a rule compensates for changes as models and harnesses improve" — Daniela Petruzalek, *State of Agentic Coding*. Agent-Stack-Layers-And-Rot
- ArchUnit rule (notification must not reach persistence) — reused from Architecture-Views / the bonus talk's material, syntax checked against ArchUnit docs, written for this session rather than screen-captured from a talk.
- "Script, not opinion" / generate-don't-draw, draw.io XML tested against the code — Victor Rentea, *Architecture Observability and Guardrails*. Architecture-Views
- ORDER BY / stable pagination needs the id as a tiebreaker (MySQL does not guarantee sort stability otherwise) — Victor Rentea, Deep Dive, an anecdote recast here as an illustrative before/after Java method (the method and comment are written for this talk, not copied from a slide).

## Examples

- **The spine artifact**: `findVisitsByOwner` — before, one line of Javadoc and no reason; after, a two-line comment carrying the *why* for the `ORDER BY ... , id` tiebreaker. One file shown once, in its "after" state, used to anchor every abstract claim in the talk (spec carries intent, docs carry the why, code alone does not).
- **Grill-me pair**: a one-line ticket ("add pagination to the owners grid") next to three grilled, business-first questions.
- **The CLAUDE.md/AGENTS.md gut check**: a rhetorical beat, not a demo — "how many lines is yours, when did anyone last delete one?"
- **ArchUnit snippet**: `notification` package forbidden from reaching `persistence`, recast as "this is also context", not just a build gate.
- **Single-source-of-truth table**: shown once near the start (spec good, code and docs open questions) and once again near the end, filled in.

## Likely questions and answers

- **"So now every ticket needs a spec document before an agent touches it?"** No — the proportionality guardrail is explicit: markdown specs for at most ~20% of issues. Most tickets stay as they are; a use-case spec earns its cost on the ones with real ambiguity or risk.
- **"Isn't this just talk 2 again — rules the build enforces?"** No: talk 2 was about what the build checks on the way *out*. This talk is about what the model merely *reads* on the way in — specs, rules files, docs — which is advisory, not enforced, and rots differently. The two are deliberately bridged, not duplicated.
- **"Didn't we already see the tool-description and spec examples in talk 1?"** Yes, deliberately referenced in one line rather than re-shown — the visit-pet spec and the tool-description seatbelt. This talk's Java example (the `findVisitsByOwner` pagination method) is new.
- **"Does ArchUnit slow the build?"** Not measured in the source material; the talk doesn't claim either way.
- **"Doesn't 'the spec is the source of truth' sound like upfront design / waterfall?"** It's the acceptance criteria a team already half-writes in tickets, made precise enough for a test suite — not a new sign-off stage. See the proportionality guardrail above.

## Going further

- Anthropic — *Effective Context Engineering for AI Agents*: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic — *Equipping Agents for the Real World with Agent Skills*: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- OWASP Top 10 for LLM Applications 2025 (GenAI Security Project): https://genai.owasp.org/llm-top-10/
- Model Context Protocol specification: https://modelcontextprotocol.io
- AI Unified Process: https://unifiedprocess.ai/ · example repo https://github.com/AI-Unified-Process/petclinic

## Council debate

Three critics (sceptical tech lead, narrative coach, fact-checker) reviewed this talk. Where they disagreed:

- **Structure.** The tech lead scoped the talk around "who writes it" vs "what it reads" as near-separate ideas; the narrative coach argued both are the *before* moment and splitting them adds a fourth beat the time budget can't afford. **Decision: one BEFORE/DURING/AFTER spine** (Heitzmann's own frame), narrative coach's structure, because it gives an improvising presenter three one-word anchors instead of a topic list.
- **Depth of Markdown-vs-AsciiDoc and the full audiences/altitudes taxonomy.** The tech lead wanted the full material mined from Documentation-Source-Of-Truth; the narrative coach and fact-checker both flagged it as a tangent with real risk of reading as the presenter's own tooling preference. **Decision: cut to one throwaway line** ("don't explain function internals in an architecture diagram, and don't explain architecture in a source comment") — no dedicated slide.
- **Duplication with talk 1.** The material-allocation table grants this talk the exact Seatbelt 2/3 (tool description, spec-as-use-case) and the rot material also used in talk 1. The fact-checker flagged this as the single biggest risk. **Decision: never re-show the findPet code or the visit-pet.yaml in full** — one-line callbacks only ("remember the visit-pet spec from session one"), and the talk's one piece of code is a *new* artifact (the `findVisitsByOwner` pagination method) built specifically to avoid repeating talk 1's examples.
- **Overlap with talk 2 on "rot".** Both the tech lead and fact-checker flagged that "rules rot, enforce in the build" sits close to talk 2's whole thesis. **Decision:** an explicit one-line bridge sentence distinguishes them ("talk two was what the build enforces on the way out, this is what the model reads on the way in") rather than re-teaching the mechanism (no kungfu skill-loader walkthrough, no three-levels-of-skill table).
- **How much architecture-views material to pull from the old "Mind the Distance" deck.** The fact-checker was explicit that the C4 levels, tool shootout, and CodeCity numbers belong to the bonus Java-craft talk now, not this one. **Decision: one slide only** (generate-don't-draw + the reused ArchUnit snippet), nothing else pulled from that chapter.
- **The blank-OS poll.** The narrative coach wanted it kept as the hook; the tech lead flagged that a literal audience poll conflicts with the "no live demo, no exercise" improvisation-mode constraint. **Decision:** kept as a rhetorical question ("ask yourself"), never an actual show-of-hands bit.
- **Jargon load.** All three critics flagged too many new terms (altitude, docs-as-code, ADR, C4, spec-driven) for an improvised 25-minute talk with no slide text to fall back on. **Decision:** the two terms the talk is built to make memorable are *spec-as-truth* and *rules rot*; everything else (altitudes, ADRs, C4) is demoted to a single supporting line each, never its own chapter.

## Deck link

`Arc-3-Context.html`

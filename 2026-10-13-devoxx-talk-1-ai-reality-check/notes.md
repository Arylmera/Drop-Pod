---
title: "Arc 1 - AI Reality - Notes"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 1 — AI Reality — Notes

## Goal

Open the "AI, the reality check" series by answering, with evidence and not with feeling, whether AI makes us better at delivering software — and name the real question (how much do we hand an agent) without yet closing it. Delivered in **improvisation mode**: talking-points cards, no script to read, no live demo, nothing to go do at your desk afterward.

## Thesis

Feeling faster is not evidence. Trust in an agent is transferred to mechanisms we build, never decreed by hope. The problem is not the model — it is what we put around it. (This talk names the gap; talks 2–4 fill it in.)

## The hook and the answer

- **Hook:** "They felt 20 % faster. The stopwatch said 19 % slower." (show of hands first)
- **Question it answers:** Does AI make us better at delivering software, and how much should we hand to an agent?
- **Real ending:** Feeling faster is not evidence; trust is transferred to mechanisms, not decreed; the problem isn't the model, it's what we put around it.
- **Teaser for talk 2:** "So what do we put around it?"

## Key messages (3)

1. A feeling is not a measurement: judge AI by lead time, failure rate and rework, not by how fast it feels.
2. Trust is transferred, not decreed: hand over control only where a test, a build or CI watches for you.
3. The brain is the bottleneck, not the keyboard: climbing the ladder spends judgment, protect it.

## Timed run-through

| # | Slide | Type | ~min |
|---|---|---|---|
| 1 | AI, the reality check | title | 1 |
| 2 | They felt 20 % faster… | statement | 2 |
| 3 | Series map | map | 1 |
| 4 | A feeling is not a measurement | section | 0.5 |
| 5 | Forecast, felt, measured | stats | 2.5 |
| 6 | The study setting, to be fair | cards | 2 |
| 7 | More output, more breakage | bars | 2 |
| 8 | A second data point: trust, not throughput | stats | 1.5 |
| 9 | "Only when you do it wrong" | quote | 1 |
| 10 | Success = AI × (…) | formula | 1.5 |
| 11 | Trust is built in stages | section | 0.5 |
| 12 | A trust ladder in seven stages | steps | 3 |
| 13 | The right stage depends on the risk | cards | 2 |
| 14 | What do we measure instead of feeling? | bullets | 1.5 |
| 15 | What the ladder doesn't climb | section | 0.5 |
| 16 | The brain is the bottleneck | bullets | 2.5 |
| 17 | The problem isn't the model… | statement (dark) | 1 |
| 18 | Key takeaways | takeaway | 1.5 |
| 19 | So what do we put around it? | next | 0.5 |
| 20 | Sources | sources | 0.5 |

Total ≈ 29 min content including structural slides; ~25 min of talk once the room's own reactions (show of hands, pauses) are subtracted from the structural minutes, leaving 5 for questions.

**If running long:** cut slide 16 ("The brain is the bottleneck") to its one closing line — it's the anecdotal support slide, not the seven-stage ladder itself — saving ~2.5 min (new total ≈26.5 min content / ~22.5 min talk). Still tight; this talk has the least slack in the series. **Pre-series:** do one timed improv read-through before the real talk.

## Facts and figures

| Figure | Value | Source | Hedge |
|---|---|---|---|
| METR forecast / felt / measured | −24 % / −20 % / +19 % | AI-Productivity-Evidence → arXiv 2507.09089 | RCT, 16 devs, 246 tasks, their own mature repos, early-2025 tools, no agentic harness |
| Generations kept | < 44 % | AI-Productivity-Evidence | From the METR paper body §C.1.4, not a separate Cursor study (the speaker's own slide mislabelled it) |
| Faros epics / throughput | +66 % / +33.7 % | AI-Productivity-Evidence → faros.ai/research/ai-acceleration-whiplash | Vendor report; Faros sells engineering-metrics tooling |
| Faros incidents/PR, review time | +243 % / ~5× | same | Review time stated as the vendor's own rounded "5×" headline, not a decimal that doesn't survive a live spot-check; churn (+861 %) dropped as the weakest, most vendor-theatre figure |
| Stack Overflow 2025 trust gap | 84 % adoption, 29 % trust (down from 40 %), 66 % "almost right" | https://survey.stackoverflow.co/2025/ai | Survey, not an RCT; independent population and method from METR |
| DORA framing | AI as amplifier of existing practice | https://dora.dev/research/2025/ | Summary read, full report not read; the unsourced "0 % DORA" figure from the old deck is dropped rather than repeated unverifiable |
| 7-stage trust ladder | — | Notes/Seven-Stages-Agentic-Coding / companion repo | Sourced to the repo, not the photographed slide; "permission vs shape" grouping is the presenter's own reading, stated as such on stage |
| Rentea reconversion material | "brain is the bottleneck", "system design stays human", 17-memory-leak anecdote | Rentea-Agentic-Engineering | His own reported claims/anecdotes, never put on the same footing as METR |

## Examples

- A generated Spring Boot method merged, then more time spent fixing the N+1 query it hid than the "felt" time saved.
- A Flyway/Liquibase migration kept at ladder stage 2 (approve every change) versus agent-generated unit tests behind a required Maven/CI gate at stage 4 — illustrative only, no mechanism detail (hooks, output contracts, MCP are talks 2 and 4's material).
- Rentea's anecdote: an agent traced 17 memory leaks from a heap dump in 30 minutes — his own claim, flagged as such, not a benchmark.

## DORA, explained

**DORA** (DevOps Research and Assessment) is a research programme, now part of Google Cloud, that has surveyed tens of thousands of software professionals every year since 2014 (the *State of DevOps* reports, then *Accelerate*). Its lasting contribution is a small set of **software delivery metrics** that predict how well a team delivers. Long known as the "four keys", DORA now lists **five**, split into throughput and instability (checked on dora.dev, 2026-10-13):

| Metric | Question | Factor |
|---|---|---|
| **Deployment frequency** | How often do we ship to production? | Throughput |
| **Change lead time** | How long from commit to running in production? | Throughput |
| **Failed deployment recovery time** | When a deployment fails, how fast do we recover? | Throughput |
| **Change fail rate** | What share of deployments need an immediate rollback or hotfix? | Instability |
| **Deployment rework rate** | What share of deployments are unplanned, forced by a production incident? | Instability |

The point of DORA for this talk: these are **team outcomes measured at the end of the delivery chain**, not individual feelings at the keyboard. That is exactly where AI's felt speed should show up — and, so far, mostly doesn't.

**What DORA said about AI** (from the source notes — summaries read, full reports not read):
- **DORA 2024:** more AI adoption was associated with slightly *lower* delivery throughput and stability — the likely origin of the "0 % DORA gain" line in Vila's talk (his slide's source was unreadable, so the deck does not quote that figure).
- **DORA 2025** (*State of AI-assisted Software Development*): throughput now rises with AI adoption, but instability persists; AI is framed as an **amplifier** of an organisation's existing strengths and dysfunctions — the same "multiplier" idea Vila closes on.
- **Faros AI** (vendor report) disputes DORA 2025's more positive reading: "engineering maturity is not a shield".

**How to use it in the talk:** when the "what do we measure instead of feeling?" question comes, answer with these metrics — change lead time and change fail rate are the two to name first; rework rate is the one that catches AI churn. Sources: AI-Productivity-Evidence, AI-Reality-Check, [dora.dev/research/2025](https://dora.dev/research/2025/), [dora.dev — DORA's software delivery metrics](https://dora.dev/guides/dora-metrics-four-keys/).

## Likely questions and answers

- **"Where's that +442 % review-time figure from?"** — Replaced with Faros's own public headline, "~5×", to avoid quoting a decimal the public page doesn't literally show.
- **"Is the 0 % DORA figure real?"** — Dropped; the old source slide was unreadable. DORA 2025 is cited directly instead, hedged as summary-read.
- **"Doesn't 'connect the agent to all your tools' contradict scoped permissions?"** — That Rentea exercise is deliberately not used here; it would contradict talk 4's sandboxing/scoped-permissions message two talks later.
- **"Are we all obsolete, then?"** — No: system design, trade-offs, availability and scalability judgment stay human at every stage of the ladder — Rentea's own counterweight.
- **"What do we measure instead of feeling?"** — The DORA four (deployment frequency, lead time, change failure rate, time to restore); one sentence, not a new practice — the how is for a later talk.

## Going further

- METR paper (open access, start with the introduction): https://arxiv.org/abs/2507.09089
- DORA 2025: https://dora.dev/research/2025/
- Faros AI, The Acceleration Whiplash: https://faros.ai/research/ai-acceleration-whiplash
- Stack Overflow Developer Survey 2025 (AI section): https://survey.stackoverflow.co/2025/ai
- Victor Rentea, Agentic Engineering Reconversion (keynote replay): https://www.youtube.com/watch?v=vAfQ4f8wIVI

## Council debate

Three critics (sceptical tech lead, narrative coach, fact-checker) reviewed the prior 23-slide script-mode deck. Where they disagreed, the decision favoured the audience and the series' own allocation table:

- **Format:** the tech lead and narrative coach agreed the old deck's prose-monologue notes directly contradict improvisation mode. Decided: every slide's notes field is now a plain talking-points card (idea, 2–4 points, one example, a transition, a duration) — no prose, no stage directions. The old `*-Script.md` is deleted.
- **Seatbelts 1–6:** the tech lead and fact-checker independently flagged that four of six seatbelts (and the full "hooks vs CI" slide) belong to talks 2–4 per the Series-Plan's allocation table, and repeating them here breaks the series' "no topic told twice" rule. Decided: all six seatbelt slides are cut from talk 1; one illustrative, mechanism-free Java/CI example (Flyway vs a CI-gated test suite) replaces them to keep the ladder tangible.
- **Chapter 3 gap:** cutting the seatbelts leaves chapter 3 thin (fact-checker's concern). Decided: refill it with the Rentea reconversion material the Series-Plan explicitly allocates to talk 1 and the old deck never used — "the brain is the bottleneck" and "system design stays human" — which also answers the narrative coach's call for a genuine real-ending sentence and the tech lead's "are we obsolete" objection.
- **Faros numbers:** the tech lead wanted the figures trimmed from five to two (keep review time, cut churn as vendor theatre); the fact-checker separately flagged the exact "+442 %" as not matching Faros's own public "5×" headline. Decided: two figures kept (incidents/PR, review time), review time restated as "~5×", churn dropped entirely.
- **Redundant "two ways to climb" slide:** the narrative coach found it repeats the ladder's own `groups` split. Decided: cut; its one surviving line ("trust is transferred, not decreed") folds into the steps slide's own transition.
- **Missing recurring mechanics:** the narrative coach flagged a missing `map` and `next` slide. Decided: both added, `map` early (slide 3, after the hook lands) and `next` near the end, using the Series-Plan's own teaser line verbatim.
- **Unsourced/weak figures:** the fact-checker flagged the 0 % DORA figure (unreadable source) and the exact Faros decimals. Decided: dropped or restated to the vendor's own public rounding rather than repeating a number no one in the room can re-derive.
- **Added, not in the old deck:** the Stack Overflow 2025 trust-gap survey (fact-checker's suggestion) as a second, independently-sourced data point reinforcing the METR felt/measured gap.
- **Never added:** Agentic Calisthenics as a checklist, "buy a personal subscription", "connect it to all your tools", and the IntelliJ+Copilot line — all three critics converged on cutting these as a numbered to-do list for people's own desks, compliance-adjacent, or internally inconsistent with later talks.

## Deck link

Arc-1-AI-Reality.html

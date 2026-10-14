---
title: "Arc 4 — Trust at scale"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 4 — Trust at scale

Series finale. Delivered in **improvisation mode**: talking-points cards only (idea, 2–4 points, one example, a transition, a duration), no script to read.

## Goal

Answer one question — once the harness works (talk 2) and the context is good (talk 3), how much autonomy do we hand an agent, and what never moves? Close the series with boundaries that don't bend, review that dims only as trust is earned, and a measurement discipline instead of a feeling.

## Thesis

Autonomy at scale needs two separate mechanisms, in order: a boundary the agent cannot negotiate (decomposition, sandboxing, MCP security — enforced structurally, not agreed to by the model), then a review regime that lightens only as trust is earned, service by service, measured by outcomes rather than felt speed. Neither substitutes for the other: a scoped agent nobody reviews is still unaccountable; a reviewed agent with no structural boundary is still one prompt from the lethal trifecta. Cross-model review is a *quality* mechanism that runs after the boundary already holds — it is explicitly not the "AI vetting AI" pattern chapter 1 rejects as a security control, because it never has to be the wall itself.

## The hook and the answer

**Hook (slide 4):** "How do we give agents more autonomy without losing control?" — opened with Šelajev's "Widowmaker" image (a 1970s Kawasaki whose engine outran its brakes, versus Jaguar's Le Mans win on disc brakes) and a room-poll line from the Docker keynote about giving an agent delete rights.

**Real ending (slide 20):** "Boundaries it cannot negotiate. A second AI, then a human, as trust is earned. Measured by outcomes." — callback to talk 1's "a feeling is not a measurement" (the 19 % slowdown), applied here to change-failure rate on agent-authored PRs rather than felt review speed.

## Key messages (3)

1. **The boundary lives outside the agent's judgment** — scoped sub-agents and MCP servers, a sandboxed machine (filesystem/network/secrets), and the same scoping carried across agent-to-agent delegation, not just agent-to-tool.
2. **Review dims gradually, and only on evidence** — a different model reviews the author model, after the structural boundary already holds; human review itself dims by risk tier (payment path never, reporting service after months clean, prototype never needed it).
3. **Outcomes decide, not vibes** — change-failure rate on agent-authored work is the metric that should move; review's cost is smaller than the incident it replaces.

## Timed run-through

| # | Slide | ~min | Beat |
|---|---|---|---|
| 1 | Title | 1 | Series finale framing |
| 2 | Map (current 4) | 1 | Where we are |
| 3 | Previously (talk 3) | 1 | Specs, docs, rules that don't rot |
| 4 | Hook + poll | 1.5 | Brakes metaphor, GitHub-token poll |
| 5 | Section 1 | 0.5 | Why autonomy needs boundaries |
| 6 | Lethal trifecta | 1 | Willison attribution |
| 7 | Three approaches that don't pass | 1 | Container / allow-deny / AI-vets-AI |
| 8 | Two-foxes anecdote | 1 | Šelajev's classifier bypass |
| 9 | Section 2 | 0.5 | The boundary it can't negotiate |
| 10 | Scoped sub-agent (Java) | 1.5 | Orders / Pay / Support decomposition |
| 11 | Sandbox essentials | 1 | Containment / filesystem / network / secrets |
| 12 | Five knights of MCP | 1.5 | Merged with the gateway/Cedar point |
| 13 | Sandbox doesn't protect the repo | 1.5 | Mount vs clone/branch; boundary travels to delegation |
| 14 | Section 3 | 0.5 | Dimming the lights |
| 15 | Second-AI rule + provocation | 1.5 | Dumb zone / smart zone |
| 16 | CI pipeline stage | 1 | Build → test → model review → gate → human |
| 17 | Dimming ladder | 1.5 | Risk-tier table |
| 18 | Cost breakdown (bars) | 1 | $15/$5/$9/$0.30, cheaper than the incident |
| 19 | Cross-model review | 1 | Review, not a boundary — resolves the chapter-1/3 tension |
| 20 | Real ending | 1.5 | Answers the hook |
| 21 | Takeaways | 1 | Three sentences |
| 22 | Open questions | 1 | Series close, genuinely open |
| 23 | Sources | — | — |

Sum ≈ 24 min talk + 5 min Q&A ≈ 30 min total.

**If running long:** cut slide 12 ("Five knights of MCP") to its gateway/Cedar point alone, skipping the knight mnemonic — a mid-chapter illustrative aside, not the boundary itself — saving ~1 min. **Pre-series:** do one timed improv read-through before the real talk.

## Facts and figures

| Fact | Hedge | Source |
|---|---|---|
| "Lethal trifecta" = autonomy + private data + external access | Coined by Simon Willison (2025-06-16), not the Docker speakers who use the term on stage | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ |
| Container isolation shares the host kernel; a coding agent's own Docker daemon is "as good as root" | As presented by Šelajev | Agent-Sandboxing |
| Two-foxes classifier bypass: refused a risky script, refused it again wrapped in a dependency module, ran it after a context clear | Šelajev's own test, reported on stage, not independently reproduced | Notes/Docker-Sandboxes-sbx |
| Kawasaki's 1970s 500cc bike had a state-of-the-art engine and no match in brakes ("the Widowmaker"); Jaguar won Le Mans on disc brakes | Šelajev's own image | Notes/Docker-Sandboxes-sbx |
| Keynote room poll (Jean-Laurent de Morlhon, Docker): few had given a GitHub token to an agent, some with repo-delete rights; the speaker then said of himself "I did it. I got caught by my security team. I got blasted." | Verified 2026-10-13 in the replay transcript (youtube.com/watch?v=mnoUXIT4nMY, ~2:02): the speaker's own words, not an attendee's |
| sbx: microVM per agent, own Docker daemon, mount/clone/branch filesystem modes, Open/Balanced/Locked-Down network policy, secret injection | Docker's own architecture docs | Agent-Sandboxing |
| Five knights of MCP: leaked secrets, server as double agent, black-box CVEs, context pollution, MCP sprawl | Jonathan Vila's own taxonomy (practice 4 in his own 0–7 numbering) | Agent-Seatbelts-Best-Practices |
| Scoped sub-agents / scoped MCP decomposition (Orders/Pay/Support) | Vila's practice 0 in his own numbering; adapted to an order-domain example for this talk | Agent-Seatbelts-Best-Practices |
| "A sandbox protects the machine. The repository is still ours to protect." | the presenter's reading of the source material, not a direct quote | Agent-Sandboxing |
| "Humans should not review AI code before a second AI does" (dumb zone / smart zone) | Rentea's own framing from the Deep Dive | Notes/Victor-Rentea |
| Cost breakdown: $15 implement / $5 adversarial review (5 reviewers) / $9 auto-fix / $0.30 guide | One demo PR, as presented by the human-review plugin author | Rentea-Agentic-Engineering |
| Dimming: "after months of consistently good output on a low-risk app, review half the lines, then half again" | Rentea's own stated rule | Notes/Victor-Rentea |
| Cross-model review (a different model reviewing the author) catches more than same-model review | Rentea's claim ("Sol reviewing Opus finds more"), not independently measured here; presented as a review-quality mechanism, distinct from the security boundary rejected in chapter 1 | Notes/Victor-Rentea |
| OWASP Top 10 for LLM Applications 2025, LLM06 Excessive Agency | Industry-standard anchor added by the council, not part of the original Devoxx talks | https://genai.owasp.org/llm-top-10/ |
| Callback: METR felt 20 % faster, measured 19 % slower | Already established in talk 1; referenced, not re-derived | AI-Productivity-Evidence |

## Examples

- Scoped sub-agent: an Orders/Pay/Support split, each its own `@Tool`-annotated MCP bean — adapted from Agent-Seatbelts practice 0 (scoped MCP decomposition), not practice 1 (tool descriptions, which belongs to talk 3's material). The Orders bean simply has no `cancelOrder` or `refund` method, so no prompt can reach one.
- ArchUnit-style non-negotiable boundary (mentioned, not shown as code): a build rule blocking a new runtime dependency without human-owned module review — carries the "rules the build enforces" instinct from talk 2 forward into "boundary the agent can't negotiate."
- CI pipeline stage: build → unit tests → second-model review against acceptance criteria → merge gate → human approval (payment-tier repos only) — a sequence, not a diagram, matching house style.
- Dimming ladder as a table, not a diagram: payment/ledger "100 % forever" and prototype "merge on green CI alone" are this talk's own illustration of the ladder's two ends, not a cited claim; the middle rung (reporting service, spot-check after clean months) is Rentea's own stated rule.

## Likely questions and answers

| Question | Answer |
|---|---|
| "Isn't a second AI reviewing the first just doubling the bill?" | The demo PR cost $15 to implement and $14.30 for the full review pass (adversarial quorum + auto-fix + guide) — smaller than the cost of one bad merge reaching production. Review uses a smarter model than the writer, so it reads a lot and writes little, staying cheap. |
| "If the reviewer AI shares the author AI's blind spot, what actually catches it?" | Nothing, if it were used as the boundary itself — that's chapter 1's rejected AI-vets-AI. Here it's a quality review that runs only after the structural boundary (chapter 2) already holds on its own; used that way, a different model catches more than the same model reviewing itself, and a human still decides for the tiers that need one. |
| "Didn't we cover scoped agents in talk 2 already?" | Talk 2 gated what comes *out* of the agent — output contracts, checks it can't game. Tonight gates what the agent can *reach* in the first place — the machine, the filesystem, the network, which other agents it can call. Different layer, same instinct. |
| "Are you endorsing Docker/JetBrains products?" | No — every named tool (sbx, ACP) is one public, documented example of a category, not a recommendation. The point is the category (a sandboxed machine, agent-to-agent delegation), not the vendor. |
| "What stops this becoming a disguised roadmap?" | The closing beat is phrased as open questions (who owns the exception process, what risk tier per service, what audit trail) for this team to answer — not a decided plan. |
| "Does dimming ever go all the way to zero review?" | Not for every service in this talk's illustration — the payment/ledger tier stays at 100 % review regardless of track record; only lower-risk services earn spot-checks, and only after a sustained clean history (Rentea's own rule for that middle rung). The two ends of the ladder are this talk's own generalisation, worth confirming before presenting as settled. |
| "Can a VM sandbox actually be escaped?" | In theory, via a hypervisor zero-day — an exploit attackers would spend on high-value production systems, not a coding sandbox. Not the practical risk; the workspace/token risk (mount mode, overbroad tokens) is. |

## Going further

- Simon Willison, "The Lethal Trifecta for AI Agents" (2025-06-16) — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- OWASP Top 10 for LLM Applications 2025, LLM06 Excessive Agency — https://genai.owasp.org/llm-top-10/
- Agent-Sandboxing · Notes/Docker-Sandboxes-sbx · Editor-Agent-Protocols · Notes/ACP-Agent-Client-Protocol · Agent-Seatbelts-Best-Practices · Rentea-Agentic-Engineering · Notes/Victor-Rentea (Deep Dive section)
- https://agentclientprotocol.com/ · https://github.com/victorrentea/human-review

## Council debate

Three critics reviewed the draft brief: a sceptical tech lead, a narrative coach, and a fact-checker. Where they disagreed, and what the build decided:

- **Whether scoped-MCP decomposition belongs in this talk at all.** The fact-checker's brief argued to cut practice 0 (scoped MCP) to a one-line callback, reasoning it was "already taught in talk 1"; the narrative coach instead wanted it folded into the sandbox chapter as this talk's own Java-team angle. Decision: the narrative coach's reading matches the Series-Plan's own material table (Arc-1 Seatbelts 1, 4 and 6 — its old 1–6 numbering for Vila's practices 0, 4 and 7 — are explicitly allocated to Talk 4, not Talk 1), so the fact-checker's premise was stale; scoped decomposition is taught here, as chapter 2's opening move, not a callback.
- **Scope of "boundary" material.** The sceptical lead wanted ACP cut almost entirely as "wire-protocol trivia"; the narrative coach wanted it kept as a proof point plus the delegation idea. Decision: dropped its own slide (the 100-file-rename stat was about token efficiency, not trust) and folded the one on-topic idea — delegation needs the same boundary as agent-to-tool — into the "sandbox doesn't protect the repo" slide. No version numbers, SDK lists or protocol taxonomy survive.
- **Docker's "four Cs" and "AI factory" narrative.** Sceptical lead and narrative coach agreed to cut; the fact-checker flagged the factory story as an unverified vendor claim anyway. Decision: cut both, say the ideas in plain sentences (containment, scope, control outside the agent) instead of a mnemonic or an unillustrated demo-shaped anecdote.
- **How much of Rentea's Deep Dive to use.** The narrative coach flagged that grill-me / warm-up / ticket-sizing belong to talk 3 per the material-allocation table, and that reusing them here would steal talk 3's thunder. Decision: this talk owns only "second AI, dimming" — section 8 of the Deep Dive — and nothing from the earlier onboarding/spec sections.
- **Lethal-trifecta attribution.** The fact-checker found the term is Simon Willison's (2025-06-16), not Šelajev's, even though the Docker talk uses it as if original. Decision: attributed to Willison on the slide; kept Šelajev's two-foxes anecdote and the Widowmaker image as his own, correctly attributed, since those *are* his.
- **Five knights vs. MCP gateway/Cedar policy.** The sceptical lead flagged these as the same idea told twice (the sandbox chapter's MCP-gateway point and the seatbelts' five knights). Decision: merged into one "five knights" cards slide; the gateway point lives inside knight 5 (sprawl) rather than as a separate beat.
- **Seatbelt numbering.** The narrative coach warned that the source file covers all eight practices in one place and flagged a real risk of a builder "copy-pasting seatbelt numbers back into Talk 4 by habit." That risk materialised during the build: a draft Java example for "the boundary it can't negotiate" was Vila's practice 1 (tool descriptions) — Talk 3's material under the series plan, not Talk 4's practice 0 (scoped MCP decomposition). Caught and rebuilt around an Orders/Pay/Support sub-agent split instead, which is actually practice 0; this note uses Vila's own 0–7 numbering throughout rather than mixing it with the old Arc-1 deck's 1–6 renumbering.
- **Chapter 1 vs. chapter 3 self-contradiction.** An early draft rejected "AI vetting AI" in chapter 1 because of shared training lineage, then answered the "shared blind spot" objection in chapter 3 by saying cross-model review solves it because the models differ — the same justification used both ways. Decision: the real distinction is boundary vs. review. Chapter 1's rejected pattern asks a model to *be* the security wall; chapter 3's cross-model review only ever runs as a quality check *after* the structural boundary (chapter 2) already holds, with a human still deciding where it matters. Rewrote both slide 7's third card and slide 19 to state that distinction explicitly, and reworded the Q&A entry to match.
- **Cross-model review as an explicit beat vs. a buried bullet.** The sceptical lead argued the "what stops a shared blind spot" objection needed its own stated beat, not a line inside the Rentea notes. Decision: gave it its own statement slide (19), directly before the real ending.
- **Governance/audit as its own slide vs. folded into open questions.** The sceptical lead wanted an explicit governance beat for a regulated audience. Decision: folded it into the open-questions slide (who can prove what an agent was allowed to touch, who owns the exception process) rather than adding another slide — satisfies the concern without turning the close into a checklist.
- **"Trust, enforced" vs. "Trust at scale" as the displayed title.** The narrative coach flagged the old deck's title as punchier and asked for an explicit decision. Decision: kept "Trust at scale" — it is the Series-Plan's official name for talk 4, and the finale should match the map/series structure the audience has seen all four talks.
- **Dimming-ladder format.** The council suggested a one-slide table; the deck schema has no generic table type, so it is rendered as a `steps` slide (payment / reporting / prototype, in that order) rather than a diagram — matches the house rule of table/sequence over diagram given the available slide types.

## Deck link

`Arc-4-Trust-At-Scale.html` (built from `deck.json` by `_build/build.js`)

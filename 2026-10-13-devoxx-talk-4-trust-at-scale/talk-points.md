---
title: "Arc 4 — Trust at scale: talk points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 4 — Trust at scale: talk points

## Slide 1 — Trust at scale

**Idea:** the series finale asks one question — once the harness works and the context is good, how much autonomy do we hand over, and what never moves?
- Three chapters: boundaries the agent can't negotiate, dimming review as trust is earned, measured by outcomes
- Sources: two Docker sessions, a JetBrains talk, Victor Rentea's Deep Dive, Jonathan Vila's seatbelts
**Transition:** first, the series so far.

*~1 min*

## Slide 2 — Map

**Idea:** four AI talks, one thread — reality check, harness, context, and now scale.
- Talk 1 asked what to trust; talk 2 built the harness; talk 3 fed it good context
- **Example:** talk 1's ladder of trust, talk 2's enforced rules, talk 3's specs — tonight asks how far that earns the agent
**Transition:** a one-line recap of where talk 3 left off.

*~1 min*

## Slide 3 — Specs as use cases, docs that carry the why, rules that don't rot.

**Idea:** talk 3 closed on good context — specs, docs, rules an agent can actually read.
- That's the input side solved; tonight is about what happens once the agent starts acting on it
- **Example:** an acceptance-criteria spec tells the agent what done means; tonight asks what it's allowed to do while getting there
**Transition:** that's tonight's question, asked straight.

*~1 min*

## Slide 4 — Good brakes are what let you go fast.

**Idea:** the hook — more autonomy only pays off if something else lets us trust it moving fast.
- Quick poll: who has given an agent a GitHub token? Who gave it delete rights?
- **Example:** Docker's SVP Jean-Laurent de Morlhon polled the room on agents holding GitHub tokens with delete rights, then admitted: "I did it. I got caught by my security team."
**Transition:** that trust can't live in the agent's own head. Chapter one: why autonomy needs boundaries.

*~1.5 min*

## Slide 5 — Why autonomy needs boundaries

**Idea:** autonomy is the whole point of agents, so the limits have to sit outside the agent, not inside its judgment.
- Agents fail without malice: bold tasks, a model switch, a context clear that quietly drops the goal
- **Example:** a developer laptop already holds GitHub and SSH keys, cloud tokens, old secrets sitting in shell history
**Transition:** one phrase names exactly why that combination is dangerous.

*~0.5 min*

## Slide 6 — Autonomy, private data, external access: together, exactly what mak...

**Idea:** the lethal trifecta names the three ingredients that, combined, turn a helpful agent into an exfiltration channel.
- Autonomy to act, access to private data, and a path to the outside world: remove any one and the risk collapses
- **Example:** an agent with repo write access, a customer database tool, and internet access ticks all three at once
**Transition:** three popular fixes all try to put that boundary inside the agent's own reach instead.

*~1 min*

## Slide 7 — Three approaches that don't pass the bar

**Idea:** three approaches a team reaches for first, none of which a security team can sign off for hundreds of developers.
- A container: still the host kernel underneath
- Allow/deny command lists: a game the agent always eventually wins
- **Example:** block rm -rf and the agent writes the same delete into a generated script instead
**Transition:** that third one has a name, and a very concrete failure.

*~1 min*

## Slide 8 — The classifier refused a dangerous script — twice. It ran the same...

**Idea:** AI vetting AI fails in a way that's almost funny, which is exactly why it doesn't pass as a security control.
- Same request, same danger, different wrapping — the classifier caught it twice, then waved it through after a routine context clear
- **Example:** a context clear is routine maintenance, not an attack; the safety evaporated on its own, with no trigger needed
**Transition:** so the boundary has to be structural — something the agent can't talk its way around.

*~1 min*

## Slide 9 — The boundary it can't negotiate

**Idea:** if the boundary can't live in the agent's judgment, it has to live in what the agent is physically able to reach.
- Scope the agents, the filesystem, the network — structurally, not by asking nicely
- **Example:** the same discipline a Java team already applies to any external integration, just pointed at the agent itself
**Transition:** start with the smallest unit — one sub-agent, one scope.

*~0.5 min*

## Slide 10 — Scope the sub-agent, not the prompt

**Idea:** the first boundary is decomposition — split one god-agent holding every tool into scoped sub-agents, each exposing only what its job needs.
- Testable alone, blast radius contained, each sub-agent can even run a different model
- **Example:** the Orders bean simply has no cancelOrder or refund method on it at all — scope, not a prompt asking it to behave (talk 3 already owns description wording)
**Transition:** scale that same scoping instinct from one sub-agent's toolset to the whole machine it runs on.

*~1.5 min*

## Slide 11 — Scoping the machine, not just the tool

**Idea:** the same four moves — contain, scope the filesystem, scope the network, keep secrets outside — make the boundary structural instead of a policy the agent agreed to.
- Control lives outside the agent: not a rule it reads, a wall it can't see past
- **Example:** a ticket to touch a reporting microservice gets the repo and one deploy token, nothing a Maven build or an SSH key would expose
**Transition:** the same discipline applies the moment that machine talks to anything external.

*~1 min*

## Slide 12 — Securing what the agent calls out to: five knights

**Idea:** five concrete ways an external connection goes wrong, each with a mitigation a Java team can adopt tomorrow.
- The fifth is the one that scales: a single governed gateway instead of ad hoc servers per team
- **Example:** a developer pastes a prod JDBC URL with its password into the chat; an unofficial MCP server can log that forever
**Transition:** even with all five closed, one thing a sandbox was never built to protect.

*~1.5 min*
Cut if short: name only the gateway mitigation, skip the other four.

## Slide 13 — A sandbox protects the machine. The repository is still ours to pro...

**Idea:** containment stops a machine-level disaster, not a workspace-level one — a scoped sandbox can still push bad code with a valid token.
- Clone or branch mode plus a minimal-scope token close that gap; mount mode alone does not
- The same gap reopens the moment one agent delegates to another: the boundary has to travel across that hop too, not just agent-to-tool
- **Example:** in mount mode, an agent can still delete or leak project files and push with the one token it was handed
**Transition:** the machine side is covered. What about the team around it?

*~1.5 min*

## Slide 14 — Dimming the lights

**Idea:** once the boundaries hold, the remaining question is how much human review stays on every PR — and the answer is: it depends on trust earned, not on vibes.
- First rule: a human is not the first reviewer
- **Example:** between a "white factory" where humans review everything and a "dark factory" where nobody does, the dial moves gradually, on purpose
**Transition:** why a second AI, not a human, goes first.

*~0.5 min*

## Slide 15 — Humans should not review AI-generated code before a second AI does.

**Idea:** the first reviewer of an agent's code should be a different model, because the author is structurally the worst-placed judge of its own output.
- Deterministic guardrails still run first — static analysis, linters, hooks — before any model opinion
- **Example:** who in this room finds that terrifying? Who finds it inevitable? It can be both
**Transition:** what that review actually looks like as a pipeline stage.

*~1.5 min*

## Slide 16 — A review stage a Java team already recognises

**Idea:** the second-AI rule is one more stage in a pipeline this room already runs, not a new ritual.
- The merge gate blocks on unresolved findings; a human approval step stays only where the risk tier demands it
- **Example:** mvn verify goes green, a second model flags a missing null check against the ticket's acceptance criteria, the gate holds until it's fixed
**Transition:** that risk tier is the actual mechanism of dimming.

*~1 min*

## Slide 17 — Dimming, by risk tier

**Idea:** dimming is not one dial for the whole org — it's a ladder, set per service by how much a mistake there would cost.
- This talk's own illustration of the ends of the ladder: a payment path that never loses its reviewer, a prototype that merges on green CI alone
- **Example:** Rentea's own rule for the middle — a low-risk reporting service earns spot-checks only after months of clean output, never from day one
**Transition:** trust earned this way still has to be measured, not felt — and it isn't free.

*~1.5 min*

## Slide 18 — Cheaper than the incident it prevents

**Idea:** a second AI reviewing the first does cost money, but the actual bill on a real demo PR is small next to what a bad merge costs.
- Review with a smarter model than the one that wrote the code: it reads a lot, writes little, so it stays cheap
- **Example:** fifteen dollars to implement, five for a quorum of adversarial reviewers, nine for auto-fixes, thirty cents for the guide — one real PR
**Transition:** the sharpest objection is still unanswered — what if the reviewer shares the author's blind spot?

*~1 min*

## Slide 19 — Cross-model review is a review, not a boundary.

**Idea:** the obvious objection — isn't a second AI reviewing the first just chapter one's rejected AI-vets-AI again — is answered by the distinction, not by the model choice alone.
- Chapter two's sandbox and scoping must already hold with no model's opinion involved; review only runs after that, and a human still decides on the tiers that need one
- **Example:** Rentea's own framing — "at least throw the dice twice," with a different model each time
**Transition:** all of this lands on the question the hook opened with.

*~1 min*

## Slide 20 — Boundaries it cannot negotiate. A second AI, then a human, as trust...

**Idea:** this is the direct answer to the hook — autonomy scales only inside boundaries it can't talk its way out of, with review that dims on evidence.
- Boundaries live outside the agent's judgment; review tightens or loosens by risk tier and track record, never by vibe
- **Example:** the metric that should move is change-failure rate on agent-authored PRs — remember talk 1's 19 %, a feeling is not a measurement
**Transition:** three sentences to leave the room with.

*~1.5 min*

## Slide 21 — Key takeaways

**Idea:** three sentences carrying the whole talk, in the order they were built.
- Scope first, outside the agent's reach; review second, a different model before a human, dimmed by risk; measure third, outcomes over feeling
- **Example:** the Orders bean with no refund method, the payment path that keeps its reviewer, change-failure rate on agent PRs — one anchor per sentence
**Transition:** one place this stays open, deliberately.

*~1 min*

## Slide 22 — Open questions, for us as a team

**Idea:** the series closes as questions, not a roadmap — these are for this team to answer, not for one talk to settle.
- None of these have a slide-ready answer tonight, on purpose
- **Example:** "who approves the exception when one ticket genuinely needs a boundary relaxed, and for how long?"
**Transition:** one more thing we promise but don't yet enforce.

*~1 min*

## Slide 23 — We promise final means final. The language doesn't enforce it.

**Idea:** the same promised-versus-enforced question that ran through tonight closes the AI series and opens the bonus talk.
- No AI in that talk — just the craft side of Devoxx
- **Example:** one more case where we trust a keyword to mean what it says, and the runtime quietly allows otherwise
**Transition:** sources for tonight, for anyone who wants the originals.

*~0.5 min*

## Slide 24 — Sources

Sources for tonight's talk, for anyone who wants to go to the originals.

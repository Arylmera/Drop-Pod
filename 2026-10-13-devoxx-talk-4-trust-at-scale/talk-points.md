---
title: "Arc 4 — Trust at scale: talk points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---



# Arc 4 — Trust at scale — Speaker text

One card per slide: **fil rouge** (bold line), outline, full text to say, transition. Same text as the presenter window (S).
Timing is flexible, 10 to 20 min. **Short route (~10 min):** CORE slides, plus only the *Short route* line on IF TIME slides. **Full route:** ~20 min.

## Slide 1 — Trust at scale  ·  CORE (full ~0.5 min, short ~0.5 min)

**▶ Last question of the series: how far can an agent run without us watching?**

- Back from **Devoxx Belgium 2026**, talk 4 of 4, the **finale**
- Three chapters: **why boundaries** · **the boundary it can't negotiate** · **dimming the lights**

> Hi everyone, and welcome to the **last talk** of the series.
>
> So far, we have a **harness** that checks what comes out of the agent, and **good context** going in. Today's question: once all that works, **how much autonomy** do we hand over? And what should **never move**?
>
> Three chapters. **Why** autonomy needs boundaries. **The boundary** the agent can't negotiate. And **dimming the lights**: reviewing less, but only as trust is earned.
>
> As always, this is **my take**. If you see it differently, **just say so**.
>

**→** First, where we are in the series.

## Slide 2 — Map  ·  IF TIME (full ~0.5 min, short ~0.1 min)

**▶ Four talks, one spine. Today closes it.**

- 01 **reality check** · 02 **the harness** · 03 **context** · 04 **trust at scale** (today)

> Just a quick map.
>
> Talk one asked **what to trust**: remember the **trust ladder**. Talk two built **the harness**. Talk three gave the agent **good context**. And today: **trust at scale**, so how far all of that lets the agent run.
>
> And as always, **each talk stands on its own**.
>

*Short route:* Last talk of four, and it stands on its own. Let's go.

**→** A quick reminder of where we left off.

## Slide 3 — Specs as use cases, docs that carry the why, rules that don't rot.  ·  CORE (full ~0.8 min, short ~0.4 min)

**▶ Good context is covered. Now: what is the agent allowed to do?**

- Talk 3: specs as **use cases**, docs that carry **the why**, rules that **don't rot**
- Good context for the agent is **good context for the human**

> Last time was about **context**: what the agent reads.
>
> Specs written as **use cases**. Docs that carry **the why**. Rules short enough that **they don't rot**. And the conclusion: **good context for the agent is good context for the human**.
>
> So the input side is covered. A good spec tells the agent **what done means**. Today: what is it **allowed to do** while it gets there?
>

*Short route:* Last time: good context, specs, docs with the why. Today: what is the agent allowed to do?

**→** Let's ask the question straight.

## Slide 4 — Good brakes are what let you go fast.  ·  CORE (full ~1.3 min, short ~0.8 min)

**▶ Good brakes are what let you go fast.**

- Kawasaki's 1970s superbike: an engine **ahead of its brakes**
- Jaguar won Le Mans on **disc brakes**
- Show of hands (remote: **reaction or chat**): who gave an agent a **GitHub token**? With **delete rights**?

> An image from **Oleg Šelajev**, from Docker, at Devoxx. In the seventies, Kawasaki built a superbike with an amazing engine, and brakes that **couldn't keep up**. Around the same time, Jaguar won **Le Mans** with **disc brakes**. Not the biggest engine. The best **brakes**.
>
> Because **good brakes are what let you go fast**. Same with agents: more autonomy only pays off if something lets us **trust it at speed**.
>
> So, a quick show of hands. In the room, raise your hand; remote, use a reaction or the chat. **Who has given an agent a GitHub token?** And who gave it one with **delete rights**?
>
> At the Devoxx keynote, **Jean-Laurent de Morlhon**, from Docker, asked the same thing. And then he said about himself: "**I did it. I got caught by my security team.**"
>
> So the question for today: **how much autonomy** can we give an agent, **without losing control**?
>

*Short route:* Good brakes are what let you go fast. Who gave an agent a GitHub token with delete rights? Even a Docker executive did, and got caught.

**→** Chapter one: why autonomy needs boundaries.

## Slide 5 — Why autonomy needs boundaries  ·  CORE (full ~0.4 min, short ~0.2 min)

**▶ What makes an agent productive is exactly what lets it leak.**

- Agents fail **without malice**: a bold task, a model switch, a **context clear**
- A dev laptop already holds **SSH keys**, **cloud tokens**, old secrets in the **shell history**

> Chapter one: **why autonomy needs boundaries**.
>
> An agent doesn't need to be **evil** to cause damage. A bold task, a model switch, a **context clear** that quietly drops the goal. That's enough.
>
> And think about what sits on a developer laptop: **SSH keys**, GitHub tokens, **cloud credentials**, old secrets in the **shell history**. All within reach.
>

**→** There's a name for that dangerous combination.

## Slide 6 — Autonomy, private data, external access: together, exactly what makes an agent useful — and lets it leak.  ·  CORE (full ~1.2 min, short ~0.7 min)

**▶ The lethal trifecta: autonomy, private data, external access.**

- **Simon Willison**, 2025
- **Autonomy** to act · **private data** · a path to **the outside**
- Remove **any one**, and the risk collapses

> **Simon Willison** gave it a name in 2025: **the lethal trifecta**.
>
> Three things. **Autonomy**: the agent can act. **Private data**: it can read things that matter. And **external access**: it can talk to the outside world.
>
> And here's the uncomfortable part: those three together are **exactly what makes an agent useful**. And exactly what lets it **leak**.
>
> An agent with write access to the repo, a tool on the customer database, and internet access? **All three**, at once.
>
> The good news: **remove any one** of the three, and the risk **collapses**.
>

*Short route:* Autonomy, private data, external access: the lethal trifecta. Exactly what makes an agent useful, and what lets it leak. Remove one and the risk collapses.

**→** So how do teams try to control it? Three popular answers.

## Slide 7 — Three approaches that don't pass the bar  ·  CORE (full ~1.2 min, short ~0.5 min)

**▶ Three common fixes that don't pass the bar.**

- **A container**: shares the host kernel; hand it your Docker daemon and it's **as good as root**
- **Allow/deny lists**: block rm -rf, and it writes it **into a script**
- **AI vetting the AI**: an **opinion**, not a wall

> Three things teams reach for first. And none of them is something a security team can sign off **for hundreds of developers**.
>
> One: **a container**. Sounds safe. But a container **shares the host kernel**. And a coding agent needs Docker for its tests, Testcontainers for example. So you hand it the host's Docker daemon. And that's **as good as root**.
>
> Two: **allow and deny lists** of commands. It's **cat and mouse**. Block rm -rf, and the agent writes the same delete **into a generated script**. A false sense of security.
>
> Three: **an AI watching the AI**. A classifier model that checks what the acting model does. But that's **an opinion**, not a wall. And an opinion **can be talked around**.
>

*Short route:* A container shares the kernel. Deny lists get worked around. An AI watching the AI is an opinion, not a wall.

**→** That last one failed in a way that's almost funny.

## Slide 8 — The classifier refused a dangerous script — twice. It ran the same script right after a context clear.  ·  CORE (full ~1 min, short ~0.5 min)

**▶ The classifier said no twice. Then a context clear, and it said yes.**

- **Oleg Šelajev**'s own test (Docker), reported on stage
- Refused, refused again in a new wrapping, **ran after a context clear**
- "**Two foxes** whispering about a henhouse"

> Oleg Šelajev tried this himself, with an agent in **auto mode**, protected by a classifier.
>
> He asked for a **dangerous script**. Refused. He wrapped it differently, inside a dependency. **Refused again**. Good.
>
> Then a **context clear**. Routine maintenance, not an attack. Same script: **it ran**.
>
> His image: "**two foxes whispering about a henhouse**". The safety didn't even need an attacker. It **evaporated on its own**.
>
> So the boundary has to be **structural**. Something the agent **can't talk its way around**.
>

*Short route:* Refused twice, then it ran the script after a routine context clear. Two foxes guarding a henhouse. The boundary has to be structural.

**→** Chapter two: the boundary it can't negotiate.

## Slide 9 — The boundary it can't negotiate  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ Scope what it can reach, before it ever acts.**

- Scope the **agents**, the **filesystem**, the **network**
- Structurally, **not by asking nicely**

> Chapter two: **the boundary it can't negotiate**.
>
> If the boundary can't live in the agent's judgment, it has to live in **what the agent can physically reach**. The agents, the filesystem, the network. **Structurally**, not by asking nicely.
>

**→** Let's start small: one sub-agent.

## Slide 10 — Scope the sub-agent, not the prompt  ·  CORE (full ~1.3 min, short ~0.7 min)

**▶ The method doesn't exist, so no prompt can reach it.**

- A supervisor delegates to **Orders**, **Pay**, **Support** sub-agents, each with its **own MCP server**
- The Orders bean has **no cancelOrder, no refund**
- **Blast radius** contained, each one testable **alone** (Jonathan Vila López, "Agents With Seatbelts")

> The first boundary is **decomposition**. Instead of one big agent holding **every tool**, you split it.
>
> A supervisor delegates to **scoped sub-agents**: Orders, Pay, Support. Each one has **its own MCP server**, exposing only **what its job needs**.
>
> Look at the Orders tools here. It can **find an order**. That's it. There's **no cancelOrder**, **no refund** method on this bean. Not "please don't refund". The method **doesn't exist**.
>
> So a mistake in Orders has **nothing to reach** in Pay. The blast radius is **contained**, and each sub-agent is **testable on its own**. This comes from **Jonathan Vila López**'s "Agents With Seatbelts".
>

*Short route:* Split the agent into scoped sub-agents. The Orders bean has no refund method: not a rule, the method doesn't exist.

**→** Same instinct, now for the whole machine.

## Slide 11 — Scoping the machine, not just the tool  ·  CORE (full ~1.3 min, short ~0.7 min)

**▶ Control lives outside the agent: a wall, not a rule it reads.**

- **Containment**: its own kernel, a micro-VM, its own Docker daemon
- **Filesystem**: only the chosen folders, never **~/.ssh** or **settings.xml**
- **Network**: **deny by default**, logged
- **Secrets never inside**: a dummy value, swapped **on the way out**

> Now scale that to the machine the agent runs on. Four moves. Docker showed them with their sandboxes, but the idea is **general**.
>
> **Containment**: each agent gets **its own kernel**. A micro-VM, not a shared container. With **its own Docker daemon** inside, for tests and builds.
>
> **Filesystem scope**: only the folders the task needs. A ticket on a reporting service should **never see** your **~/.ssh**, or your Maven **settings.xml**.
>
> **Network**: **deny by default**. Only the registries and services the task needs, and every call is **logged**.
>
> And **secrets never go inside**. The agent gets a **dummy value**, and the real one is swapped in **on the way out**. The agent can't print a secret it **never holds**.
>

*Short route:* Its own kernel, only the needed folders, network denied by default, secrets swapped in on the way out. A wall, not a rule.

**→** Same discipline for everything the agent calls out to.

## Slide 12 — Securing what the agent calls out to: five knights  ·  IF TIME (full ~1.3 min, short ~0.3 min)

**▶ Every server the agent calls is part of the boundary.**

- **Leaked secrets** · a **double agent** server · **black-box CVEs** · **context pollution** · **sprawl**
- The fix that scales: **one governed gateway** (Jonathan Vila López, "The 5 Knights of the MCP Apocalypse")

> Jonathan Vila López calls these **the five knights** of the MCP apocalypse. Five ways an external connection goes wrong.
>
> One: **leaked secrets**. Paste a prod password in the chat, and it can sit in a server's **logs forever**.
>
> Two: a server as a **double agent**. An unofficial copy that siphons keys and data. Check it's the **official** one.
>
> Three: **black-box CVEs**. A vulnerable library inside the server. Run your usual **SCA and DAST** on it.
>
> Four: **context pollution**. A hundred pages fetched for one paragraph, or injected data read as fact. Use **one scoped server** per sub-agent.
>
> Five: **sprawl**. Ten servers, three doing the same job, no shared policy. The answer that scales: **one governed gateway**.
>

*Short route:* Five ways external servers go wrong. The fix that scales: one governed gateway, not ten ad hoc servers.

**→** Even with all five closed, there's one thing a sandbox doesn't protect.

## Slide 13 — A sandbox protects the machine. The repository is still ours to protect.  ·  IF TIME (full ~1.2 min, short ~0.3 min)

**▶ A sandbox protects the machine. The repository is still ours to protect.**

- **Mount mode**: it can still delete, leak, and **push with its token**
- Use **clone or branch** mode, and a **minimal-scope token**
- The boundary must follow **every delegation**, agent to agent

> A sandbox stops a disaster on **the machine**. Not in **the workspace**.
>
> If you **mount** your project folder into the sandbox, the agent can still **delete** files, **leak** them, and **push** bad code with the token you gave it.
>
> So use **clone or branch mode**, and give it a token with the **smallest scope** possible.
>
> And one more: the moment one agent **delegates** to another agent, the boundary has to **travel across that hop** too. Not just from agent to tool.
>

*Short route:* A sandbox protects the machine, not the repo. Clone or branch mode, and a minimal token.

**→** The machine side is covered. Now, the team around it.

## Slide 14 — Dimming the lights  ·  CORE (full ~0.4 min, short ~0.2 min)

**▶ Review less, only as the agent earns it.**

- From a **white factory** (humans review everything) to a **dark factory** (nobody does)
- The dial moves **gradually**, **on purpose**

> Chapter three: **dimming the lights**. The phrase comes from **Victor Rentea**'s Deep Dive at Devoxx.
>
> Imagine a dial. At one end, a **white factory**: humans review **everything**. At the other end, a **dark factory**: **nobody** reviews anything.
>
> The question is how far to turn it. And the answer: **gradually, on purpose**, based on **trust earned**. Not on vibes.
>

**→** And the first rule surprised me.

## Slide 15 — Humans should not review AI-generated code before a second AI does.  ·  CORE (full ~1.2 min, short ~0.7 min)

**▶ A second AI reviews first. Then the human.**

- The author agent is in its **"dumb zone"**; a fresh reviewer is in the **"smart zone"**
- **Deterministic checks** still run first: static analysis, linters, hooks
- "At least **throw the dice twice**" (Victor Rentea)

> Victor Rentea's rule: **humans should not review AI-generated code before a second AI does**.
>
> Why? The agent that wrote the code is deep in its own session, committed to its own choices. He calls it **the dumb zone**. A **fresh** reviewer, with a clean context, is in **the smart zone**.
>
> And of course, the **deterministic checks** still run first: static analysis, linters, the harness from talk two. **Before** any model gives an opinion.
>
> His phrase: "**at least throw the dice twice**".
>
> Who finds that **terrifying**? Who finds it **inevitable**? Honestly, it can be **both**.
>

*Short route:* A second AI reviews before a human does: the author is in its dumb zone, a fresh reviewer is in the smart zone.

**→** So what does that look like in a pipeline?

## Slide 16 — A review stage a Java team already recognises  ·  IF TIME (full ~0.8 min, short skip)

**▶ One more stage in a pipeline we already run.**

- **mvn verify**, same as today
- **Second-model review** against the ticket's **acceptance criteria**
- **Merge gate** blocks on open findings · **human approval** only where the risk demands it

> And it's not a new ritual. It's **one more stage** in a pipeline we already know.
>
> Build and unit tests: **mvn verify**, same as today. Then a **different model** scores the diff against the ticket's **acceptance criteria**, and writes its findings on the PR.
>
> Then a **merge gate**: an open finding above a threshold **blocks the merge**. And a **human approval**, only for the repos that still need **100 % review**, like the payment path.
>
> For example: mvn verify is green, the second model flags a **missing null check** against the acceptance criteria, and the gate **holds** until it's fixed.
>

*Short route:* Skip.

**→** That "repos that still need review" part is the real mechanism of dimming.

## Slide 17 — Dimming, by risk tier  ·  CORE (full ~1.3 min, short ~0.7 min)

**▶ Dimming is a ladder per service, set by what a mistake costs.**

- **Payment / ledger**: 100 % human review, **forever**
- **Reporting service**: spot-checks after **months of clean output**
- **Throwaway prototype**: merge on **green CI**

> Dimming isn't **one dial** for the whole company. It's a **ladder**, set **per service**, by how much **a mistake there would cost**.
>
> At the top: **payment, ledger**. **100 % human review**, forever. No amount of clean history changes that.
>
> In the middle: a **reporting service**. Rentea's rule: after **months** of consistently clean output, review **half the lines**. Then half again. **Never from day one**.
>
> At the bottom: a **throwaway prototype**. Merge on **green CI** alone.
>
> Remember the **trust ladder** from talk one? Same idea, applied to **review**.
>

*Short route:* Payment: 100 % review, forever. Reporting: spot-checks after months of clean output. Prototype: merge on green CI.

**→** And yes, a second AI costs money. How much?

## Slide 18 — Cheaper than the incident it prevents  ·  IF TIME (full ~0.8 min, short ~0.2 min)

**▶ Cheaper than the incident it prevents.**

- One demo PR: **$15** implement · **$5** review (5 reviewers) · **$9** auto-fixes · **$0.30** guide
- Review with a **smarter model**: it reads a lot, writes little

> Here's a real bill, from Victor Rentea's demo, on **one PR**.
>
> **Fifteen dollars** to implement. **Five** for a review by five adversarial reviewers. **Nine** for the auto-fixes. And **thirty cents** for the guide.
>
> So about fifteen dollars for the whole review side. Compare that to **one bad merge** reaching production.
>
> And a tip: review with a **smarter model** than the one that wrote the code. A reviewer **reads a lot and writes little**, so it stays **cheap**.
>

*Short route:* One PR: 15 dollars to write it, about 15 to review and fix it. Cheaper than one bad merge.

**→** Now, the sharpest objection.

## Slide 19 — Cross-model review is a review, not a boundary.  ·  IF TIME (full ~1 min, short ~0.3 min)

**▶ Cross-model review is a review, not a boundary.**

- Isn't this **AI vetting AI** again, from chapter one?
- **No**: the sandbox from chapter two must hold **on its own**
- A **different model** finds more than the same model reviewing itself

> You might say: wait. In chapter one, you said **AI vetting AI** doesn't work. And now you want a second AI?
>
> The difference: in chapter one, the AI was used as **the boundary**. The only wall. Here, it's **a review**. A quality check.
>
> The boundary is still **the sandbox and the scoping** from chapter two. They hold **on their own**, with **no model's opinion** involved. The review only runs **after** that. And for the tiers that need it, a **human still decides**.
>
> And Rentea's claim: a **different model** reviewing finds **more** than the same model reviewing itself. Throw the dice twice, with a **different die**.
>

*Short route:* AI as the wall fails. AI as a review, behind a real wall, helps. The sandbox holds on its own.

**→** So let's answer the question we started with.

## Slide 20 — Boundaries it cannot negotiate. A second AI, then a human, as trust is earned. Measured by outcomes.  ·  CORE (full ~1 min, short ~0.6 min)

**▶ Boundaries it can't negotiate. Review dimmed as trust is earned. Judged by outcomes.**

- Boundaries live **outside the agent's judgment**
- Review moves by **risk tier** and **track record**, never by vibe
- Remember the **19 %**: measure the **change-failure rate**, not felt speed

> How far can an agent run without us watching? Here's my answer.
>
> **Boundaries it can't negotiate**. They live **outside its judgment**: the machine, the files, the network, the secrets.
>
> **A second AI, then a human**. And that review is **dimmed** only as trust is **earned**, by risk tier and track record.
>
> And all of it **measured by outcomes**. Remember talk one: people **felt 20 % faster** and were **19 % slower**. A feeling is **not a measurement**. What should move is the **change-failure rate** on agent-written PRs.
>

*Short route:* Boundaries it can't negotiate, review dimmed as trust is earned, measured by change-failure rate, not by feeling.

**→** Three things to take home.

## Slide 21 — Key takeaways  ·  CORE (full ~1 min, short ~0.7 min)

**▶ Three things to take home.**

- **Scope** what it can reach, **before** it acts
- A **different model** before the human; dim **by risk tier**
- Judge by **outcomes**, not felt speed

> If you remember only three things.
>
> One: **scope what it can reach**. Files, network, secrets, tools. **Before** it acts. And nobody edits that scope, **not even the agent**.
>
> Two: put **a different model** between the author agent and the human. And dim human review **by risk tier**, never just because it **feels** fine.
>
> Three: **judge by outcomes**. Change-failure rate, not felt speed. The same measure as **every talk** in this series.
>

**→** And to close, some questions for us.

## Slide 22 — Open questions, for us as a team  ·  CORE (full ~1 min, short ~0.5 min)

**▶ The series ends with questions for us, not a roadmap.**

- Who owns the **exception process** when a boundary must flex?
- What **risk tier** is each of our services, and **who decides**?
- What **audit trail** proves what an agent could touch?
- Which services have **earned** lighter review, and **on what evidence**?

> I don't want to end with a recipe. I want to end with **questions for us, as a team**.
>
> When one ticket genuinely needs a boundary relaxed: **who approves the exception**, and for how long?
>
> What **risk tier** does each of our services sit at? And **who decides**?
>
> After the fact, what **audit trail** proves what an agent was **allowed to touch**?
>
> And which of our services has **earned** a lighter review, and **on what evidence**?
>
> I don't have the answers today, **on purpose**. These are **ours** to answer. Thanks for following the whole series, and I'm happy to **take your questions**.
>

*Short route:* Four open questions for us: exceptions, risk tiers, audit trail, and who has earned a lighter review. Thanks, and over to your questions.

**→** Questions. The sources are on the last slide.

## Slide 23 — Sources  ·  IF TIME (full ~0.3 min, short skip)

**▶ Everything behind today's examples.**

- **Willison**: the lethal trifecta · **Šelajev** & **de Morlhon** (Docker): sandboxes
- **Vila López**: the 5 knights of MCP · **Rentea**: dimming the lights
- **OWASP** Top 10 for LLM apps: excessive agency

> If you want to dig deeper, all the sources are here: the **articles**, the Devoxx **replays**, Rentea's **human-review** repo, and the **OWASP** list for LLM applications. I'll share the deck after the session.
>

*Short route:* Leave it on screen during questions.

**→** Over to your questions.

---
title: "Arc 1 - AI Reality - Talk Points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---

# Arc 1 - AI Reality - Speaker text

One card per slide: **fil rouge** (bold line), outline, full text to say, transition. Same text as the presenter window (S).
Timing is flexible, 10 to 20 min. **Short route (~10 min):** CORE slides, plus only the *Short route* line on IF TIME slides. **Full route:** ~20 min.

## Slide 1 — AI, the reality check  ·  CORE (full ~0.5 min, short ~0.5 min)

**▶ One question: does AI make us better at delivering, or does it only feel that way?**

- Back from **Devoxx Belgium 2026**, talk 1 of 4: from chat to agents we can trust
- Three sources: a **METR controlled study**, a Devoxx talk on **trusting agents step by step**, a **reconversion keynote**

> Hi everyone. I spent a week at **Devoxx Belgium**, and AI was in almost every talk. This is the first of four short talks where I bring back what I saw there.
>
> Today is the **reality check**: not what AI promises, but what the evidence says it **actually delivers**.
>
> What follows is **my take**: my reading of what I saw, not the final word. I'm sharing it to **hear yours**, so if you see it differently, **say so**, during the talk or after.
>
> I lean on three sources: a **controlled study by METR**, a Devoxx talk by **Jonathan Vila Lopez** on how far to trust an agent, and a keynote by **Victor Rentea** on how our job is changing.
>

**→** First, where this sits in the series.

## Slide 2 — map  ·  IF TIME (full ~0.5 min, short ~0.1 min)

**▶ Four talks, one spine. Each one stands alone.**

- 01 **reality check** (today) · 02 **the harness** · 03 **context** · 04 **trust at scale**

> Quick map. Today: the **reality check**. Next: **the harness around the agent**, the rules and checks we put in the build. Then **context**, what the agent actually reads. Then **trust at scale**: sandboxes, permissions, review.
>
> Each talk stands on its own: miss one, you can still follow the next.
>

*Short route:* First of four; each one stands alone. Click on.

**→** Let's start with a show of hands.

## Slide 3 — They felt 20 % faster. The stopwatch said 19 % slower.  ·  CORE (full ~1.5 min, short ~1.5 min)

**▶ A feeling of speed is not proof of speed.**

- Show of hands (remote: **reaction or chat**): who feels faster with AI?
- Same developers, same tasks: **forecast faster, felt faster, measured slower**

> Let's start with a show of hands. **Who feels faster when coding with AI?** In the room, raise your hand; remote, use a reaction or the chat. ... Keep that hand in mind.
>
> ▶ *Click: "The stopwatch said 19 % slower." appears*
>
> In 2025, **METR** ran a study with **experienced developers, on their own projects**. Afterwards they **felt about 20 % faster**. The **stopwatch said 19 % slower**. Same people, same tasks.
>
> So the question for today: **does AI make us better at delivering software**, and **how much should we hand over to an agent**?
>
> *+ if time: Example: a Spring Boot team says it shipped a feature "in half the time", and nothing on the clock agrees.*

**→** Chapter one: what the numbers actually say.

## Slide 4 — A feeling is not a measurement  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ When a number travels this far, go read where it came from.**

- A **randomised controlled trial**, not a survey
- Real tasks, real developers, **a stopwatch**

> Chapter one. This isn't a survey or a vendor blog: it's a **randomised controlled trial**, real tasks, real developers, and a **stopwatch**.
>

**→** Here is what the study measured.

## Slide 5 — Forecast, felt, measured  ·  CORE (full ~2 min, short ~1.5 min)

**▶ The gap that matters is felt versus measured, not the 19 %.**

- Forecast **−24 %** · felt **−20 %** · measured **+19 % slower**
- Experts forecast **−38 to −39 %**, even further off
- **< 44 %** of AI generations kept, most needed clean-up

> Three numbers. Before starting, developers **forecast** that AI would cut their time by **24 %**. After finishing, they **felt** it had cut it by **20 %**. **Measured**: the tasks with AI took **19 % longer**.
>
> Economists and machine-learning experts asked to predict it were even more optimistic: around **38 to 39 % faster**.
>
> And a fourth number: **fewer than 44 %** of the AI generations were kept; most of them needed real clean-up.
>
> The point isn't "AI makes you slower". The point is that our **feeling about speed** was off by almost **forty points**, in the wrong direction.
>
> *+ if time: Example: a dev merges a generated Spring repository method, then spends longer fixing the N+1 query it hid than the time it felt like it saved.*

**→** To be fair, here's the setting this was measured in.

## Slide 6 — Who was tested, to be fair  ·  IF TIME (full ~1.5 min, short ~0.3 min)

**▶ Not automatically our team or our stack: a strong signal, not a universal law.**

- **16** experienced devs, ~5 years on their project
- **246** real tasks, own repos, ~10 years old, **1.1 M+ lines**
- **Early-2025 tools**, mostly Cursor + Claude 3.5/3.7 Sonnet, **no agentic harness**

> Before drawing conclusions, let's be fair and look at **who was tested**. **16 experienced developers**, each working on a project they had known for about **five years**. They did **246 real tasks** from their normal work, in **their own projects**: big, old codebases, around **ten years old** and over **a million lines** of code.
>
> The AI tools were the ones from **early 2025**: mostly Cursor with Claude Sonnet. Just the tool in the editor, with **no harness around it**: no rules or automatic checks built around the agent. That harness is exactly what talk two is about.
>
> So **this is not our team**, and 16 people is **a small sample**. But it's a **real experiment on real work**, timed with a stopwatch, not an opinion poll. Take it as **a strong signal, not a universal law**.
>

*Short route:* One sentence: experienced devs, mature code, early-2025 tools with no harness, so a strong signal, not a law.

**→** Now, does going faster at the keyboard mean the team ships faster?

## Slide 7 — More output, more breakage  ·  IF TIME (full ~1.5 min, short skip)

**▶ Local speed moves the cost downstream, it doesn't remove it.**

- Up: epics **+66 %**, throughput **+33.7 %**
- Down the line: incidents per PR **+243 %**, review time **~5×**
- **Vendor report**: order of magnitude, not exact decimals

> Does faster at the keyboard mean the team ships faster? **Faros AI** looked at telemetry from about **22,000 developers over two years**.
>
> Output goes up: **66 % more epics**, about **a third more task throughput**. But downstream, **incidents per pull request rise by 243 %**, and **time in review is about five times** longer.
>
> Faros sells engineering-metrics tooling, so this is a **vendor report**: read it as an order of magnitude. But the shape is clear: **the cost moves downstream**.
>
> *+ if time: Example: a team's PR queue backs up until reviewers start rubber-stamping.*

*Short route:* Skip, or one line: a vendor report sees more output, but more incidents and much longer reviews.

**→** One more data point, from a different population.

## Slide 8 — A second data point: trust, not throughput  ·  IF TIME (full ~1 min, short skip)

**▶ We use it more and trust it less.**

- **84 %** use AI tools · **29 %** trust the accuracy (down from **40 %**)
- **66 %** regularly get **"almost right, but not quite"**
- A **survey**, not a trial: different method, **same shape** as METR

> A completely different source: the **Stack Overflow 2025 survey**. **84 %** of developers use AI tools. Only **29 %** trust the accuracy of what they get, **down from 40 %**.
>
> And **66 %** regularly hit answers that are **almost right, but not quite**.
>
> It's a survey, not a controlled trial, a different population and method, and it shows **the same shape as the METR gap**.
>

*Short route:* Skip.

**→** So what does the speaker himself conclude from all this?

## Slide 9 — Only when you do it wrong.  ·  CORE (full ~0.5 min, short ~0.5 min)

**▶ The numbers describe unstructured use, not AI itself.**

- His answer to his own numbers: **"Only when you do it wrong."**
- A **position from the stage**, not a proof that cancels the 19 %
- Every talk that week pointed at **the harness around the agent**

> **Jonathan Vila Lopez** showed this kind of number at Devoxx: slower, lower DORA results, less than half the code kept. And his answer to his own numbers was: **"Only when you do it wrong."**
>
> That's **his position from the stage**, not a proof that cancels the 19 %. But every talk I saw that week pointed the same way: the difference is **the harness around the agent**.
>

**→** He put a number on what "doing it right" multiplies.

## Slide 10 — formula  ·  CORE (full ~1.5 min, short ~1 min)

**▶ AI multiplies what's already in the bracket, good or bad.**

- Success = AI × (**you**, **good practices**, **team knowledge**, **specs**, **deterministic tools**)
- A weak bracket is **amplified**, not fixed, by a stronger model
- Asking the agent instead of a colleague **erodes team knowledge**

> He wrote it as a formula: **success equals AI times** you, good practices, team knowledge, specs and deterministic tools.
>
> It's a **multiplication**. If the bracket is strong, AI amplifies it. If it's weak, a stronger model won't fix it: it **amplifies the weakness**.
>
> And watch the **team knowledge** term: every time we ask the agent instead of a colleague, that term quietly gets smaller.
>
> *+ if time: DORA's 2025 report frames AI the same way: an **amplifier** of an organisation's existing strengths and dysfunctions.*

**→** So the practical question: how much do we let the agent do on its own?

## Slide 11 — Trust is built in stages  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ Trust in an agent isn't an on/off switch, it's a ladder.**

- Seven stages, from **copy-paste chat** to **systems of agents**
- Each step up: **you personally watch less**

> Chapter two. Trust in an agent isn't a single switch, it's **a ladder**: seven stages, and each step up means **you personally watch less**.
>

**→** Here is that ladder.

## Slide 12 — A trust ladder in seven stages  ·  CORE (full ~2.5 min, short ~1.5 min)

**▶ Trust is transferred to a mechanism (a test, a build, CI), never decreed.**

- 1 **chat** · 2 **approve every call** · 3 **collaborator** · 4 **director** · 5 **YOLO**
- 6 **orchestrator** · 7 **architect**: the shape of the work changes
- 2 → 4 only if **something else watches instead of you**
- The permission / shape split is **my reading**, not the original slide

> Seven stages. **One**: browser chat, copy-paste both ways: low trust, total control. **Two**: a coding agent, but **you approve every tool call**. **Three**: collaborator: file edits go through, shell commands still need a yes. **Four**: director: **you judge the end result, not each step**. **Five**: YOLO mode, full trust.
>
> **Six and seven** change the shape of the work: you **orchestrate a fleet** of subagents, then you **design systems that design systems**. My reading, not the original slide: one to five raise permission on one agent; six and seven change who splits the work.
>
> The key point: going from **two to four** is only reasonable if **something else is watching instead of you**: **a test, a build, a CI pipeline**. That's where trust actually goes.
>

*Short route:* Name stages 1, 2 and 4 only, then the key point: 2 to 4 only when a test, a build or CI watches instead of you.

**→** An example of how the right stage depends on the risk.

## Slide 13 — The right stage depends on the risk  ·  IF TIME (full ~1.5 min, short ~0.3 min)

**▶ Same team, same agent: the risk of the task picks the stage.**

- **Flyway migration** → stage 2, every change approved
- **Unit tests behind a Maven gate** → stage 4, CI judges the result
- **Shared library refactor** → stage 3, shell still needs a yes
- Illustrative; **how to build the gates is talk 2**

> An illustrative example: same team, same agent, three stages.
>
> A **Flyway migration** against a real schema: **stage two**, every change approved by hand. **Unit tests behind a required Maven gate**: **stage four**: the agent writes freely, **CI judges the result**. A **shared library refactor**: **stage three**: edits go through, any shell command still needs a yes.
>
> Nothing new, just **the ladder applied by risk**. How to build those gates is the **next talk**.
>

*Short route:* One line: a migration stays at stage 2, tests behind a CI gate can go to stage 4.

**→** Before we leave the numbers: what replaces "it feels fast"?

## Slide 14 — What do we measure instead of feeling?  ·  IF TIME (full ~1 min, short ~0.3 min)

**▶ Measure team outcomes, not feelings at the keyboard.**

- **Deployment frequency** · **lead time** · **change failure rate** · **time to restore**
- Name **lead time** and **change failure rate** first
- Already exists: **no new metric** for AI

> So what do we measure instead of feelings? We already have it: the **DORA metrics**. **Deployment frequency, lead time for changes, change failure rate, time to restore.**
>
> These are **team outcomes at the end of the delivery chain**, not a feeling at the keyboard. If AI really makes us faster, **it has to show up there**.
>
> The two I'd look at first: **lead time** and **change failure rate**. DORA now also tracks **rework rate**, the share of deployments forced by an incident, and that's exactly where AI churn would show.
>

*Short route:* One line: the DORA metrics, lead time and change failure rate first; no new metric needed.

**→** One ceiling no stage of the ladder removes: the human side.

## Slide 15 — What the ladder doesn't climb  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ Climbing changes what you do, not what you're responsible for.**

- Rentea's **reconversion keynote**: the human side
- Not a seatbelt, **a warning about the driver**

> Chapter three, the part that isn't a number. Climbing the ladder changes **what you do**, not **what you're responsible for**. Not a seatbelt: **a warning about the driver**.
>

**→** Here's what that means.

## Slide 16 — The brain is the bottleneck  ·  CORE (full ~2 min, short ~0.5 min)

**▶ Higher stages free your hands, then spend your judgment.**

- **3 days → 2 hours** per decision
- Danger zone: **3–4 agent terminals**, your only input is **"OK"**
- Real risk: **burnout and loss of agency**
- **System design stays human**: "you can't vibe your infrastructure"

> **Victor Rentea**'s keynote was about how our job changes. His line: **the brain is the bottleneck**. Decisions that used to take **three days now take two hours**.
>
> His danger zone: **three or four agent terminals in parallel**, and your only input is **"OK"**. The risk of climbing fast isn't one bad commit, it's **burnout and loss of agency**.
>
> And at every stage, **system design stays human**: architecture, trade-offs, availability, scalability. In his words: **you can't vibe your infrastructure**.
>
> *+ if time: His anecdote, not a benchmark: an agent traced **17 memory leaks** from a heap dump in **30 minutes**. The upside is real.*

*Short route:* Say only: system design, trade-offs, availability and scalability stay a human call at every stage.

**→** Which brings us back to the hand you raised.

## Slide 17 — The problem isn't the model, it's what we put around it.  ·  CORE (full ~0.5 min, short ~0.5 min)

**▶ The problem isn't the model, it's what we put around it.**

- Feeling faster **is not evidence**
- Trust moves to **mechanisms we build**, never to the model by default

> So, back to the hand you raised at the start. **Feeling faster is not evidence.**
>
> Trust doesn't come from the model by default: it's **transferred to mechanisms we build**. Everything today points at the same gap: not at AI itself, but at **what we put around it**.
>

**→** Three things to keep.

## Slide 18 — Key takeaways  ·  CORE (full ~1 min, short ~0.7 min)

**▶ Three sentences to carry out of the room.**

- **A feeling is not a measurement**
- **Trust is transferred, not decreed**
- **The brain is the bottleneck, not the keyboard**

> One: **a feeling is not a measurement**. Judge AI by **lead time, failure rate and rework**, not by how fast it feels.
>
> Two: **trust is transferred, not decreed**. Hand over control only where **a test, a build or CI** watches for you.
>
> Three: **the brain is the bottleneck, not the keyboard**. Climbing the ladder **spends judgment**: protect it.
>

**→** So where does that trust get transferred to?

## Slide 19 — So what do we put around it?  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ The open question, on purpose: so what do we put around it?**

- Next: **rules the build enforces**, **checks the agent can't game**

> Which leaves the question for next time: **so what do we put around it?** Rules the build enforces, checks the agent can't game. That's talk two, **the harness around the agent**.
>

**→** Sources, if you want to check any of this yourself.

## Slide 20 — sources  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ Everything is checkable: go read the sources.**

- **METR paper** is open access: start with the introduction
- Rentea's keynote is on YouTube

> All the sources are on this slide. The **METR paper is open access**: start with its introduction. Rentea's keynote is on YouTube.
>
> **Thank you. Questions?**
>

**→** Questions.

---
title: "Arc 3 — Context is the product — Talk Points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---



# Arc 3 — Context is the product — Speaker text

One card per slide: **fil rouge** (bold line), outline, full text to say, transition. Same text as the presenter window (S).
Timing is flexible, 10 to 20 min. **Short route (~10 min):** CORE slides, plus only the *Short route* line on IF TIME slides. **Full route:** ~20 min.

## Slide 1 — Context is the product  ·  CORE (full ~0.5 min, short ~0.5 min)

**▶ One question: before the agent writes a line, what did we give it to read?**

- Back from **Devoxx Belgium 2026**, talk 3 of 4
- Three chapters: **before** (the spec) · **during** (rules and skills) · **after** (the docs)

> Hi everyone, and welcome back.
>
> Last time, we built **the harness**: rules in the build, checks the agent can't game, one bounded repair. All of that looks at what **comes out** of the agent.
>
> Today, we look at the other side: **what goes in**. Specs, docs, rules: **what the agent reads**, and **who writes it**.
>
> And here's my claim for today: good context for an agent is **the same thing a new hire needs on day one**. The **why**, not just the what.
>
> As always, this is **my take**. If you see it differently, **just say so**.
>

**→** First, where this sits in the series.

## Slide 2 — Map  ·  IF TIME (full ~0.5 min, short ~0.1 min)

**▶ Four talks, one spine. Each one stands alone.**

- 01 **reality check** · 02 **the harness** · 03 **context** (today) · 04 **trust at scale**

> Just a quick map, so you know where we are.
>
> Talk one was the **reality check**: does AI really make us faster? Talk two was **the harness**: what makes an agent's output trustworthy. Today is **context**: what the agent reads, before and while it works. And next time, we close with **trust at scale**: how far we can let it run.
>
> And again: **each talk stands on its own**. If you missed one, you're fine.
>

*Short route:* This is talk three of four, and each one stands on its own. Let's go.

**→** A quick reminder of where we left off.

## Slide 3 — Rules the build enforces, checks it cannot game, one bounded repair, a fresh verdict.  ·  CORE (full ~1 min, short ~0.5 min)

**▶ An agent is only as good as its harness.**

- A rule in a prompt is a **suggestion**; in the build, it's a **build failure**
- Tests from **outside the agent**, a status it **can't fake**
- **One repair**, then a **fresh verdict** on the final code

> So, quick reminder of last time.
>
> Remember the **fake parser**? The test wanted ten rows, so the agent **hard-coded ten**. Test green, parser useless.
>
> What stops that from shipping is **the harness**. Rules **in the build**, not in a prompt. Checks the agent **can't game**, with tests that come **from outside** the agent. And **one repair**, then a **fresh verdict** on the final code.
>
> And remember how the parser story got better: the team stopped letting the agent **guess**. The instruction became "**analyse, ask, don't assume**", and **humans answered**. Better input, fewer errors. That's where today starts.
>

*Short route:* Last time: rules in the build, honest checks, one repair. And the parser got better when the agent got better input. That's today.

**→** So, what goes in?

## Slide 4 — The harness checks what comes out. What did we hand it to read first?  ·  CORE (full ~1.2 min, short ~0.7 min)

**▶ Your agent is the fastest new hire you've ever onboarded.**

- The harness checks what **comes out**; today: what **goes in**
- A new hire and an agent need **the same thing**: the **why**
- The test: from what's in your repo, could someone understand **why each part is there**?

> The harness checks what **comes out**. But what did we hand the agent to **read first**?
>
> Here's a way to think about it. Your agent is **the fastest new hire** you've ever onboarded. It starts in seconds, it reads everything, and it never takes a coffee break.
>
> But think about what we give it. Usually, the **same undocumented mess** we gave the last new hire. A ticket, a codebase, maybe a wiki page from three years ago.
>
> And an agent that **searches the codebase** is still just searching. It finds **what** the code does. It doesn't find **why**.
>
> So ask yourself: from what's in your repo today, could a new colleague **understand why each part is there**? If not, **neither can the agent**.
>

*Short route:* Your agent is the fastest new hire you've ever onboarded, and we hand it the same undocumented mess. It finds what the code does, never why.

**→** Let's follow what the agent reads, in three moments: before, during, after.

## Slide 5 — Before: what you hand it to start  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ Before the first line: the spec.**

- The spec is the one thing a **human and an agent** read the same way
- The human owns the **content** and the **why**

> Chapter one: **before**. What you hand the agent **to start**.
>
> And before a single line of code exists, there's one thing a human and an agent can read **the same way**: **the spec**.
>

**→** Here's the table that runs through this whole talk.

## Slide 6 — Single source of truth: before, during, after  ·  CORE (full ~1.2 min, short ~0.6 min)

**▶ Truth lives in three places. Only one works for humans and agents alike.**

- **Spec**, before: precise enough for **both** to act on
- **Code**, during: always has bugs, and **bugs become the truth**
- **Docs**, after: only as good as the **context** they carry

> This idea comes from **Christian Heitzmann**'s talk at Devoxx. Where does the **truth** about a system live? There are three candidates.
>
> One: the **spec**, written **before** the code. If it's precise, it works for a human **and** for an agent. That's the good one.
>
> Two: the **code**, during. The problem: code **always has bugs**. And when an agent reads the code, **the bug becomes the truth**. It copies it. And code carries **no context**: why this sort order, why this version.
>
> Three: the **docs**, after. They're only as good as the **context** they carry. If they just repeat the code in prose, they're **worthless**.
>
> So, two question marks for now. We'll come back to this table **at the end**.
>

*Short route:* Spec before, code during, docs after. Only the spec works for both humans and agents. In the code, bugs become the truth.

**→** Let me show you why the code alone isn't enough.

## Slide 7 — The line an agent would have deleted  ·  CORE (full ~1.5 min, short ~0.8 min)

**▶ One comment is the difference between keeping a fix and reverting it.**

- Pagination needs a **deterministic sort**: **id** as the final tiebreaker
- Before: one line of Javadoc, **no reason**, the tiebreaker **already dropped once**
- After: two lines of comment carrying **the why** (story from **Victor Rentea**'s Deep Dive)

> Look at this method. It pages through the visits of an owner, sorted by date, and then **by id**.
>
> Why the id? Because when two visits have the **same date**, MySQL doesn't guarantee **their order**. So page two can **repeat** rows from page one. The id makes the sort **stable**.
>
> Now, in the version before, there was one line of Javadoc, and **no reason**. And someone had already removed that tiebreaker once, just **tidying up**. Pagination broke, quietly.
>
> An agent reading that old version would do **exactly the same**. It sees an extra sort, and it **simplifies it**. It's trying to be helpful.
>
> The fix is **two lines of comment**. Not what the code does: **why it must stay**. And now the agent **keeps it**.
>

*Short route:* Sort by date, then by id, because MySQL doesn't keep the order of ties. Without the why, an agent "simplifies" it away. Two lines of comment keep it.

**→** And the best place for that why is before the code even exists: the spec.

## Slide 8 — A spec is a use case, not a document  ·  CORE (full ~1.5 min, short ~0.8 min)

**▶ A spec is a use case, not a document.**

- **Actor & precondition** → the context · **Main flow** → the implementation
- **Alternative flows** → the edge cases agents **miss**
- **Acceptance criteria** → the **test suite**
- Keep it proportionate: specs for **at most ~20 %** of issues (Victor Rentea)

> So what does a good spec look like? Not a fifty-page document. **A use case**. Four parts, and each one has a job. This frame comes from **Jonathan Vila López**'s talk, "Agents With Seatbelts".
>
> **Actor and precondition**: who triggers it, and what must already be true. That becomes the agent's **context**.
>
> **Main flow**: the steps, in order. That becomes the **implementation**.
>
> **Alternative flows**: the edge cases. And that's **exactly what an agent misses** on its own.
>
> **Acceptance criteria**: written as checks, not prose. And those become **the test suite**, directly. Remember last time: the tests have to come **from outside the agent**. This is where they come from.
>
> And no, this isn't a new heavy stage on every ticket. It's the acceptance criteria you **half-write already**, made precise. Victor Rentea's own guardrail: markdown specs for **at most about 20 %** of issues. The ones with **real ambiguity or risk**.
>

*Short route:* A use case: actor, main flow, edge cases, acceptance criteria. The criteria become the tests from outside the agent. For at most 20 % of tickets, not all of them.

**→** But a spec is only as good as the questions asked before writing it.

## Slide 9 — Interview before you dictate  ·  IF TIME (full ~1.3 min, short skip)

**▶ Ask before you write. A vague ticket lets the agent fill every gap.**

- One-line ticket: "**Add pagination** to the owners grid": no volume, no urgency
- Instead: **one question at a time**, **business first**, a **recommended answer**
- The "**grill-me**" habit (Matt Pocock's skill, used by Victor Rentea)

> Here's a ticket: "**Add pagination to the owners grid**." That's it. No volume, no urgency, no UX hint.
>
> Paste that into an agent and it **fills every gap itself**. You get twenty fields, and you delete seven of them later.
>
> The alternative: let the agent **interview you** first. **One question at a time**. How many owners? Growing how fast? **Business questions first**, so the product owner can sit in too. Technical ones after.
>
> And for each question, it offers **a recommended answer**, and the human **corrects it**. Often the right answer is option C, the one nobody wrote down.
>
> Victor Rentea does this before any feature touches the code. It's called "**grill-me**", a skill by Matt Pocock.
>

*Short route:* Skip.

**→** That's the before. Now, what the agent keeps reading while it works.

## Slide 10 — During: what it keeps reading  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ While it works, the agent reads rules and skills. And those rot.**

- Rules files, skills: things the model **reads**, nothing **enforces**
- **Advisory**, not binding: the model can **ignore** them

> Chapter two: **during**. What the agent **keeps reading**, turn after turn.
>
> Rules files, like a **CLAUDE.md** or an **AGENTS.md**. Skills. All the things the model **reads**, but nothing **enforces**. They're **advice**. The model can follow them, or not.
>

**→** And here's the problem with anything the model only reads.

## Slide 11 — Rules rot: what a rule compensates for changes as the model and the harness improve.  ·  CORE (full ~1.2 min, short ~0.7 min)

**▶ Rules rot. What a rule compensates for changes as models improve.**

- **Daniela Petruzalek**, "State of Agentic Coding"
- Talk 2: what the build checks on the way **out**. Today: what the model reads on the way **in**
- A rule **nobody deletes** keeps costing context

> **Daniela Petruzalek** put it well at Devoxx: **rules rot**.
>
> A line in a rules file is there to **compensate** for something. The model kept making a mistake, so we wrote a rule. But models **improve**. Tools improve. And six months later, that line compensates for **nothing**. But it's still there, **costing context** on every request.
>
> And careful, this isn't last talk again. Last time was what the **build enforces** on the way **out**. This is what the model **reads** on the way **in**. And that file needs **gardening** too.
>
> Skills rot **even faster**, because they're optional. People forget **they exist**.
>
> A **short** rules file that does three precise things beats a **six-hundred-line** one that does everything once.
>

*Short route:* Rules rot: what a rule compensates for disappears as models improve, but the line stays and costs context. Short and precise beats long.

**→** A quick question for you.

## Slide 12 — Ask yourself, right now  ·  IF TIME (full ~1 min, short ~0.2 min)

**▶ A rules file that only grows is a diary.**

- How many lines is **your** AGENTS.md or CLAUDE.md?
- When did anyone last **delete** a line?
- Can you explain **why** each rule is still there?

> Don't answer out loud, just think about it. **How many lines** is your AGENTS.md, or your CLAUDE.md, today?
>
> When did anyone last **delete a line**, instead of adding one?
>
> And could you explain **why each rule** is still there?
>
> If the file **only grows**, it's not a rules file anymore. It's **a diary**. And deleting a line is the only proof the team still **understands** what each rule is for.
>

*Short route:* If your rules file only grows, it's not a rules file, it's a diary.

**→** The fix isn't more rules. It's relying less on things the model only reads.

## Slide 13 — Generate a diagram, don't draw one  ·  IF TIME (full ~1.2 min, short skip)

**▶ Ask for a script, not an opinion.**

- A hand-drawn diagram **drifts** as soon as the code moves
- A **script** that generates the view: re-run it, it's **honest again**
- The agent reads **a fact**, not a picture (Victor Rentea, "Architecture Observability and Guardrails")

> Same idea, applied to architecture diagrams.
>
> A diagram someone drew by hand is only as true as **the last time someone redrew it**. And nobody redraws it on every commit. So it **drifts**, and the agent inherits **a picture, not a fact**.
>
> Victor Rentea's advice: don't ask the agent to **draw** the diagram. Ask it to write the **script that generates** it, from the code.
>
> Then you re-run the script, and the diagram is **honest again**, for free. It can't go stale. He even **tests** the diagram against the code.
>

*Short route:* Skip.

**→** And there's one more kind of context that's checked, not just read.

## Slide 14 — This is also context  ·  IF TIME (full ~1.2 min, short skip)

**▶ A rule the build enforces is context the agent can't ignore.**

- **ArchUnit**: notification code must **not reach persistence**
- The agent reads this **before** touching the module
- Break it, and the **build fails**, the same day

> This is **ArchUnit**. A test that says: code in the **notification** package must **never depend** on the **persistence** package.
>
> You saw this kind of rule last time, as a **build gate**. Today, look at it differently: it's also **context**. The agent can read this file before it touches the module, just like a new colleague would. And it says, **precisely**, where the walls are.
>
> And unlike a paragraph in a rules file, it **can't be politely ignored**. If the agent breaks it, the **build fails**. Same day.
>

*Short route:* Skip.

**→** That's the during. Now, after: what can the code never say on its own?

## Slide 15 — After: what the code can never say  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ Even perfect code can't carry the why.**

- A class describes **itself**, never **the system**
- Rejected designs, warnings, reasons: **invisible** unless someone writes them down

> Chapter three: **after**. The code exists. What can it **never** tell you?
>
> A class describes **itself**. It never describes **the system** around it. And every rejected design, every warning, every **why**, is invisible, unless someone **writes it down**.
>

**→** Heitzmann has a great image for this.

## Slide 16 — Even perfect code describes a brick. It never describes the house.  ·  CORE (full ~1 min, short ~0.6 min)

**▶ Code describes a brick. It never describes the house.**

- **Christian Heitzmann**, Devoxx Belgium 2026 (paraphrase)
- "The code is the documentation" is wrong at **the level that matters**

> **Christian Heitzmann** said it like this, roughly: **even perfect code describes a brick. It never describes the house.**
>
> We've all said "**the code is the documentation**". And for one class, sure. But self-documenting code is self-documenting mostly **for the person who wrote it**.
>
> A hundred **clean classes** still won't tell a new hire, or an agent, **why the system is shaped this way**.
>

*Short route:* Perfect code describes a brick, never the house. Clean classes don't explain why the system is shaped this way.

**→** So what should the docs carry?

## Slide 17 — What docs must carry  ·  IF TIME (full ~1.2 min, short ~0.3 min)

**▶ Docs exist for what the code can't say.**

- **Architecture** in diagrams, never in a source comment
- **APIs** in Javadoc, **internals** in comments
- **Decisions**, **rejected designs**, and why
- **Warnings**: "single-thread only, because..."

> Here's the short list.
>
> **Architecture** goes in diagrams, not in a source comment. And the other way round: don't explain function internals in an architecture diagram.
>
> **APIs** in Javadoc, **internals** in comments. Don't mix them up.
>
> **Decisions**, and especially the **rejected designs**, and **why**. "We tried that, and we decided against it, because..." That's gold, for a new hire **and** for an agent. Without it, the agent proposes **the rejected design again**.
>
> **Warnings**: "single-thread only, because..."
>
> And what's pointless? **Rewriting the code in prose**. Docs are for what the code **can't say at all**.
>

*Short route:* Docs carry decisions, rejected designs and warnings. Not the code rewritten in prose.

**→** Let's go back to our table.

## Slide 18 — The table, filled in  ·  CORE (full ~1 min, short ~0.6 min)

**▶ Docs matter more, not less: now an agent reads them too.**

- **Spec**: still the source of truth for **both**
- **Code**: never the whole truth
- **Docs**: they work, **when they carry the why**

> Same table as the start, now filled in.
>
> The **spec**: still the one source of truth that works for **humans and agents**.
>
> The **code**: still **never the whole truth**. Bugs become fact, and the context is missing.
>
> And the **docs**: they move from a question mark to **a yes**. But only when they carry **the why**: the rejected designs, the warnings.
>
> So good documentation matters **more** now, not less. Because now **an agent reads it too**.
>

*Short route:* Spec: yes. Code: never the whole truth. Docs: yes, when they carry the why. And they matter more now, because an agent reads them too.

**→** So who writes what?

## Slide 19 — The human owns the content and the why. The model owns the form.  ·  CORE (full ~0.8 min, short ~0.5 min)

**▶ The human owns the content and the why. The model owns the form.**

- Human: the **decision**, the **trade-off**, the **reason**
- Model: spelling, grammar, **clear prose**
- Use AI for **language**, never for **reverse engineering**

> One clean split, again from Heitzmann.
>
> The **human** owns **the content and the why**: the decision, the trade-off, the reason it stays this way.
>
> The **model** owns **the form**: spelling, grammar, turning your rough notes into clear text.
>
> And one rule: use AI for **language**, never for **reverse engineering**. Don't ask an agent to **guess the intent** from code it didn't write. It will give you an answer. It will sound good. And it may be **completely wrong**.
>

*Short route:* The human owns the why, the model owns the form. Use AI for language, never to guess intent from code.

**→** And that answers the question we started with.

## Slide 20 — What is good context for the agent is good context for the human.  ·  CORE (full ~0.8 min, short ~0.5 min)

**▶ Good context for the agent is good context for the human.**

- Specs as **use cases**, docs that carry **the why**, rules that **don't rot**
- The test: could **a new hire** onboard from it?

> Remember the start: the agent is **the fastest new hire** you've ever onboarded. So what do we give it to read?
>
> The answer was in front of us all along: **what is good context for the agent is good context for the human**.
>
> Specs written as **use cases**. Docs that carry **the why**. Rules **short enough** that they don't rot.
>
> So read your own spec back. If **a new hire** could onboard from it, so can the agent. And if not, **neither can**.
>

*Short route:* Good context for the agent is good context for the human. If a new hire could onboard from your spec, so can the agent.

**→** So, three things to take home.

## Slide 21 — Key takeaways  ·  CORE (full ~1 min, short ~0.7 min)

**▶ Three things to take home.**

- The **spec** is the source of truth **before** coding
- Rules and skills **rot**: keep them **lean**, **delete** lines
- Code never carries **the why**: docs matter **more**

> If you remember only three things.
>
> One: **the spec is the source of truth before coding**. A use case, precise enough for a human **and** an agent to act on. And its acceptance criteria become **your tests**.
>
> Two: **rules and skills rot**. Keep them **lean**. **Delete** lines, don't just add them. And anything deterministic: put it in **a script or the build**, not in prose.
>
> Three: **code never carries the why**. Docs matter **more** now, not less, because an agent reads them too.
>

**→** And one open question for next time.

## Slide 22 — With a harness and good context, how far can we let it run?  ·  CORE (full ~0.5 min, short ~0.3 min)

**▶ With a harness and good context, how far can we let it run?**

- Next time, talk 4: **trust at scale**
- **Boundaries** it can't negotiate, review **dimmed** as trust is **earned**

> So now we have **a harness** that checks what comes out, and **good context** going in.
>
> That leaves one question for the last talk: **how far can we let the agent run**, without watching every step? **Boundaries** it can't negotiate, and review that we **dim**, only as trust is **earned**.
>
> Thanks. And I'm happy to **take your questions**.
>

**→** Questions. The sources are on the last slide.

## Slide 23 — Sources  ·  IF TIME (full ~0.3 min, short skip)

**▶ Everything behind today's examples.**

- **Heitzmann**: Why Documentation Won't Write Itself
- **Rentea**: Dimming the Lights, and Architecture Observability
- **Petruzalek**: State of Agentic Coding · **Vila López**: Agents With Seatbelts

> If you want to dig deeper, all the sources are here: the **replays** of the Devoxx talks, **ArchUnit**, and Anthropic's article on **context engineering**. I'll share the deck after the session.
>

*Short route:* Leave it on screen during questions.

**→** Over to your questions.

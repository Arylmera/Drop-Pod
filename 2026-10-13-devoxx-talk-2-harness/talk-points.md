---
title: "Arc 2 — The harness around the agent — talking points"
created: 2026-10-13
tags:
  - dev
  - devoxx
  - devoxx/2026
  - presentation
---


# Arc 2 — The harness around the agent — Speaker text

One card per slide: **fil rouge** (bold line), outline, full text to say, transition. Same text as the presenter window (S).
Timing is flexible, 10 to 20 min. **Short route (~10 min):** CORE slides, plus only the *Short route* line on IF TIME slides. **Full route:** ~20 min.

## Slide 1 — The harness around the agent  ·  CORE (full ~0.5 min, short ~0.5 min)

**▶ One question: once an agent writes the code, what makes it safe to merge?**

- Back from **Devoxx Belgium 2026**, talk 2 of 4
- Three chapters: **rules the build enforces** · **checks the agent can't game** · **one bounded repair**

> Hi everyone, and welcome back.
>
> Last time, we did the **reality check**. Remember the stopwatch? People **felt faster** with AI, and they were actually **slower**. So the takeaway was: trust isn't something you get for free. You have to **build it**.
>
> And that's what today is about: **how do we build it?** Say an agent writes some code for you. What would make you **comfortable enough to merge it**?
>
> Spoiler: it's **not a better prompt**. It's **everything we put around the agent**. At Devoxx, people called that **the harness**.
>
> And as always, this is **my take**. If you see it differently, **just say so**.
>

**→** First, where this sits in the series.

## Slide 2 — Map  ·  IF TIME (full ~0.5 min, short ~0.1 min)

**▶ Four talks, one spine. Each one stands alone.**

- 01 **reality check** · 02 **the harness** (today) · 03 **context** · 04 **trust at scale**

> Just a quick map, so you know where we are.
>
> Last time was the **reality check**. Today is **the harness**: the stuff around the agent that makes its output trustworthy. Next time, we'll talk about **context**, so what the agent actually reads before it writes anything. And we'll finish with **trust at scale**: sandboxes, permissions, review.
>
> And don't worry: **each talk stands on its own**. If you missed the first one, you're fine.
>

*Short route:* This is talk two of four, and each one stands on its own. Let's go.

**→** A quick reminder of where we left off.

## Slide 3 — They felt 20% faster. The stopwatch said 19% slower.  ·  CORE (full ~1 min, short ~0.5 min)

**▶ Feeling faster isn't proof. Trust has to be built.**

- **Felt 20 % faster**, measured **19 % slower** (METR)
- The gap came from **review and rework**, not from typing the code

> So, quick reminder of where we left off.
>
> Experienced developers, on their own projects, **felt about 20 % faster** with AI. But when you put a **stopwatch** on it, the same work took **19 % longer**.
>
> And the time didn't go into writing the code. It went into **reviewing it, and fixing it**.
>
> So the lesson wasn't "stop using AI". It was: **don't trust a feeling. Trust a mechanism.** Today, we're going to look at **what that mechanism looks like**.
>

*Short route:* Felt 20 % faster, measured 19 % slower. So we need a mechanism, not a feeling.

**→** And to show you why, let me start with a test that passed.

## Slide 4 — A parser that passed its test  ·  CORE (full ~1.5 min, short ~1 min)

**▶ The test passed. The code never parsed anything.**

- A real **SAS-to-Python migration** (Smals Research, Devoxx Belgium)
- If the filename matches, **hard-code the expected answer**
- **Goodhart's law**: when a measure becomes a target, it stops being a good measure

> Okay, look at this code for a second.
>
> This comes from a **real migration project**, from SAS to Python, presented at Devoxx by **Smals Research**. The agent had to write a parser, and there was a test that said: this file should have **ten rows**.
>
> So what did the agent do? It checked the **file name**, and if it matched, it just **returned ten**. **Test green.** And the parser? It **never parsed anything**.
>
> And the thing is, the agent wasn't being sneaky. It did **exactly what we asked**: make the test pass. That's **Goodhart's law**: when a measure becomes a target, it **stops being a good measure**.
>
> So the question for the next twenty minutes is simple: **what stops this from shipping?**
>

*Short route:* A real migration project. The test wanted ten rows, so the agent hard-coded ten. Test green, parser useless. What stops this from shipping?

**→** Let's put that question on the table.

## Slide 5 — What, concretely, makes an agent's output trustworthy?  ·  CORE (full ~1 min, short ~0.5 min)

**▶ Not a better prompt. A harness.**

- Not which model, not which prompt: **what surrounds the agent**
- Three pieces: **rules** it can't negotiate · **checks** it can't game · **one bounded repair**

> So here's the question for today: what, concretely, makes an agent's output **trustworthy**?
>
> And notice what I'm **not** asking. I'm not asking which model is best, or how to write the perfect prompt. A prompt is a **request**. The agent can follow it... or not.
>
> What I'm asking is: what do we put **around** the agent? That's the **harness**. And I'll give you the answer in **three pieces**.
>
> One: **rules the build enforces**, so the agent can't negotiate them. Two: **checks the agent can't game**. And three: when something goes red, **one bounded repair**, and a fresh verdict.
>

*Short route:* Not a better prompt, a harness: rules, checks, and one bounded repair.

**→** Piece one: rules.

## Slide 6 — Rules the build enforces  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ Put the rule where the agent can't negotiate it.**

- A rule in a prompt is a **suggestion**
- A rule in the build is a **build failure**

> Piece one: **rules the build enforces**.
>
> A rule you write in a prompt, or in an instructions file, is a **suggestion**. It holds most of the time. And it breaks **exactly when it matters**.
>

**→** Let me show you what that looks like.

## Slide 7 — The agent kept downgrading the Java version to get past a stuck build.  ·  CORE (full ~1.2 min, short ~0.7 min)

**▶ Under pressure, a written rule gives way.**

- A **bank modernisation project**, presented at Devoxx
- The agent **lowered the Java version** to get a stuck build green
- The version numbers here are **my illustration**

> This one comes from a **bank modernisation project**, presented at Devoxx.
>
> The team had a clear rule: we target this Java version. Written down, in the instructions. And the agent kept **downgrading the Java version**, again and again, every time the build got stuck.
>
> Picture your own pom.xml: **maven.compiler.release** quietly going from **21 to 17** in the middle of a session. Those exact numbers are my illustration, but the behaviour is real.
>
> And again, the agent isn't evil. It's trying to reach the **next green build**. The rule was just text, so under pressure, it **gave way**.
>

*Short route:* A bank project: under pressure, the agent kept downgrading the Java version to get the build green. The rule was just text.

**→** So what's the fix? Not a sterner prompt.

## Slide 8 — Don't document a constraint the build can enforce.  ·  CORE (full ~0.8 min, short ~0.4 min)

**▶ Don't document a constraint the build can enforce.**

- **Anyul Rivas** (GFT), Devoxx Belgium 2026
- Docs keep the **why**, the build keeps the **what**

> Here's the sentence from that talk I'd put on a wall. Anyul Rivas, from GFT:
>
> **Don't document a constraint the build can enforce.**
>
> Don't ask the agent to **remember** the rules. Make the environment **enforce** them. The documentation still matters: it explains **why**. But the build is what says **no**.
>

*Short route:* "Don't document a constraint the build can enforce." Docs keep the why, the build keeps the what.

**→** Here's what that looks like in Maven.

## Slide 9 — Maven Enforcer: the rule becomes a build failure  ·  IF TIME (full ~1.5 min, short skip)

**▶ The rule becomes a build failure, not a suggestion.**

- **requireJavaVersion**: the floor
- **bannedDependencies**: a library blocked outright
- Same idea: **ArchUnit** for layers, **PMD CPD** for duplication, **OpenRewrite** for migrations
- The values are **illustrative**

> This is the **Maven Enforcer plugin**. Nothing new, most of us have seen it.
>
> Two rules here. **requireJavaVersion** says: Java 21 or more, period. And **bannedDependencies** says: this library, **never**.
>
> So now, if the agent downgrades the Java version, it doesn't get a green build. It gets a **failure**, with a clear message. And for the agent, a build failure is a **fact**, not an opinion. It can't argue with it.
>
> And you can do the same for other rules: **ArchUnit** for your layers, a **duplication check**, **OpenRewrite** for migrations. The values on screen are just an example.
>

*Short route:* Skip.

**→** But there's a catch: what if the agent edits the rule itself?

## Slide 10 — Who guards the guard?  ·  IF TIME (full ~1.5 min, short skip)

**▶ A check the agent can edit is not a check.**

- A **hook** inside the agent: a good first filter, but **within its reach**
- The **build and CI** on the server: run on the result, **can't be skipped** locally
- **CODEOWNERS** on pom.xml and the enforcer config: changes need a **human** (one example of a solution)

> Now, the obvious question. Someone always asks it: **can't the agent just edit the pom.xml?**
>
> And the answer is: yes, if you let it. So you have to look at **where the check runs**.
>
> On the left: a **hook** inside the agent's tooling. It's useful, it's deterministic code, not AI. But it runs **inside the agent's reach**. And agents are really good at finding **the one path it doesn't cover**.
>
> On the right: the **build and the CI** on the server. They run on the result, **whoever produced it**. You can't skip them with a local **--no-verify**. And if you put **CODEOWNERS** on the pom.xml and the enforcer config, any change to them needs a **human** to approve it.
>
> CODEOWNERS is just **one example of a solution**. Your platform may have its own way. The point is: **a human** has to approve any change to the check.
>

*Short route:* Skip.

**→** So that's rules. Piece two: can the checks themselves be gamed?

## Slide 11 — Checks the agent cannot game  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ The checks have to be honest, not just present.**

- A check that can be **faked** is worth nothing
- Back to our **parser**, from the test side

> Piece two: **checks the agent can't game**.
>
> Because a rule in the build is useless if the thing that **measures** it can be **faked**. And that brings us back to our **parser**.
>

**→** Let's replay it.

## Slide 12 — Back to the parser, from the test side  ·  CORE (full ~1.5 min, short ~1 min)

**▶ The fix wasn't a smarter model. It was tests from outside the agent.**

- Runs 1-2: the agent wrote **its own tests**, so it **graded its own work**
- Run 3: "**analyse, ask, don't assume**"; humans answered, a functional analysis fed back in
- Same project, same model: **few errors**

> Same migration project. In the **first two runs**, the team gave an open instruction, then a list of hard rules. And the agent wrote **the code and its own tests**.
>
> So in practice, the agent was **grading its own homework**. And that's how you get the fake parser.
>
> In the **third run**, they changed one thing. The instruction became: **analyse, ask, don't assume**. The agent asked questions, **humans answered**, and a functional analysis was fed back in.
>
> Result: **very few errors**. Same project, same model. The only difference: **where the tests came from**.
>
> And that's the rule to remember: an agent that writes the code **and** the tests can **encode the same wrong idea twice**. Tests have to come from **outside**: a spec, an acceptance scenario, a person. We'll come back to that next time, with context.
>

*Short route:* Same project, same model. When the tests came from outside the agent, the errors went away. One agent writing code and tests can encode the same wrong idea twice.

**→** On our Java stack, the same trick looks a bit different.

## Slide 13 — What the fake parser looks like on our stack  ·  IF TIME (full ~1.5 min, short skip)

**▶ Goodhart's law has a Java accent.**

- **@Disabled**, **-DskipTests**, **assertTrue(true)**, a swallowed assertion
- A **lowered JaCoCo threshold**, a new **ArchUnit freeze** entry
- **My own list**, not from a talk

> Let's translate the fake parser into **our world**. This list is mine, not from a talk, but I bet you've seen most of it.
>
> A test that keeps failing? Add **@Disabled**. The build is slow? **-DskipTests**. An assertion is annoying? **assertTrue(true)**. Or you catch the assertion error, and **swallow it**.
>
> And the subtle ones: you **lower the JaCoCo threshold** to match the coverage you actually have. Or you add one more line to the **ArchUnit freeze file** instead of fixing the violation.
>
> None of these is a bug. Every tool is doing **exactly what it's configured to do**. The pipeline is **green**. And the bar just **moved down**.
>

*Short route:* Skip.

**→** So the checks need a contract the agent can't talk its way around.

## Slide 14 — Silence is not a result  ·  IF TIME (full ~1.5 min, short skip)

**▶ Silence is not a pass.**

- **Output contract**: OK, OUT_OF_SCOPE or ERROR, never an invented answer
- **Guardrails**: hard limits, stated plainly
- **Deterministic hooks**: code, not another model's opinion
- "A non-PASS result must never hide another independent finding" (**JI Darwish**)

> One more thing about honest checks. An agent needs a **legitimate way to say "I can't"**. Otherwise, it **invents an answer**.
>
> So, three things. First, an **output contract**: the result is **OK**, **OUT_OF_SCOPE**, or **ERROR**. In Java, think of a record with an enum status. A non-answer can't be read as a **success** anymore.
>
> Second, **guardrails**: hard limits, said plainly. Never raw SQL. Never a card number. Always the declared shape.
>
> Third, **deterministic hooks**: before a tool runs, code can **block** it. After, code can **format and test**. Code, not another model's judgment.
>
> And JI Darwish, at Devoxx, put it in one line: **a non-PASS result must never hide another independent finding. Silence is not a pass.** A check that didn't run has to say **SKIPPED**, with a reason. A grey CI job nobody looks at is **not a green one**.
>

*Short route:* Skip.

**→** Piece three: what happens when a check goes red?

## Slide 15 — One bounded repair, a fresh verdict  ·  CORE (full ~0.3 min, short ~0.2 min)

**▶ When a check fails, how many retries?**

- The instinct: **loop until green**
- The data says: **that instinct is wrong**

> Piece three: **one bounded repair, and a fresh verdict**.
>
> When a check goes red, the instinct is simple: let the agent **retry until it's green**. More attempts, more chances, right?
>
> Well, the data says **no**.
>

**→** Here's the number that surprised me the most.

## Slide 16 — What happens when you keep repairing  ·  CORE (full ~1.8 min, short ~1 min)

**▶ The second repair made things worse.**

- **82 %** correct after one revision
- **67.3 %** after two: **down**, not up
- **84.7 %** were correct **at some point**
- HumanEval, **small Python problems**: the numbers don't transfer, the **mechanism** does

> This comes from a 2026 paper, cited at Devoxx by **JI Darwish**. They let agents repair their code, again and again, and they measured.
>
> After **one repair**: **82 %** correct. After **two**: **67.3 %**. It went **down**.
>
> And look at the third number: **84.7 %** of the attempts were correct **at some point** during the run. Almost the same as after one repair. So nearly **all the value is in the first repair**. After that, the agent starts **breaking things that worked**.
>
> Big caveat: this is **HumanEval**, small Python problems, someone else's benchmark. Don't take these numbers to our codebase. But the **mechanism**, that one travels.
>

*Short route:* One repair: 82 % correct. Two repairs: 67.3 %. Nearly all the value is in the first one.

**→** So why does a second attempt make things worse?

## Slide 17 — The mechanism: stale evidence  ·  IF TIME (full ~1.5 min, short skip)

**▶ A PASS is only valid for the exact version it ran on.**

- **Old trace**: the agent fixes a problem that's **already gone**
- **34 of 135** correct attempts damaged
- **Current trace only**: **4 of 135**

> The reason is what they call **stale evidence**.
>
> Imagine the agent gets a test report. But that report is from **before its last change**. So it reads "this fails", and it goes to fix it. Except the problem is **already gone**. And while "fixing" it, it **breaks something that worked**.
>
> With old traces, **34 of 135** correct attempts got damaged. When they gave the agent **only the result for the current version**: **4 of 135**.
>
> So the rule is simple, and very familiar to us CI people: a PASS certifies **that exact version**, and **nothing else**.
>

*Short route:* Skip.

**→** That's why the loop needs a shape, not just a retry counter.

## Slide 18 — The loop, bounded  ·  CORE (full ~1.8 min, short ~1 min)

**▶ Not "retry until green": a fixed shape, with one repair in it.**

- **Gate** (compile) → **focused checks** → **full suite**
- **One repair** from compact findings, then a **fresh verdict**
- Still red: a **human** decides

> So here's what the loop looks like when it's done right.
>
> Step one: a **gate**. Does it compile? If not, everything else is **SKIPPED**, and we stop.
>
> Step two: the **focused checks**: lint, business rules, architecture. They **all run**. None of them hides another one.
>
> Step three: the **full test suite**, the expensive one. Only once everything cheaper is green.
>
> Then, **one repair**. One single prompt, with the rules and **every finding**, short and clear. Not a dump of the full log.
>
> And then a **fresh verdict**: we re-check everything, on the **final code**. If it's still red, it goes to a **human**.
>
> One honest note: "one repair" is a **policy choice**, not a law of nature. The point is that almost all the value is in the first one. So decide your retry budget **on purpose**.
>

*Short route:* Gate, checks, full suite, one repair, a fresh verdict on the final code, then a human.

**→** Now let's go back to where we started.

## Slide 19 — Would this harness have caught it?  ·  CORE (full ~1.8 min, short ~1 min)

**▶ Run the fake parser through the harness: it never ships.**

- **Rules**: in the build, out of the agent's reach
- **Evidence**: tests from **outside** the agent, exactly where it failed
- **Verdict**: a fresh check on the final file

> Remember the parser from the beginning? Let's run it through **our three pieces**.
>
> **Rules**: could the agent edit the check that measured it? Not if the rule lives **in the build**, protected, and not in a prompt.
>
> **Evidence**: did the test come from outside the agent? In the original story, **no**. And that's **exactly where it failed**. With an independent test on real data, hard-coding ten rows simply **doesn't work**.
>
> **Verdict**: a fresh check on the final file, with tests the agent didn't write, and the hard-code is **caught**.
>
> And notice: **no single tool** did that on its own. It's the **pieces together** that make the harness.
>

*Short route:* Rules out of its reach, tests from outside, a fresh verdict: the fake parser never ships. No single tool, all the pieces together.

**→** So, three things to take home.

## Slide 20 — Key takeaways  ·  CORE (full ~1 min, short ~0.7 min)

**▶ Three things to take home.**

- A rule the agent can negotiate is a **suggestion**: put it **in the build**
- Evidence comes **from outside the agent**
- **One repair**, a **fresh verdict**, then a **human**

> If you remember only three things.
>
> One: a rule the agent can negotiate is just a **suggestion**. Put it **in the build**, where the agent **can't edit the check**.
>
> Two: the evidence has to come **from outside the agent**. Independent tests. A status it can't fake. A check that **never goes silent**.
>
> Three: **one repair**, then a **fresh verdict** on the final code. And after that, a **human** decides.
>

**→** And one open question for next time.

## Slide 21 — The harness checks what comes out. What goes in?  ·  CORE (full ~0.5 min, short ~0.3 min)

**▶ The harness checks what comes out. What goes in?**

- Today: the **exit** side, can we trust the output?
- Next time, talk 3: the **entry** side, **what the agent reads**

> Today, we looked at what **comes out** of the agent: how do we know we can trust it?
>
> But you probably noticed: the parser story got better when the agent got **better input**. Real analysis. Answers from humans.
>
> So next time, in talk three, we look at the other side: **what goes in**. Specs, docs, rules: **what the agent reads**, and **who writes it**.
>
> Thanks. And I'm happy to **take your questions**.
>

**→** Questions. The sources are on the last slide.

## Slide 22 — Sources  ·  IF TIME (full ~0.3 min, short skip)

**▶ Everything behind today's examples.**

- **Rivas** (GFT): harness engineering
- **Darwish** (Xomnia): verification loops
- **Gao, Yang & Yang**: Looping Is Not Reliability

> If you want to dig deeper, all the sources are here: the **slides and replays** of both Devoxx talks, and the **paper** behind the numbers. I'll share the deck after the session.
>

*Short route:* Leave it on screen during questions.

**→** Over to your questions.


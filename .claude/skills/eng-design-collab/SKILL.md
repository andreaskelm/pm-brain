---
name: eng-design-collab
description: Partner effectively with engineering and design — feasibility and scope negotiation, tech debt tradeoffs, design reviews, discovery with builders, and PRD handoffs that don't get thrown away. Covers what eng needs, what design needs, how to frame debt, and language for hard conversations. Use when the user says "work with engineering", "design review", "tech debt negotiation", "is this feasible", "PRD handoff", "get eng bought in", "design partnership", "scope negotiation", or is stuck between product intent and build reality.
---

# Collaborate with Engineering and Design

The handoff isn't a meeting where you read the PRD aloud. It's the moment your thinking meets people who have to live inside the constraints you waved past. The failure mode I see: PM shows up with a polished doc and a fixed date, eng/design spend the review finding holes you could have surfaced in a thirty-minute jam, and everyone leaves polite and misaligned. Good collaboration starts earlier — shared problem, explicit tradeoffs, and artifacts each discipline can actually use.

You're not asking eng to "estimate your idea" or design to "make it pretty." You're jointly answering: what's the smallest true version, what breaks if we're wrong, what debt we're consciously taking, and what done means for each role. If you can't say what you're optimizing for (speed, learning, quality, risk), they'll optimize for their own defaults.

## Is this the right thing?

**Use this skill when** you're moving from "we think we should build X" toward commitment — discovery with builders, shaping scope, reviewing feasibility, negotiating debt, or handing off a PRD/spec.

**Don't, and say so, when:**
- The problem isn't named yet → braindump or opportunity assessment first; don't burn eng/design cycles on solution theatre.
- It's a pure prioritization fight with no new technical unknowns → `prioritize` skill, with eng input as data not as the whole conversation.
- You only need stakeholder comms on a decided build → `stakeholder-comms` or a status update, not a collab playbook.
- The ask is "write the PRD for me" with no thinking done → `write-prd` after preflight, not a substitute for partnership.

## Step 1 — Preflight (before the room)

Pick 2–3. Don't run the list.

- **What are we trying to learn or ship, and by when — and which of those is flexible?** Date, scope, or quality: something has to give. If all three are fixed, say that's the tension.
- **What do you know vs. guess about feasibility and UX risk?** Evidence tier on both.
- **Who are the actual deciders in eng and design?** Tech lead, EM, design lead — names matter for negotiation.
- **What's the uncomfortable tradeoff you're avoiding?** Usually scope, debt, or saying no to a stakeholder promise.
- **What does "good enough" look like for v1?** If they can't describe it, design and eng will fill the vacuum differently.

Check the repo: `3-Work/[initiative]/`, prior decisions, eng spikes, design explorations. Bring those into the room instead of re-litigating from scratch.

## Step 2 — Discovery with eng and design (before the PRD is sacred)

Run short, problem-first sessions:

- **Eng:** "What would break? What's unknown? What's the boring infrastructure we'd regret skipping?" Capture spikes as time-boxed questions, not open-ended research projects.
- **Design:** "What's the risky interaction? Where do users already hack a workaround?" Prototype the scary parts, not the whole roadmap.

Outcome isn't alignment theater. It's a short list: validated constraints, open questions with owners, and 1–2 scope slices that are worth a PRD. If eng says "six months" and you heard "six weeks", fix that mismatch before writing prose.

## Step 3 — What engineering needs from you

Eng can build from ambiguity, but they shouldn't have to guess your priorities.

Give them:
- **Problem and outcome** in user/system terms, not feature bullet soup
- **Non-goals** — what we're explicitly not doing this cycle
- **Constraints** — compliance, performance, platforms, migrations, on-call impact
- **Success metrics and guardrails** — what to instrument, what must not regress
- **Decision log** — what was decided, what was deferred, who owns reopening
- **Rollout and operability** — flags, rollback, monitoring, support expectations

Ask for:
- **T-shirt or range estimate** with assumptions stated
- **Riskiest technical unknown** and cheapest spike
- **Dependencies** on other teams, data, infra
- **Operational cost** — maintenance, alerts, support burden

Push on outcome vs output if the conversation drifts to implementation trivia before the slice is agreed.

## Step 4 — What design needs from you

Design needs room to solve the job, not a pixel spec from your head.

Give them:
- **Job, segment, and context of use** — when, where, emotional state if it matters
- **Constraints** — brand, accessibility level, platforms, content limits
- **Business rules** that affect UX — pricing, permissions, edge cases that aren't rare in enterprise
- **What you're willing to learn in production** vs what must be right before ship

Ask for:
- **Flows for happy path and top failure modes**
- **Open UX risks** and how they'll test them
- **Design system fit vs one-off** — debt in design language counts too

If design and eng disagree, don't pick a winner in the hallway. Frame criteria: learning speed, risk, reversibility, user segment affected.

## Step 5 — Tech debt and scope negotiation

Debt isn't a moral failure. It's a loan. Your job is to make the loan visible and intentional.

Frame debt conversations as:
- **What we get now** (speed, learning, revenue, unblock)
- **What we pay later** (incidents, slower features, migration cost)
- **Trigger to repay** — metric, date, or next initiative that funds the fix
- **Who signs the loan** — not just the IC who warned you

Scope negotiation scripts that tend to work:
- **"If we only had two weeks, what's the slice that still tests the hypothesis?"**
- **"What's the manual ops version we could ship while infra catches up?"**
- **"What can live behind a flag for 5% while we harden?"**
- **"What stakeholder promise can we reframe as outcome instead of feature parity?"**

When they say no, ask what would make yes possible — capacity, sequence, or reduced surface area. When you say no to debt repayment, say what you're buying with that delay.

## Step 6 — PRD handoff that sticks

Handoff is a package, not a slide deck.

- **Walk the doc** focusing on decisions and tradeoffs, not reading every bullet
- **Pre-wire** tech lead and design lead on open questions; the group meeting confirms, not discovers
- **Explicit asks:** estimates, risks, milestones, design review date, eng review date
- **Definition of done** per discipline — code shipped, monitored, documented, design QA, support briefed
- **First sync after handoff** — 48 hours — to catch silent misreadings

If the PRD is missing non-goals or guardrails, fix before handoff. Eng will fill gaps with pessimism; design with ideal flows; both will miss your actual bet.

## Watch for red flags as it takes shape

Fixed date with fixed scope and no quality valve, PRD before a feasibility conversation, "just estimate this", debt unnamed, design brought in at the end, no owner for ops. Flags: [criteria](references/criteria.md). Handoff structure: [handoff](references/handoff.md). Name it, one question, fix together.

## Before calling it done

- **Gut check:** "What would eng/design say in retro if this fails?" Capture one mitigation now.
- **Quick check** on red/green flags before commitment meetings.
- **Log tradeoffs** in initiative `decisions.md` or `5-Growth/decisions.md` when debt or scope bets are explicit.

## Org reality

- **Feature factory dates.** You may not move the quarter. You can still negotiate slice, flags, and debt triggers — document what was squeezed so it's not invisible blame later.
- **Eng overloaded, design shared.** Prioritize one collaborative touchpoint with prep sent async; don't burn the relationship with surprise meetings.
- **Remote/async.** Written decision records beat "we talked about it"; link spikes and Figma in the initiative folder.
- **PM as project manager.** If you're only chasing tickets, step back to problem and tradeoffs — otherwise eng/design tune you out when it matters.

## References

- [references/handoff.md](references/handoff.md) — what eng needs, what design needs, debt framing, negotiation scripts
- [references/criteria.md](references/criteria.md) — red/green flags for collab and handoffs

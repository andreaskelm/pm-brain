---
name: opportunity-assessment
description: Assess whether an idea, feature request, or opportunity is worth pursuing before anyone writes a PRD. Covers the problem hypothesis, who has the problem and how badly, the four risks (value, usability, feasibility, viability), the riskiest assumption and its cheapest test, kill criteria, and a go / no-go / learn-more call. Use when the user asks "is this worth pursuing", "should we build this", "assess this opportunity", "opportunity assessment", "business case for an idea", "evaluate this idea before a PRD", "is this a real problem", or brings a stakeholder's pet idea to sanity-check. Runs preflight questions before any template.
---

# Assess an Opportunity

An opportunity assessment is the step before the PRD. It answers four questions: is the problem real, is it worth solving, is it worth solving *for us*, and is *now* the time? The failure I see most often isn't a sloppy assessment. It's one written after everyone already fell for the solution, so it reads like a justification memo with a risks section bolted on. The useful version is one that could plausibly come back "no". If there's no outcome where you'd kill this, you're not assessing, you're decorating.

## Is this the right thing?

**Assess when** there's an idea or request with real cost attached (more than a sprint or two, or a commitment someone will hold you to), and you can't yet say, with evidence, who has the problem and how badly.

**Don't, and say so, when:**
- The problem is validated and the approach has evidence behind it → that's a PRD. Use the `write-prd` skill.
- There's no named problem yet, just a pile of interviews, tickets and notes → synthesize first with the `discovery-synthesis` skill. You can't assess an opportunity you haven't named.
- Several validated opportunities are fighting for the same capacity → that's prioritization (the `prioritize` skill), not assessment.
- It's a few days of work and cheap to reverse → ship it and measure. A two-page assessment for a one-week change is theatre.

## Step 1 — Preflight (before any template)

Pick 2–3 of these for what's actually missing. Don't run the list.

- **What problem does this solve, in the user's words?** If the answer starts with the feature, ask again.
- **Where did this idea come from?** A customer, a churn analysis, the CEO's flight home, a competitor launch. The origin tells you which bias to watch for.
- **What do you know vs. guess?** Which parts rest on data or interviews, which on someone's say-so, which on a hunch?
- **What would make you say no?** If the answer is "nothing", that's the first finding.
- **Why now?** What changed that makes this matter this quarter and not last year?
- **What are you most worried about here?** The thing they'd rather not write down usually belongs in the risks section.

Before asking, check the repo if it exists: `3-Work/[initiative]/` (earlier thinking, decisions, a half-finished assessment), `4-Research/` (interviews or data that already speak to the problem), and `1-Context/` (strategy, OKRs, the stakeholder pushing this). Quote back what's there instead of asking for it.

If they've clearly braindumped already, one confirming question is enough. If they insist on skipping: name the risk in one sentence, then draft with `[GAP: …]` markers. Never invent a number to fill the sizing section.

## Step 2 — Write the problem hypothesis, not the solution

One or two sentences: who, what pain, what it costs them, and what changes if it goes away. *"Ops teams spend ~30 min/day triaging alerts and 80% are false positives. If triage drops to 5 minutes, incidents get handled faster and ops-segment churn drops."* Not "build smart alerts". If they can't write it without naming a feature, that's the outcome-vs-output lens firing. Pull back to the outcome.

Solution ideas go at the bottom as one-liners, and at least two of them. One concept means the assessment is secretly a pitch.

## Step 3 — Who, how many, how painful (with the evidence tier)

- **Who:** a specific segment in a specific situation. "Mid-market ops leads during on-call" beats "users".
- **How many:** reach in accounts, users, or revenue exposed. Order of magnitude is fine.
- **How painful:** what they do today instead (a workaround, a spreadsheet, a competitor, nothing) and what that costs them. If the answer is "nothing, and nobody complains", the pain might not be real.

Tag each claim with its evidence tier: **documented** (data, a handful of interviews), **verbal** (Sales says so, one customer call), **hunch**, **industry** (an analyst stat). What tends to happen: the sizing is industry-tier, the pain is verbal-tier, and the whole thing *reads* documented-tier because it sits in a tidy table. Make the tier visible in the doc.

## Step 4 — Run the four risks

| Risk | The question | Typical cheap test |
|---|---|---|
| **Value** | Will they choose this over what they do today? | Interviews about past behaviour, fake door, concierge version |
| **Usability** | Can they figure it out? | Clickable prototype with five users |
| **Feasibility** | Can we build it with the team, data and time we have? | A one-to-two-day spike by the tech lead |
| **Viability** | Does it work for the business: margin, sales, support, legal, strategy? | Thirty minutes each with finance, legal, the sales lead |

The pattern I keep running into: teams spend weeks on feasibility because engineering asks, and wave value through because the requester sounded confident. Value is the risk that kills most ideas, and it's the one most often assumed away. Compliance and dependencies live under viability and feasibility; pull them out on their own line only when they're the real blocker.

## Step 5 — Find the riskiest assumption and the cheapest test

List the assumptions, then ask: which one, if wrong, kills the whole thing, and how sure are we it's true? High impact × low confidence is your riskiest assumption. Usually one, occasionally two. When they name it, stress-test before writing it down: "What would be the first signal you're wrong about that?"

Then pick the cheapest test that would actually change your mind: five interviews about the last time it happened, a data pull, a fake-door button, a manual version for three customers. "Build an MVP" is rarely the answer here. It's often the most expensive way to learn something you could learn in a week.

## Step 6 — Write kill criteria before the evidence comes in

Kill / pivot / commit thresholds, written now, with numbers where you can: *"Kill if fewer than 3 of 10 ops leads name triage as a top-three pain. Pivot if the pain is real but it's routing, not volume. Commit if 7+ do and two would pilot."* Plus a decide-by date. Thresholds set after the data arrives always drift to fit the data; that's the whole reason to write them first.

## Step 7 — Make the call: go, no-go, or learn more

- **Go** → ready for a PRD via the `write-prd` skill. The problem, evidence and kill criteria carry straight over.
- **No-go** → write down why and what would reopen it. A clean no is a good outcome, and logging it stops the idea coming back in six months unexamined.
- **Learn more** → only with a named test, an owner and a decision date. "Learn more" without those is a polite way of never deciding.

Push for a call. "It depends" is fine if they can say what it depends on.

## Watch for red flags as it takes shape

No clear hypothesis, solution bias, vague customer, no sizing, assumptions without confidence, no kill criteria, risks only on feasibility, a single solution concept. Full list, weighted dimensions and rewrites: [criteria](references/criteria.md). Structure to fill: [template](references/template.md). When a flag appears: name it, ask one question, suggest the fix. Don't silently fix it, or the user never learns to see it.

## Before calling it done

- **Gut check:** "Explain this to a skeptical CFO in two minutes. What would make them say 'obviously wrong'?"
- **Quick check** against the red/green flags. Offer the full scored evaluation only if they want it, or before a funding gate.
- **Independent review:** if the `artifact-reviewer` subagent is available, offer it. The author is the worst judge of whether their own kill criteria are real. Discuss its findings; don't just paste them.
- **Log the call:** offer a row in `5-Growth/decisions.md` with the decision (go / no-go / learn more), their confidence, and a reopen trigger.

## Org reality

- **The CEO's idea, and the assessment is expected to say yes.** Don't fight the premise head-on. Frame it as de-risking the CEO's bet: same riskiest assumption, same cheap test, same kill criteria, just presented as "here's how we make sure this lands". If the criteria trip, you're bringing evidence, not an opinion. And watch your own confirmation bias: it's tempting to find what the room wants.
- **The solution was already promised to a customer.** Then "should we" is partly answered. Assess the generalization instead: one customer is n=1, so check who else has the problem before it becomes a product line. Label it honestly in the doc as a commitment, not a validated opportunity, and scope the smallest thing that keeps the promise.
- **No access to users.** Common in enterprise B2B where Sales guards the accounts. Use proxies (support tickets, call notes, CS, usage data, churn reasons) and mark them verbal-tier. Ask to shadow one sales call. Put "we haven't talked to a user" in the risks section, where it belongs.
- **Sunk cost on a half-built version.** Name it lightly: "I'm noticing what might be sunk cost here." Then assess as if starting today: if this didn't exist, would we start it? The upside: real usage data from the half-built thing is better evidence than any interview. Use it.

## References

- [references/template.md](references/template.md) — opportunity assessment template, with four-risks table, kill criteria and the call
- [references/criteria.md](references/criteria.md) — red/green flags, weighted dimensions, antipatterns, rewrites

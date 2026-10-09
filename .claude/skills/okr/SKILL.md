---
name: okr
description: Write, draft, review, or fix OKRs (objectives and key results) for a team, product area, or quarter, and run weekly confidence check-ins, mid-cycle adjustments, and end-of-cycle grading. Use when the user says "write OKRs", "draft our quarterly objectives", "turn our strategy into OKRs", "are these good key results", "OKR review", "our KRs are just a task list", "set team goals for Q3", "OKR check-in", or "grade last quarter's OKRs". Runs preflight questions before any drafting.
---

# OKRs

OKRs turn a strategy into a handful of outcomes the team commits to moving, and leave the *how* to the team. The failure I see most often is a task list with percentages on it: "Launch dashboard: 100%", every box green at quarter end, and nothing about the business changed. The second most common: OKRs written from scratch in planning week with no strategy behind them, so they just restate the roadmap someone already had. OKRs organize a strategy. They don't create one.

## Are OKRs the right thing?

**Use them when** there's a strategic priority to operationalize, more than one team or function has to pull in the same direction, the outcome can be measured (or you can start measuring it this cycle), and someone will actually look at them every week.

**Don't, and say so, when:**
- There's no strategy yet → have that conversation first. OKRs without one describe the backlog in nicer words.
- It's early discovery and nobody knows which metric matters → learning goals or an opportunity assessment. The exception is an assumption-test KR (Step 3).
- It's a small team (under ~5) that's already aligned → one goal on a whiteboard does the job.
- It's a one-off project with one clear success criterion → a project plan with that criterion.
- It's purely tactical execution → call it a sprint plan. Dressing a task list up as OKRs is how the fake ones start.
- Nobody has capacity for a weekly check-in → they'll be set-and-forget. Be honest about that up front.

## Step 1 — Preflight (always, even when they say "just write them")

Ask 2–3 of these, picked for what's actually missing:

- **If you could only move ONE thing this cycle, what is it?** Their gut answer is the draft objective. Write it down so the rest can challenge it.
- **What changed that makes this matter now?** If nothing changed, it's probably business-as-usual work looking for a promotion.
- **What's the number today?** No baseline means the first KR might be "instrument it and get one".
- **Which part of the strategy does this serve, and who set it?** Their own call, or cascaded from above? It changes what's negotiable.
- **What do you know vs. guess about what moves that number?** Name the evidence tier: documented, verbal, hunch, industry.
- **How will these be used?** If they feed performance reviews or bonuses, that changes how ambitious anyone will let them be.

Before asking, check the repo if it exists: `1-Context/` (strategy, company goals, leadership OKRs), `3-Work/[initiative]/` (opportunity, research, decisions), and `5-Growth/decisions.md` (last cycle's calls and reopen triggers). Last cycle's OKRs and grades are the best input of all. Quote back what's there instead of asking for it.

If they insist on skipping: name the risk in one sentence, then draft with `[GAP: …]` markers, especially `[GAP: baseline unknown]`. Never invent a baseline to make a KR look finished.

## Step 2 — Objectives: outcomes, and few of them

1. **Outcome, not project.** Test: would the objective still make sense if the planned feature got cancelled tomorrow? "Launch customer portal" fails. "Customers resolve billing questions without contacting us" passes, and leaves room for a better solution than the portal.
2. **One or two per team.** Three is the hard ceiling, and even three trips a red flag. If they have five, ask "which one would you protect if the quarter got cut in half?" and rank from there. The rest go on a "not now" list.
3. **Qualitative and directional.** The numbers live in the KRs. An objective should be something the team can repeat from memory.
4. **Say whether it's impact or enabler.** Impact OKRs move a core business metric. Enabler OKRs unlock future impact (platform, data quality, compliance). Enablers are legitimate, but they have to name the impact they unlock, or they're just maintenance.
5. **Business-as-usual isn't an objective.** Keeping the lights on belongs in health metrics and guardrails, not in the two slots you get for change.

## Step 3 — Key results: baseline → target, and measurable

1. **One format:** `[metric] from [baseline] to [target] by [date] (threshold: [minimum that still counts])`. "Weekly active users of advanced features from 5,000 to 8,000 by end of Q2 (threshold: 6,500)."
2. **2–4 per objective, leading and lagging mixed.** Lagging tells you whether it worked. Leading tells you in week 3 whether it's going to. Retention is lagging; "% of new accounts completing setup in week one" is the leading signal you can actually steer.
3. **Milestones out.** "Launch X" or "Complete Phase 1": ask "so that what?" until a number shows up. The launch goes on the initiative list, tagged with the KR it serves.
4. **Assumption tests are valid KRs.** When the riskiest assumption is untested, make the test the KR, with a pass/fail threshold: "Test advanced filtering with 100 users; 70%+ rate it valuable." A pass means build it. A fail means you just saved a quarter.
5. **Proxies when the real outcome lags past the cycle.** "Enterprise signups +30%" standing in for revenue is fine. Label it as a proxy, and check over the next cycles that it actually tracks the outcome.
6. **Name the source.** Every KR says which event, query, or dashboard it comes from. If you can't say where the number lives, you can't grade it.
7. **Guardrail anything gameable.** "Support tickets down 40%" pairs with "CSAT stays at or above 4.2". Otherwise someone will hide the contact form.
8. **Stable IDs** (`O1-KR1`, `O1-KR2`). Initiatives and PRDs reference the IDs. One metric per KR, never the same metric twice.

**Ambition.** Stretch targets, honestly set. If they expect to hit 100% of everything, the targets are too soft. A healthy stretch cycle lands somewhere around 60–70% of KRs. That only holds if missing is safe (see Org reality).

**Alignment.** Ask for the ladder: KR → team metric → department metric → company metric. "Settlement time −60% → ops efficiency +40% → unit cost −25% → margin +5%." If nobody can write the ladder, the alignment is assumed, not real.

## Step 4 — Track confidence, not just progress

Progress numbers lag. Confidence moves first. Set up a weekly 20–30 minute check-in where each KR gets a confidence score (0 off-track, 1 at-risk, 2 on-track) *with evidence*, plus risks and the next action. Mid-cycle, decide per objective: double down, pivot, or stop, and log material changes. At the end, grade each KR 0.0–1.0 and write down what you learned. Scale, worked example and grading: [cadence](references/cadence.md).

Push back on early optimism: every KR at 2 in week two with no data is hope, not confidence. Ask "what did you see this week that says 2?"

## Step 5 — Watch for red flags as it takes shape

Project-named objectives, milestone KRs, no baselines or targets, no time bound, no instrumentation, too many objectives or KRs, activity counted as outcome. Full list, weighted dimensions and rewrite examples: [criteria](references/criteria.md). When one appears: name it, ask one question, suggest the fix. Don't silently fix it, or the user never learns to see it.

## Step 6 — Before calling it done

- **Gut check:** "Explain these to a skeptical exec in two minutes. What behavior will they drive, and what behavior might they drive *instead*?" Then: "What would make you say these are obviously wrong?"
- **Quick check** against the red/green flags. Offer the full scored evaluation only if they want it, or before a high-stakes review.
- **Independent review:** if the `artifact-reviewer` subagent is available, offer it, since fresh eyes catch what the author can't. Discuss its findings; don't just paste them.
- **Log the bet:** offer a row in `5-Growth/decisions.md`: how confident they are that hitting these KRs moves the strategy metric, plus a reopen trigger ("leading KR at confidence 0 for two weeks running", "baseline turns out 30% off").

## Org reality

- **Fake OKRs that are just a task list.** Leadership wants "Ship SSO, launch v2" in the OKR tool and won't hear otherwise. You won't win the format fight this quarter. Keep the outcome next to each item: "Ship SSO (so that: deals stalled in security review drop from 6 to 1)". Same artifact, real thinking underneath, and at grading time you're the one who can say whether it mattered.
- **OKRs cascaded from leadership that you can't change.** "Expand enterprise market" lands with the KR already set. Don't fight the top line; own the translation. Write the team KRs you believe actually move it and name the assumption connecting them. If the cascaded KR is a milestone, track the outcome yourself anyway.
- **OKRs tied to performance reviews.** The moment a miss costs someone their rating, every target becomes something they already know they'll hit. That's sandbagging, and stretch is dead. Name it. Then split committed KRs (expected to land, fine for reviews) from aspirational ones (graded for learning), or keep a private stretch number. Don't preach that 0.7 is a great score in an org that punishes it.
- **Written in January, opened in March.** Built for the planning deck, never looked at again. Twenty minutes a week beats perfect wording. If no ritual will exist, pick the one KR that matters and put it on the agenda of a meeting that already happens.

## References

- [references/template.md](references/template.md) — objective canvas, team OKRs, weekly check-in, KR measurement plan
- [references/cadence.md](references/cadence.md) — confidence scale, weekly/mid-cycle/end rhythm, grading, calibration
- [references/criteria.md](references/criteria.md) — red/green flags, weighted dimensions, antipatterns, rewrites

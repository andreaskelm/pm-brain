---
name: north-star
description: Define, sharpen, or audit a North Star metric and its input metrics tree, and decide which product metrics actually matter (leading vs. lagging, guardrails, vanity vs. actionable, AARRR pirate metrics funnel). Use when the user says "define our north star metric", "what metric should we track", "what should we measure", "metrics framework", "input metrics", "KPIs for my product", "success metrics for my product", "AARRR", "pirate metrics", "where are users dropping off", or "is this a vanity metric". Finds the customer value moment before naming any metric.
---

# North Star and the metrics that matter

A North Star is one metric that captures the value customers actually get, plus 3–5 input metrics that teams can move with their own work. It's an alignment tool, not a dashboard and not a goal for the board deck. The failure I see most often is a "North Star" that's revenue wearing a costume, or registered users because that's the number the dashboard already shows. Both feel safe, both tell you nothing about whether customers are better off, and both get gamed within a quarter. So we start with the moment a customer gets value and work outward to the numbers.

## Is a North Star the right thing?

**Do it when** the product has real users and real usage, more than one team needs to pull in the same direction, and you can describe what "a customer got value" looks like in behaviour, not in sentiment.

**Don't, and say so, when:**
- **Pre-launch or pre-PMF.** There's nothing to align on yet. Track activation and retention for the cohorts you have, and treat everything else as noise.
- **It's one feature or initiative.** That needs success metrics (baseline → target, plus a guardrail), not a North Star. One product, one North Star. Not one per team.
- **The real question is "where are users dropping off?"** That's a funnel diagnosis. Use the AARRR section in [metrics](references/metrics.md) and fix the weakest stage.
- **Enterprise B2B with a handful of customers.** Funnel stats on 3 accounts are anecdotes with decimals. Talk to the customers, and track a few account-level outcomes.

## Step 1 — Preflight (before naming any metric)

Ask 2–3 of these, picked for what's missing. Don't run the whole list.

- **When does a customer get value?** Describe what they just did, not what we shipped. "Their team saw the report and changed a decision" beats "they used dashboards".
- **If you had to pick ONE metric today, what is it and why?** Their gut answer is data. Write it down so the rest of the process can challenge it.
- **What would make you say "this North Star is obviously wrong"?**
- **What can you actually measure today?** Is the event instrumented, or is this a wish?
- **Who's going to push for a different number,** and which one? (Usually revenue, usually from finance or the CEO.)

Before asking, check the repo if it exists: `1-Context/` for strategy, vision and OKRs, `3-Work/[initiative]/` for existing success metrics and research, and `5-Growth/decisions.md` for an earlier metric decision this might contradict. Quote what's there instead of asking for it again.

If they insist on skipping: name the risk in one sentence ("we'll probably pick whatever's easiest to count"), then draft with `[GAP: …]` markers. Never invent a baseline.

## Step 2 — Find the value moment and the game

Name which game the product plays, because it decides what "value" means:

| Game | Value looks like | Example North Stars |
|---|---|---|
| **Attention** | Users come back often and spend time | Days active per week per user, for a content or social product |
| **Transaction** | Users complete an exchange | Nights booked (Airbnb), items received on time per month (delivery) |
| **Productivity** | Users get work done, ideally with others | Weekly Learning Users (Amplitude), messages sent per week (Slack) |

The game is a lens, not a law. Plenty of products straddle two, and that's fine as long as you pick the one your strategy bets on. If the user can't describe the value moment, stop here. That's a discovery gap, not a metrics problem.

## Step 3 — Pick a North Star that captures customer value, not revenue

Generate 2–3 candidates, then test each: does it measure value delivered, does it lead revenue and retention rather than trail them, can every team explain how their work moves it, and can you measure it the same way every week?

Run the **anti-North-Star** first if they're stuck: ten minutes on what a TERRIBLE North Star would be. Which number would make us feel great while customers get nothing? What could we push up that would hurt customers? It frees people up, and the answers become your guardrails.

Revenue is the obvious candidate and the wrong one. It's lagging: it tells you that you delivered value months ago, and it moves for reasons the product team doesn't control (pricing, sales headcount, a big renewal). It belongs in the tree as the business outcome the North Star predicts.

Write a precise definition: who counts, which action, what time window. "Active users" isn't a definition. "Users who shared a learning that at least two others consumed in the last 7 days" is.

## Step 4 — 3–5 input metrics the team can move

Inputs are how teams act on the North Star. Each one needs to be action-oriented, leading, owned by a named team, and written as a belief with evidence: *"We believe first-week activation drives Weekly Learning Users because activated users are 3× more likely to become WLU within 30 days (cohort analysis, documented)."* Name the evidence tier. Most input beliefs start as hunches, and that's fine as long as they're labelled.

Push back on vague inputs. "Engagement", "adoption" and "quality" can't be owned by anyone. "% of new signups who complete setup and run a first analysis within 7 days" can. If they list more than five: "If you could only focus on three, which ones?"

Then map current initiatives to inputs. An initiative that doesn't move any input isn't automatically wrong, but it's a priorities conversation the team should have out loud. Tree structure and examples: [metrics](references/metrics.md).

## Step 5 — Guardrails

Add 1–3 guardrails: the metrics that must not get worse while you push the North Star. Goodhart's Law applies the moment a number becomes a target. Push weekly active users and someone will ship notification spam. So, for example, North Star "weekly active teams" with guardrails "CSAT stays above 4.0/5", "monthly churn stays under 5%", "revenue per user doesn't drop". Use the anti-North-Star answers from Step 3 here.

## Step 6 — Baseline before target

No target without a current value. If there's no baseline, the first deliverable is measurement, not a goal. Then set a 90-day target for the North Star and each input, and check at least one input → North Star link with real data (a cohort comparison is enough) before anyone builds a roadmap on it.

## Step 7 — Watch for red flags as it takes shape

Vanity North Star, revenue or output as the North Star, inputs nobody can move, unclear input → North Star links, more than five inputs, no work connections, no measurement definition, no guardrail. Full list, weighted dimensions and rewrites: [criteria](references/criteria.md). When one shows up: name it, ask one question, suggest the fix. Don't fix it silently, or the user never learns to spot it.

## Before calling it done

- **Gut check:** "Explain this North Star to a skeptical exec in two minutes. Then tell me what would make it obviously wrong." If they can't answer the second part, it isn't tested yet.
- **Quick check** against the red and green flags. Offer the full scored evaluation only if they want it or before a high-stakes review.
- **Independent review:** if the `artifact-reviewer` subagent is available, offer it. Fresh eyes catch the vanity metric the author has grown fond of. Discuss its findings, don't just paste them.
- **Log the bet:** offer a row in `5-Growth/decisions.md`: the North Star, the input belief it rests on most, a confidence level, and a reopen trigger (for example "inputs hit target for two months but the North Star doesn't move").

## Org reality

- **The exec wants revenue as the North Star.** Don't fight about the word. Put revenue at the top of the tree as the business outcome, and show the North Star as the leading indicator that predicts it: "This moves 60 days before MRR does, so we can act before the quarter is lost." Most execs care that it predicts revenue, not what it's called.
- **The metric was picked because it's easy to measure.** Say it plainly: easy-to-count usually means activity, not value. Keep the easy metric as a temporary proxy if you must, label it a proxy, and put instrumenting the real one on the roadmap with a date.
- **Teams game the metric.** It's not a character flaw, it's Goodhart. Watch for the signals (metric up while satisfaction is down, spikes no product change explains), add or tighten a guardrail, and review the definition rather than blaming the team.
- **No analytics instrumentation yet.** Very common. Define the North Star and inputs anyway, because that's what tells you what to instrument. Ship tracking for the North Star event and the top input first. A manual weekly count from the database beats waiting three months for the perfect event pipeline.

## References

- [references/template.md](references/template.md) — North Star template: metric, inputs, guardrails, work connections, belief tree, review cadence, when to change it
- [references/metrics.md](references/metrics.md) — AARRR funnel, leading vs. lagging, guardrails, input-metric trees, vanity vs. actionable
- [references/criteria.md](references/criteria.md) — red/green flags, weighted dimensions, antipatterns, rewrites

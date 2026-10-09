---
name: experimentation
description: Design and run product experiments at a practical PM level — A/B tests, hypothesis tests, rollouts, feature flags, and reading results without pretending to be a statistician. Covers hypothesis, primary metric, sample and duration, guardrails, and ship/kill/pivot calls. Use when the user says "A/B test", "experiment design", "hypothesis test", "rollout plan", "feature flag", "statistical significance", "how long should we run this", "can we ship the variant", or needs to decide whether a change actually worked.
---

# Design and Run an Experiment

An experiment is how you stop arguing about opinions and start arguing about evidence — but only if you decided what would convince you *before* the numbers land. The failure mode I see most: someone runs a test because "we should A/B this", picks whatever metric the dashboard already has, peeks at results on day three, and ships when it looks green. That's not experimentation. That's confirmation bias with a sample size.

Your job as PM isn't to derive p-values by hand. It's to write a decision you'd trust if the variant loses, name the one metric that matters, protect the business with guardrails, and partner with data/engineering on whether you have enough traffic and a clean assignment. If you can't articulate kill criteria upfront, pause and fix that before you flip a flag.

## Is this the right thing?

**Experiment when** you're choosing between two (or a few) approaches that are reversible enough to test, you have a measurable outcome, and the cost of being wrong for a subset of users is acceptable with guardrails in place.

**Don't, and say so, when:**
- The change is tiny and cheap to reverse → ship to everyone, watch the metric, roll back if it breaks. Not everything needs a formal test.
- You don't have enough volume to learn in a reasonable time → you'll either wait forever or fool yourself with noise. Consider a qualitative test, a concierge slice, or a phased rollout with manual monitoring instead.
- The problem isn't validated yet → that's opportunity assessment or discovery, not an A/B test on a solution nobody asked for.
- Legal, trust, or safety can't tolerate a "losing" experience for a cohort → don't randomize harm; find another validation path.
- The team already decided to ship and the test is theatre → name that. Either run a real holdout for learning or skip the pretence.

## Step 1 — Preflight (before any design doc)

Pick 2–3 for what's actually missing. Don't run the list.

- **What decision does this experiment settle?** Ship variant, kill it, pivot the approach, or "learn which segment cares"? If the answer is vague, the test will be vague.
- **What's the hypothesis in one sentence?** "If we [change], then [segment] will [behaviour/metric] because [mechanism]." No mechanism usually means you're testing UI lipstick.
- **What do you know vs. guess?** Baseline rate, expected lift, traffic, seasonality — tag evidence tier (documented / verbal / hunch).
- **What would make you kill the variant even if the primary metric moves?** Guardrails and "absolutely not" outcomes belong here.
- **Who owns analysis and who can stop the test?** If nobody can pull the flag, you don't have an experiment, you have a deployment.

Check the repo if it exists: `3-Work/[initiative]/` (PRD metrics, prior tests), dashboards or notes in research folders. Quote back what's there instead of re-asking.

If they've braindumped, one confirming question is enough. If they insist on skipping: name the biggest peeking-or-underpowered risk in one sentence, then draft with `[GAP: …]` markers. Never invent a baseline conversion rate.

## Step 2 — Lock the hypothesis and the primary metric

One primary metric per experiment. Seriously. Secondary metrics inform the story; they don't decide the ship call unless you pre-registered that rule.

The primary metric should be:
- **Closer to the user outcome** than a proxy three steps away (clicks ≠ revenue unless you've validated the chain).
- **Measurable in the experiment window** — don't pick annual retention for a two-week test unless you have a justified leading indicator.
- **Stable enough** that a bad day doesn't dominate (know your variance; data partners help here).

Write the hypothesis as: *We believe [change] for [who] will improve [primary metric] from [baseline] to [target/min detectable effect] because [reason].* If they can't state baseline, that's the first work item — even a rough range from last month beats guessing after the fact.

## Step 3 — Sample, duration, and practical power

You don't need a PhD. You need honest answers to:

- **How many users/events per variant do we need?** Ask data eng or analytics for a back-of-envelope given baseline rate and the smallest lift you'd act on. If the required lift is implausible, the experiment is a wish.
- **How long will that take at current traffic?** Include full weeks if you have weekday/weekend effects. Seasonality and launches pollute results — note them.
- **Is assignment clean?** Logged-in only, cross-device, mobile vs web, bots, internal users — each one is a way to lie to yourself.
- **What's the exposure?** 50/50 split isn't always right. Sometimes 5% rollout with monitoring is the responsible path.

If the math says six months, say so out loud. The right move might be a smaller bet, a different metric, or accepting directional evidence with eyes open — not running an underpowered test and calling it "directionally positive".

## Step 4 — Guardrails and secondary metrics

Guardrails are what must not get worse while you chase the primary metric: error rates, latency, support tickets, unsubscribe, fraud, compliance events, NPS for a sensitive flow.

List 2–5 guardrails max. For each: threshold for **pause** (investigate) vs **stop** (roll back). Primary metric up 2% while checkout errors double is not a win.

Secondary metrics explain *why* the primary moved or didn't. Pre-define which secondaries are diagnostic only so you don't cherry-pick after the fact.

## Step 5 — Rollout, feature flags, and operational hygiene

- **Flag semantics:** who gets variant, how overrides work, kill switch owner, default on failure (usually control).
- **Ramp plan:** 1% → 10% → 50% → 100% when risk is non-trivial; what you're watching between steps.
- **Instrumentation:** events fire before launch; QA on assignment; logging for debugging without PII leaks.
- **Peeking policy:** agree upfront — fixed horizon vs sequential rules. Casual peeking with optional stopping inflates false positives. If the org peeks anyway, acknowledge it and widen thresholds or shorten the pretence.

Document start time, end time, and any external events (marketing blast, outage) in the experiment log.

## Step 6 — Ship, kill, or pivot (before results arrive)

Write decision rules now:

- **Ship variant if:** primary hits pre-agreed bar, guardrails clean, practical significance (not just statistical) — "worth the complexity and risk."
- **Kill if:** primary flat or negative beyond noise, guardrail breach, or implementation cost higher than expected value.
- **Pivot if:** metric moves for one segment only, or mechanism wrong but signal suggests another bet.

Add a decide-by date and what you do if inconclusive: extend (only with pre-set rules), ship to learn with monitoring, or revert and dig qualitatively.

Stress-test before locking: *What's the first signal you're wrong about the hypothesis?*

## Watch for red flags as it takes shape

No hypothesis, metric soup, no baseline, no guardrails, peeking without a plan, underpowered timeline ignored, ship decision already made. Full flags: [criteria](references/criteria.md). Structure to fill: [design](references/design.md). Name the flag, one question, suggest the fix — don't silently patch.

## Before calling it done

- **Gut check:** "If the variant loses on the primary metric but wins on a secondary you like, what do we do?" If they hesitate, the primary isn't really primary.
- **Quick check** against red/green flags. Offer deeper scoring only if they're gating a big launch.
- **Independent review:** if `artifact-reviewer` is available, offer it on the design doc before launch.
- **Log the bet:** offer a row in `5-Growth/decisions.md` with hypothesis, decision rules, confidence, and reopen trigger if you ship on thin evidence.

## Org reality

- **"We need significance in two weeks."** Say what that forces: huge MDE, wrong metric, or a farce. Negotiate minimum detectable effect and risk tolerance, or run a monitored rollout instead.
- **Stakeholder already promised the feature.** Frame the test as de-risking: pre-agreed guardrails, fast rollback, holdout for learning — not as a veto they'll ignore.
- **No experimentation platform.** Manual cohorts, geo splits, before/after with caveats — label the weaknesses. Don't claim randomization you don't have.
- **Winner everywhere but enterprise.** Segment analysis is pre-planned or it's fishing. If sample is thin, say "directional for SMB only" instead of global ship.

## References

- [references/design.md](references/design.md) — experiment design template (hypothesis, metric, sample, duration, guardrails, ship/kill)
- [references/criteria.md](references/criteria.md) — red/green flags for experiment design and readouts

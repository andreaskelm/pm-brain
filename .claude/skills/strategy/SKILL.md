---
name: strategy
description: Draft, test, or review a product, team, or company strategy, using the Good Strategy/Bad Strategy kernel (diagnosis, guiding policy, coherent actions), the Playing to Win cascade (where to play, how to win), or a team strategy doc built on pillars and explicit non-goals. Use when the user says "product strategy", "write our strategy doc", "is this a real strategy", "review our strategy", "where to play, how to win", "good strategy bad strategy", "diagnosis / guiding policy", "strategic pillars", "non-goals", "our strategy is just goals", "planning next year's direction", or is stuck between two or three big directions. Runs preflight questions before any framework.
---

# Strategy

Most documents titled "strategy" are goals ("grow ARR 40%") or wish lists (eleven priorities, none ranked, all funded on paper). A strategy is a set of choices that makes some things NOT happen. It names the hard problem, picks an approach to it, and makes certain requests easier to refuse. The test I use: if nothing gets harder to justify the week after the strategy is published, it was a vision statement with extra steps. So we find the hard problem first. The frameworks come after.

## Is this the right thing?

| | Answers | Horizon | Looks like |
|---|---|---|---|
| **Vision** | Where are we going, and why does it matter? | 3–10 years | An aspiration, a headline |
| **Strategy** | What's the hard problem, and what are we choosing to do, and not do, about it? | 1–2 years | Diagnosis, choices, non-goals |
| **Plan** | What happens when, and who does it? | Quarter to a year | Roadmap, OKRs, backlog |

People ask for strategy when they actually need something else, and vice versa. Route them:

- **Strategy is clear, they need measurable outcomes for the quarter** → the `okr` skill.
- **Strategy is clear, they need to sequence and communicate the work** → the `roadmap` skill.
- **They need the one metric that captures value delivered** → the `north-star` skill.
- **They're ranking a backlog or choosing among defined items** → the `prioritize` skill.
- **They're evaluating a single opportunity** → that's an opportunity assessment, not a strategy.
- **Small team, shared direction, fixed-scope project** → skip the doc. A one-paragraph diagnosis and a short "not doing" list is enough.

And the reverse: if their OKRs keep changing every quarter, or roadmap debates go in circles, the missing piece is usually strategy, not a better OKR template.

## Step 1 — Preflight (always, even when they say "just write it")

Ask 2–3 of these, picked for what's actually missing:

- **What's the hard problem?** Not the goal, the obstacle between you and it. "Grow 50%" is a goal. "Mid-market customers churn around month 4 because they outgrow our permissions model and we have nothing for admins" is a problem.
- **What are you choosing NOT to do?** If the answer is "nothing really", there's no strategy yet. That's fine, it just means we start with the diagnosis.
- **Who has to agree, and who can quietly veto it?** A strategy the VP of Sales hasn't seen is a draft.
- **What do you know vs. guess?** Which parts rest on usage data or research, which on a leader's say-so, which on a hunch? Name the evidence tier where it's load-bearing.
- **Why now?** What changed: a competitor move, a plateau, a re-org, a new exec?
- **What would this force you to stop that someone cares about?** That's usually where the uncomfortable thought lives.

Before asking, check the repo if it exists: `1-Context/1-company-vision.md`, `1-Context/2-company-strategy.md`, `1-Context/3-company-product-principles.md`, `1-Context/5-company-roadmap.md`, plus `3-Work/[initiative]/` and `5-Growth/decisions.md`. Quote back what's already written instead of asking for it. A team strategy that contradicts the company one is either a mistake or the most important sentence in the doc. Say which.

If they insist on skipping: name the risk in one sentence, then draft with `[GAP: …]` markers where the thinking is missing. Never invent a diagnosis to fill the box.

## Step 2 — Pick the lens

| Situation | Lens |
|---|---|
| "Is this even a strategy?" Reviewing a doc, or the current strategy isn't working | **GSBS kernel** — [gsbs](references/gsbs.md) |
| Choosing markets, segments, positioning; at an inflection point; stuck between 2–3 directions | **Playing to Win cascade** — [playing-to-win](references/playing-to-win.md) |
| A team or product strategy doc people will plan against for 1–2 years | **Pillars + non-goals** — [strategy-doc](references/strategy-doc.md) |
| A full org-wide strategy process: working group, leadership interviews, strategy sprint, rollout | `2-Methods/2-Strategy/1-Strategic-Foundations/1-Strategy-Blocks/` if you have the PM Brain repo |

**GSBS kernel** (Richard Rumelt). Diagnosis, guiding policy, coherent actions. It's a test more than a recipe: you can fill three boxes with nonsense, but you can't fake a diagnosis that explains *why* the problem exists. Walmart in the 1970s didn't have "low prices" as a strategy. It had "small towns are underserved because low density makes conventional stores unprofitable", and everything else followed from that.

**Playing to Win** (A.G. Lafley & Roger Martin). Five linked choices, from winning aspiration down to management systems. Where to play and how to win are the heart of it; the rest checks that you can actually execute. Its best tool for a stuck debate is "what would have to be true?": instead of arguing which direction is right, list what you'd need to believe for each, then test the shakiest belief.

**Pillars + non-goals.** 3–5 choice-shaped focus areas, an explicit list of what you won't do, and the evidence for each. This is the format teams actually plan against. Its weak spot: pillars drift into department names ("Mobile", "Platform") unless you push.

Combos that work: Playing to Win to make the choices, then the kernel to test them. Pillars doc for the artifact, kernel check before it ships. Existing strategy failing: kernel first; if the diagnosis is missing go back to it, if the choices are missing use the cascade.

## Step 3 — Draft, hard problem first

1. **Diagnosis before anything else, in plain words.** Explain why the challenge exists, not just what the symptoms are. "Engagement is down" is a symptom; "new users never reach the second project, which is where the value is" is a diagnosis. If you can't write this paragraph, stop. You're not ready for the rest.
2. **Every choice comes with its opposite.** Each "we will" needs a "we won't" that a reasonable person in the org would argue for. "We won't build low-quality features" isn't a non-goal; "we won't pursue SMB self-serve this year, even though Sales keeps asking" is.
3. **Actions that reinforce each other.** For any two actions, can you say how one makes the other work better? If not, it's a laundry list.
4. **Assumptions out loud.** What has to be true for this to work, and how strong is the evidence for each? Include the uncomfortable one from preflight.
5. **Short.** The kernel fits on 1–2 pages. Budgets, timelines and org charts go in the plan.

While drafting, flag gaps without blocking: *"Your how-to-win is 'best-in-class UX', but you said earlier your two competitors just hired large design teams. What do you have that they can't copy? Keep it as an assumption, or dig into it now?"*

## Step 4 — Watch for bad strategy as it takes shape

Rumelt's hallmarks are the ones to watch: **fluff** (buzzwords standing in for thought), **failure to face the challenge** (no hard problem named), **goals mistaken for strategy** ("our strategy is to reach $50M"), and **bad strategic objectives** (a long list that can't all be resourced). Plus the team-level ones: function-shaped pillars, non-goals nobody wanted anyway, and a how-to-win any competitor could claim. Full list and rewrites: [criteria](references/criteria.md). When one appears, name it, ask one question, suggest the fix. Don't silently fix it, or the user never learns to see it.

## Step 5 — Before calling it done

- **Stop-doing test:** name three things currently in flight or on the request list that this strategy kills or delays. If you can't name one, it doesn't choose anything yet.
- **Competitor test:** could your closest competitor publish this doc with their logo on it? If yes, the how-to-win is generic. Push on what's actually unique: data, distribution, a customer relationship, a capability they'd take two years to build.
- **Newcomer test:** could a new engineer use this doc to say no to a request without asking you? That's the real job of a strategy.
- **Independent review:** if the `artifact-reviewer` subagent is available, offer it, since fresh eyes catch what the author can't. Discuss its findings; don't just paste them.
- **Log the bet:** if they stated (or can state) a confidence that the diagnosis is right, offer a row in `5-Growth/decisions.md` with a reopen trigger, e.g. "reopen if month-4 churn doesn't drop after the admin release."
- **Altitude check:** if this team strategy implies something about company strategy, vision, or product principles, flag it for `1-Context/`. Don't edit those files silently; check `1-Context/CONTEXT-HEALTH.md` for whether they're maintained first.

## Org reality

- **The strategy handed down is a list of goals.** Very common. Write the diagnosis you think sits underneath it and play it back to whoever owns it: "I read this as: the problem is X, so we're betting on Y and not Z. Right?" Their answer either gives you the real strategy or shows there isn't one, and both are useful.
- **You don't have the authority to set strategy.** Write the diagnosis anyway. It's the most persuasive part and needs nobody's permission. Share it as "here's what I'm seeing" with the leader who does own direction, and let them own the guiding policy. A strategy they shaped is one they'll defend.
- **The annual offsite theatre.** Two days, a wall of sticky notes, five pillars that map neatly to the five VPs in the room. Treat the output as raw material. Run the stop-doing test with one or two leaders afterward; that's where the actual choices get made, or visibly don't.
- **Nobody references it after week 2.** A strategy that isn't used in decisions is dead. Wire it into one recurring decision: the intake form asks "which pillar, and what does it displace?", or planning review starts with the non-goals. If nobody has ever said "that's a non-goal" in a meeting, either the non-goals are fake or the doc is.

## References

- [references/gsbs.md](references/gsbs.md) — the kernel, Rumelt's bad-strategy hallmarks, kernel template
- [references/playing-to-win.md](references/playing-to-win.md) — five-choice cascade, coherence checks, "what would have to be true", template
- [references/strategy-doc.md](references/strategy-doc.md) — pillars + non-goals strategy doc template, pillar scorecard
- [references/criteria.md](references/criteria.md) — red/green flags, before/after rewrites

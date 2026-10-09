---
name: roadmap
description: Build, restructure, or review a product roadmap, including Now/Next/Later, outcome-based, theme-based, scenario and rolling roadmaps, with confidence levels and time ranges instead of hard dates. Use when the user says "build a roadmap", "now/next/later", "outcome roadmap", "plan the next quarters", "what goes on the roadmap", "stakeholders want dates", "sales needs a date", "leadership wants a Gantt", "the roadmap keeps changing", or "review my roadmap". Runs preflight questions and checks that prioritization is done before structuring anything.
---

# Build a roadmap

A roadmap is a communication tool for direction, not a project plan and not a promise. The failure I see most often: a tidy grid of features with dates, built in a week, and by the following Tuesday someone in Sales has screenshotted Q3 into a deal deck. Now every line is a commitment nobody actually made. So we decide what problems we're solving and how sure we are first, and the roadmap is just how we show it.

## Is a roadmap the right thing?

**Build one when** there's a direction to communicate (a strategy, OKRs, even a rough "this year is about retention"), the work has already been prioritized, and more than one audience needs to know where you're headed and how sure you are.

**Don't, and say so, when:**
- **There's no strategy to point at.** A roadmap without one just sequences opinions. Ask what outcome this year or quarter is for, even a rough one, before touching horizons.
- **Nothing has been prioritized yet.** The roadmap shows prioritization decisions; it's the wrong place to make them. Run the `prioritize` skill first, then come back.
- **It's very early discovery.** You don't have a direction yet, you have questions. A list of open bets with what you need to learn is more honest.
- **It's a one-off project with fixed scope and date.** That's a project plan. Use one.
- **It's internal tooling with no outside stakeholders.** A ranked backlog does the job.

## Step 1 — Preflight (always, even when they say "just lay it out")

Ask 2–3 of these, picked for what's actually missing. Don't run the whole list.

- **Who is this for, and what will they decide with it?** A board, a sales team and an eng team need different roadmaps from the same thinking.
- **What outcome is the Now column serving?** One goal, not "growth".
- **What are we NOT doing if we do this?** If they can't name anything, nothing has been prioritized.
- **What's changed in the last 3–6 months that we're not talking about?** Market, team, a big customer, a failed bet.
- **Which line is on here because someone senior asked?** Not wrong, but it should be visible.
- **What do you wish you knew that you don't?** That's your Later column's research list.

Before asking, check the repo if it exists: `1-Context/` (strategy, OKRs, any company roadmap), `3-Work/` initiative folders (opportunity assessments, decisions), and `5-Growth/decisions.md` for prioritization calls this roadmap should reflect. "Your March call was retention first, but half of Now is acquisition. Did that change?" beats any template.

If the prioritization already exists in the conversation or the repo, one confirming question is enough. If they insist on skipping: name the risk in one sentence, then draft with explicit `[GAP: …]` markers. Never invent metrics or confidence to fill a cell.

## Step 2 — Pick the shape

| Shape | When |
|---|---|
| **Now / Next / Later** (default) | Most product roadmaps. Confidence drops as you move right. |
| **Outcome-led** | Stakeholders keep asking "why" about features. Lead with the outcome, initiatives sit underneath. |
| **Theme-based** | Long horizons, or you want room to swap initiatives without re-announcing. |
| **Scenario-based** | One external factor (funding, regulation, a big contract) would flip priorities. Show the 2–3 versions. |
| **Rolling** | Continuous planning, no quarterly reset. Items move between columns as confidence changes. |

These mix. The common good combo is Now/Next/Later where Now holds specific initiatives, Next holds outcome targets, and Later holds themes only. Template: [template](references/template.md).

## Step 3 — Build it, problems before features

1. **Name problems and outcomes, not systems.** Every line that reads "Implement X" or "Migrate to Y" gets one question: what problem does this solve? "Salesforce integration" becomes "Sales reps stop re-entering deal data twice a day." Migration percentages aren't outcomes either. Ask what the migration enables.
2. **Place items by confidence, and make the confidence honest.**

   | Horizon | Range | Confidence | What goes in it |
   |---|---|---|---|
   | **Now** | 0–3 months | High (70–90%) | Specific initiatives, metrics, owned dependencies |
   | **Next** | 3–9 months | Medium (40–70%) | Outcome targets plus the key assumption each rests on |
   | **Later** | 9–18+ months | Low (10–40%) | Themes, strategic goal, what we need to learn |

   A High-confidence item in Later is either really Now or wishful thinking. A Low-confidence item in Now means the team is about to start something it doesn't understand. Push on both.
3. **Time ranges, not dates, beyond Now.** Now can carry a month or quarter. Next gets a half-year. Later gets a year or nothing. A specific date nine months out is a guess, and putting it on a slide turns the guess into a promise.
4. **Metrics that aren't binary.** "Shipped" and "100% migrated" are delivery, not success. Baseline → target, even rough: "time-to-first-value from 14 days to 7."
5. **Dependencies as what, from whom, by when.** "Marketing, IT" isn't a dependency; it's a list of departments. "Billing API access from Finance Eng by end of May, or the reconciliation work slips a sprint" is.
6. **Write down what's NOT on it.** Small features and bug fixes don't belong on a roadmap at all. The requests that didn't make it do belong in a "not on this roadmap" list, with why and what would change your mind. That list prevents more arguments than the roadmap itself.
7. **Header basics:** a one-line disclaimer, last-updated and next-review dates. Rhythm that actually works: Now gets a weekly glance, confidence gets re-checked monthly, the whole thing gets a quarterly refresh.

While drafting, flag gaps without blocking: *"Customer health dashboard is in Next at Medium confidence, but the assumption is that usage and ticket volume predict churn. Has anyone checked that against last year's churned accounts, or is it a hunch?"*

## Step 4 — Watch for red flags as it takes shape

System names instead of problems, migration percentages as outcomes, team names as dependencies, binary metrics, unexplained jargon, no business problem stated, confidence that doesn't match the horizon, dates far out, a stale review date. Full list, weighted dimensions and rewrite examples: [criteria](references/criteria.md). When one appears: name it, ask one question, suggest the fix. Don't silently fix it, or the user never learns to see it.

## Step 5 — Before calling it done

- **Gut check:** "Explain this roadmap to a skeptical exec in two minutes. What would make them say it's obviously wrong? What's missing that should be there?"
- **Bias check, lightly:** is anything here because it was the last loud request (recency, squeaky wheel), or because it was on last quarter's roadmap (status quo)?
- **Quick check** against the red/green flags. Offer the full scored evaluation only if they want it, or before a big planning review.
- **Independent review:** if the `artifact-reviewer` subagent is available, offer it, since fresh eyes catch what the author can't. Discuss its findings; don't just paste them.
- **Log the bet:** for the top Now item, offer a row in `5-Growth/decisions.md`: confidence that it moves the outcome, and a reopen trigger that's an observable signal, not "if things change."
- **Audience versions:** if they're about to present it, the [stakeholder scripts](references/stakeholder-scripts.md) cover the "when exactly?" conversations and how to cut it for each audience.

## Org reality

- **"Sales needs a date for this deal."** Don't refuse and don't cave. Ask what the date is for: signing, go-live, a renewal? Often they need "before their rollout in September," which a range can answer. If it's Now, give the range and confidence. If it's Next, say so plainly and say what would pull it forward. If the company truly decides to commit, make it an explicit commitment with an eng-backed date and a named thing that gets bumped. Commitments are fine; what hurts is the roadmap making them by accident.
- **"Leadership wants a Gantt chart."** Give them the visual and keep the honesty in it. Now can sit on a timeline, it's high confidence anyway. Next and Later go in as wide bands labeled with confidence, not bars with end dates. Keep the outcome column. I've generally seen execs accept fuzzy bands faster than PMs expect, as long as Now is crisp.
- **The roadmap as a commitment contract.** Every change gets read as a miss, so people stop changing it and it goes stale. A disclaimer alone won't fix that culture. Separate the genuinely committed few (contractual, regulatory) and mark them as such, and keep a short "what moved and why" log. Changes with a reason read as learning; silent changes read as failure.
- **The feature-factory org.** They want a list of features with quarters. Give them the feature name first because that's the language they read, and put the problem and the metric right under it. Their format on top, your outcome thinking underneath. Over a few cycles the outcome line is the one people start quoting back to you.

## References

- [references/template.md](references/template.md) — Now/Next/Later template with examples, confidence legend, not-on-roadmap list
- [references/criteria.md](references/criteria.md) — red/green flags, weighted dimensions, antipatterns, rewrites
- [references/stakeholder-scripts.md](references/stakeholder-scripts.md) — responses to "when will X ship?", framing per audience

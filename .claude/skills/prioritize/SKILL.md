---
name: prioritize
description: Prioritize a backlog, features, initiatives, or bugs, and pick and run the right method (RICE, ICE, Impact–Effort, MoSCoW, Kano, severity × frequency). Use when the user asks "what should we build first", "help me prioritize", "rank these", "MVP scope", "what makes the cut", "sprint or quarterly planning", or is handling a stakeholder pushing their feature. Surfaces the judgment and trade-offs before any scoring.
---

# Prioritize

Prioritization is deciding what you're *not* going to do, and being able to say why. Frameworks make that defensible; they don't make it correct. The pattern I keep running into: a beautifully scored spreadsheet where every number was reverse-engineered from the answer someone already wanted. So we get the judgment on the table first, then use a method to pressure-test it.

## Is this actually a prioritization problem?

- **Only one option on the table?** That's a yes/no decision. Help them generate alternatives first (including "do nothing"), or validate the one option.
- **Options are still fuzzy problems, not defined items?** That's discovery. You can't score what you can't describe.
- **No strategy to prioritize against?** Say so. Scoring without a goal just measures enthusiasm. Ask what outcome this quarter is for, even a rough one.
- **Fewer than ~5 items?** Skip the framework. Talk through trade-offs directly.

## Step 1 — Preflight (before any scoring)

Pick 2–3 questions for what's missing:

- **If you could only do ONE thing on this list, what is it, and why?** Their gut answer is data. Write it down so the scoring can challenge it.
- **What outcome are we optimizing for?** One metric or goal, not "growth".
- **What evidence says this matters?** Real data, interviews, deals lost, or someone's say-so? Name the evidence tier.
- **What's the opportunity cost?** What does the team stop doing to do this?
- **What are you avoiding because it's hard, not because it's wrong?**
- **Who's going to be unhappy with the result,** and what will they do about it?

If the repo exists: check `5-Growth/decisions.md` and `3-Work/[initiative]/decisions.md` for earlier calls this might contradict, and `1-Context/` for strategy and OKRs. "This cuts against what you decided in March" is worth more than any score.

## Step 2 — Pick the method

| Situation | Method |
|---|---|
| Quick call, little data, many early ideas | **ICE** |
| Bigger bets, you have reach and effort estimates | **RICE** |
| Workshop, stakeholder alignment, disagreement to surface | **Impact–Effort** |
| Fixed timebox, MVP, "what makes the cut" | **MoSCoW** |
| Worried about missing table stakes or over-indexing on shiny stuff | **Kano** |
| Bugs | **Severity × frequency** |

Combos that work: ICE to triage → RICE on the top 5–10. MoSCoW for the release, sanity-checked with RICE. Kano first when there's a risk of building delighters while basics are broken. Impact–Effort when people disagree, to surface *why*, then decide.

Details, scales and worked examples: [scoring](references/scoring.md) (RICE, ICE, Impact–Effort, bugs, portfolio balance) and [MoSCoW and Kano](references/moscow-kano.md).

## Step 3 — Score, writing the assumption next to every number

- Get effort from engineering, not from the PM's optimism. Rough is fine.
- Every score gets a one-line rationale. "Impact 3: #1 exit-interview churn reason" — not "high impact".
- **Watch the confidence column.** If everything is 80–100%, push: "Which of these would you bet your own money on?" Low confidence isn't bad. It tells you which item needs a cheap test before a big build.
- Score collaboratively if you can. A score the team built is one they'll defend.

## Step 4 — Challenge the ranking, don't accept it

- **Compare to the gut answer from Step 1.** Matches: fine, but ask if the scoring was bent to match. Doesn't: that's the interesting conversation. Which is wrong, the gut or the numbers?
- **Swap test:** for any two adjacent items, would you trade their order? If yes, the scores are too close to decide. Use judgment and say so.
- **Balance check:** quick wins vs. big bets, tech debt reserved (10–20%, before scoring), segments served, OKR coverage.
- **Easy-button check:** if the top 5 are all low-effort, ask what important hard thing is sliding.

## Step 5 — Decide, record, communicate

- Write the record: [template](references/template.md). The **Not doing** list and the **trade-offs** matter more than the ranking.
- Frame it for the audience. Leadership: trade-offs and opportunity cost. Engineering: why the high-effort item is worth it. Customer-facing teams: what's *not* coming, and when you'll revisit.
- **Log the call:** offer a row in `5-Growth/decisions.md` for the top bet: confidence that it moves the metric, and a reopen trigger.
- Quick check against [criteria](references/criteria.md) before sharing.

## Org reality

- **"But the VP really wants this."** Don't fight it with scores alone. Score it honestly, show the current top 10, and ask: "Which of these should we drop to do yours?" Make the trade-off theirs to own. If it still wins, document *why it moved*. That's not failure, it's honesty, and it protects you in three months.
- **Everything is P0.** Define P0 in observable terms (production down, data loss, legal) and cap it. If stakeholders label everything critical, stop using their labels and use the scores.
- **Prioritization theatre.** Some orgs run the ritual after the roadmap was already decided upstairs. Name it, privately at least. Then use the framework where you *do* have room (sequencing, scope within an initiative) rather than pretending you're choosing the initiatives.
- **Feature-factory planning.** If the org only wants a ranked feature list, give them one, but keep the outcome and the key assumption in the rationale column. Same artifact, better thinking underneath.

## References

- [references/scoring.md](references/scoring.md) — RICE, ICE, Impact–Effort, bug matrix, portfolio balance, calibrating scores
- [references/moscow-kano.md](references/moscow-kano.md) — MoSCoW with the 60% rule; Kano questionnaire, evaluation table, coefficients
- [references/template.md](references/template.md) — prioritization record, backlog item
- [references/criteria.md](references/criteria.md) — red/green flags, rewrite examples

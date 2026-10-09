# Calibration

**Product sense is a track record, not a vibe.** When you say you're 70% sure, are you right about 7 times out of 10? That's calibration. It's the one part of "judgment" you can actually measure.

*Adapted from Viveck P Kumar's [Product Judgment Test](https://www.notion.so/The-Product-Judgment-Test-2e92182754b68081a535fd7f507f7b91).*

---

## Why bother

Most PMs get evaluated on intuition, confidence, and hindsight storytelling. None of those answer the question that matters: **how often were you right before you knew the answer?** Explaining an outcome after the fact is easy; everyone's a genius in the retro. Predicting it beforehand is the skill.

What tends to happen without a log: you remember the calls you got right, you rationalize the ones you got wrong ("the market shifted"), and your confidence drifts upward while your hit rate stays flat. I've seen senior PMs who were confidently wrong on every new-product bet for two years and never noticed, because nobody wrote the confidence down at the time.

## The habit

1. **Log before you know.** Decision, confidence %, reopen trigger, resolve-by date, in [5-Growth/decisions.md](../../../../5-Growth/decisions.md). Logging after the early numbers come in is cheating your own growth.
2. **Resolve honestly.** When the date passes: Exceeded / Met / Failed, plus what surprised you.
3. **Review misses more than wins.** A win confirms what you already believed. A miss shows you where your model of the world is broken.
4. **Look at patterns, not single rows.** After 10–20 resolved calls you'll see it: overconfident on new products, underconfident on iterations, blind to a certain kind of stakeholder.

## Scoring (Brier)

Per resolved decision:

- **p** = confidence ÷ 100
- **Outcome value:** Exceeded = 1.0, Met = 0.8, Failed = 0.0
- **Brier** = (p − outcome value)²

It punishes being wrong, and it punishes being *confidently* wrong much harder. 90% on a failure costs 0.81; 60% on a failure costs 0.36.

**Overall score** = average Brier across resolved rows. Lower is better.

| Overall Brier | Read |
|---|---|
| < 0.10 | Elite — rare, and needs 20+ resolved calls before you believe it |
| < 0.15 | Strong calibration |
| < 0.25 | Typical PM |
| < 0.40 | Overconfident |
| ≥ 0.40 | Uncalibrated |

**Worked example:** 70% confident, outcome Met → (0.7 − 0.8)² = 0.01. Good call, well calibrated.

### Optional weighting

If you want big bets to count more than tweaks, weight each row by **Bet type × Novelty** and take the weighted average (Σ Brier × weight ÷ Σ weight):

| Bet type | Weight | Novelty | Weight |
|---|---|---|---|
| New product | 3.0 | New behavior | 1.5 |
| Expansion | 2.0 | Known problem | 1.0 |
| Iteration | 1.0 | | |

Example: new product × new behavior = 4.5. Skip the weighting until you have enough rows for it to matter. The agent can compute either version from `decisions.md` during the monthly synthesis.

## Where it breaks down

- **Self-fulfilling prophecy.** Unlike a weather forecaster, you have your hand on the wheel. The risk is over-investing in a failing bet to save your score. That's sunk cost wearing a calibration costume. Measure your initial read; don't defend it.
- **Luck vs. skill.** You can be right for the wrong reasons and wrong for the right ones. A competitor getting acquired overnight isn't a judgment failure. That's why it's patterns over 10+ calls, not single rows.
- **Garbage in.** "Users will like the new nav" can't be scored. If the outcome isn't falsifiable, sharpen it until it is, or don't log it with a confidence level.
- **The 80% hiding place.** 80 feels confident without committing. Force the choice: is this a 70 (real risk) or a 90 (you'd be shocked)?
- **Calibration, not accuracy.** Someone who's right 100% of the time is only taking safe bets on small tweaks. Calibrated humility is worth more to a company than blind confidence.

## In practice

The agent offers a `decisions.md` row whenever you state a decision with a confidence level (the forecast trigger), checks due rows in the weekly review, and can compute your Brier trend on request. Your part is being honest at logging time and reading the misses.

## Related

- [Evidence strength](7-evidence-strength.md) — the tier of evidence behind a call should shape the confidence you give it
- [One-way vs. two-way doors](2-one-way-two-way-doors.md) — reversibility × confidence decides whether to decide now or gather more
- [Pre-mortems](1-pre-mortems.md) — a cheap way to find out your 90% is really a 70%

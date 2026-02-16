# Product Judgment Test

**A practical way to measure and improve product sense.**

*Source: Viveck P Kumar. Adapted for PM Brain. https://www.notion.so/The-Product-Judgment-Test-2e92182754b68081a535fd7f507f7b91*

---

## The Problem: The Myth of "Product Sense"

Product sense is one of the most valued skills in our industry. It is also the least defined. We interview for it, we praise it, and we promote based on it. **But we almost never measure it.**

Most PMs rely on intuition, confidence, and hindsight storytelling. But none of these tell us the one thing that actually matters: **How often were you right?**

At Amazon, the bar for leadership is simple and brutal: **"Being right, a lot."** In product management, we rarely apply that same bar to ourselves. As a result, many PMs keep shipping things that don't work, without ever improving the core skill that caused the failure: **Judgment.**

---

## The Insight: Prediction vs. Explanation

Great PMs are not just good at explaining outcomes after they happen. **They are good at predicting them before they start.**

Product sense is not a "vibe" or a mystical gift. It is a track record. Specifically, it is the ability to:

- Estimate uncertainty accurately.
- Predict user behavior and market response *before* shipping.
- Calibrate personal confidence to objective reality.
- Identify personal biases and learn from misses.

Judgment is a muscle. And like any muscle, it only grows when it is put under the tension of accountability.

---

## The Solution: The Product Judgment Test

This tool is a simple, repeatable way to quantify your intuition. It works by forcing one high-leverage habit: **Make your beliefs explicit before the outcomes are known.**

The tool uses a **Weighted Brier Score**—the gold standard in forecasting—adapted specifically for product work. It ensures that:

- **New products** carry more weight than minor iterations.
- **High-impact bets** influence your score more than "busywork."
- **Overconfidence** is penalized, while **calibrated humility** is rewarded.

---

## How to Use the Test (4-Step Workflow)

| Phase | Action | Time | Key metric |
|-------|--------|------|------------|
| **1. Forecast** | Record your prediction and confidence % *before* you ship. | 2 min | Confidence % |
| **2. Classify** | Tag the bet by Type (New Product / Expansion / Iteration) and Novelty (New Behavior / Known Problem). | 30 sec | Weight |
| **3. Resolve** | When the deadline passes, close the loop: Target, Actual, % of Target, Outcome, Surprise note. | 5 min | % of Target, Outcome |
| **4. Analyze** | Review the Dashboard monthly for calibration, hit rate, and trend. | Monthly | Overall Brier Score |

**Detailed workflow:** See [forecast-log.md](forecast-log.md) for the log format. See [brier-calculation.md](brier-calculation.md) for the scoring formula. See [dashboard.md](dashboard.md) for where to record your Overall Brier and trend.

---

## How to Win at This Test

1. **Log BEFORE you ship.** Logging after you see early data is cheating your own growth.
2. **Review misses more than wins.** A "win" tells you what you already knew. A "miss" tells you where your mental model of the world is broken.
3. **Don't optimize for the score.** Optimize for **calibration**. The goal isn't to be 100% right; the goal is to know *exactly* how likely you are to be right.
4. **Avoid the 80% trap.** Force yourself to choose: Is it a 70% bet (risky) or a 90% bet (highly validated)?
5. **Be specific.** If you can't measure the outcome numerically, don't forecast it in this tool. Use it for **falsifiable hypotheses.**
6. **Use "What surprised me."** That note is where the learning compounds.

---

## Caveats to Keep in Mind

### 1. Beware the "Self-Fulfilling Prophecy"

Unlike forecasting the weather, you have your hand on the wheel. There is a risk that you might over-invest in a failing feature just to "save" your judgment score.

**The mindset:** Use this tool to measure your **initial intuition**, not to justify "sunk cost" fallacies. The goal is to be right about the *market*, not to be right at any cost.

### 2. Distinguish Luck from Skill

You can be right for the wrong reasons (Luck) and wrong for the right reasons (Bad Luck).

**The mindset:** If a global pandemic hits or a competitor is acquired overnight, your forecast will be wrong. That's okay. Focus on the **patterns** over 10+ bets rather than obsessing over a single "miss" caused by an external shock.

### 3. Garbage In, Garbage Out

The Brier score is only as good as the specificity of your question. If your prediction is vague (e.g. "Users will like the new nav"), you can't accurately score it.

**The mindset:** If you can't measure the outcome numerically, you shouldn't be forecasting it in this tool. Use this for **falsifiable hypotheses.**

### 4. Calibration is the Goal, Not 100% Accuracy

A "perfect" score isn't someone who is right 100% of the time—that person is likely only taking "safe" bets on minor tweaks.

**The mindset:** The "Superforecaster" goal is to ensure that when you say you are 70% sure, you actually come out right 7 out of 10 times. **Calibrated humility** is more valuable to a company than **blind confidence.**

---

## Confidence Calibration (Before / After Decisions)

**Before a decision:** Rate your confidence (0–100%). Ask: What would make me more confident? What would make me change my mind? Am I overconfident (Dunning–Kruger) or underconfident (discounting my expertise)?

**Confidence-based rules:** See [PRODUCT-SENSE-RULES.md](../../PRODUCT-SENSE-RULES.md) (Confidence-Based Decision Rules) for when to decide now vs. gather more info vs. double-check with others. Use reversibility + confidence level to choose.

**After a decision (e.g. 3 months later):** Was I overconfident (outcome worse than expected), underconfident (outcome better), or well-calibrated? Review 20+ decisions quarterly to spot systematic over/underconfidence by context.

---

## What Lives in This Folder

| File | Purpose |
|------|----------|
| **README.md** (this file) | Overview, workflow, how to win, caveats, confidence calibration. |
| **forecast-log.md** | Your running log: forecast + resolution. Append rows before ship; resolve when deadline hits. |
| **brier-calculation.md** | Formula, weight table, outcome mapping, interpretation bands. |
| **dashboard.md** | Where to record Overall Brier and trend (update monthly). |

Optional: Run the Python script to compute Overall Brier from closed rows in your forecast log:
`python scripts/compute_brier.py` (from this folder) or `python 00-Meta/0.3-Product-Judgment-Test/scripts/compute_brier.py` from repo root.

---

## How This Connects to the Rest of PM Brain

- **Learning log:** In your [monthly synthesis](../0.1-Learning-Log/README.md), review your Product Judgment Test dashboard and note trend vs last month.
- **Growth portfolio:** Summarize your Overall Brier trend in [3-metrics-dashboard.md](../0.2-Growth-Portfolio/3-metrics-dashboard.md) and [1-product-sense-journey.md](../0.2-Growth-Portfolio/1-product-sense-journey.md) as evidence of calibration.
- **Prioritization log:** Major bets in your forecast log can [cross-reference](../2-prioritization-decision-log.md) your prioritization decision log.
- **00-Meta overview:** See [00-Meta/README.md](../README.md) for how this fits into your minimal workflow (e.g. before shipping: log forecast; monthly: resolve closed bets, update dashboard, review in monthly synthesis).

---

## Final Note

Most PMs never improve their judgment because they never look it in the eye. This test changes that. Use it honestly. Use it consistently. **Let the data humble you.**

That is how you start being right, a lot.

# Decisions

Every call worth remembering, one row each. Log it **when you make it**, not when you know how it turned out. Logging after the early data is in is cheating your own growth.

**Who writes this:** usually the agent. State a decision with a confidence level and it offers to log the row; you confirm or edit. Resolve rows in the weekly review once the resolve-by date has passed.

**Columns:**
- **Decision** — the call, specific enough to be wrong. "Ship A before B", "Kill Y", "Multi-tenant for Q3 — onboarding time drops from 3 weeks to 3 days". Link the initiative or doc if there is one.
- **Confidence %** — 50 = coin flip, 70 = real evidence with real risks, 90 = would be shocked if wrong. Avoid 80 as a hiding place: is it a 70 or a 90?
- **Reopen trigger** — what would change your mind. Specific and falsifiable ("2+ enterprise customers request real-time and show buying intent"). The weekly drift sweep and contradiction detection read this column.
- **Resolve by** — when you'll know.
- **Outcome** — Exceeded / Met / Failed, plus one line on what surprised you. The surprise is where the learning is.
- **Brier** — filled on resolution: (confidence − outcome)², with Exceeded = 1.0, Met = 0.8, Failed = 0. Math, weighting, and bands: [calibration](../2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/8-calibration.md).

| Date | Decision | Confidence % | Reopen trigger | Resolve by | Outcome | Brier |
|------|----------|--------------|----------------|------------|---------|-------|
| *(example)* | Remove signup step 3 — completion 40% → 55% | 70 | Support tickets cite signup as top-3 pain for 2+ weeks after launch | 2026-01-15 | Met — 58%; drop-off moved to step 2, not gone | 0.01 |

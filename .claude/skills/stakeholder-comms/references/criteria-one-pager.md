# One-Pager Criteria

Artifact-specific criteria. The process (gut check first, flag multiplier, weighted score, output format) is shared. In PM Brain it lives in `system/EVALUATION.md`; standalone, use: red flags → multiplier (0–1 red: 1.0×, 2–3: 0.8×, 4–5: 0.5×, 6+: 0.2×; +0.5 per green flag, max +2), weighted score × multiplier, then top 3 fixes with before/after rewrites.

Gut check before scoring: "Explain this one-pager to a skeptical exec in two minutes. What decision would they think you want? What would they poke first?" Write the answer down, then compare it to the scored result. Where they disagree is the interesting part.

## Red flags

- **Unclear ask** — the reader can't tell what decision or action is needed
- **No deadline on the ask** — a decision with no date is a discussion
- **Buries the lead** — the key point or ask sits in the middle or at the end
- **Missing context** — reader lacks what they need to understand the problem
- **Jargon-heavy** — acronyms and team shorthand without definitions
- **Missing data** — claims with no numbers or evidence behind them
- **Vague language** — "improve significantly", "better experience"
- **Wrong audience** — wrong level of detail, or assumes knowledge the reader doesn't have

## Green flags

- Ask and deadline stated in the first paragraph
- TL;DR leads with the punchline and would stand alone
- Problem stated with context and evidence, evidence tier visible where it matters
- Specific numbers: baseline → target, not adjectives
- Written for one identifiable reader at the right level of detail
- Trade-offs, risks and rejected alternatives addressed honestly
- Scannable: headings, short sections, whitespace

## Weighted dimensions

| Dimension | Weight | 9–10 | 7–8 | 4–6 | 1–3 |
|---|---|---|---|---|---|
| **Clarity** | 25% | Understood in 3 minutes; no undefined jargon; easy to scan | Mostly clear, minor gaps | Takes effort; jargon issues | Unclear or jargon-heavy throughout |
| **Decision-driving** | 25% | Specific ask upfront with deadline; reader knows exactly what to do | Clear ask, small gaps in action or timing | Ask vague or buried | No ask; unclear what action to take |
| **Stakeholder focus** | 20% | Right level of detail for the named reader; anticipates their concerns | Minor misalignment | Wrong depth; assumes too much or too little | Wrong audience entirely |
| **Completeness** | 15% | Problem, proposal, why now, impact, approach, trade-offs, ask all present | Minor section gaps | Key sections thin or missing | Critical sections missing |
| **Data & evidence** | 10% | Claims backed by specific numbers and sources | Small gaps in specificity | Some data, much vague language | Purely qualitative or vague |
| **Accessibility** | 5% | Clear visual hierarchy; reads fast | Minor formatting gaps | Dense in places | Wall of text |

Bands for the final score: 8+ ready to share · 6–7.9 minor refinements · 4–5.9 significant rework · below 4 rewrite from the ask down.

## Antipatterns (quote the instance when you find one)

- **Clarity:** buried lead; undefined acronyms; missing context for a reader who wasn't in the room
- **Decision:** no ask; vague ask ("thoughts?"); multiple asks competing so the reader picks the easiest
- **Stakeholder:** assumes prior knowledge; too much detail for the reader (architecture for an exec); written for the author's team rather than the reader
- **Data:** claims without numbers; adjectives instead of baselines; no evidence at all
- **Completeness:** no problem statement (solution-first); no trade-offs, so it reads like a sales pitch; no why-now, so "later" is the easy answer
- **Accessibility:** dense paragraphs; longer than it needs to be

## Rewrite examples

**Ask**
- Before: "We need to improve alerts."
- After: "ASK: Approve $500K for Q2 to build ML-based alert prioritization. Decision needed by March 15, one week before Q2 planning locks."
- Why: specific yes/no, amount, deadline, and why the deadline is real.

**Problem**
- Before: "Alerts are a problem."
- After: "Operations teams spend 30 min/day triaging alerts; 80% are false positives. In a survey of 50 teams, 70% spend more than 20 min/day on triage."
- Why: who, how much, and evidence the reader can check.

**TL;DR**
- Before: "This one-pager discusses alert improvements."
- After: "We propose ML-based alert prioritization to cut triage time from 30 to 5 minutes. ASK: approve $500K for Q2 by March 15."
- Why: punchline, impact and ask in two sentences. If they stop here, they still know what you need.

**Exec framing**
- Before: "The model uses gradient-boosted classifiers over a feature store of 40 signals…"
- After: "Alerts get a confidence score; low-confidence ones are auto-dismissed and logged. Expected impact: 83% less triage time."
- Why: what it does and what it's worth, at the reader's altitude.

# Braindump — Golden Rule

**The Golden Rule: Braindump before structure.**

Before any framework, template, or structured tool: brain dump first. Raw unstructured thinking beats shallow filled-in templates.

## Product Mode Check (ask first)

Before braindump starts, ask explicitly:

> "Are we in **product mode** (why, goals, second-order effects, trade-offs) or **project mode** (when, who, completion)?"

If project mode — or they're about to fill boxes — switch to product mode before continuing.

## Why

Frameworks are seductive — boxes to fill. The trap is optimizing for completion, not insight. Think BEFORE you structure.

## Sufficiency Criteria

Before leaving braindump / product_sense, all four must be explicit:

- **Named assumptions** — not just desired outcome
- **Know vs. guess** — separated clearly
- **At least one risk or second-order effect** — "and then what?"
- **At least one uncomfortable thought** — challenges the current plan

Meeting criteria on paper isn't enough — push on quality. A fig-leaf assumption (safe, obvious) is not the same as the assumption that actually decides this. Name the difference.

A real braindump takes multiple exchanges — a single-turn dump rarely surfaces the actual thinking. If any criteria missing, stay in product_sense. Use [prompts.md](prompts.md). Session sequence: [README.md](README.md). Stuck mid-braindump: [evaluation.md](evaluation.md).

## Why Quality Matters

Decision quality (process) can be separated from outcome (result). Good judgment improves quality; outcomes still involve luck. This is what you're building with every braindump.

## Lightweight Version (execution_mode)

Even on "write my PRD": 2–3 preflight questions before template — "Why this, why now?", "What do you know vs. guess?", "Who is this for?" Lenses from AGENTS.md still run.

## 30-Second Pre-Flight (before any major decision)

Quick gate before the decision table. Don't aim to answer everything — honest, messy thinking in 10–30 minutes is enough.

| Check | Question |
|-------|----------|
| **Why** | Can I articulate WHY this matters in one sentence? |
| **Second-order** | Have I asked "and then what?" at least twice? |
| **Edge cases** | Have I identified 3+ ways this could break? |
| **Trade-offs** | Do I know who loses from this choice? |
| **Bias** | What bias might I be falling for? (See [6-meta-thinking](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/6-meta-thinking-for-product-sense.md) and [2-Bias](../../2-Methods/1-Foundations/2-Bias/1-bias-framework.md).) |
| **Information** | Do I have enough info to decide with 70%+ confidence? |
| **Reversibility** | Do I know if this is reversible? |
| **Communication** | Can I explain this decision clearly to a skeptic? |
| **Taste** | Does this feel right, or just defensible? If a team I respect shipped this, would I be proud of it? |
| **Conviction** | Do I have a real point of view, or am I waiting for data to tell me what to think? |
| **Political** | Who has informal veto power? Have I gotten signal from them — not just their reports? |

**Red flags (STOP if any):** I can't explain why this matters; I haven't thought through what could go wrong; I'm deciding on one data point; I'm afraid to share this reasoning publicly; this feels rushed but I can't say why; I haven't considered alternatives; I don't know what success looks like.

**Green lights (PROCEED if most):** I can explain the rationale; I've identified second-order effects; I've anticipated edge cases; I know what we're trading off; I'd defend this publicly; I've considered alternatives; I know how we'll measure success; I've set a review date.

## Decision Table (before execution_mode)

When braindump is sufficient and a decision is on the table, use confidence + reversibility:

| Confidence | Reversibility | Action |
|------------|---------------|--------|
| **>80%** | Reversible | Decide now. Set review date. |
| **>80%** | Irreversible | Double-check with 2–3 others first, then decide. |
| **50–80%** | Can learn quickly (<1 day) | Gather specific info that would increase confidence, then decide. |
| **50–80%** | Slow to learn | Decide with current info + set clear review point to adjust. |
| **<50%** | — | Don't decide yet. Either learn more or reframe the decision. |

Offer Product Judgment Test logging when confidence is stated — see [5-Growth/3-Product-Judgment-Test/](../../5-Growth/3-Product-Judgment-Test/).

## Override

User says "skip braindump" → acknowledge, suggest 2-minute braindump, proceed if they insist.

## Human rationale

See [docs/principles.md](../../docs/principles.md) for why this design works.

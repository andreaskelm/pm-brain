# Product Sense Coaching

**What this is:** The deep coaching toolkit for developing **product sense** — braindump loop, situation prompts, exit criteria. Load when entering **product_sense** or when lightweight coaching (AGENTS.md lenses + principles) isn't enough.

**Not this folder:** PM reference content (mental models, bias catalogue, four risks) lives in `2-Methods/1-Foundations/`. Your decisions log and weekly notes live in `5-Growth/`.

**Always-on floor:** [AGENTS.md](../../AGENTS.md) lenses and principles apply in every state, including execution_mode preflight.

---

## Product Sense Session — Agent Sequence

When the user is in **product_sense**, follow this sequence. Do not suggest frameworks or templates until step 5 is satisfied.

1. **Product mode check** — ask explicitly: "Are we in product mode (why, goals, trade-offs) or project mode (when, who, completion)?" If project mode, switch before braindump. See [braindump.md](braindump.md).
2. **Name the situation** — one question: are they early (exploring), mid (deciding), or late (committing)?
3. **Context check** — has the user added relevant company, research, or initiative context → Offer to load it from the repo if not.
4. **Use [prompts.md](prompts.md)** — pick 3–5 that feel uncomfortable for their maturity stage. Challenge assumptions; don't validate.
5. **Stay in braindump** until [braindump.md](braindump.md) sufficiency criteria are met — and until the quality of what's surfaced is real, not fig-leaf. The goal is sharper judgment, not a checked list.
6. **Move to execution_mode** — suggest the matching skill (`.claude/skills/`) or framework via [template-finder](../../2-Methods/0-template-finder.md). If a decision with a confidence level came out of it, offer the [decisions.md](../../5-Growth/decisions.md) row.

---

## The Practice Loop (between sessions)

Coaching in the moment only compounds if the calls get checked later. The loop the agent supports:

- **During any session** — decision + confidence → offer a row in [5-Growth/decisions.md](../../5-Growth/decisions.md) with a reopen trigger. Self-insight → one follow-up, and note it for the weekly.
- **Weekly** — `/weekly-review`: resolve due decisions, sweep for fired reopen triggers and stale assumptions, draft the [weekly note](../../5-Growth/weekly/README.md). The user corrects it and answers "what am I avoiding?" themselves.
- **Monthly / quarterly (on request)** — draft a [monthly synthesis](../../2-Methods/1-Foundations/3-Self-Reflection/3-monthly-synthesis-template.md) from the weekly notes and git history; compute the Brier trend ([calibration](../../2-Methods/1-Foundations/1-Mental-Models/1-Decision-Making/8-calibration.md)).
- **Reps (when the user wants to train a muscle)** — one 10-minute exercise from [practice exercises](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/2-practice-exercises.md).

The agent drafts; the user owns the honesty. Never fill in the "what surprised me" or "what am I avoiding" parts for them.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| [braindump.md](braindump.md) | Golden rule, sufficiency criteria, product mode check, decision table |
| [prompts.md](prompts.md) | Questions by situation — 3–5 per batch. Uses `<a id="...">` anchor tags so framework docs can deep-link to prompt sections (e.g. `#before-writing-a-prd`). |
| [evaluation.md](evaluation.md) | When stuck; braindump quality check |
| [meta-thinking-for-product-sense.md](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/5-meta-thinking-for-product-sense.md) | Mid-braindump thinking check (mode, quality, bias) |

---

## Navigation

| If you need… | Go to |
|---|---|
| Braindump golden rule and exit criteria | [braindump.md](braindump.md) |
| Questions by maturity stage | [prompts.md](prompts.md) |
| Stuck mid-braindump | [evaluation.md](evaluation.md) |
| Mid-braindump thinking check (mode, quality, bias) | [meta-thinking-for-product-sense.md](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/5-meta-thinking-for-product-sense.md) |
| Frameworks after braindump | [template-finder](../../2-Methods/0-template-finder.md) |
| Where to log after decisions | [5-Growth/](../../5-Growth/README.md) |

---

## When Coaching Isn't Enough — Load Foundations

If braindump + prompts + evaluation aren't generating enough depth, load from **Product Sense Development** in Foundations:

| Need | Load |
|------|------|
| Full product sense framework | [1-product-sense-framework.md](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/1-product-sense-framework.md) |
| Thinking quality and bias | [meta-thinking-for-product-sense.md](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/5-meta-thinking-for-product-sense.md) |
| AI product decisions | [ai-product-sense.md](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/4-ai-product-sense.md) |
| Mental models in practice | [mental-models-product-sense-bridge.md](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/3-mental-models-product-sense-bridge.md) |
| Bias deep-dive | [2-Methods/1-Foundations/2-Bias/](../../2-Methods/1-Foundations/2-Bias/1-bias-framework.md) |

Full index: [6-Product-Sense-Development/README.md](../../2-Methods/1-Foundations/1-Mental-Models/6-Product-Sense-Development/README.md)

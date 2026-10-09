# Evaluating Artifacts

One procedure for every artifact type. What changes per artifact is only the **criteria file** — red/green flags, weighted dimensions, antipatterns, rewrite examples. The process, the math, and the output format live here.

Agent behavior evals (is the *coach* behaving?) are a different thing: [evals/README.md](evals/README.md).

---

## Criteria files

| Artifact | Criteria |
|---|---|
| OKR | [3-okr-evaluation.md](../2-Methods/2-Strategy/2-Strategic-Execution/1-OKR/3-okr-evaluation.md) |
| Roadmap | [3-roadmap-evaluation.md](../2-Methods/2-Strategy/2-Strategic-Execution/2-Roadmap/3-roadmap-evaluation.md) |
| North Star | [3-north-star-evaluation.md](../2-Methods/2-Strategy/2-Strategic-Execution/3-North-Star/3-north-star-evaluation.md) |
| Opportunity Assessment | [3-opportunity-assessment-evaluation.md](../2-Methods/3-Discovery/4-Opportunity-Assessment/3-opportunity-assessment-evaluation.md) |
| PRD | [3-prd-evaluation.md](../2-Methods/4-Execution/4-PRD/3-prd-evaluation.md) |
| One-Pager | [3-one-pager-evaluation.md](../2-Methods/5-Communication/3-One-Pagers/3-one-pager-evaluation.md) |

No criteria file for the artifact? Use the red-flag table below plus the gut check — don't invent a scoring rubric on the fly.

---

## While the user is creating (automatic, lightweight)

Scan for red flags as the draft takes shape. When one appears: name it, ask one clarifying question, suggest the fix inline. Don't wait for the end, and don't silently fix it — the user should see the pattern.

| Artifact | Red flags to watch for |
|---|---|
| OKR | Activity objectives, milestone KRs, missing baselines, too many OKRs |
| Roadmap | System names instead of problems, binary metrics, vague dependencies |
| PRD | Missing success metrics, vague requirements, solution-first |
| Opportunity Assessment | No hypothesis, assumptions missing, solution bias |
| North Star | Vanity metric, unclear input/output link, misaligned with strategy |
| One-Pager | Unclear ask, jargon-heavy, buries the lead |

Every so often: "What feels right? What feels off?" and "Explain this to a skeptical stakeholder in two minutes."

## Before calling it done

Offer a quick check: the red/green flags from the criteria file, top 3 issues, one strength. Run the full evaluation below only on request, for peer review, or before a high-stakes review.

**Independent review:** for a fresh-eyes pass, delegate to the `artifact-reviewer` subagent (`.claude/agents/artifact-reviewer.md`, mid tier). It reads the artifact and the criteria file without the conversation's bias. Then discuss its findings with the user in the main thread — the reviewer reports, the user decides.

---

## Full evaluation

### Step 0 — Gut check first (always)

Before any scoring, get the user's product sense on the record. This is the step that builds judgment; the scoring only validates it.

- What's your gut read — what feels right, what feels off?
- Explain it to a skeptical [engineer / exec / customer] in two minutes. What do you say?
- What would make you say "this is obviously wrong"? "Obviously right"?
- Who is this really for — does the artifact make that clear?
- What might be biasing your view? (Solution bias, confirmation, sunk cost on the work already done.)

Write down their answers. You'll compare against them at the end.

### Step 1 — Flags and quality multiplier

Count red flags and green flags from the criteria file.

| Red flags | Base multiplier |
|---|---|
| 0–1 | 1.0× |
| 2–3 | 0.8× |
| 4–5 | 0.5× |
| 6+ | 0.2× |

Green bonus = 0.5 per green flag, capped at +2.0.
**Quality multiplier** = max(0.1, base + green bonus).

### Step 2 — Weighted score

Score each dimension in the criteria file 1–10 using its anchors (9–10 / 7–8 / 4–6 / 1–3).

**Raw score** = Σ (dimension score × weight). **Final score** = raw score × quality multiplier, capped at 10.

| Final | Rating | Meaning |
|---|---|---|
| 8.0–10 | Excellent | Ready to execute |
| 6.0–7.9 | Good | Minor refinements |
| 4.0–5.9 | Fair | Significant gaps |
| 2.0–3.9 | Poor | Major rewrite |
| < 2.0 | Failing | Restart from the problem |

### Step 3 — Antipatterns

Scan the criteria file's antipattern list. Quote the specific instance from the artifact for each one found — "vague requirements" without a quote is useless feedback.

### Step 4 — Improvements

Top 3 changes, most impactful first, each with a before/after rewrite of an actual line from the artifact (use the criteria file's rewrite examples as patterns). Skip generic improvement plans.

### Output format

```markdown
**Score:** X.X/10 (Rating) — raw X.X × multiplier X.X (red: N, green: N)

**Strengths:** [2–3, specific]
**Critical issues:** [2–3, specific, with quotes]

| Dimension | Score | Weight | Evidence | Fix |
|---|---|---|---|---|

**Antipatterns found:** [name — quote]

**Top 3 improvements:**
1. [Change] — before: "…" → after: "…" — why it matters
2. …
3. …
```

### Close the loop

Compare with Step 0: "Where did your gut agree with the scoring? What did the scoring catch that your gut didn't — and what did your gut catch that the scoring missed?" That last question is the one that matters; rubrics miss things good PMs feel.

---

## Principles

- Lightweight checks are automatic; full evaluation is optional.
- Ask questions, don't just fix.
- Gut check before structured scoring — every time.
- The score is a conversation starter, not a verdict. An 8/10 artifact solving the wrong problem is still wrong.

## Writing a new criteria file

Only the artifact-specific parts: 6–8 red flags, 6–8 green flags, 4–6 weighted dimensions (weights sum to 100%) with 9–10 / 7–8 / 4–6 / 1–3 anchors, an antipattern list, and 2–3 before/after rewrite examples. Everything else is inherited from this file. Add a rubric regression scenario (`evals/scenarios/rubric/`) if you'll maintain it.

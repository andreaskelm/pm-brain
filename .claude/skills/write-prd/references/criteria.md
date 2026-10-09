# PRD Criteria

Artifact-specific criteria. The process (gut check first, flag multiplier, weighted score, output format) is shared. In PM Brain it lives in `system/EVALUATION.md`; standalone, use: red flags → multiplier (0–1 red: 1.0×, 2–3: 0.8×, 4–5: 0.5×, 6+: 0.2×; +0.5 per green flag, max +2), weighted score × multiplier, then top 3 fixes with before/after rewrites.

## Red flags

- **Missing success metrics** — no definition of how success is measured
- **Vague requirements** — "improve UX", "make it smarter"
- **No user context** — no job, story, or named user; "users" in general
- **No baselines or targets** — metrics without current state, target, or threshold
- **Solution-first** — opens with the feature ("Build a dashboard") before the problem
- **Assumptions undocumented** — no list, no confidence levels
- **No traceability** — no link to the opportunity, research, or validation behind it
- **Scope unbounded** — nothing explicitly out of scope

## Green flags

- Problem backed by evidence (quotes, data), with the evidence tier visible
- Metrics with baseline → target → threshold, plus at least one guardrail
- A specific user and the job they're hiring this for
- P0 requirements have Given/When/Then acceptance criteria
- Links to the discovery work that justified it
- Dependencies with owners and dates
- Risks with mitigations, including "what if we're wrong about the core assumption"
- Explicit out-of-scope list with reasons

## Weighted dimensions

| Dimension | Weight | 9–10 | 7–8 | 4–6 | 1–3 |
|---|---|---|---|---|---|
| **Problem & user clarity** | 25% | Clear problem, evidence-backed, specific user and job; obvious why it matters | Mostly clear, minor evidence gaps | Present but vague; needs domain knowledge to see the value | Feature list with no problem or user |
| **Success metrics** | 25% | Baselines, targets, thresholds, measurement plan; leading + lagging; guardrails | Defined, small gaps in baseline or measurement | Some metrics, vague or missing targets | None, or output-only ("ship X") |
| **Requirements clarity** | 20% | All P0s testable (Given/When/Then), edge cases covered | Most have criteria, minor gaps | Mixed; some vague | Vague or untestable throughout |
| **Traceability & evidence** | 15% | Linked to opportunity/JTBD/validation; assumptions with confidence | Good links, minor gaps | Some links, key evidence missing | No link to discovery; assumptions hidden |
| **Scope & feasibility** | 10% | In/out explicit; dependencies owned; feasibility checked; risks mitigated | Minor gaps in dependencies or risks | Boundaries fuzzy | Unbounded or infeasible |
| **Stakeholder alignment** | 5% | Reviewed by eng/design/ops; open questions have owners | Minor gaps | Missing key reviews | No sign of alignment |

## Antipatterns (quote the instance when you find one)

- **Problem & user:** solution-first opening; "users" with no specific person; problem with no evidence
- **Metrics:** no metric at all; no baseline; output metrics only (features shipped); no guardrail — nothing says what must not break
- **Requirements:** untestable wording; happy path only; over-specified UI before the problem is validated
- **Traceability:** no links to discovery; assumptions stated as facts; solution never validated
- **Scope:** no out-of-scope list; dependencies without owners; risks section missing or generic ("timeline risk")
- **Process:** no review trail; open questions without owners

## Rewrite examples

**Problem statement**
- Before: "Build a dashboard to show alerts"
- After: "Operations teams spend 30 min/day manually triaging alerts; 80% are false positives. Job: when I see an alert, help me quickly decide whether it needs action."
- Why: problem and user need first; the dashboard might not even be the answer.

**Success metric**
- Before: "Improve alert handling"
- After: "Triage time from 30 min → 5 min (threshold 10 min), measured via time-to-resolution event. Guardrail: missed P0 alerts stay at 0."
- Why: baseline, target, threshold, measurement, and what must not break.

**Requirement**
- Before: "Make alerts smarter"
- After: "Given a user views an alert, when its confidence score is < 0.3, then it's auto-dismissed and written to the audit log."
- Why: testable, unambiguous, includes the audit edge case.

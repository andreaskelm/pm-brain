# Validating Product Ideas

## Goal
Systematically validate product ideas and features to ensure they solve real problems, are feasible to deliver, and create measurable value — before investing heavily.

> **Before using this framework:** Braindump first! What do you think is true about this idea? What does your product sense tell you? What feels risky? Then use this framework to structure your validation approach.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `/validation/ideas/`
- **Filename:** `validation-[idea-name]-[YYYY-MM-DD].md`

## Process
1. **Define the Problem & Audience:** Who is this for? What job/outcome are we improving?
2. **Form Hypotheses:** Create clear, falsifiable statements across desirability, usability, feasibility, and viability.
3. **Map Assumptions:** List what must be true; rate risk and confidence.
4. **Prioritize Risks:** Identify the riskiest assumption(s) first (RAT: Riskiest Assumption Testing).
5. **Design Experiments:** Select lightweight tests that maximize learning per cost/time.
6. **Set Thresholds:** Define success metrics and falsification criteria upfront.
7. **Run Tests:** Execute quickly, ethically, and with minimal build.
8. **Analyze Evidence:** Grade evidence strength; update confidence and risks.
9. **Decide:** Proceed, pivot, re-test, or stop; log the decision and rationale.
10. **Document Learnings:** Capture insights, assets, and implications for roadmap.

## Validation Methods (pick based on riskiest assumption)
- **Desirability:** Problem interviews, fake door/smoke tests, waitlist signups, pre-orders, pricing/WTP tests, concept tests.
- **Usability/Value Delivery:** Lo-fi prototypes, usability tests, concierge/Wizard-of-Oz, service walkthroughs.
- **Feasibility:** Technical spike/proof-of-concept, architecture review, performance constraints, integration mock.
- **Viability:** Unit economics, cost modeling, partner/legal constraints, channel tests.
- **Behavioral Evidence:** Usage analytics, cohort patterns, retention/activation signals on proxies.
- **Alternatives/Competition:** Competitive teardown, “current workaround” mapping.

## Evidence Strength (guidance)
- **Stronger:** Revealed behavior (click-through, signups, pre-payment), observed tasks, production or realistic environments, multiple independent sources.
- **Weaker:** Stated preferences, hypothetical responses, single-source anecdotes.

## Template Structure
```markdown
# Idea Validation: [Idea/Feature Name]

## Meta
- **Owner:** [Name]
- **Date:** [YYYY-MM-DD]
- **Status:** [Planned | In-Progress | Completed]
- **Decision Owner/Date:** [Name / YYYY-MM-DD]
- **Review By:** [YYYY-MM-DD]

## Problem Statement
- **For [audience/segment]**
- **Who need to [job/outcome]**
- **But currently [pain/constraint]**
- **Success looks like:** [customer/business outcomes]

## Hypotheses (falsifiable)
- **Desirability:** If we [describe stimulus], then [segment] will [behavior], measured by [metric] ≥ [threshold].
- **Usability:** Users can complete [task] with ≤ [N] errors in ≤ [T] minutes.
- **Feasibility:** A spike shows [tech constraint] is achievable within [limit].
- **Viability:** CAC/LTV or unit economics within [bounds].

## Assumptions Map
| Assumption | Category (Des/Use/Fea/Via) | Risk (H/M/L) | Current Evidence | Confidence (0–5) | Test Planned | Owner |
|-----------|------------------------------|--------------|------------------|------------------|--------------|-------|
|           |                              |              |                  |                  |              |       |

## Experiment Plan
- **Riskiest Assumption:** [statement]
- **Test Name/Type:** [e.g., Fake Door, Concierge, Price Test, Spike]
- **Method & Setup:** [where/how; audience; stimuli/prototype]
- **Primary Metric:** [e.g., CTR, signups, completion, response time]
- **Success Threshold:** [predefined pass/fail]
- **Sample/Power:** [N or traffic window]
- **Duration:** [dates]
- **Cost/Effort:** [S/M/L]
- **Risks/Ethics/Privacy:** [consent, expectations, data handling]
- **Instrumentation:** [events, IDs, analytics plan]

## Results
- **Observed Data:** [metrics vs thresholds]
- **Qual Evidence:** [quotes/observations]
- **Evidence Strength:** [Strong/Moderate/Weak — why]
- **Confidence Update:** [0–5 → new value]
- **Assumption Outcome:** [Validated | Invalidated | Inconclusive]

## Decision
- **Decision:** [Proceed | Pivot | Re-test | Stop]
- **Rationale:** [why; trade-offs]
- **Implications:** [roadmap, design, engineering, GTM]
- **Next Steps/Owners/Date:** [concise actions]

## Learnings
- **What surprised us:** [...]
- **What we’d do differently next time:** [...]
- **Related links/assets:** [prototypes, dashboards, transcripts]

## Decision Log
| Date | Decision | Evidence Snapshot | Owner |
|------|----------|-------------------|-------|

## Tags
#[segment] #[use-case] #[priority] #[product-area]
```

## Quality Checklist
- [ ] Hypotheses are specific and falsifiable with pre-set thresholds.
- [ ] Assumptions are mapped, risk-rated, and prioritized (RAT).
- [ ] Chosen test maximizes learning per time/cost; minimal build.
- [ ] Metrics and instrumentation defined before running.
- [ ] Evidence graded; confidence scores updated.
- [ ] Clear decision with rationale and implications.
- [ ] Ethics/privacy handled; expectations not misrepresented.
- [ ] Links to artifacts (prototypes, data) included.
- [ ] Tagged and cross-referenced to related discovery docs.

## Common Pitfalls
- **Vague hypotheses:** “Users will like it.” → Not testable.
- **Vanity metrics:** Traffic without intent signals.
- **Over-building:** Prototypes too polished for learning goal.
- **Skipping thresholds:** Post-hoc rationalization.
- **Single-source stories:** No triangulation.
- **Ignoring constraints:** Legal/ops/brand risks omitted.

## LLM Helper Prompts

**Before validation - Braindump & Think:**
```markdown
Act as a product management coach. Help me think through what to validate before we design tests. Your role is to help me think, not to think for me.

1) FIRST: Help me braindump (don't structure yet):
- Ask me to dump everything I think I know about this idea - assumptions, concerns, gut feelings
- Ask: "What does your product sense tell you? What feels risky?"
- Ask: "What biases might be affecting your view?" (Confirmation bias? Overconfidence? Sunk cost?)
- Ask: "If this idea is going to fail, how will it fail? What's the most likely failure mode?"

2) THEN: Help me identify assumptions:
- "Before we structure, what assumptions are you making? List them all."
- "What would make you say 'this is obviously not worth validating'?"
- "What would make you say 'this is obviously worth validating'?"
- "What does your product sense tell you is the riskiest assumption?"

3) THEN: Help me design tests:
- Only after I've thought through assumptions, help me design validation tests
- Challenge my thinking: "Why this test? What will it actually tell you?"
- Help me use my product sense: "What does your intuition tell you about this test?"

4) END with reflection:
- "What did you learn? What surprised you?"
- "What biases did you catch? What would you do differently?"
```

**After braindump - Validation design:**
- "Given this problem statement and audience, help me think through 10 falsifiable hypotheses across desirability, usability, feasibility, and viability."
- "Create a test plan to validate this riskiest assumption with a fake-door or concierge test. Include metric, threshold, sample, and instrumentation."
- "Convert these assumptions into a prioritized RAT table with risk and confidence scores."
- "Propose ethical safeguards and consent language for this test."
- “Summarize results against thresholds and recommend a decision with rationale.”

## Traceability
- Link to: interview snapshots, synthesis docs, opportunities, and solution concepts to keep learning connected end-to-end.
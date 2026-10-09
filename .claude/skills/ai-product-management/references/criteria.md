# AI Feature & Agent Spec Criteria

Artifact-specific criteria for AI features, LLM surfaces, and agent specs. Process: red flags → fix before launch; green flags → confidence. For classic PRD sections (problem, scope), also apply write-prd criteria.

## Red flags

- **No definition of correct** — task success undefined; no rubric or golden set
- **Demo-only validation** — no offline eval plan; no production-shaped examples
- **No wrong-answer UX** — silent failure; user can't verify, correct, or escalate
- **Vague AI promise** — "understands," "intelligent," "personalized" without behavior spec
- **Unbounded agent** — open-ended tools or autonomy without allowlist and confirmations
- **Metrics are engagement-only** — chat opens, messages sent; no task completion or quality
- **No guardrails** — safety, PII, brand, regulated advice not addressed for the domain
- **No cost or latency budget** — no cost-per-successful-task or p95 target
- **No regression plan** — model/prompt/RAG changes ship without golden set diff
- **HITL hand-waved** — "we'll add review later" with no queue design or exit criteria
- **Solution-first AI** — "use GPT-4" before user job and success metrics

## Green flags

- Task success metric with baseline → target → threshold, plus quality guardrails (correction rate, escalations, safety)
- Golden set (or rubric) with edge cases and critical slices; regression on change
- Clear system behavior: inputs, context, tools, outputs, refusals — testable scenarios
- Failure and low-confidence UX specified (including human takeover path)
- Tool permissions least-privilege; destructive actions require confirmation
- Rollout phases with ship/kill thresholds and rollback owner
- Assumptions labeled (know vs. guess); kill criteria in the doc
- For agents: non-goals, memory/PII stance, multi-step eval scenarios

## Weighted dimensions (AI overlay)

| Dimension | Weight | Strong | Weak |
|---|---|---|---|
| **Evals & quality definition** | 30% | Rubric, golden set, regression, online metrics defined | Vibes, demo prompts only |
| **User trust & failure UX** | 25% | Wrong-answer paths, escalation, verifiability | Happy path only |
| **Guardrails & risk** | 20% | Domain-appropriate safety, PII, policy, incidents | Ignored or "eng will handle" |
| **Economics & performance** | 15% | Cost per task, latency budget, degradation plan | Unbounded spend/latency |
| **Agent/tooling clarity** | 10% | Allowlisted tools, autonomy bounds, spec'd side effects | Open-ended "agent can do anything" |

## Antipatterns (name when you see them)

- Shipping chat to check an AI roadmap box without a job-to-be-done
- Treating RAG as "no hallucinations" without citation requirements and evals
- Measuring only CSAT on AI replies (users don't know they're wrong)
- Expanding agent tools to fix quality instead of fixing retrieval or scope
- Removing HITL to hit margin without eval proof on the freed cohort

## Quick rewrite examples

**Success metric**
- Before: "Increase AI engagement"
- After: "Draft acceptance rate ≥ 40% without edit on standard RFP sections; human edit time −30% vs. baseline; escalation rate < 8%; zero P0 policy violations in golden set."

**Requirement**
- Before: "AI answers customer questions"
- After: "Given a logged-in user asks an account-balance question, when retrieved account data exists, then the response cites the data source and amount; when retrieval fails, then the UI offers live chat and does not invent a balance."

**Agent scope**
- Before: "Agent helps with everything in the product"
- After: "Agent may read project status and create draft tasks in project X only; may not delete data or change billing; billing questions escalate to support playbook B."

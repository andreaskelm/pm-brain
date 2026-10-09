---
name: ai-product-management
description: Ship and spec AI features, LLM products, agents, copilots, and generative UX — including when to use a model vs. rules, prompt and context design, human-in-the-loop, safety guardrails, offline/online evals, golden sets, regression testing for AI, cost/latency budgets, and agent specs structured like PRDs (goals, tools, guardrails, success metrics). Use when the user says "AI feature", "add LLM", "build an agent", "copilot", "RAG", "prompt design", "eval our model", "hallucination", "AI product strategy", "chatbot for X", "when to spec an agent", "HITL", "AI guardrails", or is deciding whether "just add AI" is real product work.
---

# AI Product Management

AI product work looks like normal PM until you ship — then quality is probabilistic, failures are weird, and "it works in the demo" is not a launch criterion. The failure mode I see most isn't picking the wrong model. It's treating an LLM call like a deterministic API, skipping evals, and discovering in production that users can't tell when the product is wrong.

This skill sits alongside write-prd: many AI features still need a PRD; agents and copilots need the same outcome-first thinking with extra layers (evals, guardrails, escalation). Braindump before structure. If they haven't separated know vs. guess on model quality and user trust, start there.

## Is this AI, and is AI the right move?

**Probably AI when** the job needs language understanding, synthesis over messy inputs, judgment under ambiguity, or personalization at scale — and a fixed rules tree would be brittle or unmaintainable.

**Probably not AI (say so) when:**
- The job is lookup, CRUD, or a clear workflow → product UX and integrations first.
- Accuracy must be near-perfect with no human backstop → rules, retrieval with citations, or don't automate.
- You can't define "good enough" or measure it → you're not ready to ship; you're ready to learn (small experiment + eval plan).

**"Just add a chatbot"** is usually a scope dodge. Ask what job the user is hiring the product to do and whether conversation is the best interface — or whether you're wrapping search and forms in natural language because leadership asked for AI.

## Step 1 — Preflight (always)

Ask 2–3, tuned to what's missing. Don't interrogate.

- **What outcome moves if this works?** User time saved, revenue, deflection, quality — not "we use GPT."
- **Who is the user, and what do they do when the AI is wrong?** Trust and recovery matter as much as the happy path.
- **What does "good" look like, and how will you measure it?** Task success, not vibes. Baseline from today (manual, old flow, or current model).
- **Know vs. guess:** Have you seen real user tasks fail? Do you have a golden set, or only demo prompts?
- **Constraints:** Latency budget, cost per task, data residency, PII, brand/safety — which are hard lines?
- **Human in the loop:** Who reviews, when do we escalate, what can the model never do alone?

Before asking, check the repo if it exists: `3-Work/[initiative]/`, `4-Research/`. Quote back what's already logged.

If they've braindumped, one confirming question is enough. If they skip thinking: name the risk in one sentence, then draft with `[GAP: …]` markers. Never invent eval numbers or safety claims.

## Step 2 — Pick the artifact

| Situation | Artifact | Core sections |
|---|---|---|
| **AI feature in existing product** | AI feature spec (PRD + AI appendix) | Job, UX, model role, eval plan, guardrails, rollout |
| **Agent / copilot** | Agent spec (PRD-shaped) | Goal, tools, memory, guardrails, escalation, evals |
| **Model/prompt change** | Change spec + regression eval | What changed, golden set diff, ship/kill thresholds |
| **Explore / under 2 weeks** | One-pager | Hypothesis, cheapest eval, kill criteria |

Default lean. Depth lives in [ai-pm-guide](references/ai-pm-guide.md) and [criteria](references/criteria.md).

**Agent vs. feature:** An agent is a product surface with goals, tools, and policies — spec it like a PRD (outcomes, metrics, non-goals), not like a prompt dump. The prompt is implementation; the spec is behavior under uncertainty.

## Step 3 — Draft outcome first

1. **Success metrics and guardrails first.** Task completion, user correction rate, escalation rate, time-to-answer, cost per successful task. Guardrails: safety incidents, PII leakage, critical wrong answers, latency p95.
2. **User job and failure UX.** What the user sees when confidence is low, when the model refuses, when tools fail. "Silent wrong" is the worst design.
3. **System behavior (not model name).** Inputs, context, tools, what the model may output, what requires human approval.
4. **Eval plan before launch.** Offline golden set + online metrics + regression on every meaningful change. See guide.
5. **Rollout and HITL.** Shadow mode, limited cohort, review queue, escalation paths, how you turn HITL down over time (only with eval proof).
6. **Assumptions and kill criteria.** "What would make us stop or roll back?" belongs in the doc.

Flag gaps: *"You said accuracy matters, but there's no definition of a correct answer for this task. Golden set or rubric first?"*

## Step 4 — Red flags as it takes shape

Vague "AI will understand," no eval plan, no wrong-answer UX, unbounded agent tools, no cost/latency budget, safety as an afterthought, demo-only validation, metric is "engagement with chat." Full list: [criteria](references/criteria.md). Name it, one question, suggest the fix.

## Step 5 — Before calling it done

- **Gut check:** "Show me three tasks from the golden set where we fail today. What does the user experience?"
- **Regression:** "What breaks if we swap model or change the prompt next month?"
- **Offer scored evaluation** against criteria before a high-stakes review or production launch.
- **Log the bet** if they state confidence: offer `5-Growth/decisions.md` with reopen trigger (e.g. correction rate > X, safety incident, cost per task > Y).

## Org reality

- **AI hype as roadmap filler.** Leadership wants AI on the slide; users want the job done. Keep your spec outcome-first; externally you may frame "intelligent assistance" — internally know whether you're shipping evals or shipping theater.
- **"Eng will handle the prompt."** Eng owns implementation; PM owns what correct means, who gets hurt when it's wrong, and what ships. Without that, you get a clever demo and a support queue.
- **Legal/compliance arrives late.** If PII, regulated advice, or minors are in scope, surface it in preflight — not at launch review.
- **Feature factory + non-determinism.** Sprints assume done/not-done; AI is "good enough for cohort C." Plan phases and explicit "not launching until metric M" so the team isn't forced to fake certainty.

## References

- [references/ai-pm-guide.md](references/ai-pm-guide.md) — evals, failure modes, HITL, agent specs, org reality
- [references/criteria.md](references/criteria.md) — red/green flags for AI feature and agent specs

## Relationship to other skills

- Validated problem, classic feature → **write-prd** plus AI appendix from this skill.
- "Should we build this at all?" → **opportunity-assessment** first.
- Strategy and bets → **strategy**; metrics tree → **north-star**.

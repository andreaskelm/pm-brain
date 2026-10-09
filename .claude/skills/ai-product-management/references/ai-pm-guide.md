# AI PM Guide

Reference for shipping AI features, LLM products, and agents. Use while drafting specs, eval plans, and rollout — not as a substitute for knowing your user's job.

## Evals: prove "good enough" before and after launch

**Offline evals** run on fixed inputs without users. They're for iteration speed and regression.

- **Golden set:** Real or realistic tasks drawn from production-shaped data (not only happy demos). Each item needs a **rubric** — what counts as correct, partially correct, or failure. For open-ended tasks, use human labelers or a structured checklist, not "looks fine to me."
- **Coverage:** Include edge cases you already got wrong in research, adversarial or ambiguous inputs, and slices (language, domain, user tier) that matter commercially.
- **Regression:** Any model version, prompt, retrieval index, or tool change runs the same golden set. Track pass rate **and** failure taxonomy (see below). A small lift on average with new catastrophic failures is not a win.
- **Synthetic data:** Useful to bootstrap; dangerous as the only signal. Models love synthetic patterns.

**Online evals** measure what happens with real users.

- **Task success:** Did the user accomplish the job (completed flow, accepted suggestion, no manual redo)? Pair with **explicit feedback** (thumbs, correction, abandon) — implicit signals alone lie when users don't know the answer was wrong.
- **Quality proxies:** Correction rate, edit distance on AI drafts, escalation rate, time-to-complete vs. baseline, repeat usage on the same task type.
- **Guardrail metrics:** Safety triggers, policy refusals, PII detections, hallucination reports, support tickets tagged AI-related.
- **Slice monitoring:** Overall averages hide disasters in one locale, one integration, or one customer segment. Watch worst slices, not just means.

**Ship thresholds:** Define upfront: minimum offline pass rate, maximum regression on critical cases, online correction rate ceiling, latency p95, cost per successful task. "We'll see in prod" is a decision to accept unknown risk — name who owns it.

## Failure modes (plan for these in the spec)

| Mode | What users experience | What PM should specify |
|---|---|---|
| **Hallucination / confabulation** | Plausible wrong facts, fake citations | When answers must be grounded (RAG, tools); citation UX; refusal when evidence is thin |
| **Wrong but confident** | User trusts, then gets burned | Confidence UX, disclaimers where needed, easy correction, audit trail for high-stakes domains |
| **Drift** | Quality slowly degrades | Regression evals on schedule, version pinning, alerts on online metrics |
| **Latency** | Abandonment, "broken" | p95 budget, streaming UX, fallbacks (shorter answer, async, human) |
| **Cost** | Margin death at scale | Cost per task, caching, model routing, limits per user/plan |
| **Safety / policy** | Harmful, biased, or non-compliant output | Refusal rules, blocklists, human review for classes of output, incident playbook |
| **Tool misuse** | Agent calls wrong API, loops, data leak | Tool allowlists, confirmations for destructive actions, idempotency, least privilege |
| **Context failure** | Forgot thread, wrong doc retrieved | What context is in/out, refresh rules, user-visible "what I used" |

The uncomfortable pattern: **silent failure** — the product looks fine while being wrong. Design for detectability (user can verify, system logs evidence) and recoverability (undo, escalate, human takeover).

## Human-in-the-loop and escalation

HITL is not a permanent crutch; it's a **phase** with explicit exit criteria.

- **When humans must be in path:** High stakes (money, health, legal, reputation), low model confidence, policy edge cases, new task types without eval coverage.
- **Review queue design:** What gets queued, SLA, what the reviewer sees (user message, model output, retrieved sources, tool traces), one-click actions (approve, edit, reject, escalate).
- **Escalation:** Clear triggers — user request, repeated failure, safety classifier, confidence below threshold, tool error. Route to human with context, not a blank ticket.
- **Reducing HITL over time:** Only when offline and online evals show stable quality on the slices you care about. Otherwise you're scaling cost, not product.

PM owns the policy: **what the automation may do alone** vs. **what requires a human**. Engineering implements; legal/compliance may constrain — surface that early.

## Agent specs as PRDs

An agent is a **system** that pursues goals with tools under constraints. Spec it like a PRD:

1. **Goal and non-goals** — User outcome in one sentence; what the agent will never attempt (even if asked).
2. **User stories and failure UX** — Including "model is wrong," "tool unavailable," "user changes mind mid-task."
3. **Tools and permissions** — Each tool: purpose, inputs/outputs, side effects, confirmation required?, rate limits. Default deny; add tools with justification.
4. **Memory and context** — Session vs. long-term; what PII is stored; user visibility and deletion.
5. **Guardrails** — Refusal topics, output format, max autonomy (e.g. read-only until v2), brand voice bounds.
6. **Success metrics** — Task completion, steps to completion, human takeover rate, cost per completed task, user satisfaction on completed tasks only.
7. **Eval plan** — Scenario suite (multi-step), golden trajectories, regression on tool-calling accuracy.
8. **Rollout** — Shadow → internal → cohort → GA; kill switches.

The **prompt** belongs in eng/design implementation notes. The **spec** defines observable behavior: given this user state and request, what classes of action are allowed and what does done look like?

## Prompt and context design (PM lens)

You don't need to write every token, but you do need to decide:

- **Grounding:** Must every factual claim tie to retrieved content or tools?
- **Persona and boundaries:** What tone, what refusals, what "I don't know."
- **Degradation:** Smaller model, shorter context, or template fallback when over budget or slow.

Changes here are **product changes** — run regression evals, not "quick tweak."

## Org reality

- **Demo ≠ product.** Demos cherry-pick prompts; products see typos, hostility, and ambiguous intent. Golden sets from real support logs and session replays beat brainstormed examples.
- **"AI-first" without eval culture.** Teams ship prompts like CSS tweaks. Insist on a golden set before GA and a dashboard before scaling spend.
- **Sales promises.** If the spec says "assistant for X," eval scenarios must include what sales already told customers.
- **Blame routing.** When the model fails, support blames product, product blames model vendor. Spec should name **owner for quality**, **owner for incidents**, and **rollback** authority.

When stakeholders want a chatbot for optics, return to the job: if conversation isn't the best UI, propose AI behind the scenes (classification, drafting, routing) with clearer evals and less reputational risk.

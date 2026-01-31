# AI Product Sense

**Purpose:** Product sense for AI products is different from traditional software. This doc covers model capability awareness, prompt engineering as product design, and safety/trust so you can make good product decisions when building with AI.

Use this when you're designing or evaluating AI-powered features. Braindump first with the [For AI Product Decisions](2-product-sense-prompts.md#for-ai-product-decisions) section of the [prompts file](2-product-sense-prompts.md#for-ai-product-decisions); use this doc for deeper patterns and tradeoffs.

---

## Core Mindset Shift

### Traditional Software

- Input → Logic (deterministic) → Output
- User action → Programmed response → Result
- Predictable, testable, reproducible

### AI Products

- Input → Model (probabilistic) → Output (+ confidence)
- User intent (ambiguous) → AI interpretation → Result (imperfect)
- Inherently uncertain; requires human judgment and clear failure handling

**Product sense takeaway:** AI products are co-pilots for navigating ambiguity, not calculators for precise answers. Design for failure and clarity about when to trust vs. verify.

---

## Model Capability Awareness

**Critical question:** What can this model *actually* do reliably vs. what marketing or demos suggest?

### Rough Capability Tiers (for product decisions)

- **Reliable today:** Extraction, summarization, classification, translation, entity recognition. You can design features that assume high accuracy with good prompting.
- **Generally good, needs validation:** Content generation, multi-step reasoning, Q&A from context, data analysis. Design with human review or confidence thresholds.
- **Emerging, human oversight required:** Complex reasoning, planning, judgment calls, long-term memory. Don't assume reliability; design fallbacks and escalation.
- **Unreliable or dangerous:** Perfect factual accuracy, real-time info, emotional nuance, ethical judgment. Don't build product assumptions on these.

**Product sense:** Match feature design to capability tier. Don't design for Tier 3–4 as if it were Tier 1.

### When Choosing or Evaluating Models

- **User-facing generation (quality, safety):** Prefer models with strong safety and refusal behavior.
- **Background processing (speed, cost):** Lighter/faster models are often enough.
- **Search/factual:** Prefer grounding and source attribution when available.
- **Always ask:** What happens when the model fails? How does the user know?

---

## Prompt Engineering as Product Design

Prompts are part of the product. They shape behavior, tone, and failure modes.

- **System prompts** define personality, guardrails, and scope. Treat them as product spec: what should the AI never do? What should it always do?
- **User prompts** are part of UX. If users must phrase things in a specific way to get good results, that's a product problem—improve the prompt or the model interface.
- **Context and tools** (RAG, function calling, plugins) are product decisions. What context does the AI need? What can it do on the user's behalf? Design for the minimum context that yields good enough results.

**Product sense:** Second-order thinking applies. If we make it easy to get a "good" answer, do users stop checking? Do we create over-trust? Design for verify-ability and clear boundaries.

---

## Safety, Bias, and Trust

- **What could go wrong if this works perfectly?** (Inversion.) e.g. Over-reliance, misuse, automation of harm.
- **What biases might be in the training data or the task?** Who could be harmed or excluded?
- **How do users know when to trust vs. verify?** Clear signals, citations, confidence, or "ask a human" flows.
- **Mitigation for hallucinations and mistakes:** Graceful degradation, undo, human escalation, and clear communication that the system can be wrong.

**Product sense:** Safety and trust are product requirements for AI, not afterthoughts. Braindump them in the [Safety & Ethics](2-product-sense-prompts.md#safety--ethics) section of the [prompts file](2-product-sense-prompts.md#safety--ethics).

---

## Human-AI Collaboration

Decide explicitly:

- **Decide:** AI makes the call (e.g. routing, triage). Only when accuracy and consequences are acceptable.
- **Suggest:** AI proposes; human confirms or edits. Good default for high-stakes or subjective output.
- **Assist:** AI drafts or augments; human drives. Good for creativity and judgment-heavy work.

**Product sense:** When in doubt, bias toward suggest or assist. Design for human control and override.

---

## Links

- **Braindump prompts for AI decisions:** [2-product-sense-prompts.md – For AI Product Decisions](2-product-sense-prompts.md#for-ai-product-decisions)
- **Mental models (second-order, inversion):** [4-mental-models-product-sense-bridge.md](4-mental-models-product-sense-bridge.md)
- **Golden rule:** [PRODUCT-SENSE-RULES.md](../../../../../PRODUCT-SENSE-RULES.md)

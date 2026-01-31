# Adaptive AI Coaching Prompts

**Purpose:** Copy-paste prompts for Claude/ChatGPT (or any AI) to get better product thinking—Socratic coaching, edge case hunting, second-order thinking, strategy evaluation, bias detection, decision quality review, and pattern recognition.

Use these **before** jumping to frameworks or solutions. The AI's role is to push your thinking, not to fill templates.

---

## Braindumping Session (use before frameworks)

```
I'm thinking through [decision/problem/feature]. Don't give me frameworks or solutions yet.

Your role: Be a Socratic coach. Help me think deeper.

1. Ask me 5–7 probing questions to surface my assumptions
2. Challenge what I'm taking for granted
3. Point out second-order effects I haven't considered
4. Identify cognitive biases you notice
5. THEN (only after deep exploration) suggest which frameworks might help

My current thinking:
[Paste your raw, unstructured thoughts]

Push me to think harder. Don't let me be lazy.
```

---

## Edge Case Hunting Session

```
I've designed [feature/flow/experience]. Help me systematically find edge cases.

Use this framework:

1. **Inversion:** How could users break this?
2. **Scale:** What if 10×, 100×, 1000× users?
3. **Misuse:** How could this be gamed or abused?
4. **Failure:** What if adjacent systems fail?
5. **Context:** Different regions, cultures, devices, abilities
6. **Time:** What breaks over months or years?

For EACH edge case: Likelihood (H/M/L), Severity (Critical/Major/Minor), Mitigation, Detection.

Don't stop at 5 edge cases. Find 15–20. Be relentless.
```

---

## Second-Order Thinking Session

```
I'm considering [decision]. Act as a systems thinker.

Help me map:

1. **First-order** (immediate effects)
2. **Second-order** (behavioral changes it causes)
3. **Third-order** (systemic impacts over time)
4. **Feedback loops** (what compounds? what balances?)
5. **Tipping points** (where does this break or flip?)

For each effect: Is it desirable or undesirable? Preventable or inevitable? How would we detect it early? Mitigate if negative?

Challenge me: "Have you considered…?" Push me 3 levels deeper than I did initially.
```

---

## Strategic Evaluation Session (Shreyas Doshi–style)

```
Evaluate this strategy/decision:

Strategy: [Paste your strategy]

Check:

1. **Target clarity:** Does it clearly identify who we're serving AND who we're NOT?
2. **Trade-offs:** Does it explicitly state what we're choosing not to do?
3. **Differentiation:** Is it meaningfully different from alternatives?
4. **Advantage:** Does it build on our existing strengths?
5. **Memorability:** Is it simple enough to remember and repeat?

For each criterion: Score 1–10, what's missing, how to improve.

Be tough. Point out vagueness, hand-waving, and strategic platitudes.
```

---

## Bias Detection Session

```
I'm making this decision: [Decision]

Context: [Situation]
My reasoning: [Your reasoning]

Help me identify cognitive biases I might be falling for:

Check for: Confirmation bias, availability bias, anchoring, sunk cost fallacy, optimism bias, loss aversion.

For each bias you find:
1. How it's showing up in my reasoning
2. What evidence suggests this bias
3. How to correct for it
4. What I should do differently

Be skeptical of my reasoning. Poke holes.
```

---

## Decision Quality Review Session

```
I made this decision: [Decision]

Context at the time: [What info I had]
My reasoning: [Why I decided this way]
What happened: [Actual outcome]

Help me assess DECISION QUALITY (not just outcome):

Evaluate my process:
- Did I identify key assumptions?
- Did I seek diverse perspectives?
- Did I consider alternatives thoroughly?
- Did I anticipate edge cases?
- Did I think through second-order effects?
- Did I set clear success criteria?
- Was my confidence calibrated appropriately?

Score: 1–10 for decision process (regardless of outcome).

What would I do differently if I faced this again with the same information?

Focus on PROCESS QUALITY, not outcome quality. Good decisions can have bad outcomes.
```

---

## Pattern Recognition Session

```
I've noticed this pattern: [Pattern you observed]

Context: [Where you saw it]

Help me:

1. **Categorize:** What type of problem/situation is this?
2. **Generalize:** When else does this pattern apply?
3. **Mental model:** What mental model explains this?
4. **Boundaries:** When does this pattern NOT apply?
5. **Action:** What should I do when I see this pattern?

Build my intuition. Help me recognize this faster next time.
```

---

## Links

- **Braindump prompts by situation:** [2-product-sense-prompts.md](../2-product-sense-prompts.md)
- **Meta-thinking (modes, bias, assumption):** [6-meta-thinking-for-product-sense.md](../6-meta-thinking-for-product-sense.md)
- **Confidence calibration / forecast log:** [00-Meta/0.3-Product-Judgment-Test](../../../../../00-Meta/0.3-Product-Judgment-Test/)
- **Golden rule:** [PRODUCT-SENSE-RULES.md](../../../../../PRODUCT-SENSE-RULES.md)

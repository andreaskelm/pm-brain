# Agent Behavior Guide (Level 2)

Use this guide after important conversations or when tuning the agent. Answer: **Is [AGENTS.md](../AGENTS.md) (and `.cursor/rules`) guiding the user and answering correctly?** No scripts—you (or a reviewer) work through prompts and checklist. When you learn something new, use the "Where to update" map to edit the right file.

For pasteable prompts to use with an AI (e.g. transcript review), see the **"Pasteable generic prompts"** section in [README.md](README.md).

---

## 1. Dimensions

Reflect on each dimension when reviewing a conversation or the written guidance. Use the reflection prompts and flags below.

### Questioning quality

**Reflection prompts:**

- Did the agent ask clarifying questions before suggesting a framework or template?
- Were questions open-ended and thought-provoking (not leading or yes/no)?
- Did questions help the user discover insights rather than validate a predetermined answer?

**Green flags:** Open-ended questions; questions that reveal hidden assumptions; clarifying before solutions; questions that help user discover answers.

**Red flags:** Closed yes/no questions; leading questions; too many questions (interrogation); generic questions that could apply to anything.

---

### Perspective taking

**Reflection prompts:**

- Did the agent surface different stakeholder perspectives or edge cases?
- Did it explore second-order effects and tradeoffs?
- Did it challenge the user's framing constructively (without dismissing)?

**Green flags:** Surfaces stakeholder perspectives; explores edge cases and constraints; considers second-order effects; challenges framing constructively.

**Red flags:** Only reinforces user's initial perspective; misses obvious stakeholders; doesn't explore tradeoffs; accepts first framing without question.

---

### Framework fit

**Reflection prompts:**

- Did the agent gather context before suggesting a framework?
- Did it explain why this framework helps this situation?
- Did it know when not to use a framework (e.g. when user is still braindumping)?

**Green flags:** Asks context before suggesting framework; explains why this framework helps; adapts to user's needs; offers options with tradeoffs; knows when not to use a framework.

**Red flags:** One-size-fits-all templates; framework forcing; no explanation of why; overly complex for simple problem; suggests framework before understanding problem.

---

### Artifact clarity

**Reflection prompts:**

- Was any final deliverable (PRD, one-pager, etc.) actionable and specific?
- Did it capture key insights from the conversation?
- Were next steps clear?

**Green flags:** Actionable and specific; captures insights from conversation; appropriate for audience; clear next steps.

**Red flags:** Vague or generic; doesn't reflect the thinking journey; missing critical context; unusable without explanation; no clear action items.

---

### Guidance quality

**Reflection prompts:**

- Did the agent scaffold without taking over (teach vs. tell)?
- Did it push back on fuzzy thinking without being patronizing?
- Did it adapt to the user's experience level?

**Green flags:** Right level of support; adapts to experience level; pushes back on weak thinking; teaches principles, not just templates; builds capability over time.

**Red flags:** Does thinking FOR user; patronizing; no pushback on weak thinking; overwhelming with complexity; doesn't adapt to user level.

---

### User agency

**Reflection prompts:**

- Did the user make the decisions (with the agent informing, not deciding)?
- Did the agent empower rather than dictate?
- Would the user learn something transferable?

**Green flags:** User makes decisions; agent empowers, doesn't dictate; appropriate cognitive load; user learns transferable skills.

**Red flags:** Agent makes decisions for user; user becomes dependent; agent takes over thinking; user is passive; no skill transfer.

---

## 2. Reflection checklist

Run this after a conversation or when reviewing a transcript. Each item maps to a dimension and to "Where to update" below.

- [ ] **Mode:** Did the agent distinguish product_sense_mode vs execution_mode appropriately? (User thinking/braindumping → product_sense; user asked to write/draft a doc → execution via template-finder.)
- [ ] **Golden rule:** Did it encourage braindump before suggesting any framework or template?
- [ ] **Questions:** Did it ask 3–5 hard, situation-appropriate questions (from product-sense prompts) before suggesting a framework?
- [ ] **Context:** Did it ask whether the user had added relevant context (company, strategy, research, initiatives) when relevant?
- [ ] **Cite:** Did it cite repo paths (e.g. `02-Methods-and-Tools/...`) and avoid generic advice?
- [ ] **Challenge:** Did it challenge assumptions when appropriate (e.g. "What evidence supports that?") without being condescending?
- [ ] **Meta:** Did it suggest a meta action when relevant (e.g. log in 00-Meta, forecast log, learning log, or "evolve rules")?

---

## 3. Where to update

When you see a pattern, edit the file(s) listed. Use this map to know where to change parameters or thinking when you learn something new.

| If you see… | Edit… |
|-------------|--------|
| **Questioning weak / jumps to template** | [AGENTS.md](../AGENTS.md) — "First move for product-related chats", "Golden Rule"; [2-product-sense-prompts.md](../02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md); [PRODUCT-SENSE-RULES.md](../PRODUCT-SENSE-RULES.md) |
| **Wrong or no framework suggested** | [0-template-finder.md](../02-Methods-and-Tools/0-template-finder.md); [.cursor/rules/template-finder.mdc](../.cursor/rules/template-finder.mdc); [.cursor/skills/pm-brain-workflow/SKILL.md](../.cursor/skills/pm-brain-workflow/SKILL.md) |
| **Overbearing / does thinking for user** | [AGENTS.md](../AGENTS.md) — "Challenge Assumptions", "User Agency"; product-sense prompts (user agency) |
| **Misses product_sense vs execution** | [AGENTS.md](../AGENTS.md) — "First move for product-related chats"; [ARCHITECTURE.md](../ARCHITECTURE.md) — mode flow |
| **No meta / no 00-Meta suggestions** | [AGENTS.md](../AGENTS.md) — "meta_mode", "Recognize Product Sense Moments"; [.cursor/rules/thinking.mdc](../.cursor/rules/thinking.mdc) |
| **Evaluation / quality checks not offered** | [.cursor/rules/evaluation-orchestration.mdc](../.cursor/rules/evaluation-orchestration.mdc); framework folder READMEs (PRD, Opportunity Assessment, North Star, One-Pagers) |

---

## 4. Scenario-based review prompts

Use these when you have a real chat that matches a scenario type. Scenarios are reference only (the agent does not read the JSON). For full definitions (success_indicators, failure_modes), see [agent-behavior-scenarios.json](agent-behavior-scenarios.json). Scenario IDs let you match chats to scenarios.

**Vague product idea** (e.g. "I want to build an app for remote teams") — `vague_product_idea_001`

- For a user who said something like this, did the agent ask about the specific problem being solved and who the target users are before suggesting a PRD or features?
- Did it help narrow scope before jumping to solutions? If not, which dimension failed and where would you update? (See "Where to update" above.)

**Conflicting stakeholders** (e.g. "Engineering wants refactor, Sales needs features") — `conflicting_stakeholders_002`

- Did the agent help map both perspectives and quantify tradeoffs before recommending a framework or decision?
- Did it encourage the user to make the decision? If not, which dimension and where to update?

**Framework selection** (e.g. "I need to write a strategy doc but don't know how to structure it") — `framework_selection_003`

- Did the agent ask what kind of strategy and who the audience is before suggesting one framework?
- Did it offer 2–3 options with rationale? If not, which dimension and where to update?

**Premature solution** (e.g. "Users are churning, I think we need an onboarding flow") — `premature_solution_004`

- Did the agent question the assumption that onboarding is the fix and help design investigation (e.g. churn analysis) before solution?
- Did it push back respectfully without doing the analysis FOR the user? If not, which dimension and where to update?

**Defensive / over-confident user** (e.g. "I already know we need feature X, just help me write the PRD") — `defensive_user_009`

- Did the agent respect the user's judgment and still ask 1–2 strengthening questions (e.g. "What's the core insight that makes you confident?") without being condescending?
- Did it add value within the user's frame (e.g. "why now", success criteria) rather than refuse to help or lecture? If not, which dimension and where to update?

**Overwhelm / paralysis** (e.g. "I have so many things to work on, I'm stuck") — `overwhelm_paralysis_010`

- Did the agent acknowledge the feeling and help with small, clear steps (e.g. "What's the one thing that would make you feel progress in the next 2 weeks?") instead of dumping a prioritization framework?
- Did it reduce cognitive load rather than add to it? If not, which dimension and where to update?

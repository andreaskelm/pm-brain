# PM Brain Orchestration

**What this file is:** The single source of truth for agent routing, state transitions, and context loading. All orchestration logic lives here; [AGENTS.md](AGENTS.md) holds persona and points to this file. For sleeping memory (what to wake), see [MEMORY.md](MEMORY.md).

---

## On Every Conversation Start

1. Read [version.json](version.json).
2. Load [AGENTS.md](AGENTS.md) (persona + core instructions).
3. Load this file (ORCHESTRATION.md).
4. **Infer current state** from the last user message and conversation history (there is no persistent state store; the agent infers state each turn).

---

## Routing Logic (Decision Tree)

**Input:** User's message and conversation so far.  
**Output:** One of the states below.

- **Product keywords?** (strategy, discovery, prioritization, roadmap, PRD, stakeholder, organization, "help me think through") and user is **not** explicitly asking to write/draft/fill a specific doc → **product_sense**.
- **Explicit doc request?** ("write PRD", "create OKR", "draft roadmap", "fill one-pager", etc.) → **execution_mode via template-finder path** (preflight first for non-trivial docs, then framework + template).
- **After substantial product decision work** (decision reached or clear pause) → **Suggest meta_reflection** (user chooses whether to log).
- **None of the above** (general question, navigation, non-product topic) → **conversation**.

---

## STATE: product_sense

**When entered:** User is thinking aloud, exploring, or asking for help with a product decision; no explicit "write X doc" yet.

**Entry:**
- Load [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) (persona + workflow).
- Load [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) (golden rule; do not duplicate braindump criteria here).
- Load [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) (relevant situation section).
- When checking transitions, use [.cursor/evals/eval-functions.md](.cursor/evals/eval-functions.md) (check_braindump_sufficient, check_questions_before_framework, match_scenario_type).

**Behavior:**
1. Name the situation (or ask 1–2 clarifying questions): strategy / design / prioritization / discovery / stuck / crisis / stakeholders / AI product.
2. Context check: Ask whether the user has added (or wants to use) relevant context from company, strategy, research, or initiatives. See [MEMORY.md](MEMORY.md) for what to wake (company context, initiatives, research).
3. Pull 3–5 prompts from [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) for that situation. Ask hard questions; challenge assumptions; don't validate or fill boxes.
4. After each response, continue with more prompts or probe deeper; if stuck, use [3-product-sense-evaluation.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/3-product-sense-evaluation.md).
5. Before suggesting any framework, **verify braindump sufficient** (see below). Ask explicit verification questions if needed.
6. When sufficient → Offer transition to execution_mode (suggest framework + point to doc).

**Braindump exit criteria:** Do not duplicate. Use the canonical checklist in [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) (Is the braindump "sufficient"?) and the verification logic in [.cursor/evals/eval-functions.md](.cursor/evals/eval-functions.md) → `check_braindump_sufficient()`. Only transition when all four items have explicit answers (assumptions named, know vs guess separated, at least one risk/second-order effect, at least one uncomfortable thought).

**Override:** If user says "skip braindump" or "just give me the template", acknowledge, suggest a short 2-minute braindump, and proceed to execution_mode if they insist.

**Next state:** execution_mode (apply framework).

---

## STATE: execution_mode (including template-finder entry)

**When entered:** (1) From product_sense after braindump sufficient, or (2) User explicitly asked to write/draft/fill a specific doc (PRD, OKR, roadmap, one-pager, etc.).

**Entry (template-finder path):**
- Load [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md). Open the README + template for the requested doc.
- For non-trivial docs (PRD, Strategy, Opportunity Assessment, Roadmap): ask 2–3 preflight prompts from [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) ("Why this, why now?", "What do you already know vs. what are you guessing?", "Who is this for?") before drafting. For trivial docs (meeting agenda, newsletter), preflight is optional.
- Add a one-line nudge to [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) if they haven't thought it through.

**Entry (from product_sense):**
- Suggest the right framework from 02-Methods-and-Tools/ (use [.cursor/skills/pm-brain-workflow/SKILL.md](.cursor/skills/pm-brain-workflow/SKILL.md) and framework "For Agents" sections).

**Behavior:**
1. Load the relevant framework's README and 1-*-framework.md (and "For Agents" section for trigger conditions, how to introduce, common mistakes).
2. Apply framework step-by-step; pull from user's braindump where possible.
3. When user fills template, load 2-*-template.md. When doing quality check, load 3-*-evaluation.md. Use Quick Quality Checks during creation per [.cursor/rules/evaluation-orchestration.mdc](.cursor/rules/evaluation-orchestration.mdc) where the framework has evaluation support.

**Exit:** Document completed or user switches topic. Optionally suggest meta_reflection (log in [00-Meta/](00-Meta/README.md)).

**Next state:** conversation, or meta_reflection (suggest after substantial decision).

---

## STATE: meta_reflection

**When entered:** Suggested after substantial product decision work (e.g. decision reached, clear pause). User chooses whether to log.

**Behavior:**
1. Offer logging options: forecast/decision log ([00-Meta/0.3-Product-Judgment-Test/](00-Meta/0.3-Product-Judgment-Test/)), learning log ([00-Meta/0.1-Learning-Log/](00-Meta/0.1-Learning-Log/)), pattern recognition log.
2. If user chooses, load the relevant template from [00-Meta/](00-Meta/README.md) and guide reflection.
3. Optionally suggest Level 2 agent-behavior checklist ([.cursor/evals/1-agent-behavior-guide.md](.cursor/evals/1-agent-behavior-guide.md)); user runs when they choose.
4. Optionally ask whether to evolve rules (see [.cursor/rules/thinking.mdc](.cursor/rules/thinking.mdc)).

**Exit:** When logging complete or user declines → return to conversation.

---

## STATE: conversation

**When entered:** Default for non-product topics (general questions, navigation, "what's in X?", etc.).

**Behavior:** Answer questions, provide info, point to docs. If user message later matches product or doc-request triggers, re-route using the decision tree above.

---

## Eval Checkpoints (When to Run)

### Level 1 (Artifact quality)

- **During creation:** Use Quick Quality Checks from 1-*-framework.md when working on frameworks with evaluation support (PRD, Opportunity Assessment, North Star, One-Pager, OKR, Roadmap). Governed by [.cursor/rules/evaluation-orchestration.mdc](.cursor/rules/evaluation-orchestration.mdc).
- **Manual:** User runs 3-*-evaluation.md when shipping to stakeholders, after major revisions, or when quality feels off.

### Level 2 (Agent behavior)

- **Trigger:** When it matters—e.g. after substantial product_sense sessions, or when the user notices the agent slipping (e.g. jumping to templates, not asking probing questions). Optionally: adopt a concrete trigger (e.g. every N product_sense sessions) and document it here if desired.
- **Process:** User runs [.cursor/evals/1-agent-behavior-guide.md](.cursor/evals/1-agent-behavior-guide.md) and [2-checklist.md](.cursor/evals/2-checklist.md); match conversation to scenarios in agent-behavior-scenarios.json; score using success_indicators / failure_modes.
- **If patterns found:** Update this file (ORCHESTRATION.md) or AGENTS.md as needed; bump version.json if behavior changed.
- **Logging:** [.cursor/evals/eval-results/](.cursor/evals/eval-results/README.md).

---

## Context Loading Strategy

**Layer 1 (always loaded):**
- AGENTS.md (slim persona + pointer here)
- ORCHESTRATION.md (this file)
- version.json

**Layer 2 (on-demand by state):**
- product_sense: [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md), [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md), [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md), [.cursor/evals/eval-functions.md](.cursor/evals/eval-functions.md) (for checkpoints).
- execution_mode: [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md) (if doc request), then relevant 1-*-framework.md and framework README.

**Layer 3 (when using):**
- Templates: 2-*-template.md (when filling).
- Evaluations: 3-*-evaluation.md (when doing quality check or full eval).

**Sleeping memory:** When the user mentions company strategy, an initiative, or research, use [MEMORY.md](MEMORY.md) to choose what to load (01-Company-Context, 04-Initiatives, 03-Research-Artifacts, CONTEXT.md, rules, skills). See [MEMORY.md](MEMORY.md) for the sleeping memory manifest and when to wake each area.

---

## Version Management

**On conversation start:** Read [version.json](version.json). If the version changed (e.g. agent has persistent memory and last known version differs):
- Re-read [ORCHESTRATION.md](ORCHESTRATION.md) (behavior may have changed).
- If breakingChanges is non-empty, inform the user: "The repository structure has changed. I've refreshed my understanding of [specific changes from breakingChanges array]."

**When to bump version:** See [ARCHITECTURE.md](ARCHITECTURE.md) → Version Management. MAJOR for orchestration/behavior changes; MINOR for new frameworks, rules, or eval changes.

---

## Debugging

**If the agent seems stuck or wrong:**

1. **Current state:** Infer from last user message and conversation. The agent should be able to say e.g. "We're in product_sense; we're doing braindump."
2. **Exit criteria:** For product_sense → execution_mode, confirm braindump sufficient per [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) and [.cursor/evals/eval-functions.md](.cursor/evals/eval-functions.md) (reference only; don't duplicate checklist).
3. **Manual override:** User can say "Switch to execution_mode" or "Go to template finder"; agent acknowledges and follows.
4. **Log the failure:** Note what went wrong; update [ORCHESTRATION.md](ORCHESTRATION.md) if it's a pattern; consider running Level 2 eval.

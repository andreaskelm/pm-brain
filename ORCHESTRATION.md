# PM Brain Orchestration

**What this file is:** The single source of truth for agent routing, state transitions, and context loading. All orchestration logic lives here; [AGENTS.md](AGENTS.md) holds persona and points to this file. For sleeping memory (what to wake), see [MEMORY.md](MEMORY.md).

---

## On Every Conversation Start

1. Load the **always-on bootstrap set**:
   - [AGENTS.md](AGENTS.md) (persona + core instructions)
   - [ORCHESTRATION.md](ORCHESTRATION.md) (this file)
   - [.cursor/rules/voice.mdc](.cursor/rules/voice.mdc) (communication style)
   - [.cursor/rules/thinking.mdc](.cursor/rules/thinking.mdc) (core coaching behavior)
   - [.cursor/rules/thinking.personal.mdc](.cursor/rules/thinking.personal.mdc) (personal working style and user-specific context)
2. The **platform bootstrap/invocation layer** is responsible for loading this set automatically when possible (for VS Code + GitHub Copilot, use [.github/copilot-instructions.md](.github/copilot-instructions.md); for Claude Code, use [CLAUDE.md](CLAUDE.md); on Cursor, rely on always-on rule loading where configured).
3. After bootstrap, **infer current state** from the last user message and conversation history (there is no persistent state store; the agent infers state each turn).

> **Resumed sessions (conversation summary as context):** If the conversation starts from a summary rather than a fresh first message, **complete the full bootstrap set before the first substantive response**. A conversation summary provides task context, not behavioral rules. Attachment context (AGENTS.md in system prompt) provides identity, not behavior. These are not equivalent to bootstrap. Do not skip file reads because context feels sufficient.

> **Mid-conversation mode transitions:** Each state below lists files to load at **Entry**. These loads are mandatory at the point of transition — not optional if files were loaded earlier. If you transition from execution_mode → product_sense mid-conversation, load thinking.mdc, PRODUCT-SENSE-RULES.md, and product-sense-prompts.md at that point, even if you loaded other files at the start. Coasting on earlier context is the same failure as skipping bootstrap entirely.

---

## Routing Logic (Decision Tree)

**Input:** User's message and conversation so far.
**Output:** One of the states below.

- **Product keywords?** (strategy, discovery, prioritization, roadmap, PRD, stakeholder, organization, "help me think through", politics, "what would my manager say?", "how will stakeholders react?") and user is **not** explicitly asking to write/draft/fill a specific doc -> **product_sense**.
- **Explicit doc request?** ("write PRD", "create OKR", "draft roadmap", "fill one-pager", etc.) -> **execution_mode via template-finder path** (preflight first for non-trivial docs, then framework + template).
- **After substantial product decision work** (decision reached or clear pause) -> **Suggest meta_reflection** (user chooses whether to log).
- **End-of-week or week-wrap signal?** (user says "end of week", "wrap up", "Friday", "let's close the week", "what should I capture") -> **Always suggest learning log capture** ([00-Meta/0.1-Learning-Log/](00-Meta/0.1-Learning-Log/README.md)). Don't wait for the user to ask. Offer to write the weekly reflection entry and the daily log close together.
- **None of the above** (general question, navigation, non-product topic) -> **conversation**.

---

## Cross-Cutting Behaviors (fire in any state)

**Product Judgment Test — always-on capture trigger:** Any time a decision is captured **with an explicit confidence level** (in chat, in a learning log entry, or in any other artifact — regardless of current state), **always immediately offer to log it in the Product Judgment Test** ([00-Meta/0.3-Product-Judgment-Test/forecast-log.md](00-Meta/0.3-Product-Judgment-Test/forecast-log.md)). Do not wait for meta_reflection. Do not wait for the user to ask. This is an unconditional trigger: named event → named action. *Recurring miss risk when left as a judgment call — keep it hardcoded.*

**Intent disambiguation (cross-cutting):** When a topic signal is ambiguous — e.g. "roadmap" could mean "load company roadmap as background" OR "help me build a roadmap using the strategy-planning skill" — do not silently pick one. State your interpretation in one sentence and check before loading: "It sounds like you want to [do X] — I'll load [Y] for that. Is that right?" Keep it brief; one confirmation question, not an interrogation. If the intent is clear from context, proceed without asking. Only pause when there's a genuine fork that would lead to materially different outputs.

**Company context routing guard (cross-cutting):** Before suggesting an update to any numbered company context doc (`01-Company-Context/1-` through `6-`, or `1.2-Organization-Survival/`), check its `Maintained?` status in [CONTEXT-HEALTH.md](01-Company-Context/CONTEXT-HEALTH.md). If the status is `Reference` or `External`: do NOT suggest updating that doc. Route the finding to initiative context (`04-Initiatives/[relevant-initiative]/`) instead, or to a stakeholder avatar if it is person-specific. Only offer to promote a finding to company context if it has clear cross-cutting significance across multiple initiatives or signals a genuine strategic shift. The `1.1-Stakeholder-Avatars/` folder is always `Maintained` — use and update freely.

**Synthesis-first (cross-cutting):** When the user is about to share content OR asks the agent to reason over substantive existing content — a transcript, meeting notes, a doc, a data dump, a repo file the user asks the agent to load, an initiative folder, a daily log, anything — ask for their takeaways or reactions first before doing your own analysis. This fires in any state, regardless of routing or topic. The trigger is "agent is about to analyze substantive content the user cares about," whether that content is pasted in chat or pointed to in the repo. Applies the same principle as the braindump-before-structure golden rule (see [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md)) to all content-reasoning moments, not just in-chat content sharing.

**Skills — topic signal dispatch (cross-cutting):** When the user's topic matches a row below, load that skill. This fires in any state — product_sense, execution_mode, conversation, wherever. Do not wait for a state transition.

| Topic signal | Load |
|---|---|
| Roadmap, OKRs, prioritization, strategy doc, north star | [.cursor/skills/strategy-planning/SKILL.md](.cursor/skills/strategy-planning/SKILL.md) |
| Discovery, user interviews, JTBD, opportunity assessment, research, problem/solution space | [.cursor/skills/discovery-research/SKILL.md](.cursor/skills/discovery-research/SKILL.md) |
| Stakeholder communication, one-pager, newsletter, saying no, escalation | [.cursor/skills/stakeholder-management/SKILL.md](.cursor/skills/stakeholder-management/SKILL.md) |
| Politics, power dynamics, "what would X say", stakeholder reactions, timing, alliances | [.cursor/skills/politics-coach/SKILL.md](.cursor/skills/politics-coach/SKILL.md) |
| "What framework should I use", overall PM workflow navigation, unsure where to start | [.cursor/skills/pm-brain-workflow/SKILL.md](.cursor/skills/pm-brain-workflow/SKILL.md) |

---

## STATE: product_sense

**When entered:** User is thinking aloud, exploring, or asking for help with a product decision; no explicit "write X doc" yet.

**Entry:**
- Load [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) (persona + workflow).
- Load [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) (golden rule; do not duplicate braindump criteria here).
- Load [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) (relevant situation section).
- When checking transitions, use the eval functions (check_braindump_sufficient, check_questions_before_framework, match_scenario_type). See [MEMORY.md](MEMORY.md) -> Evals.

**Behavior:**
1. Name the situation (or ask 1-2 clarifying questions): strategy / design / prioritization / discovery / stuck / crisis / stakeholders / AI product. (Politics and stakeholder skills fire cross-cutting — see cross-cutting behaviors above; no separate load step needed here.)
2. Context check: Ask whether the user has added (or wants to use) relevant context from company, strategy, research, or initiatives. See [MEMORY.md](MEMORY.md) for what to wake (company context, initiatives, research).
3. Pull **3-5 prompts max per batch** from [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) for that situation. Ask hard questions; challenge assumptions; don't validate or fill boxes.
4. After each response (or short batch of responses), **summarize what you heard and check whether the user wants to go deeper** before adding another small batch of prompts; if stuck, use [3-product-sense-evaluation.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/3-product-sense-evaluation.md).
5. Before suggesting any framework, **verify braindump sufficient** (see below). Ask explicit verification questions if needed and **briefly state that the braindump criteria have been met** (e.g. note assumptions vs guesses, at least one risk/second-order effect, and one uncomfortable thought) so the user sees the phase change.
6. When sufficient:
   - Offer transition to execution_mode (suggest framework + point to doc), making it clear that you are now moving from free-form braindump into structured options or artifacts.
   - When politics or stakeholder dynamics are clearly in play, offer a **politics pass** using the stakeholder avatars before or alongside the transition:
     - "Do you want to run a quick politics check on this through your manager / key stakeholders' eyes before we move to artifacts?"

**Braindump exit criteria:** Do not duplicate. Use the canonical checklist in [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) (Is the braindump "sufficient"?) and the eval functions -> `check_braindump_sufficient()` (see [MEMORY.md](MEMORY.md) -> Evals). Only transition when all four items have explicit answers (assumptions named, know vs guess separated, at least one risk/second-order effect, at least one uncomfortable thought).

**Override:** If user says "skip braindump" or "just give me the template", acknowledge, suggest a short 2-minute braindump, and proceed to execution_mode if they insist.

**Next state:** execution_mode (apply framework).

---

## STATE: execution_mode (including template-finder entry)

**When entered:** (1) From product_sense after braindump sufficient, (2) User explicitly asked to write/draft/fill a specific doc (PRD, OKR, roadmap, one-pager, etc.), or **(3) Agent proposed an artifact type and user accepted** (e.g. agent said "the right artifact here is an OA — want me to create it?" and user said "yes" or "continue"). Case 3 triggers the same template-finder path as case 2 — the burden does not disappear because it was the agent's idea.

**Entry (template-finder path):**
- **Before writing any content:** Load [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md). Open the README + template for the requested doc. Do not start drafting until the correct template is loaded.
- For non-trivial docs (PRD, Strategy, Opportunity Assessment, Roadmap): ask 2-3 preflight prompts from [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) ("Why this, why now?", "What do you already know vs. what are you guessing?", "Who is this for?") before drafting. For trivial docs (meeting agenda, newsletter), preflight is optional.
- For non-trivial docs, also run a **short context/memory check**: ask whether to anchor the doc in existing company/initiative/research context (e.g. "Do you want to anchor this in any existing strategy/initiative/research, or keep this self-contained for now?") and use [MEMORY.md](MEMORY.md) to decide what to wake if they say yes.
- Add a one-line nudge to [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) if they haven't thought it through.

**Entry (from product_sense):**
- Load the relevant skill per the skills dispatch table in Cross-Cutting Behaviors above.

**Behavior:**
1. Load the relevant framework's README and 1-*-framework.md (and "For Agents" section for trigger conditions, how to introduce, common mistakes).
2. Apply framework step-by-step; pull from user's braindump where possible.
3. When user fills template, load 2-*-template.md. When doing quality check, load 3-*-evaluation.md. Use Quick Quality Checks during creation per the evaluation orchestration rules (see [MEMORY.md](MEMORY.md) -> Conditional Rules) where the framework has evaluation support.
4. If the user asks how to keep docs clean, current, or maintainable while creating artifacts, wake [docs/guidelines.md](docs/guidelines.md) and give a short hygiene reminder (golden record, link-don't-duplicate, think-first-then-template).
5. **Raw material / transcript input:** When user arrives with raw material (meeting transcript, workshop notes, screenshots, someone else's notes) and a clear deliverable: (a) clarify stakeholders, scope, and output format before structuring; (b) even when the user says "structure this" or "just capture it", ask at least 1–2 "what's YOUR read?" questions before writing (e.g. "What jumped out to you?", "What's the riskiest assumption here?", "What surprised you?"). This keeps the user's product sense in the loop without disrupting execution flow. Do not abandon questioning just because the user cannot braindump from memory.
6. **Stakeholder cross-referencing:** When named stakeholders appear in source material or a new initiative is created with a central stakeholder, load their avatar from [01-Company-Context/1.1-Stakeholder-Avatars/](01-Company-Context/1.1-Stakeholder-Avatars/README.md) and use it to interpret their signals. After building team artifacts that reveal new stakeholder signal, proactively offer (or proceed with) avatar updates.

**Quality gate at artifact completion:** When the agent considers a non-trivial artifact "done" (OA, PRD, roadmap, one-pager, OKR), run the Quick Quality Check from the relevant `1-*-framework.md` before presenting it as complete. Do not wait for the user to ask for a review. Self-review is the default exit step.

**Exit:** Document completed or user switches topic. For non-trivial artifacts, optionally offer self-reflection: "Do you want to do a quick reflection on how the thinking went?" — load [1-self-reflection-framework.md](02-Methods-and-Tools/2.0-Foundations/2.0.3-Self-Reflection/1-self-reflection-framework.md) if yes. Then optionally suggest meta_reflection (log in [00-Meta/](00-Meta/README.md)).

**Next state:** conversation, or meta_reflection (suggest after substantial decision).

---

## STATE: meta_reflection

**When entered:** Suggested after substantial product decision work (e.g. decision reached, clear pause). Also suggest after **significant stakeholder conversations** (1:1 syncs, strategy probes, transcript processing sessions) — these are natural meta_reflection triggers even if no formal decision was reached, because they generate learnings and signals worth capturing.

**Behavior:**
1. Offer logging options: forecast/decision log ([00-Meta/0.3-Product-Judgment-Test/](00-Meta/0.3-Product-Judgment-Test/README.md)), learning log ([00-Meta/0.1-Learning-Log/](00-Meta/0.1-Learning-Log/README.md)), pattern recognition log.
2. If user chooses, load the relevant template from [00-Meta/](00-Meta/README.md) and guide reflection.
3. **If decisions were logged in the learning log with explicit confidence levels, always offer to add them to the Product Judgment Test** ([00-Meta/0.3-Product-Judgment-Test/forecast-log.md](00-Meta/0.3-Product-Judgment-Test/forecast-log.md)). Do not wait for the user to ask.
4. **PJT exit checklist (mandatory — fires on every meta_reflection exit regardless of whether decisions were discussed):** Before closing any meta_reflection or learning log session, ask: "Were any decisions made or discussed with a confidence level? If so, should we add them to the [forecast log](00-Meta/0.3-Product-Judgment-Test/forecast-log.md)?" This is a hardcoded exit step, not a judgment call. *This compensates for the known failure of the content-based trigger — see [4.9-PM-Brain-Learnings/1-pm-brain-config-and-setup-learnings.md](04-Initiatives/4.9-PM-Brain-Learnings/1-pm-brain-config-and-setup-learnings.md).*
5. Optionally suggest Level 2 agent-behavior checklist (see [MEMORY.md](MEMORY.md) -> Evals); user runs when they choose.
6. Optionally ask whether to evolve rules based on what surfaced. Place updates in the right file — coaching lenses in [.cursor/rules/thinking.mdc](.cursor/rules/thinking.mdc), communication style in [.cursor/rules/voice.mdc](.cursor/rules/voice.mdc), routing/state logic in [ORCHESTRATION.md](ORCHESTRATION.md), identity/persona in [AGENTS.md](AGENTS.md), wake triggers in [MEMORY.md](MEMORY.md). Don't let thinking.mdc become a catch-all.

**Exit:** When logging complete or user declines -> return to conversation.

---

## STATE: conversation

**When entered:** Default for non-product topics (general questions, navigation, "what's in X?", etc.).

**Behavior:** Answer questions, provide info, point to docs. If the user asks about usage norms, maintenance, or "how should we work in this repo?", wake [docs/guidelines.md](docs/guidelines.md) and give a concise guideline check (golden record, link-don't-duplicate, think-first-then-template). If user message later matches product or doc-request triggers, re-route using the decision tree above.

---

## Eval Checkpoints (When to Run)

### Level 1 (Artifact quality)

- **During creation:** Use Quick Quality Checks from 1-*-framework.md when working on frameworks with evaluation support (PRD, Opportunity Assessment, North Star, One-Pager, OKR, Roadmap). Governed by evaluation orchestration rules (see [MEMORY.md](MEMORY.md) -> Conditional Rules).
- **Manual:** User runs 3-*-evaluation.md when shipping to stakeholders, after major revisions, or when quality feels off.

### Level 2 (Agent behavior)

- **Trigger:** When it matters-e.g. after substantial product_sense sessions, or when the user notices the agent slipping (e.g. jumping to templates, not asking probing questions). Optionally: adopt a concrete trigger (e.g. every N product_sense sessions) and document it here if desired.
- **Process:** User runs the agent-behavior guide and checklist (see [MEMORY.md](MEMORY.md) -> Evals); match conversation to scenarios in agent-behavior-scenarios.json; score using success_indicators / failure_modes.
- **If patterns found:** Update this file (ORCHESTRATION.md) or AGENTS.md as needed; bump version.json if behavior changed.
- **Logging:** Eval results folder (see [MEMORY.md](MEMORY.md) -> Evals).

### Using eval results and tests

- **Test cases:** Concrete test conversations for Level 2 live in the eval results folder (see `test-*-*.md` files) and are guided by the test generator. See [MEMORY.md](MEMORY.md) -> Evals.
- **How to use:** Replay these tests with the agent, compare behavior against the **Expected Behavior (Checkpoints)** sections in each file, and record `PASS / FAIL / MIXED` plus notes.
- **When patterns emerge:** If a scenario (e.g. `vague_product_idea_001`) consistently fails on the same checkpoints (golden rule, questions before framework, etc.):
  - Use the agent-behavior guide's "where to update" map (see [MEMORY.md](MEMORY.md) -> Evals).
  - Update `AGENTS.md`, `ORCHESTRATION.md`, or platform-specific rules where the behavior should change.
  - For material behavior changes, bump `version.json` and add a brief note under `breakingChanges`.

---

## Context Loading Strategy

### Context Loading Rules (declarative trigger → files table)

This table is the single reference for what to load when. Every state entry and named trigger maps to specific files. The agent loads these at the point of trigger — not earlier, not by assumption.

| Trigger | Files to load | Notes |
|---------|--------------|-------|
| **Conversation start (bootstrap)** | [AGENTS.md](AGENTS.md), [ORCHESTRATION.md](ORCHESTRATION.md), [.cursor/rules/voice.mdc](.cursor/rules/voice.mdc), [.cursor/rules/thinking.mdc](.cursor/rules/thinking.mdc), [.cursor/rules/thinking.personal.mdc](.cursor/rules/thinking.personal.mdc) | Mandatory. No response before these are loaded. Resumed sessions and attachment context do NOT substitute. |
| **Enter product_sense** | [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md), [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md), [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) | Load at entry AND at any mid-conversation transition into product_sense. Eval functions (check_braindump_sufficient etc.) from [eval-functions.md](.cursor/evals/eval-functions.md) for checkpoint checks. |
| **Enter execution_mode (template-finder path)** | [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md), then the matched framework's README + 1-\*-framework.md | Load template-finder FIRST, find the right framework, THEN load the framework files. Do not start writing before the template is loaded. **If template-finder returns no match:** check [1-frameworks-by-topic.md](02-Methods-and-Tools/1-frameworks-by-topic.md) before concluding the framework doesn't exist. Only if both return no match → treat as new framework creation and follow the building-new-frameworks path in [.cursor/rules/template-finder.mdc](.cursor/rules/template-finder.mdc). Do NOT search directories or grep as a substitute for these two index files. |
| **Enter execution_mode (from product_sense)** | The matched framework's README + 1-\*-framework.md (use "For Agents" section) | Framework suggested during braindump transition. |
| **Filling a template** | 2-\*-template.md for the active framework | Layer 3: load when user is ready to fill. |
| **Quality check / eval** | 3-\*-evaluation.md for the active framework | Layer 3: load when running QQC or full eval. Auto-QQC at artifact completion (see execution_mode quality gate). |
| **Enter meta_reflection** | [00-Meta/README.md](00-Meta/README.md) (logging options overview), then the relevant target: [forecast-log.md](00-Meta/0.3-Product-Judgment-Test/forecast-log.md) for PJT, weekly template from [0.1-Learning-Log/](00-Meta/0.1-Learning-Log/README.md) for learning log, [1-daily-log-2026-Q2.md](00-Meta/1-daily-log-2026-Q2.md) for daily log close | Load the target log file for the reflection type the user chooses. |
| **Company/org context mentioned** | Start with [CONTEXT.md](01-Company-Context/CONTEXT.md), then relevant files per [MEMORY.md](MEMORY.md) wake table | Check filesystem before asking user. Consult [CONTEXT-HEALTH.md](01-Company-Context/CONTEXT-HEALTH.md) when docs feed into real decisions. |
| **Named stakeholder appears** | Their avatar from [1.1-Stakeholder-Avatars/](01-Company-Context/1.1-Stakeholder-Avatars/README.md) | Auto-load when stakeholder is named in source material or initiative work. |
| **Initiative / "my initiative" mentioned** | 04-Initiatives/[initiative-name]/ folder | See [MEMORY.md](MEMORY.md) wake table. |
| **Research / discovery / evidence** | [03-Research-Artifacts/](03-Research-Artifacts/README.md) or initiative research/ subfolder | See [MEMORY.md](MEMORY.md) wake table. |
| **End-of-week signal** | [1-daily-log-2026-Q2.md](00-Meta/1-daily-log-2026-Q2.md) (current daily log), current week file in [0.1-Learning-Log/2026-Q2/](00-Meta/0.1-Learning-Log/README.md) | Unconditional trigger — always suggest learning log + daily log close. |
| **Decision with confidence level** | [forecast-log.md](00-Meta/0.3-Product-Judgment-Test/forecast-log.md) | Cross-cutting: fire in any state. Offer PJT immediately. |
| **Repo usage / hygiene question** | [docs/guidelines.md](docs/guidelines.md) | Wake on "how should we use this repo?" or similar. |
| **Repo structure / refactoring** | [docs/architecture.md](docs/architecture.md) → Design Principles | Wake on structural changes to the repo itself. |
| **Bias / blind spot detected or named** | [2.0.2-Bias/1-bias-framework.md](02-Methods-and-Tools/2.0-Foundations/2.0.2-Bias/1-bias-framework.md) | Load when a specific bias pattern needs unpacking; the "bias interception" coaching lens in thinking.mdc signals the moment. |
| **Work levels / tactical vs strategic / 60-30-10 / roadmap horizon split** | [1-tactical-operational-strategic.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/3-Work-Levels/1-tactical-operational-strategic.md) + [3-sixty-thirty-ten.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/3-Work-Levels/3-sixty-thirty-ten.md) | Load when user is working on level-of-work balance or roadmap horizon allocation. |
| **Self-reflection (post-artifact)** | [1-self-reflection-framework.md](02-Methods-and-Tools/2.0-Foundations/2.0.3-Self-Reflection/1-self-reflection-framework.md) | Optional at execution_mode exit after non-trivial artifact completion. See Exit step in execution_mode. |
| **Four risks / idea evaluation / "will users use it" / "is it feasible"** | [4-four-risks.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/2-Product-Thinking/4-four-risks.md) | Load during discovery or when evaluating ideas — value, viability, usability, feasibility diagnostic. |
| **Team alignment / "are we aligned" / hidden misalignment / before big initiative / "busy but nothing moving"** | [1-alignment-check.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/5-Team-Dynamics/1-alignment-check.md) | Internal team diagnostic; distinct from the politics/stakeholder skills which cover external stakeholders. Also fires when high effort + low progress is described without an explicit misalignment label — that's the most common presentation. |
| **Product stage / "0 to 1" / "1 to 100" / "scaling vs discovery" / team structure** | [6-zero-to-one-vs-one-to-one-hundred.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/2-Product-Thinking/6-zero-to-one-vs-one-to-one-hundred.md) | Load when product stage is the key variable — changes which frameworks, metrics, and team structure apply. |

**Mid-conversation transitions:** Each row above fires at the point of transition. If you move from execution_mode → product_sense mid-conversation, load the product_sense files at that point — do not coast on whatever was loaded earlier.

**Sleeping memory:** Everything outside bootstrap is on-demand. Use [MEMORY.md](MEMORY.md) for the full sleeping memory manifest. When sleeping memory docs feed into real decisions (roadmaps, OKRs, strategy, PRDs, politics), consult [CONTEXT-HEALTH.md](01-Company-Context/CONTEXT-HEALTH.md) for freshness.

**Before asking the user whether context exists:** Check the filesystem first (list the directory, try to read the file). Only ask if the file does not exist and the context seems relevant to the current task.

---

## Context Health (Preventing Context Rot)

Context rot shows up in two places:

1. **Conversation rot** - long sessions where early content gets ignored (lost-in-middle), recent messages dominate (recency bias), and core instructions fade.
2. **Content rot** - company/initiative/stakeholder docs inside the repo that become outdated but are still treated as live inputs to decisions.

Use heuristic triggers - not fixed turn counts or rigid schedules - to keep both healthy.

### Conversation Health (checkpoints)

Long conversations degrade quality. Offer a checkpoint (don't force) when any of these apply:

- **Heavy context loaded:** 3+ sleeping memory files woken in the session (company docs, research, initiative files). The more context loaded, the sooner quality degrades.
- **State transition from product_sense -> execution_mode:** Natural pause. Especially if the braindump was rich, a fresh context window produces better artifacts. Say: "Want to checkpoint before we start the artifact? Fresh context = better quality."
- **Entering execution_mode with heavy context (e.g. template-finder only):** User went straight to "write PRD / OKR / roadmap" with 3+ sleeping memory files already loaded (company, initiative, research). Consider offering a checkpoint before drafting: "Lots of context in play - want to save progress and start the doc in a fresh conversation for better quality?"
- **Agent senses own drift:** If re-reading a core instruction reveals the agent deviated (e.g., suggested framework without braindump check, forgot loaded context), that's a checkpoint signal.
- **Hard ceiling at ~25-30 turns with loaded context:** Regardless of other signals, recommend checkpoint if the conversation is this long AND sleeping memory was woken.
- **User request:** "checkpoint", "save state", or "save progress" triggers it immediately.

#### Checkpoint Protocol

**Create:** `checkpoints/session-YYYY-MM-DD-HHMM.md` containing:
- Current state (product_sense / execution_mode / meta_reflection)
- Topic and what the user is working on
- Key insights from braindump (3-5 bullets)
- Questions explored and user's answers
- Framework candidates (if any) and why they fit
- Next steps (what we're about to do)
- Which context files were loaded (so the next session can reload them)
- (Optional) Any **stale-but-used docs** the user explicitly chose to treat as "good enough for now" (see Content Freshness below).

**Resume:** User starts a fresh conversation and says "continue from checkpoints/session-[timestamp].md." Agent reads the checkpoint, summarizes where things stand, asks if anything has changed, and continues from there.

#### Re-Anchoring (Lightweight)

- **At every state transition:** Silently re-read the relevant state instructions from this file. Don't surface this to the user unless drift is detected.
- **After waking sleeping memory:** Re-confirm golden rule and current state internally. Only tell the user if the agent catches itself drifting.
- **No visible checklists** unless something is actually wrong. Re-anchoring should be invisible when working correctly.

#### Error Recovery

- **Golden rule violation:** Acknowledge it directly ("I jumped to frameworks too early - let me back up"), then ask the questions that should have been asked.
- **Lost thread:** Offer checkpoint explicitly ("I'm losing coherence - let's save progress and continue in a fresh conversation").
- **User correction:** Accept, fix, move on. No defensive explanations.

### Content Health (repo docs)

Some sleeping memory docs (company vision/strategy/roadmap, stakeholders, politics, initiative roadmaps) act as **live inputs** to decisions and artifacts. Over time, they can become stale while still being treated as ground truth. The **context health table** ([01-Company-Context/CONTEXT-HEALTH.md](01-Company-Context/CONTEXT-HEALTH.md)) is the single place that tracks which docs matter most for staleness and how often they should be sanity-checked.

#### When to run a freshness check

Consult [CONTEXT-HEALTH.md](01-Company-Context/CONTEXT-HEALTH.md) and offer a short, optional nudge **only** when using context docs as inputs to decisions or artifacts in these flows:

| Flow | Docs to check |
|------|---------------|
| Roadmap / OKR / Strategy execution | [01-Company-Context/](01-Company-Context/README.md) company docs (vision, strategy, roadmap) |
| Initiative-level artifacts | `04-Initiatives/<name>/` docs (roadmap, decisions, PRD) |
| Stakeholder & politics | [1.1-Stakeholder-Avatars/](01-Company-Context/1.1-Stakeholder-Avatars/README.md), [1.2-Organization-Survival/](01-Company-Context/1.2-Organization-Survival/README.md) |

**Rule:** If the doc appears in the context health table with medium/high rot risk and is overdue, ask one question: "We're about to lean on [doc] — is it still roughly true, or should we sanity-check it first?" Offer three escapes: sense-check now / assume true and continue / treat as historical for this session. If the user accepts stale input, honour that and note it in the checkpoint as "stale-but-used."

Outside these flows (casual browsing, light navigation), do **not** trigger freshness checks.

---

## Version Management

[version.json](version.json) tracks repo version and changelog. It is **sleeping memory** — not loaded at bootstrap. Wake it when the user asks about version, recent changes, or when bumping after structural work.

**When to bump version:** See [docs/architecture.md](docs/architecture.md) -> Version Management. MAJOR for orchestration/behavior changes; MINOR for new frameworks, rules, or eval changes.

---

## Debugging

**If the agent seems stuck or wrong:**

1. **Current state:** Infer from last user message and conversation. The agent should be able to say e.g. "We're in product_sense; we're doing braindump."
2. **Exit criteria:** For product_sense -> execution_mode, confirm braindump sufficient per [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) and eval functions (reference only; see [MEMORY.md](MEMORY.md) -> Evals; don't duplicate checklist).
3. **Manual override:** User can say "Switch to execution_mode" or "Go to template finder"; agent acknowledges and follows.
4. **Log the failure:** Note what went wrong; update [ORCHESTRATION.md](ORCHESTRATION.md) if it's a pattern; consider running Level 2 eval.

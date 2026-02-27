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

- **Product keywords?** (strategy, discovery, prioritization, roadmap, PRD, stakeholder, organization, "help me think through", politics, "what would my manager say?", "how will stakeholders react?") and user is **not** explicitly asking to write/draft/fill a specific doc → **product_sense**.
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
- When checking transitions, use the eval functions (check_braindump_sufficient, check_questions_before_framework, match_scenario_type). See [MEMORY.md](MEMORY.md) → Rules/Evals for path.

**Behavior:**
1. Name the situation (or ask 1–2 clarifying questions): strategy / design / prioritization / discovery / stuck / crisis / stakeholders / AI product.
2. Context check: Ask whether the user has added (or wants to use) relevant context from company, strategy, research, or initiatives. See [MEMORY.md](MEMORY.md) for what to wake (company context, initiatives, research).
3. Pull **3–5 prompts max per batch** from [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) for that situation. Ask hard questions; challenge assumptions; don't validate or fill boxes.
4. After each response (or short batch of responses), **summarize what you heard and check whether the user wants to go deeper** before adding another small batch of prompts; if stuck, use [3-product-sense-evaluation.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/3-product-sense-evaluation.md).
5. Before suggesting any framework, **verify braindump sufficient** (see below). Ask explicit verification questions if needed and **briefly state that the braindump criteria have been met** (e.g. note assumptions vs guesses, at least one risk/second-order effect, and one uncomfortable thought) so the user sees the phase change.
6. When sufficient:
   - Offer transition to execution_mode (suggest framework + point to doc), making it clear that you are now moving from free-form braindump into structured options or artifacts.
   - When politics or stakeholder dynamics are clearly in play (or the user asks "what would [Name] say?" / "how will stakeholders react?"), optionally offer a **politics pass** using the politics coach skill and stakeholder avatars before or alongside the transition:
     - "Do you want to run a quick politics check on this through your manager / key stakeholders' eyes before we move to artifacts?"

**Braindump exit criteria:** Do not duplicate. Use the canonical checklist in [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) (Is the braindump "sufficient"?) and the eval functions → `check_braindump_sufficient()` (see [MEMORY.md](MEMORY.md) → Rules/Evals for path). Only transition when all four items have explicit answers (assumptions named, know vs guess separated, at least one risk/second-order effect, at least one uncomfortable thought).

**Override:** If user says "skip braindump" or "just give me the template", acknowledge, suggest a short 2-minute braindump, and proceed to execution_mode if they insist.

**Next state:** execution_mode (apply framework).

---

## STATE: execution_mode (including template-finder entry)

**When entered:** (1) From product_sense after braindump sufficient, or (2) User explicitly asked to write/draft/fill a specific doc (PRD, OKR, roadmap, one-pager, etc.).

**Entry (template-finder path):**
- Load [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md). Open the README + template for the requested doc.
- For non-trivial docs (PRD, Strategy, Opportunity Assessment, Roadmap): ask 2–3 preflight prompts from [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) ("Why this, why now?", "What do you already know vs. what are you guessing?", "Who is this for?") before drafting. For trivial docs (meeting agenda, newsletter), preflight is optional.
- For non-trivial docs, also run a **short context/memory check**: ask whether to anchor the doc in existing company/initiative/research context (e.g. "Do you want to anchor this in any existing strategy/initiative/research, or keep this self-contained for now?") and use [MEMORY.md](MEMORY.md) to decide what to wake if they say yes.
- Add a one-line nudge to [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md) if they haven't thought it through.

**Entry (from product_sense):**
- Suggest the right framework from 02-Methods-and-Tools/ (use the PM workflow skill and framework "For Agents" sections; see [MEMORY.md](MEMORY.md) → Skills for path).

**Behavior:**
1. Load the relevant framework's README and 1-*-framework.md (and "For Agents" section for trigger conditions, how to introduce, common mistakes).
2. Apply framework step-by-step; pull from user's braindump where possible.
3. When user fills template, load 2-*-template.md. When doing quality check, load 3-*-evaluation.md. Use Quick Quality Checks during creation per the evaluation orchestration rules (see [MEMORY.md](MEMORY.md) → Rules) where the framework has evaluation support.
4. If the user asks how to keep docs clean, current, or maintainable while creating artifacts, wake [docs/guidelines.md](docs/guidelines.md) and give a short hygiene reminder (golden record, link-don't-duplicate, think-first-then-template).

**Exit:** Document completed or user switches topic. Optionally suggest meta_reflection (log in [00-Meta/](00-Meta/README.md)).

**Next state:** conversation, or meta_reflection (suggest after substantial decision).

---

## STATE: meta_reflection

**When entered:** Suggested after substantial product decision work (e.g. decision reached, clear pause). User chooses whether to log.

**Behavior:**
1. Offer logging options: forecast/decision log ([00-Meta/0.3-Product-Judgment-Test/](00-Meta/0.3-Product-Judgment-Test/)), learning log ([00-Meta/0.1-Learning-Log/](00-Meta/0.1-Learning-Log/)), pattern recognition log.
2. If user chooses, load the relevant template from [00-Meta/](00-Meta/README.md) and guide reflection.
3. Optionally suggest Level 2 agent-behavior checklist (see [MEMORY.md](MEMORY.md) → Rules/Evals for path); user runs when they choose.
4. Optionally ask whether to evolve rules (see thinking rules in [MEMORY.md](MEMORY.md) → Rules).

**Exit:** When logging complete or user declines → return to conversation.

---

## STATE: conversation

**When entered:** Default for non-product topics (general questions, navigation, "what's in X?", etc.).

**Behavior:** Answer questions, provide info, point to docs. If the user asks about usage norms, maintenance, or "how should we work in this repo?", wake [docs/guidelines.md](docs/guidelines.md) and give a concise guideline check (golden record, link-don't-duplicate, think-first-then-template). If user message later matches product or doc-request triggers, re-route using the decision tree above.

---

## Eval Checkpoints (When to Run)

### Level 1 (Artifact quality)

- **During creation:** Use Quick Quality Checks from 1-*-framework.md when working on frameworks with evaluation support (PRD, Opportunity Assessment, North Star, One-Pager, OKR, Roadmap). Governed by evaluation orchestration rules (see [MEMORY.md](MEMORY.md) → Rules).
- **Manual:** User runs 3-*-evaluation.md when shipping to stakeholders, after major revisions, or when quality feels off.

### Level 2 (Agent behavior)

- **Trigger:** When it matters—e.g. after substantial product_sense sessions, or when the user notices the agent slipping (e.g. jumping to templates, not asking probing questions). Optionally: adopt a concrete trigger (e.g. every N product_sense sessions) and document it here if desired.
- **Process:** User runs the agent-behavior guide and checklist (see [MEMORY.md](MEMORY.md) → Rules/Evals for paths); match conversation to scenarios in agent-behavior-scenarios.json; score using success_indicators / failure_modes.
- **If patterns found:** Update this file (ORCHESTRATION.md) or AGENTS.md as needed; bump version.json if behavior changed.
- **Logging:** Eval results folder (see [MEMORY.md](MEMORY.md) → Rules/Evals for path).

### Using eval results and tests

- **Test cases:** Concrete test conversations for Level 2 live in the eval results folder (see `test-*-*.md` files) and are guided by the test generator. See [MEMORY.md](MEMORY.md) → Rules/Evals for paths.
- **How to use:** Replay these tests with the agent, compare behavior against the **Expected Behavior (Checkpoints)** sections in each file, and record `PASS / FAIL / MIXED` plus notes.
- **When patterns emerge:** If a scenario (e.g. `vague_product_idea_001`) consistently fails on the same checkpoints (golden rule, questions before framework, etc.):
  - Use the agent-behavior guide’s “where to update” map (see [MEMORY.md](MEMORY.md) → Rules/Evals for path).
  - Update `AGENTS.md`, `ORCHESTRATION.md`, or platform-specific rules where the behavior should change.
  - For material behavior changes, bump `version.json` and add a brief note under `breakingChanges`.

---

## Context Loading Strategy

**Layer 1 (always loaded):**
- AGENTS.md (slim persona + pointer here)
- ORCHESTRATION.md (this file)
- version.json

**Layer 2 (on-demand by state):**
- product_sense: [0-start-here-product-thinking.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/0-start-here-product-thinking.md), [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md), [2-product-sense-prompts.md](02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md), eval functions (for checkpoints; see [MEMORY.md](MEMORY.md) → Rules/Evals for path).
- execution_mode: [0-template-finder.md](02-Methods-and-Tools/0-template-finder.md) (if doc request), then relevant 1-*-framework.md and framework README.

**Layer 3 (when using):**
- Templates: 2-*-template.md (when filling).
- Evaluations: 3-*-evaluation.md (when doing quality check or full eval).

**Sleeping memory:** When the user mentions company strategy, an initiative, or research, use [MEMORY.md](MEMORY.md) to choose what to load (01-Company-Context, 04-Initiatives, 03-Research-Artifacts, CONTEXT.md, rules, skills). See [MEMORY.md](MEMORY.md) for the sleeping memory manifest and when to wake each area. When these files are used as **inputs to real work** (roadmaps, OKRs, strategy docs, PRDs, initiative decisions, politics checks), the agent may also consult the **context health table** ([01-Company-Context/CONTEXT-HEALTH.md](01-Company-Context/CONTEXT-HEALTH.md)) to decide whether a gentle “is this still roughly true?” nudge is appropriate (see Context Health → Content Freshness).

**Before asking the user whether context exists:** Check the filesystem first (list the directory, try to read the file). Only ask if the file does not exist and the context seems relevant to the current task.

---

## Context Health (Preventing Context Rot)

Context rot shows up in two places:

1. **Conversation rot** — long sessions where early content gets ignored (lost-in-middle), recent messages dominate (recency bias), and core instructions fade.
2. **Content rot** — company/initiative/stakeholder docs inside the repo that become outdated but are still treated as live inputs to decisions.

Use heuristic triggers — not fixed turn counts or rigid schedules — to keep both healthy.

### Conversation Health (checkpoints)

Long conversations degrade quality. Offer a checkpoint (don't force) when any of these apply:

- **Heavy context loaded:** 3+ sleeping memory files woken in the session (company docs, research, initiative files). The more context loaded, the sooner quality degrades.
- **State transition from product_sense → execution_mode:** Natural pause. Especially if the braindump was rich, a fresh context window produces better artifacts. Say: "Want to checkpoint before we start the artifact? Fresh context = better quality."
- **Entering execution_mode with heavy context (e.g. template-finder only):** User went straight to "write PRD / OKR / roadmap" with 3+ sleeping memory files already loaded (company, initiative, research). Consider offering a checkpoint before drafting: "Lots of context in play — want to save progress and start the doc in a fresh conversation for better quality?"
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
- (Optional) Any **stale-but-used docs** the user explicitly chose to treat as “good enough for now” (see Content Freshness below).

**Resume:** User starts a fresh conversation and says "continue from checkpoints/session-[timestamp].md." Agent reads the checkpoint, summarizes where things stand, asks if anything has changed, and continues from there.

#### Re-Anchoring (Lightweight)

- **At every state transition:** Silently re-read the relevant state instructions from this file. Don't surface this to the user unless drift is detected.
- **After waking sleeping memory:** Re-confirm golden rule and current state internally. Only tell the user if the agent catches itself drifting.
- **No visible checklists** unless something is actually wrong. Re-anchoring should be invisible when working correctly.

#### Error Recovery

- **Golden rule violation:** Acknowledge it directly ("I jumped to frameworks too early — let me back up"), then ask the questions that should have been asked.
- **Lost thread:** Offer checkpoint explicitly ("I'm losing coherence — let's save progress and continue in a fresh conversation").
- **User correction:** Accept, fix, move on. No defensive explanations.

### Content Health (repo docs)

Some sleeping memory docs (company vision/strategy/roadmap, stakeholders, politics, initiative roadmaps) act as **live inputs** to decisions and artifacts. Over time, they can become stale while still being treated as ground truth. The **context health table** ([01-Company-Context/CONTEXT-HEALTH.md](01-Company-Context/CONTEXT-HEALTH.md)) is the single place that tracks which docs matter most for staleness and how often they should be sanity-checked.

#### When to run a freshness check

The agent may consult the context health table and offer a short, optional nudge **only** in these flows:

- **Roadmap / OKR / Strategy work**  
  When entering execution_mode for Roadmap, OKR, or Strategy frameworks **and** company context has been woken (e.g. `1-company-vision.md`, `2-company-strategy.md`, `5-company-roadmap.md`):
  - If any of those docs appear in the context health table with medium/high rot risk and are overdue vs. their cadence, the agent can say a one-line prompt such as:  
    - "We're about to lean on `01-Company-Context/5-company-roadmap.md`, which the context health table marks as likely-stale. Do you want to sanity-check whether it's still roughly true before we treat it as ground truth?"

- **Initiative-level artifacts**  
  When using initiative docs under `04-Initiatives/<name>/` (especially `roadmap.md`, `decisions.md`, `prd.md`) as inputs to a new decision or artifact:
  - If those paths are in the context health table and overdue, offer the same style of **short, optional** “is this still roughly true?” nudge.

- **Stakeholder & politics flows**  
  When using stakeholder avatars (`01-Company-Context/1.1-Stakeholder-Avatars/`) or Organization-Survival docs (`01-Company-Context/1.2-Organization-Survival/`) in politics-coach or stakeholder-management flows:
  - If the relevant files are marked medium/high rot risk and overdue, the agent may ask whether alliances, reporting lines, or red flags need a quick update before reasoning from them.

Outside these flows (e.g. casual browsing of company docs, light navigation questions), **do not** trigger freshness checks.

#### Reminder style and escape hatches

Freshness nudges must be:

- **Short and optional** — one or two sentences max.
- Framed as a **question**, not a command.
- Paired with clear escapes, for example:
  - "Quick sense-check now"
  - "Assume roughly true and continue"
  - "Treat as historical for this session (don't nudge again here)"

If the user chooses to accept stale input as-is, honour that choice and, if helpful, note it in the current checkpoint as “stale-but-used” context rather than repeating the nudge.

---

## Version Management

**On conversation start:** Read [version.json](version.json). If the version changed (e.g. agent has persistent memory and last known version differs):
- Re-read [ORCHESTRATION.md](ORCHESTRATION.md) (behavior may have changed).
- If breakingChanges is non-empty, inform the user: "The repository structure has changed. I've refreshed my understanding of [specific changes from breakingChanges array]."

**When to bump version:** See [docs/architecture.md](docs/architecture.md) → Version Management. MAJOR for orchestration/behavior changes; MINOR for new frameworks, rules, or eval changes.

---

## Debugging

**If the agent seems stuck or wrong:**

1. **Current state:** Infer from last user message and conversation. The agent should be able to say e.g. "We're in product_sense; we're doing braindump."
2. **Exit criteria:** For product_sense → execution_mode, confirm braindump sufficient per [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md) and eval functions (reference only; see [MEMORY.md](MEMORY.md) → Rules/Evals for path; don't duplicate checklist).
3. **Manual override:** User can say "Switch to execution_mode" or "Go to template finder"; agent acknowledges and follows.
4. **Log the failure:** Note what went wrong; update [ORCHESTRATION.md](ORCHESTRATION.md) if it's a pattern; consider running Level 2 eval.

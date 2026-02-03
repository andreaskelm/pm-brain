# Eval Functions - Agent Behavior Instrumentation

**What this file is:** Structured checks that the agent can use to evaluate its own behavior against scenario success_indicators and failure_modes. These functions help detect when the agent violates the golden rule or drifts into bad behavior patterns.

**How to use:** The agent should call these checks at key transition points (before suggesting frameworks, after user responses, at mode transitions). Results are logged for pattern detection, not blocking.

---

## Core Eval Functions

### check_braindump_sufficient()

**When to call:** Before transitioning from `product_sense_mode` to `execution_mode` (before suggesting any framework or template).

**What to check:** Verify that the "braindump sufficient" checklist from `PRODUCT-SENSE-RULES.md` is met:

1. **Assumptions named:** Has the user explicitly stated assumptions? (Look for phrases like "I'm assuming...", "I think...", "My hypothesis is...")
2. **Know vs guess separated:** Has the user distinguished facts from guesses? (Look for phrases like "I know...", "I'm guessing...", "The data shows...", "I believe...")
3. **Risk/second-order effect:** Has the user mentioned at least one risk, edge case, or second-order effect? (Look for phrases like "What if...", "One risk is...", "And then what...", "This could lead to...")
4. **Uncomfortable thought:** Has the user surfaced something challenging or uncomfortable? (Look for phrases like "What worries me...", "I'm concerned about...", "The hard part is...", "What makes me uncomfortable...")

**Implementation:**
- Scan the conversation history for explicit mentions of each checklist item
- If any item is missing, ask a specific verification question before transitioning
- Log which items were found/missing for pattern detection

**Example verification prompts:**
- "Before we structure this, let me check: What assumptions are you making about [X]?"
- "What's one thing that could go wrong if this works?"
- "What makes you uncomfortable about this approach?"

**Success criteria:** All 4 checklist items have explicit answers before framework suggestion.

---

### check_questions_before_framework()

**When to call:** Before suggesting any framework or template (in both `product_sense_mode` and `execution_mode`).

**What to check:** Count how many clarifying questions were asked before suggesting a framework.

**Success indicators:**
- At least 3-5 open-ended questions asked before framework suggestion
- Questions probe assumptions, not just validate
- Questions are situation-specific (from `2-product-sense-prompts.md`)

**Failure modes:**
- Framework suggested in first or second message
- Only yes/no or multiple-choice questions
- Generic questions that could apply to anything
- No questions asked before framework

**Implementation:**
- Count questions asked in current conversation
- Categorize question type (open-ended vs closed, probing vs validating)
- Check if questions reference prompts from `2-product-sense-prompts.md`
- Log count and quality for pattern detection

**Alert threshold:** If < 3 questions asked before framework suggestion, log warning.

---

### match_scenario_type()

**When to call:** At the start of `product_sense_mode` or when user's request matches a known pattern.

**What to check:** Identify which scenario from `agent-behavior-scenarios.json` matches the current conversation.

**Scenarios to match:**
- `vague_product_idea_001` - User says "I want to build X"
- `conflicting_stakeholders_002` - User mentions conflicting priorities
- `framework_selection_003` - User asks "how do I structure X?"
- `premature_solution_004` - User jumps to solution without problem definition
- `defensive_user_009` - User says "I already know, just help me write the doc"
- `overwhelm_paralysis_010` - User says "I'm stuck" or "too many things"

**Implementation:**
- Match user's initial prompt to scenario patterns
- Load scenario's `success_indicators` and `failure_modes`
- Use these as a checklist during the conversation
- Log which scenario matched and whether success indicators were met

**Example:** If user says "I want to build an app for remote teams" → match `vague_product_idea_001` → ensure agent asks about specific problem, target users, existing tools before suggesting PRD.

---

### check_golden_rule_violation()

**When to call:** Continuously during conversation, especially at mode transitions.

**What to check:** Detect violations of the golden rule: "Braindump before structure."

**Violation patterns:**
- Framework suggested before any braindump prompts
- Template opened before user has done any thinking
- Agent validates user's idea without challenging assumptions
- Agent fills in template boxes without user's insights

**Implementation:**
- Track conversation flow: braindump prompts → user responses → framework suggestion
- Flag if framework appears before sufficient braindump
- Check if agent is asking questions vs. providing answers

**Alert:** Log violation with context (what was suggested, what stage conversation was at).

---

## Eval Checkpoints

### Checkpoint 1: Entry to product_sense_mode

**When:** User starts a product-related conversation.

**Checks:**
1. Call `match_scenario_type()` to identify scenario
2. Verify agent adopts persona from `0-start-here-product-thinking.md`
3. Verify agent asks context check question (company/strategy/research/initiatives)
4. Verify agent does NOT suggest framework in first message

**Log:** Scenario type matched, persona adopted, questions asked.

---

### Checkpoint 2: During braindump loop

**When:** After each user response in `product_sense_mode`.

**Checks:**
1. Call `check_questions_before_framework()` - ensure questions are being asked
2. Verify questions are from `2-product-sense-prompts.md` for relevant situation
3. Verify questions probe assumptions, not just validate
4. Check if user's responses indicate braindump is progressing

**Log:** Question count, question quality, braindump depth indicators.

---

### Checkpoint 3: Before mode transition (product_sense → execution)

**When:** Agent is considering suggesting a framework.

**Checks:**
1. Call `check_braindump_sufficient()` - verify checklist is met
2. If checklist not met, ask verification questions before transitioning
3. Call `check_questions_before_framework()` - ensure enough questions were asked
4. Verify framework matches user's situation and braindump insights

**Log:** Checklist status, question count, framework match quality.

---

### Checkpoint 4: Template finder path

**When:** User explicitly asks to write/draft/fill a specific doc.

**Checks:**
1. For non-trivial docs (PRD, Strategy, Opportunity Assessment, Roadmap), verify preflight prompts are asked
2. Check if preflight prompts probe "why this, why now?" and "what do you know vs guess?"
3. Verify agent doesn't skip to template without preflight for non-trivial docs

**Log:** Doc type, preflight asked (yes/no), preflight quality.

---

## Logging and Pattern Detection

**Where to log:** `.cursor/evals/eval-results/` directory (see [eval-results/README.md](eval-results/README.md) for log format).

**Log format:**
```markdown
# Eval Log - [Date] - [Conversation ID]

## Scenario Matched
- Type: vague_product_idea_001
- Initial prompt: "I want to build an app for remote teams"

## Checkpoints

### Entry (product_sense_mode)
- ✅ Persona adopted
- ✅ Context check asked
- ✅ No framework in first message

### Braindump Loop
- Questions asked: 4
- Question quality: High (probed assumptions)
- Braindump depth: Medium

### Before Transition
- Braindump sufficient: ❌ (missing: uncomfortable thought)
- Questions before framework: 4
- Verification asked: ✅

### Framework Suggestion
- Framework: PRD
- Match quality: High
- Based on braindump: ✅

## Issues Found
- None

## Pattern Detection
- Agent asked good questions but transitioned before uncomfortable thought surfaced
```

**Pattern detection queries:**
- "Agent keeps jumping to templates in scenario X"
- "Braindump sufficient checklist rarely met before transition"
- "Preflight prompts skipped for non-trivial docs"

---

## Integration Points

**Files that should call these evals:**

1. **AGENTS.md** - Add eval checkpoints at mode transitions
2. **.cursor/rules/product-sense.mdc** - Call evals during braindump loop
3. **.cursor/rules/template-finder.mdc** - Call evals before template access
4. **0-start-here-product-thinking.md** - Reference eval functions in workflow

**Note:** These evals are **non-blocking**. They log issues for pattern detection but don't prevent the agent from continuing. The goal is visibility, not enforcement (enforcement happens through improved instructions).

---

## Success Metrics

**Track over time:**
- % of conversations where braindump sufficient checklist is met before framework
- Average questions asked before framework suggestion
- % of non-trivial docs where preflight prompts are asked
- Most common failure modes detected

**Goal:** Improve these metrics over time by updating instructions based on eval findings.

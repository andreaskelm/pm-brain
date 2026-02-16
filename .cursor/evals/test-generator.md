## Eval Test Generator - PM Brain

**What this file is:** A guide for generating lightweight, realistic test conversations for the Level 2 (agent behavior) eval system in `.cursor/evals/`. It helps you turn the scenarios in `agent-behavior-scenarios.json` into concrete test cases and log files in `eval-results/`.

This is intentionally **manual and guidance-based** (no scripts). You use it to:
- Design test conversations
- Specify expected behavior at key checkpoints
- Log pass/fail outcomes in `eval-results/`
- Feed patterns back into `AGENTS.md`, `ORCHESTRATION.md`, and `.cursor/rules/`

For how evals fit into the system overall, see:
- `.cursor/evals/README.md`
- `.cursor/evals/eval-functions.md`
- `.cursor/evals/eval-results/README.md`
- `ORCHESTRATION.md` → Eval Checkpoints

---

## 1. Test Case Structure

Each **test case** corresponds to one scenario from `agent-behavior-scenarios.json` (e.g. `vague_product_idea_001`) and lives in `eval-results/` as a markdown file.

**File naming (recommended):**
- `test-[scenario_id]-2026-02-04-01.md`
- Example: `test-vague_product_idea_001-2026-02-04-01.md`

**Each test file should include:**

1. **Header**
   - Scenario id
   - Date
   - Short description
2. **Conversation Script**
   - Alternating `User:` / `Agent:` turns
   - Keep it short and focused (5–15 turns)
3. **Checkpoint Expectations**
   - Which eval functions apply (from `eval-functions.md`), e.g.:
     - `check_questions_before_framework`
     - `check_braindump_sufficient`
     - `match_scenario_type`
     - `check_golden_rule_violation`
   - What “good” behavior looks like at each checkpoint, tied to:
     - `success_indicators` / `failure_modes` in `agent-behavior-scenarios.json`
     - Checkpoints in `eval-functions.md`
4. **Outcome Section**
   - Space to record whether a real run of the agent **passed** or **failed**
   - Notes on what went wrong or worked well

You can copy the pattern from the seeded test files in `eval-results/` and adapt.

---

## 2. How to Generate New Tests

Use this checklist when you want to add more test cases.

1. **Pick a scenario**
   - Open `.cursor/evals/agent-behavior-scenarios.json`
   - Choose one `scenario_id` (e.g. `framework_selection_003`)

2. **Write a realistic conversation**
   - Start from the scenario’s `initial_prompt`
   - Imagine how a real user would continue (confusions, constraints, pushes)
   - Keep to **one main behavior pattern** per test (e.g. “agent jumps to template too fast”)

3. **Annotate expected behavior**
   - For this scenario, skim its `success_indicators` and `failure_modes`
   - For each major section of the conversation, write:
     - What the **agent should do** (success)
     - What would count as a **clear failure**
   - Tie expectations to specific functions from `eval-functions.md` where applicable.

4. **Save the test file**
   - Put it in `.cursor/evals/eval-results/`
   - Use the `test-[scenario_id]-YYYY-MM-DD-XX.md` naming pattern

5. **(Optional) Run it with the agent**
   - Replay the user turns with the real agent
   - Compare the actual responses to the **Expected behavior** section
   - Record pass/fail and notes in the same file (see below)

---

## 3. Seeded Scenario Families

The initial set of tests should cover at least these scenario families (from `agent-behavior-scenarios.json`):

- **Vague product ideas / premature solutions**
  - `vague_product_idea_001`
  - `premature_solution_004`
- **Stakeholder and complex tradeoffs**
  - `conflicting_stakeholders_002`
  - `complex_tradeoff_005`
- **Framework and structure selection**
  - `framework_selection_003`
  - `first_time_roadmap_006`
  - `metrics_confusion_007`
- **Research and discovery**
  - `user_research_planning_008`
- **Tricky interaction patterns**
  - `defensive_user_009`
  - `overwhelm_paralysis_010`

For each scenario family, aim for **3–5 test cases** over time. Start small (1–2 per scenario) and grow as you discover real failure modes.

---

## 4. Using Tests with the Agent

To actually use these tests to evaluate the agent:

1. **Pick a test file**
   - From `.cursor/evals/eval-results/test-[scenario_id]-*.md`

2. **Replay the conversation**
   - Paste each `User:` line into the agent one by one
   - After each agent reply, compare with the **Expected behavior** notes

3. **Record outcomes**
   - In the same test file, fill in an **Eval Run** section:

   ```markdown
   ## Eval Run - 2026-02-04

   **Result:** [PASS / FAIL / MIXED]  
   **Notes:**  
   - [What matched expectations]  
   - [Where it diverged]  
   - [Which success_indicators / failure_modes were hit]
   ```

4. **Feed patterns back into the repo**
   - When you see a recurring failure (e.g. “keeps suggesting templates too early”):
     - Use `.cursor/evals/1-agent-behavior-guide.md` → “Where to update” map
     - Update `AGENTS.md`, `ORCHESTRATION.md`, or relevant `.cursor/rules/*.mdc`
     - If behavior changes meaningfully, bump `version.json` (see `docs/architecture.md` → Version Management)

---

## 5. Example Test Skeleton

Here is a minimal example you can copy into a new file in `eval-results/`:

```markdown
# Test - vague_product_idea_001 - 2026-02-04-01

**Scenario:** vague_product_idea_001  
**Date:** 2026-02-04  
**Description:** User has a vague idea for an app for remote teams.

## Conversation Script (Ideal)

User: I want to build an app for remote teams.  
Agent: [Asks clarifying questions about specific problem, for whom, and existing tools; does **not** mention templates or frameworks yet.]  
... (continue for ~5–10 turns)

## Expected Behavior (Checkpoints)

- `match_scenario_type`: correctly matches `vague_product_idea_001`
- `check_questions_before_framework`:
  - At least 3–5 open-ended questions before any framework is mentioned
  - No template or framework names in the first reply
- `check_golden_rule_violation`:
  - No template or structure suggested before sufficient braindump

## Eval Run - [fill in after running with real agent]

**Result:** [PASS / FAIL / MIXED]  
**Notes:**  
- ...
```

Use the seeded tests in this directory as concrete, filled-out examples.


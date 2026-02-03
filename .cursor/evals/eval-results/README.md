# Eval Results - Agent Behavior Logs

**What this directory is:** Logs of agent behavior evaluations for pattern detection and improvement tracking.

**How to use:** Agent (or you) can append eval results here to track behavior over time and identify patterns.

---

## Log File Format

Create one log file per conversation or eval session. Use this format:

```markdown
# Eval Log - [Date] - [Conversation ID or Brief Description]

**Date:** YYYY-MM-DD  
**Conversation Type:** [product_sense / execution_mode / template_finder]  
**User Request:** [Brief description of what user asked]

## Scenario Matched
- Type: [scenario_id from agent-behavior-scenarios.json]
- Initial prompt: "[user's initial request]"

## Checkpoints

### Entry (product_sense)
- ✅/❌ Persona adopted
- ✅/❌ Context check asked
- ✅/❌ No framework in first message
- Questions asked before framework: [count]

### Braindump Loop
- Questions asked: [count]
- Question quality: [High/Medium/Low]
- Braindump depth: [Deep/Medium/Shallow]
- Prompts used: [list key prompts]

### Before Transition
- Braindump sufficient: ✅/❌
  - Assumptions named: ✅/❌
  - Know vs guess separated: ✅/❌
  - Risk/second-order mentioned: ✅/❌
  - Uncomfortable thought surfaced: ✅/❌
- Questions before framework: [count]
- Verification asked: ✅/❌

### Framework Suggestion
- Framework: [name]
- Match quality: [High/Medium/Low]
- Based on braindump: ✅/❌
- Preflight prompts asked: ✅/❌ (if template-finder path)

## Issues Found
- [List any issues: golden rule violations, premature transitions, etc.]

## Pattern Detection Notes
- [Any patterns noticed: e.g., "Agent asked good questions but transitioned before uncomfortable thought surfaced"]

## Success Indicators Met
- [List which success_indicators from scenario were met]

## Failure Modes Detected
- [List any failure_modes from scenario that occurred]
```

---

## Pattern Detection Queries

When reviewing logs, look for patterns:

- "Agent keeps jumping to templates in scenario X"
- "Braindump sufficient checklist rarely met before transition"
- "Preflight prompts skipped for non-trivial docs"
- "Questions asked before framework: consistently < 3"
- "Framework match quality: consistently Low"

---

## Usage

**For agents:** When eval checkpoints are hit, append results to a log file in this directory. Use format above.

**For manual logging:** After important conversations, create a log file using the format above.

**For pattern detection:** Review multiple log files to identify systemic issues, then update instructions in `AGENTS.md`, `ORCHESTRATION.md`, or `.cursor/rules/` based on findings.

---

## File Naming

Use descriptive names:
- `eval-2026-02-03-prd-creation.md`
- `eval-2026-02-03-prioritization-decision.md`
- `eval-2026-02-03-vague-product-idea.md`

Or use conversation IDs if available.

---

## Git Tracking

**Decision:** Should eval logs be tracked in git?

- **Track them:** Enables pattern detection over time, team can review agent behavior
- **Ignore them:** Keeps repo clean, logs are temporary

**Recommendation:** Add `*.md` to `.gitignore` in this directory if you don't want to track logs. Or track them if you want to review agent behavior over time.

---

## Success Metrics to Track

Over time, track these metrics across logs:

- % of conversations where braindump sufficient checklist is met before framework
- Average questions asked before framework suggestion
- % of non-trivial docs where preflight prompts are asked
- Most common failure modes detected
- Framework match quality trends

**Goal:** Improve these metrics over time by updating instructions based on eval findings.

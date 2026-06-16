# Eval Results

**What this directory is:** Local run output from the eval harness and optional manual review logs.

**Git:** Harness JSON (`*.json`) and self-critique queue files are **gitignored** — ephemeral local history, not repo content. Only `README.md` is tracked here.

---

## Harness output (JSON)

Automated runs write JSON here, then **auto-prune** to the newest 2 files per pattern (override with `--keep-results N` or env `PM_BRAIN_EVAL_KEEP=0` to disable):

| File pattern | Source |
|---|---|
| `{scenario_id}-{timestamp}.json` | `harness/run_scenario.py` (L2 behavior) |
| `rubric-regression-{timestamp}.json` | `harness/run_rubric_regression.py` (L1 rubric) |

Each payload includes `"dry_run": true|false`. On failure, assertions name `spec_owner` — edit that file, then re-run.

### This is not where learning lives

Harness JSON is **ephemeral test output** — like CI logs. It is gitignored and auto-pruned (keep 2 newest per pattern). Deleting or rotating these files does **not** lose learnings.

| What | Where learning actually persists |
|---|---|
| Spec fixes from eval findings | `AGENTS.md`, `pm-brain.mdc`, `ORCHESTRATION.md`, etc. |
| Human transcript reviews | `eval-results/YYYY-MM-DD-*.md` (optional; track in git if you want history) |
| Self-critique queue | `self-critique-queue-*.md` (not auto-pruned) |
| Your backlog from eval patterns | `TODO.md`, `5-Growth/` |

The agent does **not** read harness JSON to learn between conversations. It reads the spec files you update when something fails.

### Dry-run vs live

| Mode | What it tests | Needs Cursor CLI? |
|---|---|---|
| **`--dry-run`** (CI default) | Harness wiring, YAML parsing, structural checks | No — mock agent response |
| **Live** | Real agent behavior + LLM judges | Yes — see [platform-setup.md](../../../docs/platform-setup.md#cursor-cli-optional--live-evals) |

Dry-run passing means the **infrastructure** works, not that the agent behaves correctly.

---

## Self-critique queue

The stop hook (`trigger-self-critique.js`) appends to:

- `self-critique-queue-YYYY-MM-DD.md`

Agent reads the queue, applies `judges/self_critique_coaching.md`, writes report, and **drafts** spec edits (human applies in v1).

---

## Canonical Eval Log Format

Every eval result file MUST follow this structure. Use this template for new evals. Sections are in fixed order — include all of them, even if a section is "N/A" or brief.

```markdown
# Eval Log — [YYYY-MM-DD] — [Brief Description]

**Date:** YYYY-MM-DD
**Conversation Type:** [product_sense / execution_mode / meta_reflection / mixed — list transitions]
**User Request:** [Brief description of what the user asked]
**Platform:** [VS Code + GitHub Copilot / Cursor / Claude Code / other]

├──

## Scenario Matched

[Which scenario_id from agent-behavior-scenarios.json best matches → If none, note "no exact match" and name the closest analog + whether a new scenario should be added.]

├──

## Dimension Scores

| Dimension | Rating | Notes |
|---|---|---|
| Questioning quality | [Strong / Good / Medium / Weak] | [1-2 sentence justification] |
| Perspective taking | [Strong / Good / Medium / Weak] | [1-2 sentence justification] |
| Framework fit | [Strong / Good / Medium / Weak / N/A] | [1-2 sentence justification] |
| Artifact clarity | [Strong / Good / Medium / Weak / N/A] | [1-2 sentence justification] |
| Guidance quality | [Strong / Good / Medium / Weak] | [1-2 sentence justification] |
| User agency | [Strong / Good / Medium / Weak] | [1-2 sentence justification] |

├──

## What Worked Well

[2-5 bullet points. Each should name a specific moment or pattern, not generic praise. Say WHY it worked, not just THAT it worked.]

├──

## What Needs Improvement

[2-5 bullet points. Each should name the specific miss, what should have happened, and — critically — the structural root cause (not just "agent didn't follow the rule"). Apply the Root Cause Quality Check from 1-agent-behavior-guide.md §5.]

├──

## Pattern Detection Notes

[Patterns confirmed from prior evals, new patterns identified, new failure modes. Reference prior eval files by name when a pattern recurs.]

├──

## Assertions Met

[Checklist: ✅ / ❌ for each relevant structural and content assertion from the matched scenario's `expected.yaml`. If no scenario matched, list the key behavioral checks from [behavior-assertions.md](../behavior-assertions.md) and score them.]

├──

## Files to Update

| What to change | Where (file path) | Priority | Status |
|---|---|---|---|
| [Description of fix] | [File path] | [High / Medium / Low] | [Open / Done YYYY-MM-DD] |

[Use "Done" with date when a fix has been implemented. This makes it possible to audit which eval recommendations were actioned.]
```

---

## Notes on the Format

**Why fixed sections:** Earlier evals used inconsistent structures (some had "Checkpoints" sections, some had "Key Findings", some had "Eval Findings"). The fixed structure makes it possible to scan across evals for patterns without re-learning each file's layout.

**Dimension Scores are mandatory.** Even for sessions where some dimensions don't apply (e.g. no framework in a reflection session), rate them "N/A" with a note — don't skip the row.

**Root cause quality matters.** In "What Needs Improvement", always ask: "Why was this structurally likely?" — not just "what happened." See [1-agent-behavior-guide.md](../1-agent-behavior-guide.md) §5.

**Files to Update tracks implementation.** Mark fixes as "Done" with a date when implemented. During eval review sessions, scan this column across all evals to find unresolved recommendations.

---

## Pattern Detection Queries

When reviewing logs, look for patterns:

- "Agent keeps jumping to templates in scenario X"
- "Braindump sufficient checklist rarely met before transition"
- "Preflight prompts skipped for non-trivial docs"
- "Questions asked before framework: consistently < 3"
- "Framework match quality: consistently Low"
- "Same structural root cause appearing across multiple evals"

**For agents:** When eval checkpoints are hit, append results to a log file in this directory. Use format above.

**For manual logging:** After important conversations, create a log file using the format above.

**For pattern detection:** Review multiple log files to identify systemic issues, then update instructions in `AGENTS.md`, `../ORCHESTRATION.md`, or `../EVALUATION.md` based on findings.

---

## File Naming

Use: `YYYY-MM-DD-brief-description.md`

Examples from actual evals:
- `2026-03-27-week-wrap-reflection-and-learning-capture.md`
- `2026-03-23-stakeholder-avatar-refactoring.md`
- `2026-03-13-user-research-planning.md`

---

## Git tracking (manual logs only)

Harness JSON never belongs in git. For manual transcript review logs:

- **Track them** if you want shared pattern detection over time
- **Ignore them** if logs are personal scratch — add `*.md` to this folder's `.gitignore` (except `README.md`)

---

## Success Metrics to Track

Over time, track these metrics across logs:

- % of conversations where braindump sufficient checklist is met before framework
- Average questions asked before framework suggestion
- % of non-trivial docs where preflight prompts are asked
- Most common failure modes detected
- Framework match quality trends

**Goal:** Improve these metrics over time by updating instructions based on eval findings.

# Behavior Assertions — Principle → Observable Output

Maps each [AGENTS.md](../../AGENTS.md) invariant principle to testable pass/fail criteria. Use with [1-agent-behavior-guide.md](1-agent-behavior-guide.md) and scenarios in [agent-behavior-scenarios.json](agent-behavior-scenarios.json).

**Harness scenarios:** Executable scenarios live under `system/evals/scenarios/behavior/`. Each `expected.yaml` assertion includes a `spec_owner` field pointing at the file that owns the behavior.

---

## Principle 1: Think first, always

**Observable:** Agent asks questions before structure; user's read requested before content analysis.

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `vague_product_idea_001` | ≥2 braindump questions before any framework named | Framework or template in first response |
| `novel_framework_build_012` | Continues questioning when braindump incomplete | Suggests artifact creation mid-braindump |
| `defensive_user_009` | ≥2 preflight questions before loading template (non-trivial doc) | Starts filling template with zero questions |
| `transcript_to_artifact_013` | Asks user's takeaways before analyzing repo file they pointed at | Analyzes file without asking user's read first |

---

## Principle 2: Minimal footprint / SSoT

**Observable:** Agent links or updates existing structure; does not create duplicate files.

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `transcript_to_artifact_013` | Checks existing content before writing; updates in place when possible | Creates new file when existing structure fits |
| `end_of_week_wrap_011` | Links to external or existing doc for raw data | Embeds full duplicate of content already elsewhere |

---

## Principle 3: Challenge before validate

**Observable:** Agent names assumptions, risks, or uncomfortable thoughts; does not only affirm.

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `premature_solution_004` | Prompts user to separate know vs guess | Validates plan without naming assumptions |
| `conflicting_stakeholders_002` | ≥1 follow-up when user surfaces self-insight mid-session | Switches to implementation without follow-up |

---

## Principle 4: PJT trigger

**Observable:** Decision + confidence level → immediate PJT offer.

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `pjt_trigger_001` | Offers forecast log when confidence stated | Decision logged without PJT offer |
| `end_of_week_wrap_011` | PJT exit checklist on meta_reflection close | Closes reflection without PJT checklist |

---

## Principle 5: Check filesystem before asking user

**Observable:** Agent lists/reads repo before asking whether context exists.

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `transcript_to_artifact_013` | Checks avatar/org context before asking user to explain named org | Asks user to explain org that exists in repo |
| `end_of_week_wrap_011` | Lists initiative folder before asking what's in it | Asks user what's in initiative without checking |

---

## Principle 6: Layer 1 identity

**Observable:** Intent, assumptions, success criteria surfaced before execution artifacts.

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `transcript_to_artifact_013` | Clarifying questions on intent/scope before structuring transcript | Structures transcript with no intent questions |
| `complex_tradeoff_005` | Artifact draft includes named assumptions or explicit non-scope | Template filled with no assumptions section |

---

## Coaching Lenses (cross-cutting)

**Observable:** Lens named in passing when shaping a question.

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `premature_solution_004` | Names bias type when pattern detected | Addresses substance without naming bias |
| `vague_product_idea_001` | Pulls back to outcome when user is output-heavy | Helps build feature without outcome check |

---

## Bootstrap Compliance

| Scenario ID | Pass | Failure |
|-------------|------|---------|
| `vague_product_idea_001` | Reads full bootstrap set (AGENTS.md + pm-brain.mdc + system/MEMORY.md) before substantive response | Responds without loading bootstrap set |
| `framework_selection_003` | Full read of AGENTS.md (not capped partial) | Partial read misses principles/lenses |

---

## Calibrated harness scenarios (01–02)

Scenarios **01** and **02** have structural + content judges in `expected.yaml`. Listed in [agent-behavior-scenarios.json](agent-behavior-scenarios.json) for discovery and stub generation.

| Scenario ID | Purpose | spec_owner |
|-------------|---------|------------|
| `braindump_floor_gate_001` | No artifact before braindump sufficiency | `.cursor/rules/pm-brain.mdc` |
| `pjt_trigger_001` | Unconditional PJT offer when decision + confidence stated | `AGENTS.md` |

Scenarios **03–15** have partial structural checks; see each folder's `expected.yaml` and principle tables above.

---

## Where to Update on Failure

| Failure type | Update |
|--------------|--------|
| Principle violation | [AGENTS.md](../../AGENTS.md) |
| Routing / state / context loading | [system/ORCHESTRATION.md](../ORCHESTRATION.md) |
| Wake triggers | [system/MEMORY.md](../MEMORY.md) |
| Deep coaching process | [system/coaching/](../coaching/) |
| Always-on lenses / braindump floor | [.cursor/rules/pm-brain.mdc](../../.cursor/rules/pm-brain.mdc) |

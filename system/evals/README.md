# PM Brain Evals

How you find out whether the coach still behaves like the coach — after a rules edit, a model change, or a new skill. One file: what runs, what's covered, how to review a real transcript, and where to fix things when they break.

Maintainer notes (fork policy, CI): [docs/evals-fork.md](../../docs/evals-fork.md). Artifact quality rubrics are a different thing — see [../EVALUATION.md](../EVALUATION.md).

---

## What runs where

| Tier | What | Command | Runs in CI |
|---|---|---|---|
| **L0** | Repo health — broken links, encoding corruption, scenario files point at real inputs/judges/rubrics | `python system/evals/checks/verify-markdown.py` | Yes |
| **L4** | In-turn write gate — blocks template scaffolds in `3-Work/` without thinking markers | `python system/evals/harness/checks/test_hook_validator.py` (unit tests); live via `.cursor/hooks.json` | Yes (tests) |
| **L2** | Live behavior scenarios — real agent, multi-turn, structural checks + LLM judges | `python system/evals/harness/run_scenario.py <scenario-dir>` | No — needs the Cursor CLI |
| **L1** | Rubric regression — does a criteria file PASS a good specimen and FAIL a bad one? | `python system/evals/harness/run_rubric_regression.py --all` | No — needs the Cursor CLI |
| **L3** | Human transcript review | [Reviewing a real conversation](#reviewing-a-real-conversation) below | — |

**Be honest about what CI proves:** L0 and L4 are real checks. Behavior is only tested by live L2 runs. A `--dry-run` returns a mock response — it tests harness wiring, nothing about the agent. Run live L2 after any edit to `AGENTS.md`, a skill, or after switching models.

```bash
pip install -r system/evals/requirements.txt
python system/evals/checks/verify-markdown.py
python system/evals/harness/checks/test_hook_validator.py

# Live (Cursor CLI installed + authenticated — see docs/platform-setup.md#live-evals-optional)
python system/evals/harness/run_all.py                    # all behavior scenarios
python system/evals/harness/run_scenario.py system/evals/scenarios/behavior/03-voice-check --runs 3
```

Env: `PM_BRAIN_CURSOR_BIN` (default `cursor-agent`), `PM_BRAIN_TURN_MODEL`, `PM_BRAIN_JUDGE_MODEL`. Judges are mid-tier work — pin a mid-tier model to keep cost down ([model tiers](../../docs/platform-setup.md#model-tiers)). Results go to `eval-results/` (gitignored, auto-pruned) — see [eval-results/README.md](eval-results/README.md).

---

## Behavior scenarios

Each folder in `scenarios/behavior/` is self-describing: `README.md` (what and why), `expected.yaml` (assertions), `inputs/turn-NN-user.md` (one per turn). Multi-turn scenarios carry the full prior conversation into each turn, and judges see it too.

| # | Scenario | What it guards | Failure → edit |
|---|---|---|---|
| 01 | [braindump-floor-gate](scenarios/behavior/01-braindump-floor-gate/README.md) | "Write my PRD" → preflight questions, no file in `3-Work/` | AGENTS.md → Golden Rule |
| 02 | [forecast-trigger](scenarios/behavior/02-forecast-trigger/README.md) | Decision + confidence → offer to log it | AGENTS.md → Principle 5 |
| 03 | [voice-check](scenarios/behavior/03-voice-check/README.md) | Voice against the "Voice in action" samples; pushback on an adoption assumption | AGENTS.md → Voice |
| 04 | [premature-execution](scenarios/behavior/04-premature-execution/README.md) | Half-met braindump floor → keep coaching, no artifact offer | AGENTS.md → Golden Rule; [coaching/](../coaching/README.md) |
| 05 | [self-insight-mid-execution](scenarios/behavior/05-self-insight-mid-execution/README.md) | User reveals a pattern mid-task → one follow-up before carrying on | AGENTS.md → Principle 8 |
| 06 | [coaching-in-main-thread](scenarios/behavior/06-coaching-in-main-thread/README.md) | Stakeholder simulation (subagent allowed) still gets a coaching layer; decision stays with user | AGENTS.md → Delegation |

Judges live in `judges/` — one file per behavior, each ending in a single `VERDICT: PASS|FAIL|UNCERTAIN — reason` line.

### Adding a scenario

Add one when a real conversation goes wrong in a way that will recur. Model it on the actual transcript (strip company details). Create `scenarios/behavior/NN-slug/` with:

```yaml
scenario_id: slug_001            # unique; L0 checks it
description: |
  What the user does and what the agent must / must not do.
pass_threshold: { structural: 1.0, content: 0.8 }
turns:
  - turn: 1
    input: turn-01-user.md       # in inputs/
    structural:                  # deterministic, cheap
      - type: question_count_at_least
        arg: 2
        spec_owner: AGENTS.md    # the file to edit when this fails
    content:                     # LLM judge
      - judge: my_judge
        rubric: judges/my_judge.md
        spec_owner: AGENTS.md
        expected_meaning: "What a passing reply does"
        must_not: "The specific failure"
final_state:
  structural: []                 # checked against the whole run (e.g. all_internal_links_valid)
```

Structural types (see `harness/checks/structural.py`): `question_count_at_least`, `response_contains`, `response_not_contains`, `response_not_links_template`, `file_exists`, `file_exists_glob`, `file_not_created_glob`, `file_modified`, `file_modified_or_created`, `decision_logged`, `all_internal_links_valid`, `no_duplicate_content`.

Keep the set small. Six scenarios you actually run beat fifteen stubs you don't.

### Rubric scenarios

`scenarios/rubric/<slug>/` — `expected.yaml` with `type: rubric_regression`, a `rubric_path`, and `fixtures/good.md` + `fixtures/bad.md`. Use when you change a criteria file and want to know it still discriminates. One folder per rubric you actively maintain.

---

## Reviewing a real conversation

Use after an important session, or when something felt off. Paste the transcript into a fresh chat with: *"Review this PM Brain session against system/evals/README.md → Reviewing a real conversation. For each finding: what happened, why it was structurally likely, which file to edit."*

**Dimensions** — what good and bad look like:

| Dimension | Green | Red |
|---|---|---|
| **Questioning** | Open, situation-specific questions that surface hidden assumptions before solutions | Yes/no or leading questions; interrogation; generic questions that fit anything |
| **Perspective** | Surfaces stakeholders, edge cases, second-order effects; challenges framing constructively | Only reinforces the user's first framing; misses obvious stakeholders |
| **Framework fit** | Context before framework; explains why this one; knows when *not* to use one | Template forcing; framework before the problem is understood |
| **Voice** | Prose, experience-led, specific, honest, invites dialogue | Bullet walls, corporate filler, sign-offs, sugarcoating |
| **Guidance** | Scaffolds without taking over; pushes on fuzzy thinking; adapts to level | Does the thinking for the user; patronizing; no pushback |
| **User agency** | User makes the call; learns something transferable | Agent decides; user goes passive |
| **Artifact clarity** | Specific, actionable, carries real sentences from the braindump | Generic; doesn't reflect the thinking; no next steps |

**Checklist:**

- [ ] Read `AGENTS.md` (and `USER.md`) before the first reply — including on resumed sessions?
- [ ] Right state? Thinking aloud → coaching; doc request → preflight, then the matching skill.
- [ ] Braindump floor met (assumptions, know vs. guess, a risk, an uncomfortable thought) before any structure?
- [ ] Lenses named in passing when used?
- [ ] Checked the repo (avatars, `1-Context/`, `5-Growth/decisions.md`) before asking the user?
- [ ] Decision + confidence → logging offered in the same reply?
- [ ] Self-insight mid-task → one follow-up?
- [ ] Coaching stayed in the main thread; subagents only fetched, reviewed, or simulated?
- [ ] Did it sound like the "Voice in action" samples?

### Where to update

| If you see… | Edit… |
|---|---|
| Jumps to template, weak questions, premature artifact | [AGENTS.md](../../AGENTS.md) → Golden Rule; [coaching/](../coaching/README.md) |
| Voice drift — flat, corporate, bullet-heavy | [AGENTS.md](../../AGENTS.md) → Voice; then re-run scenario 03 |
| Lens never fires, or fires as a lecture | [AGENTS.md](../../AGENTS.md) → Coaching Lenses |
| Wrong state, wrong load, wrong routing | [ORCHESTRATION.md](../ORCHESTRATION.md) |
| Wrong or no framework | Matching skill in `.claude/skills/`; [2-Methods/0-index.md](../../2-Methods/0-index.md) |
| Artifact quality checks missing or wrong | [EVALUATION.md](../EVALUATION.md); the skill's `references/criteria.md` |
| Subagent took over coaching, or wrong subagent | [AGENTS.md](../../AGENTS.md) → Delegation; `.claude/agents/` |
| Personal preference (tone, format, language) | [USER.md](../../USER.md) — not the shared rules |

### Root-cause quality bar

"The agent didn't follow the rule" is a symptom, not a root cause. For each finding ask: **why was this structurally likely?** And: **would the fix prevent recurrence, or just name it?** A new "don't skip X" line rarely fixes a routing gap.

| Observed | Structural cause to check |
|---|---|
| Recurring miss despite a rule existing | Is the trigger a judgment call (fragile) or a named event (reliable)? Make it a named event. |
| Rule ignored on long sessions | Is it buried? Rules near the top of AGENTS.md survive context pressure better. |
| Skill not used | Is the skill's `description` specific enough to match how the user actually phrases the request? |
| Rule landed in the wrong file | Universal behavior → AGENTS.md. Routing → ORCHESTRATION.md. Personal → USER.md. Procedure → the skill. |

When a finding recurs, turn it into a scenario.

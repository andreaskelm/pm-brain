# Evals — Maintainer Guide

Everything about running and extending evals lives in [system/evals/README.md](../system/evals/README.md). This page covers what's specific to maintaining the repo: CI, and how evals interact with forks.

---

## CI

[`.github/workflows/evals.yml`](../.github/workflows/evals.yml) runs on every PR and on push to `main`/`master`:

1. **L0** — `verify-markdown.py`: broken links, encoding corruption, and scenario consistency (every `expected.yaml` points at inputs, judges, and rubrics that exist; no duplicate IDs or folder prefixes).
2. **L4** — `test_hook_validator.py`: unit tests for the write-gate hook.

That's deliberately all. Earlier versions also ran the behavior harness in `--dry-run` mode, but a mock agent response proves nothing about behavior — it was green regardless. **Behavior is only tested by live runs**, which need the Cursor CLI and cost tokens, so they run locally.

## When to run live evals

- After editing `AGENTS.md` — especially Voice, Golden Rule, or Principles
- After adding or changing a skill in `.claude/skills/`
- After switching the default model (or when the tier table in [platform-setup.md](platform-setup.md#model-tiers) changes)
- Before opening a PR to the public upstream

```bash
python system/evals/harness/run_all.py --runs 2
```

`--runs 3` on scenario 03 (voice) is worth it after any Voice edit — single runs are noisy.

## Behavior changes

Use the **Where to update** map in [system/evals/README.md](../system/evals/README.md#where-to-update). The short version: universal behavior → `AGENTS.md`; routing → `system/ORCHESTRATION.md`; procedure → the skill; personal preference → `USER.md`. When a real-session failure recurs, turn it into a scenario.

---

## Private fork merge policy

If you keep a **private fork** with company content:

```bash
git fetch upstream
git merge upstream/main
```

- **Eval docs, harness, scenarios, CI** — merge normally. If you customized the harness, review the diff before accepting upstream wholesale.
- **Personal content** (`1-Context/`, `3-Work/`, `4-Research/`, `5-Growth/`, `USER.md`) — keep yours on conflict (`git checkout --ours <file>`).
- **Scenarios built from real sessions** — strip company names, people, and numbers before contributing them upstream.

Older forks: see [legacy-migration.md](legacy-migration.md).

## Related

- [platform-setup.md](platform-setup.md) — wiring, model tiers, Cursor CLI for live evals
- [architecture.md](architecture.md) — how the pieces fit

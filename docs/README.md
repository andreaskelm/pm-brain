# PM Brain — Human Documentation

Human-facing docs for setup, architecture, and maintenance. **The agent does not load this folder at bootstrap** — behavior lives in [AGENTS.md](../AGENTS.md) and [USER.md](../USER.md). Individual docs here load **on demand** when a conversation needs them (see the wake table in AGENTS.md).

---

## Start here

| Doc | Audience | Purpose |
|-----|----------|---------|
| [setup.md](setup.md) | New users | Onboarding, who it's for, day-to-day loop, upkeep, 1–5 folders, privacy, first initiative |
| [platform-setup.md](platform-setup.md) | All users | AGENTS.md bootstrap + per-platform wiring (Cursor, Copilot, Claude Code, ChatGPT) |
| [principles.md](principles.md) | All users | Why the repo is designed this way — golden record, think-first, privacy |

---

## Reference

| Doc | Audience | Purpose |
|-----|----------|---------|
| [architecture.md](architecture.md) | Maintainers | Structure, loading, eval overview, linking conventions |
| [credits.md](credits.md) | Contributors | Framework attributions and external links |

---

## Fork maintainers

| Doc | Audience | Purpose |
|-----|----------|---------|
| [evals-fork.md](evals-fork.md) | Maintainers | Harness, CI, scenario hygiene, private-fork merge policy |
| [legacy-migration.md](legacy-migration.md) | Migrators | `00–04` → `1–5`, Meta→Growth split, 2026-10 AGENTS-only wiring |

---

## Related (outside `docs/`)

- **Agent bootstrap:** [AGENTS.md](../AGENTS.md) → [USER.md](../USER.md) (if present)
- **Routing detail:** [system/ORCHESTRATION.md](../system/ORCHESTRATION.md) (state entry, not bootstrap)
- **Workflows:** [2-Methods/0-index.md](../2-Methods/0-index.md) → [`.claude/skills/`](../.claude/skills/)
- **Eval harness:** [system/evals/README.md](../system/evals/README.md)
- **Repo overview:** [README.md](../README.md)

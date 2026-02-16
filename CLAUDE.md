# PM Brain — Claude Code Configuration

This file is read automatically by Claude Code on every conversation.

## Setup

1. Read [AGENTS.md](AGENTS.md) for persona and core principles.
2. Read [.cursor/rules/voice.mdc](.cursor/rules/voice.mdc) for communication style (on Cursor this auto-loads; here you must read it explicitly).
3. Read [ORCHESTRATION.md](ORCHESTRATION.md) for routing, state transitions, and context loading.
4. Read [version.json](version.json) for current version.
5. Follow the same state machine and layered context loading as defined in ORCHESTRATION.md.

## Key Differences from Cursor

- **No auto-loaded rules.** On Cursor, `.cursor/rules/` files load automatically. Here, read rule content from `.cursor/rules/` when MEMORY.md or ORCHESTRATION.md says to (e.g., voice rules, evaluation orchestration, product-sense rules).
- **No skills or slash commands.** Use the framework paths in `02-Methods-and-Tools/` directly. The skills in `.cursor/skills/` contain useful workflow guidance — read them when relevant.
- **File system access.** You can read all repo files directly. Use [MEMORY.md](MEMORY.md) to know what exists and when to load it.

## Context Management

- Use `/compact` when context grows heavy — this is Claude Code's built-in context compression.
- Follow the checkpoint protocol in [ORCHESTRATION.md](ORCHESTRATION.md) → Context Health for longer sessions.
- The `checkpoints/` folder is available for saving session state.

## Golden Rule

Braindump before structure. See [PRODUCT-SENSE-RULES.md](PRODUCT-SENSE-RULES.md). Never suggest frameworks until sufficient braindumping has happened.

## Reference

- **Persona:** [AGENTS.md](AGENTS.md)
- **Orchestration:** [ORCHESTRATION.md](ORCHESTRATION.md)
- **Sleeping memory:** [MEMORY.md](MEMORY.md)
- **Frameworks:** [02-Methods-and-Tools/README.md](02-Methods-and-Tools/README.md)
- **Full setup:** [docs/setup.md](docs/setup.md)

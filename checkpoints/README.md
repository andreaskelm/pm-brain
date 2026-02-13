# Checkpoints — Conversation State Management

Checkpoints save conversation progress so you can start fresh conversations without losing context. This prevents context rot (quality degradation in long AI conversations) and lets you resume work across sessions.

## How It Works

1. **Agent offers checkpoint** — based on heuristic triggers (heavy context loaded, state transitions, long conversations). See [ORCHESTRATION.md](../ORCHESTRATION.md) → Context Health.
2. **Agent creates a checkpoint file** — `session-YYYY-MM-DD-HHMM.md` in this folder with: current state, braindump summary, questions explored, framework candidates, next steps, and which context files were loaded.
3. **You start a fresh conversation** — clean context window means higher quality.
4. **You say "continue from checkpoints/session-[timestamp].md"** — the agent reads the checkpoint and picks up where you left off.

## When to Checkpoint

**Good times:** Before switching from braindump to artifact creation, when lots of context files are loaded, multi-day projects, or when conversation quality feels like it's dropping.

**Not needed:** Quick questions, short template fills, conversations under ~15 turns with minimal context loaded.

## Cleanup

Checkpoints are working files. Archive or delete them after work is completed, learning is captured in 00-Meta/, or the artifact is created. Keep only active checkpoints in this folder.

---

**Platform-agnostic.** Works on any AI platform — just text files, fresh conversations, and a reference to pick up from.

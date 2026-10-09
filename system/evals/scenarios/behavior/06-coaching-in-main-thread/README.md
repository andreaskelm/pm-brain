# Scenario 06 — Coaching Stays in the Main Thread

User asks for a stakeholder simulation. Delegating to the `stakeholder-simulator` subagent is allowed; handing the conversation over to it is not. Subagents return evidence; the main thread owns the coaching and the judgment call.

**Tests:** Delegation and Model Tiers (AGENTS.md), politics coaching, evidence-strength lens ("four deals a year" — is that documented or verbal?), decision stays with the user.

**spec_owner on failure:** [AGENTS.md](../../../../../AGENTS.md) → Delegation and Model Tiers; [stakeholder-simulator](../../../../../.claude/agents/stakeholder-simulator.md)

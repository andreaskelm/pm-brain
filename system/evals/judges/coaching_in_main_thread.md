# Judge: Coaching Stays in the Main Thread

The user asked for a stakeholder simulation. The agent may delegate the simulation to a subagent (`stakeholder-simulator`) or do it inline — either is fine. `AGENTS.md` → Delegation: subagents return evidence; the main thread owns the coaching and the judgment call.

## PASS if
- Reply contains the simulated reactions (or a clear synthesis of them)
- AND the agent then coaches on them in its own voice: which objection actually matters, what the user is underestimating, or what they'd change
- AND the final decision about what to change stays with the user (a question back, not a rewritten pitch)

## FAIL if
- Reply is only the raw simulation output, with no coaching layer on top
- Agent rewrites the pitch for the user without asking what they'd change
- Agent tells the user what to decide

## UNCERTAIN if
- Coaching layer is present but thin (one generic line after a long report)

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>

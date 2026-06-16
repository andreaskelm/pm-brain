# Judge: Preflight Before Template

Grade whether the agent asked preflight or braindump questions before suggesting or opening any template.

## PASS if
- Agent asks at least 2 clarifying questions about intent, assumptions, audience, or evidence
- Agent does NOT link to or name a specific template path in the first reply
- Agent signals think-first posture (braindump, preflight, or "before we structure")

## FAIL if
- Agent opens, links, or starts filling a template in the first reply
- Agent only acknowledges the request without questions
- Agent jumps to execution_mode artifacts immediately

## UNCERTAIN if
- Borderline: one weak question plus template mention

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>

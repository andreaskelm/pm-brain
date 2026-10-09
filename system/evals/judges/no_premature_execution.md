# Judge: No Premature Execution

The user is mid-braindump. The thinking is NOT complete against the braindump floor in `AGENTS.md` (named assumptions, know vs. guess, a risk or second-order effect, an uncomfortable thought). Grade whether the agent stays in the thinking.

## PASS if
- Agent keeps coaching: asks about whatever floor criterion is still missing (usually the risk or the uncomfortable thought)
- Agent may *name* that an artifact could come later, but does not propose drafting one now
- Agent reflects back what has been surfaced so far, so the user sees the gaps

## FAIL if
- Agent proposes or starts a PRD, one-pager, OKR, roadmap, or any template ("Want me to draft…", "Let's capture this in a PRD")
- Agent declares the thinking "solid" or "ready" while a floor criterion is clearly missing
- Agent summarizes into a structured artifact (headers, filled sections) instead of continuing the conversation

## UNCERTAIN if
- Agent asks good questions but also slips in an artifact offer at the end

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>

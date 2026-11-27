# Judge: Floor Quality

The user ticked every box of the braindump floor in `AGENTS.md`, but with fig-leaf content: the assumption ("users want a better dashboard") is one nobody disputes; the know/guess split is real but thin (an "ok" satisfaction score, no complaints); the risk is schedule, not whether the redesign changes anything; the "uncomfortable thought" ("might not be perfect at launch") is not uncomfortable. They ask for the PRD. Grade whether the agent sees through this and pushes on what actually decides the outcome, as `AGENTS.md` → Golden Rule requires.

## PASS if
- Agent says the content is safe or doesn't yet bite, and names why (not just "dig deeper")
- Agent identifies the assumption that would decide this (e.g. that a redesign changes what users do, or that an "ok" score is a problem worth solving) and asks for evidence or a first signal it is wrong
- Agent contrasts the fig-leaf risk or discomfort with a real one, or asks for the one the user is avoiding
- Agent does not write or offer to draft the PRD yet; it may say what the PRD would need once the thinking holds
- Tone is direct and in the coach's voice, not condescending

## FAIL if
- Agent accepts the floor as met and proposes or starts the PRD, a template, or a structured summary
- Agent only asks generic questions ("tell me more about users") without saying why the current answers are weak
- Agent praises the braindump as solid
- Agent lectures about frameworks instead of pushing on the specific content

## UNCERTAIN if
- Agent pushes back correctly on one weak item but leaves the others unremarked
- Agent pushes on the right thing but slips in an offer to draft at the end

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>

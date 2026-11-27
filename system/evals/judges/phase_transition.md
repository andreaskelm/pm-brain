# Judge: Phase Transition

The user's braindump already meets the braindump floor in `AGENTS.md` with real substance: a named, unchecked assumption (reps skip logging because of double entry; managers would use better data), an honest know-vs-guess split (55% is from the CRM report; two reps spoken to), a second-order risk (managers police call counts, reps game the calendar), and a genuine uncomfortable thought (the metric may have been handed to them via the director's QBR quote). They then ask to turn it into something for their director. Grade whether the agent recognises the thinking is done and moves on, per `system/ORCHESTRATION.md` (product_sense exit, then execution preflight).

## PASS if
- Agent says, in plain words, that there's enough to structure now (no internal state names)
- Agent picks up the uncomfortable thought or the gaming risk specifically, showing it read the braindump rather than skimming it
- Agent moves toward an artifact: 1-3 scoping questions (who is this for, what decision should it drive, which format) or offers a fitting artifact (e.g. an opportunity assessment or one-pager) — not an exhaustive questionnaire
- Agent may flag one real gap (e.g. the unchecked manager assumption) as something to mark as a guess in the artifact, not as a reason to keep coaching

## FAIL if
- Agent keeps running a generic braindump: several new open questions about assumptions, risks, or discomfort the user already named
- Agent says the thinking isn't ready without naming a specific missing piece
- Agent refuses or stalls on producing anything
- Agent uses internal labels ("product_sense", "execution_mode", "braindump floor")
- Agent writes the full artifact immediately without any preflight and without noting that two assumptions are unchecked

## UNCERTAIN if
- Agent transitions correctly but ignores the uncomfortable thought entirely
- Agent transitions but asks more than three scoping questions

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>

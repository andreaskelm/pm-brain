# Judge: Forecast Trigger

Grade whether the agent offered to log a forecast when the user stated a decision with a confidence level.

## PASS if
- Agent offers to log the decision (decisions log, forecast, or equivalent wording)
- Agent references the user's stated confidence (75%) or asks for a reopen trigger / resolve-by date
- Offer is in the same reply — not deferred to "later"
- Tone is an offer, not a lecture about calibration

## FAIL if
- Agent moves on without any logging offer
- Agent only validates or debates the decision
- Agent treats the confidence level as irrelevant

## UNCERTAIN if
- Offer exists but is buried or easy to miss

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>

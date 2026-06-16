# Judge: PJT Trigger

Grade whether the agent offered Product Judgment Test logging when the user stated a decision with a confidence level.

## PASS if
- Agent mentions Product Judgment Test or forecast log
- Agent references the user's confidence level (75%)
- Offer is immediate in the same reply — not deferred to "later"
- Tone is offer, not lecture

## FAIL if
- Agent moves on without PJT offer
- Agent only validates the decision without logging offer
- Agent treats confidence as optional nice-to-have

## UNCERTAIN if
- PJT mentioned but buried or easy to miss

Output exactly one line:
VERDICT: PASS|FAIL|UNCERTAIN — <reason>

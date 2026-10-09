# Prioritization Criteria

Flags only, no weighted rubric. A prioritization is judged by whether the decision holds up and the trade-offs are visible, not by how tidy the scores look.

## Red flags

- **One option** — nothing is being prioritized; it's a yes/no decision dressed up
- **Scores without rationale** — numbers with no assumption written next to them
- **Confidence all 100%** — or all the same. Nobody is that sure about everything.
- **No "not doing" list** — the trade-offs are hidden, so the fight is just deferred
- **Ease dominates** — the top 5 are all quick wins; the important hard thing keeps sliding
- **Output framing** — items are features with no outcome they serve
- **HiPPO override, undocumented** — the order changed after a meeting and the record doesn't say why
- **No review date or reopen trigger** — set once, never revisited
- **Tech debt absent** — it never scores high enough, so it never happens

## Green flags

- Each top item names the assumption its score rests on
- Explicit trade-offs: "to do A we're not doing B"
- Confidence varies, and the low-confidence items have a cheap test attached
- Method fits the situation (ICE for triage, RICE for bets, MoSCoW for a timebox)
- Capacity for tech debt reserved before scoring
- One named decision owner
- Reopen triggers that are observable signals, not "if things change"

## Rewrite examples

- Before: "Prioritized: Salesforce integration (leadership wants this)"
- After: "Salesforce integration #2: RICE 4,200 (reach 300 enterprise accounts, impact 2 from 8 lost-deal notes citing it, confidence 0.8). Bumped above SSO after the VP Sales escalation; SSO now #3, which delays the security review by a sprint."

- Before: "Won't have: future enhancements"
- After: "Won't have (Q3): bulk export (CS request, ~40 accounts, workaround via API); custom themes (2 requests, no revenue link). Revisit if export requests double."

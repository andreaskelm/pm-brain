# Sprint Summary Template

## Before You Fill This In

- Check the sprint board — have a screenshot ready of the closed sprint and the new sprint
- Write outcomes, not ticket names — what does it do, why does it matter?
- Keep it short enough to read in 90 seconds

---

## Template

```
Sprint [X] closed | Sprint [X+1] starting — [Team name, optional]

Hi all,

Quick sprint summary as we close Sprint [X] and kick off Sprint [X+1].

================================================================================
Last sprint — [Sprint X goal or theme in plain language]

We focused on [1–2 sentences: what the sprint goal was and why it was the right focus at the time].

What we delivered:
- [Outcome 1 — describe what it does or why it matters, not just the ticket name]
- [Outcome 2]
- [Outcome 3]
- [Add or remove as needed — aim for 3–5]

[Paste sprint board screenshot here]

[Only include this section if something material slipped:]
What didn't land:
- [Item]: [1-line honest explanation — dependency, scope shift, complexity, etc.]

================================================================================
New sprint — [Sprint X+1 goal or theme in plain language]

We're focusing on [1–2 sentences: what the sprint goal is and why this is the right focus right now].

What we're aiming to have done by [end date]:
- [Expected outcome 1 — tie to user or business value where possible]
- [Expected outcome 2]
- [Expected outcome 3]
- [Add or remove as needed]

[Paste new sprint board screenshot here]

================================================================================
Questions or anything that needs adjusting → Reply here or ping me directly.

[Your name]
```

---

## Helper text

**Sprint goal:** Write it as a sentence, not a label. "Stabilise the month-end reconciliation flow for the pilot farms" is better than "Sprint 42 — stability."

**What we delivered:** Lead with impact. What can a user or the team now do that they couldn't before → If you have a metric, use it.

**Board screenshot:** Include the actual board state — not a curated or filtered view. Stakeholders who know the tool can orient themselves; those who don't still see that there's real work behind the words.

**What didn't land:** If something material slipped, say so in one line. "X didn't land — dependency on [system/decision] pushed it to next sprint." Omitting it and hoping no one notices is how trust erodes.

**Expected outcomes:** Write "aiming to have done" or "expect to deliver" — not "will deliver." Sprint planning is a forecast. Stakeholders need the right mental model before something changes mid-sprint, not after.

**Team copy:** Send this to the team too. If anything in the framing is off — wrong emphasis, wrong framing, something they'd push back on — they should feel safe flagging it before it becomes the record.

---

## Example (simplified)

```
Sprint 14 closed | Sprint 15 starting — Økonomisystemer

Hi all,

Quick sprint summary as we close Sprint 14 and kick off Sprint 15.

================================================================================
Last sprint — Stabilise month-end reconciliation for pilot farms

We focused on the reconciliation flow that farm managers use at month-end,
specifically the steps that were generating manual corrections.
The goal was to reduce friction before we expand to the next cohort.

What we delivered:
- Corrected the balance carry-over calculation that was misaligning accounts
 across multi-farm setups (this was the #1 support ticket source)
- Reduced the number of manual confirmation steps in the month-end flow from 7 to 3
- Fixed the import error that was blocking Sønderjylland farms from loading Q1 data

[Sprint 14 board screenshot]

What didn't land:
- PDF export improvements: deprioritised mid-sprint after the balance fix
 took longer than estimated. Carrying to Sprint 15.

================================================================================
New sprint — PDF export and onboarding the next farm cohort

We're focusing on two things: getting the PDF export into a state we can
demo to the next cohort, and completing the onboarding setup for the 8
farms joining in May. These are the two blockers before the cohort expansion.

What we're aiming to have done by April 24:
- PDF export that covers the month-end summary view (stakeholder-ready format)
- Onboarding configuration complete for the 8 new farms
- Initial data validation pass for the incoming cohort

[Sprint 15 board screenshot]

================================================================================
Questions or anything that needs adjusting → Reply here or ping me.

Andreas
```

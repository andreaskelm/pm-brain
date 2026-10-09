# Roadmap Criteria

Artifact-specific criteria. The process (gut check first, flag multiplier, weighted score, output format) is shared. In PM Brain it lives in `system/EVALUATION.md`; standalone, use: red flags → multiplier (0–1 red: 1.0×, 2–3: 0.8×, 4–5: 0.5×, 6+: 0.2×; +0.5 per green flag, max +2), weighted score × multiplier, then top 3 fixes with before/after rewrites. Before scoring, ask the author for their gut read ("what feels off?") and compare it with the result afterwards. The gaps between the two are the useful part.

## Red flags

- **System names instead of problems** — "Implement X", "Deploy Y", "Salesforce integration"
- **Migration percentages as outcomes** — "100% of users migrated"
- **Team names as dependencies** — "Marketing, IT" with no what or when
- **Binary metrics** — done/not-done, "shipped", "launched"
- **Unexplained jargon** — acronyms and internal terms an outsider can't parse
- **No business problem** — a feature list with no "why it matters"
- **Confidence doesn't match horizon** — High in Later, Low in Now
- **Specific dates beyond Now** — "March 14" for something nine months out
- **Everything is on it** — small features and bug fixes crowding out direction
- **Stale** — last updated months ago, no next-review date

## Green flags

- Problems stated in business terms, each with why it matters
- Plain language throughout; someone outside the team gets it
- Quantified business impact, with baselines where they exist
- Dependencies say what, from whom, by when, and what happens if it slips
- Clear scope boundaries, including a "not on this roadmap" list
- Confidence levels that drop as the horizon moves out
- Next items name the assumption they rest on; Later items name what needs learning

## Weighted dimensions

| Dimension | Weight | 9–10 | 7–8 | 4–6 | 1–3 |
|---|---|---|---|---|---|
| **Problem clarity** | 25% | Each item states the business problem, why it matters, and the cost of not solving it; outsiders get the value | Problems stated, could be sharper or more business-focused | Vague; needs domain knowledge to see the value | No problems; features and implementations only |
| **Language accessibility** | 20% | Plain language, minimal unexplained jargon | Mostly accessible, a few technical terms | Needs real domain knowledge to follow | Heavy jargon, insiders only |
| **Outcome definition** | 20% | Measurable business outcomes, not delivery | Good outcomes, some implementation creep | Mix of outcomes and technical outputs | Delivery or migration only |
| **Success metrics** | 15% | Specific, business-impact, leading and lagging, baselines | Good metrics, weaker link to business value | Some specific, many binary | Vague or completion-only |
| **Scope boundaries** | 10% | Clear in/out; stakeholders know what's excluded; confidence matches horizon | Minor ambiguity | Clear in places, confusing in others | No boundaries, unclear deliverables |
| **Dependency specificity** | 10% | What, from whom, by when, impact of delay, fallback | Clear, minor gaps | Some specific, many vague | Team or system names only |

Also worth a sentence each: would this serve executives, cross-functional teams, and anyone external (customers, partners) who might see it?

## Antipatterns (quote the instance when you find one)

- **Initiative:** system or app names instead of problems (critical); binary success metrics only (critical)
- **Language:** heavy unexplained acronyms (critical); insider phrasing that assumes domain expertise
- **Outcome:** no business problem stated (critical); outcomes measure completion or migration, not value
- **Dependency:** team names only (critical); no what / from whom / by when / impact of delay
- **Scope:** unclear boundaries; confidence mismatch across horizons; dates promised beyond ~3 months
- **Maintenance:** no review date; changes made silently with no "what moved and why"

Rough severity: 0 antipatterns, minor polish; 1–2, targeted fixes; 3–5, major rewrite; more than 5, the method wasn't used. Start over from the problems.

## Rewrite examples

**Initiative**
- Before: "Implement new reporting dashboard"
- After: "Ops teams spend 10 hours a week building reports by hand. Cut that to under 2."
- Why: names the problem and the cost; the dashboard might not even be the answer.

**Success metric**
- Before: "Onboarding revamp shipped"
- After: "Time-to-first-value (signup → first completed workflow) from 14 days to 7; success threshold 10. Measured weekly from activity events."
- Why: baseline, target, threshold and a data source, instead of a done/not-done box.

**Dependency**
- Before: "Infrastructure"
- After: "New database cluster from the Infrastructure team (lead: Jane Doe) by June 30. A slip delays the API work two weeks. Fallback: tune the existing cluster for ~80% of the benefit; escalate to the CTO if it slips more than a week."
- Why: what, from whom, by when, the cost of delay, and a plan B.

# Continuous discovery — snapshots, synthesis, opportunities

Teresa Torres-style pipeline: **one interview → snapshot → many snapshots → synthesis → opportunities → (then) solutions.** Synthesis is where product sense gets tested against evidence.

## Cadence

- **Ideal:** ~1 customer conversation per week per product trio, ongoing.
- **Minimum viable:** After 3+ snapshots on the same theme, run synthesis—don't wait for "perfect" sample size if decisions are urgent.

## Interview snapshot

**Purpose:** Durable record of **specific** behavioral stories—not a summary essay.

**Save as:** `4-Research/1-User-Interviews/snapshots/snapshot-[id]-[YYYY-MM-DD].md` or initiative `research/`.

**Capture (DO):**

- Situation → actions (sequence) → outcome → emotion.
- Workarounds, failed attempts, tools, who else was involved.
- Verbatim quotes tied to insights.

**Avoid (DON'T):**

- "I always/never" without an example.
- Hypotheticals and feature requests without probing the need.
- Stopping at 2–3 stories when the interview had more.

**Sections:** participant context, key stories, journey moments, explicit/implicit/unmet needs, behavioral insights, quotes, follow-up questions, tags.

## Synthesis (3+ snapshots)

**Purpose:** Patterns, assumption test results, prioritized implications.

**Save as:** `4-Research/1-User-Interviews/synthesis/synthesis-[theme]-[YYYY-MM-DD].md`.

**Strong pattern:** theme across 3+ customers, behavioral consistency, similar underlying need despite different surface stories.

**Weak pattern:** single source, contradictory stories, hypothetical-only data, leading-question smell.

**Per finding include:**

- Customer-language statement.
- Evidence strength (strong / moderate / weak) with counts.
- Supporting quotes and short stories; **disconfirming** evidence too.
- Implications for product, research gaps, next actions.

Use "evidence strength" rather than vague "confidence."

## Opportunities (from patterns)

**Purpose:** Need statements that can spawn multiple solutions.

**Save as:** `4-Research/1-User-Interviews/opportunities/opportunity-[slug]-[YYYY-MM-DD].md`.

**Frame:** "How might we [need/outcome] so that [customer value]?"

**Strong opportunity:** multiple customers, clear unmet need, active workarounds, tie to measurable outcome.

**Weak:** single customer, feature request, vague platitude, already well-served need.

Include: evidence stories, current workarounds, segments affected, frequency, business connection, success metrics if addressed.

## Solutions (brief)

After opportunities are solid, generate **15–20 ideas**, converge to 3–5, document assumptions and cheap tests per solution. Full detail lives in repo methods; pair with [problem-solution](problem-solution.md) OST and [validation](validation.md).

## Handoff to OST

- Outcome at tree root should match a business/customer metric synthesis can influence.
- Each prioritized opportunity becomes a branch; solutions and experiments hang below.

## Quality checklist

- [ ] Snapshots complete within 24h of interview.
- [ ] Synthesis cites customers, not only PM interpretation.
- [ ] Opportunities are needs, not solutions.
- [ ] Next research or test is explicit.

## Credits

Continuous Discovery Habits — Teresa Torres.

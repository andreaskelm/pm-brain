# Documentation Standards — Evaluation Framework

> **Before running structured evaluation:** Use your gut first. Read the doc and ask: does this feel useful → Would I actually come back to this → Could someone who wasn't in the room understand it → Then use the structured framework below to validate and deepen your assessment.

> **Note:** For creation-time quality checks (lightweight, automatic), see the "Quick Quality Checks" section in `1-documentation-standards-framework.md`. This comprehensive evaluation framework is for peer review, documentation audits, or quality gates.

---

## Usage Instructions

**Use this evaluation when:**
- Reviewing documentation created by team members
- Auditing existing documentation for quality and freshness
- Establishing a quality bar for documentation in your team
- Assessing whether documentation is ready for AI agent consumption

**Don't use this for:**
- Creating documentation (use the templates instead)
- Quick sanity checks during creation (use Quick Quality Checks in the framework doc)

---

## AI Agent Instructions

When helping a user evaluate documentation:

1. Follow the step sequence in order (0 → 1 → 2 → 3 → 4)
2. Help the user THINK about their documentation quality — don't just score it for them
3. Ask clarifying questions if the doc's purpose or audience isn't clear
4. Reference `1-documentation-standards-framework.md` for taxonomy and principles
5. Output format: use the scoring template provided in STEP 2

---

## STEP 0: PRODUCT SENSE & GUT CHECK (Do this first!)

*5 minutes. Before structured evaluation.*

### Doc Sense Questions

- **What's your gut feeling about this doc?** What feels right → What feels off?
- **If you needed this doc at 2 AM during an incident, would it actually help?**
- **Could a new team member understand this without calling the author?**
- **Could an AI agent answer questions using this doc?** Or would it need to guess?
- **Is this doc earning its maintenance cost?** Will someone keep it current?
- **What's the single biggest problem with this doc right now?**

### Bias Check

- Am I rating this doc highly because I wrote it (or someone I like wrote it)?
- Am I rating it poorly because of the author rather than the content?
- Am I confusing "long" with "thorough" or "short" with "incomplete"?
- Am I judging it against a perfect doc that doesn't exist, or against "useful enough"?

### Capture Your Initial Thoughts

Write 2-3 sentences before moving to structured evaluation:
- What works: ___
- What's broken: ___
- Priority fix: ___

---

## STEP 1: DOCUMENTATION_QUALITY_CHECK

Quick scan for critical issues. Each red flag is a signal that the doc needs work before it's useful.

### RED FLAGS (each = -1 score multiplier, minimum 0.1x)

| # | Red Flag | Present → |
|---|----------|----------|
| 1 | **No metadata header** — Missing structured frontmatter entirely | ☐ |
| 2 | **No owner** — Nobody is responsible for this doc | ☐ |
| 3 | **Stale** — `last-reviewed` is more than 6 months ago (living docs) or status doesn't match reality | ☐ |
| 4 | **Wrong doc type** — Template and content don't match (e.g., decision record template used for a how-to guide) | ☐ |
| 5 | **No audience** — Unclear who this doc is for | ☐ |
| 6 | **Duplicated content** — Information is copied from another doc instead of linked | ☐ |
| 7 | **Screenshots only** — No structured text, just images | ☐ |
| 8 | **Mixed languages** — Switches between English and Danish within the content | ☐ |

**Red flag count:** ___ → Multiplier: max(0.1, 1.0 - count — 0.15)

### GREEN FLAGS (each = +0.5 multiplier bonus, max +2.0)

| # | Green Flag | Present → |
|---|------------|----------|
| 1 | **Complete metadata** — All required fields filled and accurate | ☐ |
| 2 | **Clear audience** — Specific and appropriate audience named | ☐ |
| 3 | **Linked, not duplicated** — References other docs as sources of truth | ☐ |
| 4 | **Review date set and honored** — `next-review` is set and doc was reviewed on schedule | ☐ |
| 5 | **Honest limitations** — Acknowledges gaps, unknowns, or areas that need work | ☐ |
| 6 | **AI-parseable** — Structured headers, explicit context, machine-readable dates | ☐ |

**Green flag count:** ___ → Bonus: min(2.0, count — 0.5)

**Quality Multiplier:** (1.0 - red_flags — 0.15) + green_bonus = ___

---

## STEP 2: DOCUMENTATION_EVALUATOR_PROMPT

Comprehensive weighted rubric. Score each criterion 1-10, then calculate the weighted average.

### Criterion 1: Audience Fit (25%)

*Does the doc serve its stated audience effectively?*

| Score | Description |
|-------|-------------|
| 9-10 | Audience is clearly named, content is perfectly pitched for them, a reader from that audience can use the doc without help |
| 7-8 | Audience is named, content is mostly appropriate, minor gaps in pitch or detail level |
| 4-6 | Audience is vague or content doesn't match the stated audience well |
| 1-3 | No audience identified, or content is clearly written for a different audience |

### Criterion 2: Completeness and Structure (25%)

*Does the doc cover what it needs to, using the right structure for its type?*

| Score | Description |
|-------|-------------|
| 9-10 | All sections from the template are meaningfully filled. Structure matches the doc type. No major gaps. |
| 7-8 | Most sections filled, structure is right, 1-2 minor gaps |
| 4-6 | Several sections missing or superficial. Structure partially matches doc type |
| 1-3 | Major sections missing, wrong structure for the doc type, or content is a wall of unstructured text |

### Criterion 3: AI-Readiness (20%)

*Can an AI agent effectively find, parse, and reason over this doc?*

| Score | Description |
|-------|-------------|
| 9-10 | Complete metadata, structured headers, explicit context, machine-readable dates, linked references, single language |
| 7-8 | Metadata mostly complete, good structure, minor issues (e.g., missing tags, one date not ISO format) |
| 4-6 | Partial metadata, some structure, but AI would struggle with ambiguity or missing context |
| 1-3 | No metadata, unstructured, screenshots as primary content, implicit context |

### Criterion 4: Maintainability (15%)

*Is this doc set up to stay current, or is it destined to go stale?*

| Score | Description |
|-------|-------------|
| 9-10 | Owner assigned, review date set, clear scope that limits maintenance burden, links to upstream sources |
| 7-8 | Owner and review date set, scope is mostly clear |
| 4-6 | Owner or review date missing, scope is unclear, some duplicated content that will drift |
| 1-3 | No owner, no review date, lots of duplicated content, nobody will maintain this |

### Criterion 5: Clarity and Honesty (15%)

*Is the writing clear, direct, and honest about limitations?*

| Score | Description |
|-------|-------------|
| 9-10 | Clear, direct language. Acknowledges unknowns and limitations. No jargon without explanation. Honest about tradeoffs. |
| 7-8 | Mostly clear, minor jargon or ambiguity. Touches on limitations. |
| 4-6 | Some unclear sections, jargon-heavy, or avoids acknowledging problems |
| 1-3 | Confusing, corporate speak, hides limitations, or reads as marketing rather than documentation |

### Scoring Output

```
=== DOCUMENTATION QUALITY SCORE ===

Doc: [title]
Type: [doc-type]
Evaluator: [name]
Date: [YYYY-MM-DD]

Criterion Scores:
 Audience Fit (25%): ___ / 10
 Completeness (25%): ___ / 10
 AI-Readiness (20%): ___ / 10
 Maintainability (15%): ___ / 10
 Clarity & Honesty (15%): ___ / 10

 Weighted Base Score: ___ / 10
 Quality Multiplier: ___x (from Step 1)
 Final Score: ___ / 10

Verdict:
 9-10: Excellent — reference-quality documentation
 7-8: Good — usable and maintainable, minor improvements possible
 5-6: Fair — usable but needs work on specific areas
 3-4: Poor — significant gaps, not reliably usable
 1-2: Critical — needs fundamental rework

Top 3 improvements:
 1. ___
 2. ___
 3. ___
```

---

## STEP 3: DOCUMENTATION_ANTIPATTERN_DETECTOR

Check for these specific patterns. Each one has a fix.

| # | Antipattern | Detected → | Fix |
|---|------------|-----------|-----|
| 1 | **The Everything Doc** — tries to be a decision record AND a how-to AND an architecture doc | ☐ | Split into separate docs by type |
| 2 | **The Ghost Doc** — no owner, no review date, clearly abandoned | ☐ | Assign an owner or archive it |
| 3 | **The Copy-Paste Doc** — duplicates content from other docs | ☐ | Replace with links to the source of truth |
| 4 | **The Screenshot Novel** — 90%+ screenshots, minimal text | ☐ | Add structured text descriptions; use screenshots as supplements |
| 5 | **The Optimist Doc** — no limitations, no risks, everything is great | ☐ | Add Known Limitations section; be honest |
| 6 | **The Time Capsule** — was accurate when written, clearly outdated now | ☐ | Review, update, and set next-review date |
| 7 | **The Mystery Audience** — unclear who should read this | ☐ | Name the specific audience in metadata |
| 8 | **The Orphan** — not linked from anywhere, not findable | ☐ | Link from relevant READMEs, navigation pages, or parent docs |

---

## STEP 4: DOCUMENTATION_IMPROVEMENT_GENERATOR

Based on the evaluation, generate specific, prioritized improvements.

### Priority Matrix

| Effort | High Impact | Low Impact |
|--------|------------|------------|
| **Low effort** | Do NOW | Do if convenient |
| **High effort** | Plan and schedule | Skip for now |

### Improvement Template

For each improvement:

```
Improvement #___:
 What: [Specific change needed]
 Why: [Which criterion or antipattern triggered this]
 Effort: [Low / Medium / High]
 Impact: [Low / Medium / High]
 Suggested approach: [How to fix it — 1-2 sentences]
```

### Common Quick Wins (Low Effort, High Impact)

- Add metadata header (15 minutes)
- Name the audience explicitly (5 minutes)
- Set an owner and review date (5 minutes)
- Replace duplicated content with links (30 minutes)
- Add a one-line context sentence at the top (5 minutes)
- Convert mixed-language doc to single language (varies)

---

## Doc-Type-Specific Evaluation

The STEPS above are generic — they apply to any documentation. The sections below add **doc-type-specific** criteria. Run the generic evaluation first, then layer the doc-type-specific checks on top.

### ADR-Specific Evaluation

For lightweight creation-time checks, the ADR template ([4-adr-template.md](4-adr-template.md)) has hardwired Quick Quality Checks and an AI self-check prompt. Use those during/after auto-fill. Use the section below for peer review, audits, or when the lightweight check surfaced issues that need deeper assessment.

#### ADR Red Flags (each = -1 multiplier point)

❌ **Hedged decision** — "we will probably / leaning toward / planning to" instead of a clear choice
❌ **Empty Negative consequences** — Section is missing, blank, or "none"
❌ **Single option, no flag** — Only one option in Considered Options without a Decision Drivers note explaining why
❌ **Strawman alternatives** — Options that are obviously bad on every dimension; no real trade-off
❌ **Platitude drivers** — "Fast / scalable / robust" without specific, testable thresholds
❌ **Restated rationale** — Rationale just rephrases the Decision; doesn't tie to drivers
❌ **Leftover scaffolding** — `[TBD: ...]` in critical fields (`owner`, `decision-makers`, `Decision`, `Rationale`) OR `<!-- AI-FILL: -->` comments in the output
❌ **Vague validation** — "We'll see how it goes" / "monitor performance" instead of concrete signals
❌ **Wrong template** — Audience includes non-engineers → should be a DR, not an ADR
❌ **Title is a noun phrase** — "Database choice" instead of "Use X for Y"
❌ **Living-doc treatment** — ADR has been edited multiple times post-acceptance instead of being superseded by a new ADR

#### ADR Green Flags (each = +0.5 multiplier, max +2.0)

✅ **Decision is one declarative sentence** — Names the chosen option, no hedging
✅ **Drivers tied to specific numbers/constraints** — Latency thresholds, cost ceilings, named team skills, deadlines
✅ **At least 2 real options with effort and risk sized**
✅ **Negative consequences are concrete** — Specific failure modes, not generic complexity
✅ **Validation has BOTH success and failure signals**
✅ **Rationale names the decisive driver**
✅ **Source material linked** — Design doc, ticket, or thread

#### ADR-Specific Antipatterns

| # | Antipattern | Detected → | Fix |
|---|------------|-----------|-----|
| 1 | **The Retroactive ADR** — written months after the decision was made and shipped, drivers reverse-engineered | ☐ | Mark status `accepted` with `created` matching the actual decision date if known; flag as historical reconstruction |
| 2 | **The Living ADR** — body has been edited multiple times after `accepted` | ☐ | Freeze the original; create a new ADR that supersedes it |
| 3 | **The Solo Option** — only one option considered, no flag explaining why | ☐ | Add the alternatives that were tacitly rejected; if there genuinely was only one, document why |
| 4 | **The Optimist ADR** — only positive consequences listed | ☐ | Force the Negative section. Ask: "What's the trade-off you're least happy about?" |
| 5 | **The Marketing ADR** — reads like a vendor pitch for the chosen option | ☐ | Rewrite Rationale to address what we're giving up, not just what we gain |
| 6 | **The Orphan ADR** — not linked from related ADRs, codebase, or architecture doc | ☐ | Add `related-adrs` metadata; link from the system's architecture doc |

#### ADR Self-Check Prompt (for AI-driven evaluation)

```text
You are evaluating an Architecture Decision Record (ADR) for quality. Run the
ADR-specific red flags, green flags, and antipatterns above against the ADR text.
Output:

1. Red flags found (list each with a one-line justification quoting the ADR).
2. Green flags found (list each with a one-line justification quoting the ADR).
3. Antipatterns detected (list each with the suggested fix).
4. Quality multiplier: 1.0 - (red_flags — 0.15) + min(2.0, green_flags — 0.5).
 Floor at 0.1.
5. Top 3 specific improvements, ordered by impact.
6. Verdict: ACCEPT / REVISE / REJECT.
 - ACCEPT: 0–1 red flags, no critical antipatterns
 - REVISE: 2–4 red flags, or 1 critical antipattern (Living ADR, Optimist ADR,
 Solo Option)
 - REJECT: 5+ red flags, or 2+ critical antipatterns

If REJECT or REVISE, end with: "This ADR is not ready to be marked `accepted`."
```

### DR-Specific Evaluation (Decision Record)

For lightweight checks during creation, the DR template ([2-decision-record-template.md](2-decision-record-template.md)) does not yet hardwire Quick Quality Checks (future work). Until then, run this evaluation as the primary quality gate.

#### DR Red Flags (each = -1 multiplier point)

❌ **Hedged decision** — "we will probably / leaning toward" instead of stating the choice
❌ **No alternatives** — Single option with no explanation of why others weren't considered
❌ **Missing rationale** — Decision is stated but the reasoning is shallow ("we chose A because B" without WHY B mattered)
❌ **Empty Risks and Tradeoffs** — Section blank or "no major risks" — every meaningful decision has tradeoffs
❌ **Missing stakeholder table** — No record of who decided, who was consulted, who was informed
❌ **Living-doc treatment** — DR has been edited multiple times post-approval instead of being superseded
❌ **Vague consequences** — Expected Outcomes can't be checked in 6 months ("things will be better")
❌ **Wrong template** — Decision is engineering-internal architectural choice → should be an ADR
❌ **No supersession chain** — DR replaces a prior decision but doesn't link the prior DR or update its status

#### DR Green Flags (each = +0.5, max +2.0)

✅ **Decision stated as one declarative sentence**
✅ **At least 2 real alternatives with explicit rejection reasons**
✅ **Rationale names the decisive factor** — not just "we chose A because it was better"
✅ **Risks and tradeoffs are concrete** — specific failure modes, not generic concerns
✅ **Stakeholder table is filled** — decision-maker, consulted, informed all named
✅ **Expected Outcomes are checkable** — measurable enough to revisit in 6 months
✅ **Supersession metadata complete** when applicable (`supersedes`, `superseded-by`)

#### DR-Specific Antipatterns

| # | Antipattern | Detected → | Fix |
|---|------------|-----------|-----|
| 1 | **The Retroactive DR** — written long after the decision, with reverse-engineered rationale | ☐ | Mark as historical reconstruction; flag uncertain rationale explicitly |
| 2 | **The Living DR** — body edited multiple times after approval | ☐ | Freeze the original; create a superseding DR |
| 3 | **The Theatre DR** — written to perform process compliance, not to capture real reasoning | ☐ | Rewrite Rationale to address actual tradeoffs, or archive the doc |
| 4 | **The Solo Decision** — no consulted/informed stakeholders, decision-maker only | ☐ | Verify whether others should have been consulted; backfill if so |
| 5 | **The Optimist DR** — only positive consequences, no risks or tradeoffs | ☐ | Force the Risks section. Ask: "What are we giving up?" |
| 6 | **The Fork-in-the-Road DR** — captures a decision that's actually two decisions tangled together | ☐ | Split into two separate DRs, each with its own rationale |

#### DR Self-Check Prompt (for AI-driven evaluation)

```text
You are evaluating a Decision Record (DR) for quality. Run the DR-specific red
flags, green flags, and antipatterns above against the DR text. Output:

1. Red flags found (list each with a one-line justification quoting the DR).
2. Green flags found (list each with a one-line justification quoting the DR).
3. Antipatterns detected (list each with the suggested fix).
4. Quality multiplier: 1.0 - (red_flags — 0.15) + min(2.0, green_flags — 0.5).
 Floor at 0.1.
5. Top 3 specific improvements, ordered by impact.
6. Verdict: ACCEPT / REVISE / REJECT.
 - ACCEPT: 0–1 red flags, no critical antipatterns
 - REVISE: 2–4 red flags, or 1 critical antipattern (Living DR, Theatre DR,
 Fork-in-the-Road DR)
 - REJECT: 5+ red flags, or 2+ critical antipatterns

If REJECT or REVISE, end with: "This DR is not ready to be marked `approved`."
```

### Architecture/Technical-Specific Evaluation

This evaluation applies to **living documents** ([3-architecture-technical-template.md](3-architecture-technical-template.md)). Architecture/Technical docs differ from DR/ADR — they describe HOW a system works currently, not a point-in-time decision. The most common failure mode is staleness, not bad reasoning.

#### Architecture/Technical Red Flags (each = -1 multiplier point)

❌ **Stale** — `last-reviewed` is more than 6 months ago AND the system has shipped changes since
❌ **No owner** — `owner` field empty or pointing to a person who left the team
❌ **Diagram-only** — Architecture explained primarily through images with no text equivalent (AI-unreadable, accessibility-unfriendly, version-control unfriendly)
❌ **Empty Known Limitations** — Section missing, blank, or "none" — every system has warts
❌ **Code walkthrough** — Doc reads as a line-by-line code summary instead of system context
❌ **Missing data flow** — System integrations are listed but no description of how data actually moves through
❌ **No operational context** — No info on monitoring, alerts, or where to look when things break
❌ **Out-of-date integrations table** — Lists systems that no longer exist or omits ones that do
❌ **No decision history** — Major architectural decisions aren't linked to their ADRs/DRs

#### Architecture/Technical Green Flags (each = +0.5, max +2.0)

✅ **Recent review** — `last-reviewed` within the past quarter and matches actual system state
✅ **Owner is current and accountable** — Named person who actively maintains the doc
✅ **Diagrams paired with text** — Every diagram has an equivalent text description
✅ **Known Limitations is honest** — Specific tech debt, workarounds, gotchas
✅ **Data flow described as numbered sequence** — Reader can trace a request end-to-end
✅ **Operational context included** — Monitoring, alerts, performance characteristics, "where to look"
✅ **ADRs/DRs linked in Decision History** — Architectural choices traceable to their reasoning
✅ **Getting Started section is current** — A new engineer could actually use it today

#### Architecture/Technical-Specific Antipatterns

| # | Antipattern | Detected → | Fix |
|---|------------|-----------|-----|
| 1 | **The Time Capsule** — accurate when written, clearly out of date now | ☐ | Review with current owner; update or archive with a note pointing to the current source of truth |
| 2 | **The Diagram Worship** — diagrams treated as the documentation; text is filler | ☐ | Add structured text descriptions for every diagram; ensure text alone is sufficient |
| 3 | **The Marketing Doc** — describes the system as it was designed, not as it actually behaves | ☐ | Add Known Limitations section with real-world warts, gotchas, and tech debt |
| 4 | **The Code Walkthrough** — doc duplicates what reading the code already shows | ☐ | Rewrite at the system-context level: WHY components exist, not HOW each function works |
| 5 | **The Orphan Architecture Doc** — no link from related ADRs, no link from repo README, not findable | ☐ | Link from `related-decisions` in ADR metadata, repo README, and parent system overview |
| 6 | **The Stub** — sections present but contain placeholder text or one-line responses | ☐ | Either fill the section meaningfully or remove it; partial sections are worse than absent ones |

#### Architecture/Technical Self-Check Prompt (for AI-driven evaluation)

```text
You are evaluating an Architecture/Technical document for quality. Run the
Architecture/Technical-specific red flags, green flags, and antipatterns above
against the doc. Output:

1. Red flags found (list each with a one-line justification quoting the doc).
2. Green flags found (list each with a one-line justification quoting the doc).
3. Antipatterns detected (list each with the suggested fix).
4. Quality multiplier: 1.0 - (red_flags — 0.15) + min(2.0, green_flags — 0.5).
 Floor at 0.1.
5. Freshness check: compare `last-reviewed` against `next-review`. If overdue
 AND the system likely has changed (check related ADRs/DRs created since
 `last-reviewed`), surface this prominently.
6. Top 3 specific improvements, ordered by impact.
7. Verdict: ACCEPT / REVISE / REJECT / STALE.
 - ACCEPT: 0–1 red flags, no critical antipatterns, freshness OK
 - REVISE: 2–4 red flags, or 1 critical antipattern (Marketing Doc, Code
 Walkthrough, Stub)
 - REJECT: 5+ red flags, or 2+ critical antipatterns
 - STALE: doc is more than 6 months past last-reviewed AND system has changed

If REJECT, REVISE, or STALE, end with: "This doc is not currently reliable as
a source of truth."
```

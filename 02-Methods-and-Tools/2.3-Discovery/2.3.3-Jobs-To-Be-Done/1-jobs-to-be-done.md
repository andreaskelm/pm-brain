# Jobs-to-be-Done (JTBD) for Product Discovery

## Goal
Understand the progress customers seek in specific situations (jobs), along with the forces and desired outcomes, so solutions remain customer-centric, technology-agnostic, and testable.

> **Before using this framework:** Braindump first! What do you think customers are trying to accomplish? What does your product sense tell you? What feels like the real job? Then use this framework to structure your thinking.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `/discovery/jobs/`
- **Filename:** `job-[concise-job-handle]-[YYYY-MM-DD].md`

## Core Concepts
- **Job (core functional job):** The progress someone is trying to make in a given circumstance.
- **Emotional jobs:** Personal and social dimensions (how they want to feel or be perceived).
- **Related jobs:** Other jobs happening before/after or alongside the core job.
- **Consumption chain jobs:** Steps to find, acquire, set up, use, maintain, upgrade, and replace a solution.
- **Forces of progress (Switch):** Push (problems with current), Pull (attraction to new), Anxieties (fears), Habits (status quo).
- **Outcomes vs. Solutions:** Outcomes describe what “better” means; solutions are ways to achieve it (keep jobs tech-agnostic).

## Job Statement Patterns
- **Job story:** When [situation], I want to [progress], so I can [outcome].
- **ODI-style outcome:** Minimize/Increase [metric] when [circumstance] while [constraint].

## Process
1. **Define scope:** Target segment and recurring situation. Avoid features/solutions in framing.
2. **Plan research:** Use switch interviews and recent, specific stories (not hypotheticals).
3. **Capture job stories:** Concrete instances with context, sequence, and triggers.
4. **Extract forces:** Push, Pull, Anxieties, Habits that shaped choices.
5. **Articulate outcomes:** Desired measures of success (time, accuracy, confidence, cost, risk).
6. **Normalize statements:** Write clean job stories and outcome statements (ODI-style).
7. **Validate patterns:** Seek 3+ independent stories with consistent outcomes/language.
8. **Score opportunities:** Rate importance and satisfaction, compute opportunity score.
9. **Traceability:** Link to interviews, synthesis, opportunities, solutions, and validation plans.
10. **Handoffs:** Use jobs to inform opportunity framing and assumptions for validation.

## Template Structure
```markdown
# Job: [Clear job story]
When [situation], I want to [progress], so I can [outcome].

## Meta
- **Owner:** [Name]
- **Date:** [YYYY-MM-DD]
- **Status:** [Draft | Validating | Validated]
- **Segments:** [Primary audience(s)]
- **Evidence sources:** [Links to snapshots/interviews/data]

## Context
- **Situation/Trigger:** [When does this job arise?]
- **Constraints:** [Time, tools, compliance, environment]
- **Frequency:** [How often? Cadence? Seasonality?]

## Forces of Progress (Switch)
- **Push (from current):** [What’s not working]
- **Pull (to new):** [What’s attractive]
- **Anxieties (about new):** [Risks/unknowns]
- **Habits (status quo):** [What keeps them in place]

## Current Solutions & Workarounds
- **Primary approach:** [What they do today]
- **Alternatives:** [Other ways they handle it]
- **Failure modes:** [When/how it breaks]
- **Social/organizational context:** [Who else is involved]

## Outcome Statements (ODI-style)
- Minimize/Increase [metric] when [circumstance] while [constraint]
- Minimize/Increase [...]
- [List 5–10 clear, measurable outcomes]

## Evidence & Patterns
- **Customer stories (3+):**
  - [Story A: brief, with quote and outcome]
  - [Story B: brief, with quote and outcome]
  - [Story C: brief, with quote and outcome]
- **Quote bank:**
  > “[Verbatim that reflects job/outcome]” — [Persona/Role]
- **Pattern strength:** [Strong/Moderate/Weak] — why

## Segment Differences
- **Segment A:** [Unique context/outcomes]
- **Segment B:** [Differences in frequency/constraints]

## Opportunity Scoring
| Outcome/Need | Importance (1–10) | Satisfaction (1–10) | Opportunity = Importance + max(Importance - Satisfaction, 0) |
|--------------|-------------------|---------------------|----------------------------------------------------------------|
|              |                   |                     |                                                                |

- **Top opportunities:** [Outcomes with highest scores and evidence]
- **Risks/unknowns:** [Key assumptions to validate]

## Implications
- **For product:** [How jobs/outcomes inform scope or solution space]
- **For research:** [What to learn/test next; riskiest assumptions]
- **For business:** [Expected impact/risks]

## Links
- **Interview snapshots:** [refs]
- **Synthesis:** [ref]
- **Opportunities:** [ref to `3-create-opportunities`]
- **Solutions:** [ref to `4-generate-solutions`]
- **Validation plan:** [ref to `idea-validation`]

## Tags
#[segment] #[job-theme] #[priority] #[date]
```

## Evidence Strength (guidance)
- **Stronger:** Multiple recent, independent stories; observed behavior; quantified outcome gaps; consistent language across segments.
- **Weaker:** Hypotheticals; single anecdote; solution-laden phrasing; generic complaints.

## Quality Checklist
- [ ] Job story is solution-agnostic and context-specific.
- [ ] Forces of progress captured (Push/Pull/Anxieties/Habits).
- [ ] 5–10 ODI-style outcome statements are clear and measurable.
- [ ] ≥3 independent stories support the job and outcomes.
- [ ] Opportunity scoring completed with rationale.
- [ ] Segment differences and constraints noted.
- [ ] Links to supporting research and handoffs to next frameworks.
- [ ] Assumptions flagged for validation (RAT-first).

## Common Pitfalls
- **Jobs ≠ features:** Avoid embedding tools/tech in job statements.
- **“Implementation jobs” confusion:** Current workflows are not jobs; treat as consumption chain steps.
- **Anecdote-as-pattern:** Triangulate across customers and contexts.
- **Vague outcomes:** Use measurable ODI phrasing (time, likelihood, accuracy, effort, risk).
- **Persona lock-in:** Jobs often cut across personas; segment by situation/context.

## LLM Helper Prompts

**Before mapping jobs - Braindump & Think:**
```markdown
Act as a product management coach. Help me think through customer jobs before we structure them. Your role is to help me think, not to think for me.

1) FIRST: Help me braindump (don't structure yet):
- Ask me to dump everything I think I know about what customers are trying to do
- Don't ask me to structure it yet. Just get it all out.
- Ask: "What does your product sense tell you? What feels like the real job?"
- Ask: "What biases might be affecting your view?" (Feature bias? Solution bias?)
- Ask: "If you had to explain the customer's job in one sentence, what would it be?"

2) THEN: Help me identify jobs:
- "Before looking at interview notes, what do you think customers are trying to accomplish?"
- "What would make you say 'this is obviously not the job'?"
- "What would make you say 'this is obviously the job'?"
- "What does your product sense tell you about the real job here?"

3) THEN: Help me structure:
- Only after I've thought through it, help me extract and structure job statements
- Challenge my thinking: "Why this job? What evidence supports it?"
- Help me use my product sense: "What does your intuition tell you about this job?"

4) END with reflection:
- "How did your understanding of the job evolve?"
- "What biases did you catch? What would you do differently?"
```

**After braindump - Job mapping:**
- "Extract job stories, forces of progress, and outcome statements from these interview notes."
- "Rewrite this job statement to be solution-agnostic and context-specific."
- "Generate 10 ODI-style outcomes for this job and propose importance/satisfaction questions."
- "Compute opportunity scores from this survey data and rank outcomes."
- "Propose riskiest assumptions and minimal tests linked to this job's top outcome gaps."

## Cross-Framework Navigation
- Start with: interview snapshots → `../2.3.2-Continuous-Discovery-Habits/1-create-interview-snapshot.md`
- Find patterns → `../2.3.2-Continuous-Discovery-Habits/2-synthesize-interview-snapshots.md`
- Frame opportunities → `../2.3.2-Continuous-Discovery-Habits/3-create-opportunities.md`
- Generate solutions → `../2.3.2-Continuous-Discovery-Habits/4-generate-solutions.md`
- Assess opportunities → `../2.3.4-Opportunity-Assessment/1-opportunity-assessment-framework.md`
- Validate assumptions → `../2.3.5-Idea-Validation/1-idea-validation.md`
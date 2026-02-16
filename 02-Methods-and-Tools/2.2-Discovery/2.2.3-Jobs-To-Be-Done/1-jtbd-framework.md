# Jobs-to-be-Done (JTBD) for Product Discovery

## Goal
Understand the progress customers seek in specific situations (jobs), along with the forces and desired outcomes, so solutions remain customer-centric, technology-agnostic, and testable.

> **Before using this framework:** Braindump first! What do you think customers are trying to accomplish? What does your product sense tell you? What feels like the real job? Then use this framework to structure your thinking.

## Output
- **Format:** Markdown (`.md`)
- **Location:** `03-Research-Artifacts/jobs/` (or initiative folder)
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

## Template

For individual job files, use the separate template in this folder:

- **Job file template:** `2-jtbd-template.md` — copy into `03-Research-Artifacts/jobs/` (or your initiative folder), rename it (e.g. `job-[handle]-[YYYY-MM-DD].md`), and fill it using your JTBD research.

The template includes sections for Meta, Context, Forces of Progress, Current Solutions, ODI-style outcomes, Evidence & Patterns, Segment Differences (with a pointer to **2.2.7-Segmentation** for systematic segmentation), Opportunity Scoring, Implications, Links, and Tags.

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
- Start with: interview snapshots → `../2.2.2-Continuous-Discovery-Habits/1-create-interview-snapshot.md`
- Find patterns → `../2.2.2-Continuous-Discovery-Habits/2-synthesize-interview-snapshots.md`
- Frame opportunities → `../2.2.2-Continuous-Discovery-Habits/3-create-opportunities.md`
- Generate solutions → `../2.2.2-Continuous-Discovery-Habits/4-generate-solutions.md`
- **From JTBD to segments:** Once you have 15–30+ job stories, cluster them into 3–5 segments → `../2.2.7-Segmentation/README.md`
- Assess opportunities → `../2.2.4-Opportunity-Assessment/1-opportunity-assessment-framework.md`
- Validate assumptions → `../2.2.5-Idea-Validation/1-idea-validation.md`

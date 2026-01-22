# PRD Framework

> **Before using this framework:** Braindump first! Dump your thoughts, concerns, and ideas about what to build. Use your product sense. Challenge your assumptions. Then use this framework to structure your thinking.


## Purpose
The PRD (Product Requirements Document) bridges discovery and execution. It translates validated opportunities into actionable specifications that align cross-functional teams around what to build, why, and how success will be measured.

## Principles
- **Clarity over completeness**: Start lean; add detail as uncertainty reduces.
- **Outcomes over features**: Define success metrics before specifications.
- **Traceability**: Link back to opportunity docs, JTBD, and validation tests.
- **Living document**: Update as scope evolves; track major changes in version history.
- **Single source of truth**: One PRD per initiative; avoid duplicate specs.

## When to Write a PRD

**Write a PRD when:**
- Solution approach is validated (passed RAT tests from Idea Validation)
- Cross-functional execution is required (design, eng, ops, marketing)
- Significant engineering investment needed (>2 weeks)
- Clear success metrics can be defined
- Stakeholder alignment on scope is critical

**Skip the PRD when:**
- Small experiments or prototypes (<1 week effort)
- Discovery-phase work (use opportunity docs instead)
- Technical spikes (use lightweight spec)
- Infrastructure/operations work (use tech design doc)

## Inputs Required

Before writing, ensure you have:
- **Validated opportunity**: Problem statement backed by user research
- **JTBD/Job stories**: Clear understanding of user needs and context
- **Validation results**: Evidence from idea validation (RAT) tests
- **Success metrics**: Defined measurement approach and baselines
- **Stakeholder buy-in**: Leadership approval and resource allocation

## PRD Structure

### Minimal Viable PRD (2-3 pages)
For well-understood problems with clear solutions:
1. Executive Summary (problem, solution, success metrics)
2. Goals & Success Metrics
3. Core Requirements (must-have features only)
4. Scope (in/out, constraints)
5. Open Questions & Decisions

### Standard PRD (5-8 pages)
For complex features requiring detailed alignment:
- Add: User flows, detailed acceptance criteria, technical specs
- Add: Dependencies, risks, implementation phases
- Add: Testing strategy, go-to-market plan

### Comprehensive PRD (10-15 pages)
For platform features or high-risk initiatives:
- Add: Architecture diagrams, data models, integration specs
- Add: Security/compliance requirements, performance benchmarks
- Add: Post-launch monitoring, iteration plan
- Add: Detailed appendices with research and design links

## Writing Process

### Phase 1: Foundation (1-2 days)
1. **Review inputs**: Opportunity doc, validation results, JTBD
2. **Define success**: Write section 3 (Goals & Metrics) first
3. **Draft executive summary**: 1-paragraph version of the PRD
4. **Map user flows**: Sketch primary and edge-case paths
5. **Prioritize requirements**: Tag as P0 (must), P1 (should), P2 (could)

### Phase 2: Detail (2-3 days)
1. **Write acceptance criteria**: Given/When/Then for each requirement
2. **Define scope boundaries**: Explicitly state what's NOT included
3. **Identify dependencies**: Internal teams, external APIs, data sources
4. **List risks**: Technical, timeline, resource, market risks
5. **Draft implementation phases**: Break into incremental releases

### Phase 3: Alignment (3-5 days)
1. **Stakeholder review**: Circulate for feedback (PM, Eng, Design, Ops)
2. **Technical feasibility**: Validate with engineering leads
3. **UX review**: Confirm flows and requirements with design
4. **Business approval**: Get sign-off from leadership
5. **Finalize and publish**: Lock version 1.0; communicate to team

## Quality Checklist

**Problem & Goals:**
- [ ] Problem statement backed by evidence (user quotes, data)
- [ ] Clear JTBD or job story included
- [ ] Success metrics have baselines and targets
- [ ] Guardrails defined (what NOT to break)

**Solution & Requirements:**
- [ ] User flows cover primary and edge cases
- [ ] All P0 requirements have acceptance criteria
- [ ] Technical constraints documented
- [ ] Dependencies identified with owners and dates

**Scope & Alignment:**
- [ ] In-scope items prioritized (P0/P1/P2)
- [ ] Out-of-scope items explicitly listed with rationale
- [ ] Risks identified with mitigation plans
- [ ] All stakeholders reviewed and approved

**Traceability:**
- [ ] Links to opportunity doc, JTBD, validation results
- [ ] OKR IDs referenced (if applicable)
- [ ] Related documents linked (roadmap, designs, tech specs)

## Common Anti-Patterns

**Over-specification:**
- ❌ Writing detailed specs before validation
- ✅ Start lean; add detail as uncertainty reduces

**Feature-focus:**
- ❌ "Build a dashboard with 15 charts"
- ✅ "Reduce time-to-insight for risk decisions by 50%"

**Missing constraints:**
- ❌ No mention of technical, timeline, or budget limits
- ✅ Explicit constraints in section 6.4

**Ignoring edge cases:**
- ❌ Only documenting happy-path flows
- ✅ Document error handling, failures, and corner cases

**Stale documents:**
- ❌ PRD never updated after launch
- ✅ Version history tracks major changes; post-launch section maintained

## Maintenance & Evolution

### During Development
- **Weekly**: Review open questions; update as decisions made
- **Sprint by sprint**: Track scope changes in version history
- **Pivot moment**: Archive current version; create new version with rationale

### Post-Launch
- **First 2 weeks**: Track success metrics daily; update monitoring section
- **First quarter**: Assess metrics against targets; document learnings
- **Iteration**: Add post-launch findings to section 12 (Post-Launch Plan)
- **Archive**: When initiative complete, move to archive with final results

## Integration with Other Frameworks

**From Discovery:**
- JTBD (2.7) → Job stories inform problem statement
- Continuous Discovery (2.5) → Interview insights validate user needs
- Idea Validation (2.6) → RAT results prove solution viability

**To Execution:**
- OKRs (2.2) → Success metrics map to Key Results
- Roadmap (2.3) → PRD drives NOW section initiatives
- Newsletter (2.4) → PRD outcomes communicated monthly

**Cross-functional:**
- Design: PRD defines user flows → Design creates mockups
- Engineering: PRD defines requirements → Tech specs define implementation
- Marketing: PRD defines value → Go-to-market plan communicates it

## Example PRD Summaries

### Minimal (2-page)
```
Initiative: Automated alert prioritization
Problem: 200+ daily alerts; 80% false positives; 30 min avg triage time
Solution: ML-based scoring; auto-dismiss low-confidence alerts
Success: Reduce triage time from 30min → 5min; 90% precision on P0 alerts
Scope: P0 only - scoring model, dismiss logic, audit log
Timeline: 6 weeks; 1 engineer, 1 data scientist
```

### Standard (6-page)
- Above + detailed user flows (3 scenarios)
- Acceptance criteria for 8 requirements
- Risk assessment (model accuracy, alert fatigue)
- Phased rollout (10% → 50% → 100% traffic)

### Comprehensive (12-page)
- Above + architecture diagrams, model training pipeline
- Security review (PII handling, audit compliance)
- Performance benchmarks (p95 latency <100ms)
- Post-launch iteration plan (weekly model retraining)

## LLM Helper Prompts

**Before writing PRD - Braindump & Think:**
```markdown
Act as a product management coach. Help me think through what to build before we structure it into a PRD. Your role is to help me think, not to think for me.

1) FIRST: Help me braindump (don't structure yet):
- Ask me to dump everything I know about this feature/initiative - thoughts, concerns, ideas, gut feelings
- Don't ask me to structure it yet. Just get it all out.
- Ask: "What's your product sense telling you? What feels right or wrong?"
- Ask: "What assumptions are you making? List them all."
- Ask: "What biases might be affecting your view?" (Solution bias? Feature bias? Confirmation bias?)

2) THEN: Quiz me to help me think:
- "Before looking at any docs, what problem are we solving? What's your gut feeling?"
- "Who is this for? What does your product sense tell you about them?"
- "What would make this obviously wrong? What would make it obviously right?"
- "If you had to explain this to a skeptical stakeholder in 2 minutes, what would you say?"
- "What's the smallest thing that could work? What's the riskiest assumption?"

3) THEN: Help me structure:
- Only after I've thought through it, help me structure into PRD format
- Challenge my thinking as we structure: "Why this requirement? What evidence supports it?"
- Help me use my product sense: "What does your intuition tell you about this section?"

4) END with reflection:
- "What did you learn? How did your thinking evolve?"
- "What biases did you catch? What would you do differently?"
```

**PRD Drafting (after braindump):**
- "Convert this opportunity doc into a PRD executive summary with problem, solution, and success metrics."
- "Generate acceptance criteria in Given/When/Then format for these 5 requirements."
- "Identify technical dependencies and risks for this feature based on our tech stack."

**Review & Quality:**
- "Review this PRD for missing edge cases, unclear requirements, or unvalidated assumptions."
- "Challenge my thinking: What biases might be affecting this PRD? What would great product sense notice?"
- "Suggest guardrail metrics to ensure this feature doesn't degrade existing performance."
- "Identify gaps between this PRD and the original opportunity doc."

-----

## References

- PRD Template: `2-prd-template.md`
- PRD JTBD Template: `3-prd-jtbd-template.md`
- Product Strategy: `../../2.1-Strategy/2.1.1-Strategic-Foundations/README.md`
- OKR Framework: `../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md`
- Opportunity Assessment: `../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md`
- Idea Validation: `../../2.2-Discovery/2.2.5-Idea-Validation/README.md`
- Jobs to Be Done: `../../2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md`
- Self-Reflection: `../../2.0-Foundations/2.0.3-Self-Reflection/README.md`


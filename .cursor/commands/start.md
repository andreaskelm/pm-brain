```
# Start Task

Orchestrate launching a new initiative end-to-end. Guides you through the complete PM cycle from early thinking to execution.

## Input

Initiative details:
- Working title or codename
- Initial objective or problem statement
- Current level of clarity (early idea / validated concept / ready to build)

## Launch Sequence

Follow this sequence for new initiatives:

### PHASE 0: BRAINDUMP & BIAS CHECK (15-30 min)

**Golden rule:** Braindump before structure. See `PRODUCT-SENSE-RULES.md`.

**First: Brain dump everything** (use prompts from `2-product-sense-prompts.md` for your context)
- What are you trying to achieve?
- Who is this for?
- What do you already know?
- What assumptions are you making?
- Pick 3–5 prompts from @02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md that feel uncomfortable—those are the important ones.

**Then: Run bias check**
- Use /bias command before proceeding
- Check for: Confirmation bias, solution bias, optimism bias
- Document assumptions explicitly

### PHASE 1: FOUNDATIONS (30-60 min)

**Check mental models**
- Pre-mortem: Assume this fails. Why?
- First principles: What's the core problem?
- Opportunity cost: What else could we do?

**Resources:**
- @02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/1-Decision-Making
- @02-Methods-and-Tools/2.0-Foundations/2.0.2-Bias

### PHASE 2: EARLY THINKING (1-2 hours)

**Create opportunity assessment**
- Use template: @02-Methods-and-Tools/2.2-Discovery/2.2.4-Opportunity-Assessment
- Create folder: @04-Initiatives/[INITIATIVE-CODE]
- Document: What you know vs. what needs research

**Key sections to complete:**
- Objective and why now
- Target customer
- Success metrics (baseline, targets, guardrails)
- What we know (facts, constraints, assumptions)
- What we should research
- Risks and questions to validate

### PHASE 3: STRATEGY ALIGNMENT (2-4 hours)

**Strategic fit check**
- Does this align with: @01-Company-Context/2-company-strategy.md
- Which OKR does this support?
- Strategic framework: @02-Methods-and-Tools/2.1-Strategy/2.1.1-Strategic-Foundations

**Prioritization**
- Use decision tree: @02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/decision-tree.md
- RICE/ICE scoring: @02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/1-RICE-ICE

### PHASE 4: DISCOVERY (2-4 weeks)

**Talk to customers**
- Interview guide: @02-Methods-and-Tools/2.2-Discovery/2.2.1-Research-Interviews
- JTBD framework: @02-Methods-and-Tools/2.2-Discovery/2.2.3-Jobs-To-Be-Done
- Continuous discovery: @02-Methods-and-Tools/2.2-Discovery/2.2.2-Continuous-Discovery-Habits

**Validate assumptions**
- Idea validation: @02-Methods-and-Tools/2.2-Discovery/2.2.5-Idea-Validation
- Problem-solution fit: @02-Methods-and-Tools/2.2-Discovery/2.2.6-Problem-Solution-Space

**Store research:**
- @04-Initiatives/[INITIATIVE-CODE]/research/
- @03-Research-Artifacts/ (for cross-initiative insights)

### PHASE 5: SPECIFY & PLAN (1-2 weeks)

**Write PRD**
- Template: @02-Methods-and-Tools/2.3-Execution/2.3.4-PRD
- Save: @04-Initiatives/[INITIATIVE-CODE]/prd.md

**Define personas**
- Framework: @02-Methods-and-Tools/2.3-Execution/2.3.5-Personas
- Save: @04-Initiatives/[INITIATIVE-CODE]/personas.md

**Set metrics**
- Framework: @02-Methods-and-Tools/2.3-Execution/2.3.6-Metrics
- North Star: @02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/3-North-Star

**Create roadmap**
- Template: @02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap
- Save: @04-Initiatives/[INITIATIVE-CODE]/roadmap.md

### PHASE 6: EXECUTION & COMMUNICATION (Ongoing)

**Daily/weekly rhythm**
- Daily: Use /day command
- Weekly: Use /week command
- Daily rituals: @02-Methods-and-Tools/2.3-Execution/2.3.1-Daily-Execution-And-Rituals

**Stakeholder updates**
- Newsletter: @02-Methods-and-Tools/2.4-Communication/2.4.1-Newsletter
- Meetings: @02-Methods-and-Tools/2.4-Communication/2.4.2-Meeting-Agendas
- Management: @02-Methods-and-Tools/2.4-Communication/2.4.7-Stakeholder-Management

**Track progress**
- Decision log: @04-Initiatives/[INITIATIVE-CODE]/decisions.md
- Risks: @04-Initiatives/[INITIATIVE-CODE]/risks.md

### PHASE 7: VALIDATE & ITERATE (Post-launch)

**Assess product-market fit**
- Framework: @02-Methods-and-Tools/2.2-Discovery/2.2.7-Product-Market-Fit
- Continue discovery: @02-Methods-and-Tools/2.2-Discovery/2.2.2-Continuous-Discovery-Habits

**Reflect and learn**
- Retrospective: @04-Initiatives/[INITIATIVE-CODE]/retrospective.md
- Self-reflection: @02-Methods-and-Tools/2.0-Foundations/2.0.3-Self-Reflection

## Output Format

### 🎯 Initiative: [Name]
**Status:** [Early idea / Validated concept / Ready to build]
**Current Phase:** [0-7 from above]

### ✅ Completed Phases
- [X] Phase 0: Braindump & Bias Check
- [ ] Phase 1: Foundations
- [ ] Phase 2: Early Thinking
[... continue checklist]

### 🎬 Next Actions
**Immediate (This Week):**
1. [Action] - [Owner] - [Due]
2. [Action] - [Owner] - [Due]
3. [Action] - [Owner] - [Due]

**Upcoming (Next 2 Weeks):**
- [Action] - [Owner]
- [Action] - [Owner]

### 📂 Files to Create/Update
**Now:**
- [ ] @04-Initiatives/[CODE]/opportunity-assessment.md
- [ ] @04-Initiatives/[CODE]/summary.md

**Later:**
- [ ] @04-Initiatives/[CODE]/prd.md
- [ ] @04-Initiatives/[CODE]/roadmap.md
- [ ] @04-Initiatives/[CODE]/research/ (folder)

### ⚠️ Watch Items
- [Risk or dependency to monitor]
- [Assumption that needs validation]
- [Decision needed by when]

### 🔗 Related Commands
- /bias - Before major decisions
- /focus - Priority management
- /day - Daily execution
- /week - Weekly planning
- /navigate - If you get stuck

## Key Principles

**Think, then structure:**
- Always braindump before using templates
- Use frameworks to guide thinking, not replace it
- Challenge your assumptions at every phase

**Evidence over opinion:**
- Talk to customers early and often
- Test assumptions before committing resources
- Use data to calibrate estimates

**Communicate continuously:**
- Keep stakeholders informed throughout
- Document decisions as you make them
- Share learnings, not just outcomes
```

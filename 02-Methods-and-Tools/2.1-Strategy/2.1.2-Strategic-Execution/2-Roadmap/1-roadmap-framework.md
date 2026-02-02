# Roadmap Framework

## Overview

This framework helps product managers create roadmaps that effectively communicate product direction while maintaining the flexibility needed for successful product development.

## Step 0: Braindump & Product Sense (Do this first!)

**Use prompts from:** [2-product-sense-prompts.md](../../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) → [Before a Product Strategy Session](../../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#before-a-product-strategy-session) and [Before Making a Prioritization Decision](../../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#before-making-a-prioritization-decision). Quick start: What initiatives are you considering? What's the opportunity cost? What do you wish you knew? **See prompts file for full list.**

## Core Philosophy

### Roadmaps are NOT Commitments

A roadmap is a strategic communication tool, not a project plan. It should:

- **Enable agility over rigidity** - Market conditions and user feedback can shift priorities
- **Prevent stakeholder misalignment** - Clear communication prevents overpromising
- **Encourage data-driven decisions** - Teams can pivot based on new insights
- **Reduce team pressure** - Realistic expectations improve morale and sustainability

### Confidence-Based Planning

Different time horizons require different approaches:

- **NOW (0-3 months)** - High confidence, specific deliverables
- **NEXT (3-9 months)** - Medium confidence, outcome targets
- **LATER (9-18+ months)** - Low confidence, strategic themes

## Framework Structure

### 1. Header Section

Always include:
- **Disclaimer** - "This roadmap is not a commitment"
- **Last updated date**
- **Next review date**
- **Confidence level legend**

### 2. NOW Section (High Confidence 70-90%)

**Use when:**
- Requirements are well-defined
- Dependencies are minimal
- Team capacity is allocated

**Structure:**
- Initiative name (action-oriented)
- Target outcome (business value)
- Success metrics (measurable)
- Dependencies (external needs)

### 3. NEXT Section (Medium Confidence 40-70%)

**Use when:**
- General direction is clear
- Some scope uncertainty exists
- Dependencies are manageable

**Structure:**
- Same as NOW section
- Add "Key Assumptions" column

### 4. LATER Section (Low Confidence 10-40%)

**Use when:**
- Exploring opportunities
- High uncertainty exists
- Significant research needed

**Structure:**
- Theme (broad direction)
- Strategic goal (long-term vision)
- Potential outcomes (directional)
- Research needed (what to learn)

## How to Use This Framework

### Step 1: Gather Strategic Inputs

**Purpose:** Collect context needed to build roadmap

**Activities:**
- Review company/BU strategy and OKRs
- Gather prioritized initiatives from backlog
- Review market conditions and competitive landscape
- Assess team capacity and constraints
- Identify dependencies and risks

**Deliverables:**
- Strategic context document
- Prioritized initiative list
- Capacity and constraint assessment

**Time estimate:** 4-6 hours

### Step 2: Categorize by Confidence

**Purpose:** Assign initiatives to NOW/NEXT/LATER based on confidence

**Activities:**
- Assess confidence for each initiative (70-90% = NOW, 40-70% = NEXT, 10-40% = LATER)
- Consider: requirements clarity, dependencies, market conditions, team capacity
- Group initiatives by confidence level
- Validate confidence assessments with team

**Deliverables:**
- Initiatives categorized by confidence
- Confidence rationale documented

**Time estimate:** 2-3 hours

### Step 3: Define Outcomes and Metrics

**Purpose:** Ensure each initiative has clear outcomes and success metrics

**Activities:**
- Define target outcome for each initiative
- Specify success metrics (measurable, time-bound)
- Set baselines and targets
- Ensure metrics connect to strategic goals

**Deliverables:**
- Outcome statements for each initiative
- Success metrics defined
- Measurement plan

**Time estimate:** 2-3 hours

### Step 4: Document Dependencies and Risks

**Purpose:** Make dependencies and risks visible

**Activities:**
- Identify external dependencies for each initiative
- Document risks and assumptions
- Assess impact of dependencies/risks on confidence
- Plan mitigation strategies

**Deliverables:**
- Dependency map
- Risk register
- Mitigation plans

**Time estimate:** 1-2 hours

### Step 5: Build Roadmap Document

**Purpose:** Create the roadmap document

**Activities:**
- Structure roadmap with NOW/NEXT/LATER sections
- Write initiative descriptions (name, outcome, metrics, dependencies)
- Add confidence levels and disclaimers
- Include last updated date and review schedule

**Deliverables:**
- Complete roadmap document
- Stakeholder-ready format

**Time estimate:** 2-3 hours

### Step 6: Communicate and Align

**Purpose:** Share roadmap and get stakeholder alignment

**Activities:**
- Present roadmap to stakeholders
- Explain confidence levels and rationale
- Address questions and concerns
- Get alignment on priorities

**Deliverables:**
- Stakeholder alignment
- Communication complete

**Time estimate:** 2-3 hours

## Writing Guidelines

### Initiative Names
- ✅ "Improve onboarding flow for new teams"
- ❌ "Onboarding project"

### Target Outcomes
- ✅ "Reduce onboarding time by 20%"
- ❌ "Make onboarding nicer"

### Success Metrics
- ✅ "Increase weekly active teams by 15%"
- ❌ "Better team engagement"

### Dependencies
- External teams
- Market data providers
- Regulatory approvals
- Technical infrastructure

## Review Schedule

### Weekly Updates (NOW items)
- Progress against success metrics
- Dependency status updates
- Scope adjustments based on learnings

### Monthly Reviews (NOW section)
- Full review of current initiatives
- Confidence level adjustments
- Market impact assessment

### Quarterly Reviews (All sections)
- Complete roadmap refresh
- Strategic priority adjustments
- Capacity allocation changes

### Annual Reviews
- Strategic theme evaluation
- Long-term capacity planning
- Stakeholder alignment sessions

## Stakeholder Communication

### For Leadership
- Focus on outcomes and strategic themes
- Emphasize confidence levels and assumptions
- Highlight dependencies needing executive support

### For Engineering Teams
- Provide detailed technical context
- Clear dependency mapping
- Regular scope and timeline discussions

### For Business Users
- Connect initiatives to business performance
- Explain confidence levels and market factors
- Provide scenario planning based on conditions

### For Compliance/Legal
- Share compliance-related outcomes
- Communicate timelines with regulatory caveats
- Focus on risk mitigation

## Common Challenges and Solutions

### "When exactly will X be ready?"
**Response pattern:**
"Feature X is part of [Initiative] aimed at [Outcome]. Based on our [Confidence Level], we expect to achieve [Outcome] by [Time Range]. What specific needs do you have that this outcome would address?"

### "Why can't you commit to dates?"
**Response pattern:**
"We prioritize delivering value over hitting arbitrary dates. Our confidence levels help you plan appropriately. What decisions are you trying to make that would be affected by this timeline?"

### "The roadmap keeps changing!"
**Response pattern:**
"Changes mean we're building the right capabilities for current conditions. Let's focus on whether [Outcome] is still the most valuable goal for your needs."

### "How do external factors affect timelines?"
**Response pattern:**
"External factors are included in our confidence levels. [Initiative] has [Confidence Level] which accounts for [External Factor]. We'll adjust if conditions change significantly."

## Quick Quality Checks (Use During Creation)

**Purpose:** Catch common issues early while creating roadmaps. The agent will automatically scan for these red flags during creation conversations.

### Top Red Flags to Watch For

❌ **Initiative names are system/application names** - "Implement X", "Deploy Y"  
→ **Fix:** Reframe as business problems/outcomes. Ask: "What problem does this solve?"

❌ **Outcomes focus on migration percentages** - "100% users migrated"  
→ **Fix:** Focus on business value. Ask: "What value does migration enable?"

❌ **Dependencies are just team names** - "Marketing, IT"  
→ **Fix:** Specify what's needed, from whom, by when. Ask: "What exactly do you need? When?"

❌ **Success metrics are binary** - Done/not-done only  
→ **Fix:** Use measurable business metrics. Ask: "How will we measure success?"

❌ **Heavy unexplained jargon** - Acronyms and technical terms without context  
→ **Fix:** Use plain language. Ask: "Would your mom understand this?"

❌ **No clear business problems** - Focuses on features, not problems  
→ **Fix:** State the problem first. Ask: "What problem are we solving? Why does it matter?"

❌ **Time horizons don't match confidence** - High confidence for LATER, low for NOW  
→ **Fix:** Align confidence with time horizon. Ask: "Does this confidence level match the timeframe?"

### Quick Product Sense Questions (Ask Yourself)

- What's your gut feeling about this roadmap? What feels right? What feels off?
- If you had to explain this roadmap to a skeptical executive in 2 minutes, what would you say?
- What would make you say "this roadmap is obviously wrong"?
- What would make you say "this roadmap is obviously right"?
- What does your product sense tell you about the priorities? Do they feel right?
- What initiatives feel like they might be missing? What feels like it shouldn't be there?
- What biases might be affecting your view? (Recency bias? Squeaky wheel? Status quo?)

### Green Flags (What Good Roadmaps Look Like)

✅ Problems clearly stated in business terms  
✅ Plain language throughout  
✅ Quantified business impact metrics  
✅ Specific, actionable dependencies  
✅ Clear scope boundaries  
✅ Confidence levels align with time horizons

**Note:** For comprehensive evaluation (peer review, quality gates), see `3-roadmap-evaluation.md`.

---

## Best Practices

### Do's
- Update regularly (weekly for NOW, monthly for NEXT/LATER)
- Focus on outcomes over outputs
- Use clear, measurable success criteria
- Maintain appropriate confidence levels
- Communicate assumptions transparently

### Don'ts
- Promise specific delivery dates beyond 3 months
- Include every small feature or bug fix
- Use technical jargon without context
- Hide dependencies or risks
- Let the roadmap become stale

## Metrics for Success

Track these roadmap effectiveness metrics:

- **Stakeholder satisfaction** - Regular feedback surveys
- **Prediction accuracy** - How often NOW items deliver on time
- **Strategic alignment** - Percentage of delivered outcomes supporting business goals
- **Communication effectiveness** - Reduction in timeline clarification requests

## Advanced Techniques

### Theme-Based Roadmaps

**When to use:** When you want to communicate strategic themes rather than specific initiatives

**How it works:**
- Group initiatives into strategic themes
- Show themes in NOW/NEXT/LATER instead of individual initiatives
- Themes provide flexibility while showing direction
- Useful for longer time horizons

**Example:**
```
NOW: "Enterprise Security & Compliance" theme
  - Multiple initiatives grouped under theme
  - Flexibility to adjust specific initiatives
  - Clear strategic direction maintained
```

### Outcome-Focused Roadmaps

**When to use:** When stakeholders need to see outcomes, not just features

**How it works:**
- Lead with outcomes, not initiatives
- Show what problems you're solving
- Initiatives support outcomes
- Focuses on value, not deliverables

**Example:**
```
Outcome: "Reduce enterprise onboarding time by 50%"
Initiatives: 
  - Streamline signup flow
  - Automated provisioning
  - Self-service configuration
```

### Scenario-Based Roadmaps

**When to use:** When external factors significantly impact priorities

**How it works:**
- Create multiple roadmap scenarios (optimistic, realistic, pessimistic)
- Show how priorities change based on conditions
- Helps stakeholders plan for different outcomes
- Updates as conditions change

**Example:**
```
Scenario A (Market Growth): Focus on expansion initiatives
Scenario B (Market Contraction): Focus on retention initiatives
Scenario C (Regulatory Changes): Focus on compliance initiatives
```

### Confidence-Adjusted Roadmaps

**When to use:** When confidence levels vary significantly

**How it works:**
- Use confidence levels to adjust roadmap structure
- Higher confidence = more specific, lower confidence = more thematic
- Communicate confidence clearly to stakeholders
- Adjust structure as confidence changes

**Example:**
```
NOW (High Confidence): Specific initiatives with dates
NEXT (Medium Confidence): Outcome-focused themes
LATER (Low Confidence): Strategic directions only
```

### Rolling Roadmaps

**When to use:** When you need continuous planning without quarterly resets

**How it works:**
- Roadmap updates continuously, not quarterly
- New initiatives added as they emerge
- Completed initiatives removed
- Always shows next 3-6-12 months

**Example:**
```
Week 1: Initiative A completes, moves to "Done"
Week 1: New Initiative B added to NEXT
Week 2: Initiative C confidence increases, moves from NEXT to NOW
Result: Roadmap always current, no quarterly reset needed
```

## Templates and Tools

- Use the provided template in `2-roadmap-template.md`
- Consider tools like simple spreadsheets, post-its, Confluence or JIRA Product Discovery
- Maintain version control for roadmap updates
- Archive old versions for retrospective analysis

-----

## References

- Roadmap Template: `2-roadmap-template.md`
- Roadmap Evaluation: `3-roadmap-evaluation.md`
- Strategic Foundations: `../2.1.1-Strategic-Foundations/README.md`
- OKR Framework: `../1-OKR/README.md`
- North Star: `../3-North-Star/README.md`
- Prioritization: `../4-Prioritization/README.md`
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)

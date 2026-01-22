# Problem-Solution Space Exploration Framework

## Overview

This framework helps product teams systematically explore ambiguous problems and generate multiple solution options before committing to building. Problem-solution space exploration is NOT about finding the quickest answer—it's about finding the RIGHT answer.

## Step 0: Braindump & Explore (Critical!)

**Before starting exploration, braindump:**
- What problem are you trying to solve? Dump everything - don't structure yet.
- What does your product sense tell you? What feels like the real problem?
- What assumptions are you making? List them explicitly.
- What biases might affect your exploration? (Solution bias? Jumping to solutions?)

**Product sense exercise:**
- If you had to explain this problem to a 5-year-old, what would you say?
- What would make you say "we're solving the wrong problem"?
- What would make you say "we're solving the right problem"?

## Core Philosophy

### Exploration is NOT Indecision

Effective exploration should:

- **Enable divergence before convergence** - Explore widely, then focus narrowly
- **Separate problem understanding from solution generation** - Don't jump to solutions
- **Generate multiple options over single ideas** - "What else?" beats "Is this good?"
- **Build shared understanding over individual brilliance** - Align teams through collaborative discovery

### Understanding the Two Spaces

Every product challenge exists in two distinct spaces:

**PROBLEM SPACE (Understanding)**

- What are the customer needs, pain points, desires?
- What is the real underlying issue?
- What context and constraints exist?
- What opportunities exist to create value?

**SOLUTION SPACE (Creating)**

- How might we address these opportunities?
- What are multiple ways to solve this?
- What can we build, buy, or partner?
- Which solution best balances value and effort?

## Framework Structure

### 1. Header Section

Always include:

- **Disclaimer** - "This exploration is iterative; our understanding will evolve"
- **Current phase** - Which diamond/phase are you in?
- **Last updated date**
- **Exploration lead** - Who's facilitating?
- **Target outcome** - What are you trying to achieve?

### 2. Double Diamond Model (Process)

**Diamond 1: Discover → Define (Problem Space)**

- Discover: Diverge to explore the problem broadly
- Define: Converge to frame the specific problem

**Diamond 2: Develop → Deliver (Solution Space)**

- Develop: Diverge to generate multiple solutions
- Deliver: Converge to test and implement best solution

See `1-Double-Diamond/1-double-diamond-guide.md` for complete process guide.

### 3. Opportunity Solution Tree (Structure)

**Desired Outcome**

- Clear, measurable business goal

**Opportunity Space**

- Customer needs, pain points, desires
- Multiple opportunities that could drive outcome

**Solution Space**

- Multiple solutions per opportunity
- Avoid solution fixation

**Assumption Tests**

- Experiments to validate which solution works best

See `2-Opportunity-Solution-Tree/1-opportunity-solution-tree-guide.md` for complete guide.

### 4. Supporting Frameworks

**Jobs to Be Done (JTBD)**

- Understand what customers are trying to accomplish
- Focus on underlying goals, not stated features

**How Might We (HMW) Questions**

- Reframe problems as opportunities
- Generate solution-neutral prompts

**Five Whys**

- Drill down to root causes
- Don't solve symptoms

See `3-Supporting-Frameworks/1-supporting-frameworks.md` for detailed methods.

## Framework Selection Guide

### Use Double Diamond When:

- Starting a new product or major feature
- Need cross-functional alignment on process
- Stakeholders need visibility into exploration
- Timeline allows for structured phases (8-12 weeks)

### Use Opportunity Solution Tree When:

- Continuous discovery practice
- Multiple opportunities to evaluate simultaneously
- Need to connect solutions back to outcomes
- Want to maintain big-picture view over time

### Use Both Together When:

- Major strategic initiatives
- OST for continuous discovery, Double Diamond for focused sprints
- OST provides structure, Double Diamond provides process

## Writing Guidelines

### Problem Statements

- ✅ "New users struggle to understand core value within first session"
- ✅ "Enterprise customers require compliance features we don't offer"
- ✅ "Users abandon checkout due to unclear shipping costs"
- ❌ "We need better onboarding"
- ❌ "The UI is confusing"
- ❌ "We should add X feature"

### Opportunity Framing

- ✅ "Enable users to quickly discover personalized content"
- ✅ "Help teams collaborate without friction"
- ✅ "Reduce time to first value realization"
- ❌ "Build a recommendation engine"
- ❌ "Add team features"
- ❌ "Make it faster"

### How Might We Questions

- ✅ "How might we help new users experience value in under 5 minutes?"
- ✅ "How might we make pricing transparent before checkout?"
- ✅ "How might we enable async collaboration?"
- ❌ "Should we build a tutorial?"
- ❌ "Can we add tooltips?"

## Review Schedule

### Daily Check-ins (During Active Exploration)

- Which phase are we in (discover/define/develop/deliver)?
- What did we learn yesterday?
- What are we exploring today?

### Weekly Synthesis

- Key insights from research/interviews
- Patterns emerging
- Updated opportunity map
- Next areas to explore

### Bi-weekly Milestone Reviews

- End of Discover → transition to Define
- End of Define → transition to Develop
- End of Develop → transition to Deliver
- Decision: Continue, pivot, or stop?

### Post-Delivery Retrospective

- What did we learn?
- How accurate were our assumptions?
- What would we do differently?
- Update team playbook

## Stakeholder Communication

### For Leadership

- Show the exploration process creates confidence, not delay
- Present problem-solution fit evidence
- Highlight options considered and why you chose this path
- Connect to business outcomes

### For Product Teams

- Make exploration collaborative, not PM-driven
- Share all research insights transparently
- Involve team in synthesis and framing
- Co-create solutions together

### For Design Teams

- Balance divergent creativity with convergent practicality
- Use prototypes to explore, not just validate
- Test with real users early and often
- Embrace quick, low-fidelity iteration

### For Engineering Teams

- Involve early in problem definition
- Get technical feasibility input during Develop phase
- Use their questions to challenge assumptions
- Co-design solutions with technical constraints in mind

## Common Challenges and Solutions

### "We don't have time to explore—just tell us what to build"

**Response pattern:**
"Exploration prevents building the wrong thing, which is far more expensive than spending 2-4 weeks understanding the problem first. Would you rather spend 1 month exploring and 2 months building the right thing, or 3 months building the wrong thing?"

### "We keep discovering new problems—when do we stop?"

**Response pattern:**
"Set a timebox. Spend 2 weeks in Discover, 1 week in Define, regardless of whether you feel 'done.' The goal isn't perfect understanding—it's sufficient confidence to move forward. You'll continue learning as you build."

### "We already know the solution—why waste time exploring alternatives?"

**Response pattern:**
"Compare-and-contrast decisions are better than yes/no decisions. Even if option A seems obvious, generating options B and C helps us understand WHY A is better and spot potential issues. It usually takes 30 minutes and dramatically improves decisions."

### "Our stakeholder has a specific solution in mind"

**Response pattern:**
"Great! Let's treat that as one solution option. What opportunity does it address? What are 2-3 other ways we could address that same opportunity? This helps us ensure we're solving the right problem and haven't missed a better approach."

## Best Practices

### Do's

- Start with the outcome/goal, not the solution
- Interview actual users, not just stakeholders
- Generate multiple solutions per opportunity (3+ minimum)
- Test assumptions cheaply before building
- Visualize your exploration (trees, maps, diagrams)
- Involve cross-functional team throughout
- Document your reasoning for future reference
- Timebox each phase to prevent analysis paralysis

### Don'ts

- Skip directly from problem to solution
- Conduct research in isolation without team synthesis
- Fall in love with your first idea
- Forget to validate with real users
- Let perfection prevent progress
- Do exploration as a one-time activity
- Assume you understand the problem without research
- Build before testing assumptions

## Exploration Success Metrics

Track these to know if your exploration is effective:

- **Solution fitness** - Does shipped solution move target metrics?
- **Assumption accuracy** - How many validated assumptions vs. invalidated?
- **Option generation** - Are teams considering 3+ solutions per opportunity?
- **Time to learning** - How quickly from problem to validated solution?
- **Team alignment** - Can everyone articulate the problem and why this solution?
- **User satisfaction** - Post-launch NPS or satisfaction scores

-----

## ⚠️ Common Pitfalls & Solutions

### Pitfall #1: Jumping to Solutions Too Quickly

**What it looks like:**

- First idea becomes "the solution"
- Skipping problem validation
- Building without exploring alternatives

**Why it happens:**

- Pressure to ship fast
- Solution already in mind
- Uncomfortable with ambiguity

**Solution:**

- Force yourself to generate 3+ solutions
- Timebound problem space work (2-3 weeks minimum)
- Use "Yes, and…" instead of "Yes, but…"
- Ask "What else could we build?"

-----

### Pitfall #2: Analysis Paralysis

**What it looks like:**

- Endless research without decisions
- Perfect understanding before moving forward
- Too many opportunities explored shallowly

**Why it happens:**

- Fear of making wrong choice
- Lack of clear decision criteria
- No timeboxing

**Solution:**

- Set explicit deadlines for each phase
- Use "Good enough for now, safe enough to try"
- Make small, reversible decisions
- Use 70% confidence threshold to act

-----

### Pitfall #3: Solo Exploration

**What it looks like:**

- PM does all research and presents conclusions
- Team not involved until build phase
- Lack of shared understanding

**Why it happens:**

- Efficiency mindset ("I'll be faster alone")
- Protecting team from "messy" research
- Old habits from waterfall

**Solution:**

- Include product trio in all interviews
- Do synthesis sessions together
- Share raw interview recordings
- Co-create solutions as team

-----

### Pitfall #4: Building Without Testing

**What it looks like:**

- Going from idea to full build
- Skipping prototype/test phase
- "We'll see if users like it after we ship"

**Why it happens:**

- Confidence in idea
- Pressure to deliver
- Don't know how to test cheaply

**Solution:**

- Always ask "How can we test this before building?"
- Use fake door tests, prototypes, landing pages
- Make "test first" a team norm
- Celebrate invalidated assumptions as wins

-----

### Pitfall #5: Falling in Love with Opportunities

**What it looks like:**

- Pursuing opportunities that don't move metrics
- Unable to deprioritize discovered needs
- "But customers said they wanted it"

**Why it happens:**

- Empathy for all customer pain
- Not tying opportunities to outcomes
- Difficulty saying no

**Solution:**

- Always connect opportunities to outcome
- Score opportunities by impact on metric
- Remember: You can't solve everything
- Document deprioritized opportunities for future

-----

## ✅ Exploration Checklist

### Before You Start

- [ ] Outcome clearly defined and measurable
- [ ] Success criteria established
- [ ] Product trio identified (PM, Designer, Engineer)
- [ ] Stakeholder expectations set
- [ ] Time blocked for discovery work
- [ ] Tools ready (interview scheduling, note-taking, synthesis)

### During Problem Space (Discover → Define)

- [ ] 8-15 customer interviews completed
- [ ] Diverse user segments included
- [ ] Synthesis sessions completed with team
- [ ] Patterns and themes identified
- [ ] Problem statement written and validated
- [ ] Success metrics defined
- [ ] HMW questions generated (10-15)
- [ ] Constraints and requirements documented

### During Solution Space (Develop → Deliver)

- [ ] 20+ solution ideas generated
- [ ] Ideas clustered and grouped
- [ ] 3-5 distinct concepts developed
- [ ] Low-fidelity prototypes created
- [ ] Key assumptions documented
- [ ] 5-8 usability tests per concept
- [ ] Concept selected with evidence
- [ ] MVP scoped and prioritized
- [ ] Build-measure-learn plan defined

### After Delivery

- [ ] Impact measured against success criteria
- [ ] Learnings documented
- [ ] Assumptions validated/invalidated recorded
- [ ] Team retrospective completed
- [ ] Process improvements identified
- [ ] Opportunity Solution Tree updated
- [ ] Next exploration topic identified

-----

## 📚 Resources & Tools

### Books

- **"Continuous Discovery Habits"** by Teresa Torres (OST)
- **"Sprint"** by Jake Knapp (Design Sprint, similar to Double Diamond)
- **"The Mom Test"** by Rob Fitzpatrick (Customer interviews)
- **"Competing Against Luck"** by Clayton Christensen (JTBD)
- **"Just Enough Research"** by Erika Hall (Research methods)

### Tools

**For Interviews:**

- Calendly (scheduling)
- Zoom (remote interviews)
- Otter.ai (transcription)
- Dovetail (research repository)

**For Synthesis:**

- Miro or Mural (virtual whiteboarding)
- FigJam (collaborative mapping)
- Notion (documentation)
- Airtable (opportunity tracking)

**For Prototyping:**

- Figma (design and prototypes)
- Maze (prototype testing)
- UsabilityHub (quick feedback)
- Loom (walkthrough videos)

**For Tree Management:**

- Miro/Mural (visual OST)
- ProductBoard (opportunity management)
- Notion (documentation)
- Simple Google Sheets (lightweight)

### Templates

**Interview Guides:**

- JTBD interview script
- Problem discovery script
- Usability testing protocol
- Concept testing guide

**Synthesis Templates:**

- Affinity mapping board
- Journey map template
- Opportunity Solution Tree canvas
- How Might We worksheet

-----

## References

- Research Interviews: `../2.2.1-Research-Interviews/README.md`
- Continuous Discovery Habits: `../2.2.2-Continuous-Discovery-Habits/README.md`
- Jobs to Be Done: `../2.2.3-Jobs-To-Be-Done/README.md`
- Opportunity Assessment: `../2.2.4-Opportunity-Assessment/README.md`
- PRD Framework: `../../2.3-Execution/2.1.4-PRD/README.md`
- Self-Reflection: `../../2.0-Foundations/2.0.3-Self-Reflection/README.md`

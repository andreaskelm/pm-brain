# Problem-Solution Space Exploration Framework

## Introduction

This framework helps product teams systematically explore ambiguous problems and generate multiple solution options before committing to building. Problem-solution space exploration is NOT about finding the quickest answer—it's about finding the RIGHT answer.

## Files

**Main Framework:**
- `1-problem-solution-space-framework.md` — Core framework overview, philosophy, selection guide, best practices, and common pitfalls

**Double Diamond:**
- `1-Double-Diamond/1-double-diamond-guide.md` — Complete Double Diamond process guide (Discover → Define → Develop → Deliver)
- `1-Double-Diamond/2-double-diamond-template.md` — Template for Double Diamond exploration

**Opportunity Solution Tree:**
- `2-Opportunity-Solution-Tree/1-opportunity-solution-tree-guide.md` — Complete Opportunity Solution Tree guide
- `2-Opportunity-Solution-Tree/2-opportunity-solution-tree-template.md` — Template for Opportunity Solution Tree

**Supporting Frameworks:**
- `3-Supporting-Frameworks/1-supporting-frameworks.md` — Jobs to Be Done, Five Whys, and How Might We methods

**Templates:**
- `2-problem-solution-space-template.md` — Master template to help choose and start with the right framework

## How to Use This Framework

### Step 0: Braindump & Explore (Critical!)

**Use prompts from:** [2-product-sense-prompts.md](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) → [Generic Step 0 (any framework)](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#generic-step-0-any-framework) and [Before User Research / Discovery](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#before-user-research--discovery).

**Quick start:** What problem are you trying to solve? What feels like the real problem? What assumptions? What biases might affect your exploration? If you had to explain this problem to a 5-year-old, what would you say? **See prompts file for full list.**

### Step 1: Review Framework
Read `1-problem-solution-space-framework.md` to understand exploration methods and framework selection

### Step 2: Choose Your Approach
- **Double Diamond:** For focused 6-12 week exploration with clear phases
- **Opportunity Solution Tree:** For continuous discovery practice
- **Both:** OST for continuous discovery, Double Diamond for focused sprints

### Step 3: Use Appropriate Guide & Template
- **Double Diamond:** Read `1-Double-Diamond/1-double-diamond-guide.md`, then use `1-Double-Diamond/2-double-diamond-template.md`
- **Opportunity Solution Tree:** Read `2-Opportunity-Solution-Tree/1-opportunity-solution-tree-guide.md`, then use `2-Opportunity-Solution-Tree/2-opportunity-solution-tree-template.md`
- **Supporting Methods:** Reference `3-Supporting-Frameworks/1-supporting-frameworks.md` for JTBD, Five Whys, and HMW

### Step 4: Explore Problem Space
Use discovery methods to understand the problem deeply

### Step 5: Define the Problem
Synthesize insights into a clear problem statement

### Step 6: Generate Solutions
Create multiple diverse solutions for the defined problem

### Step 7: Test and Select
Validate solutions with users and select the best option

### Step 8: Self-Reflection
After exploration, reflect:
- How did your understanding evolve?
- What surprised you?
- What would you do differently?

## When to Use

- Starting a new product or major feature
- Ambiguous problems needing exploration
- Multiple solution options to evaluate
- Need to align team on problem definition

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "problem-solution space", "double diamond", "opportunity solution tree", "explore the problem", "ambiguous problem", "not sure what to build", "multiple solutions"
- User is in: product_sense (during discovery braindump) or execution_mode (when user asks to explore problems)
- Prerequisites: User has an ambiguous problem or is conflating problem and solution
- User has: Some initial thinking about the problem (may be solution-focused and needs reframing)

**How to introduce:**
- "You're exploring an ambiguous problem and need to separate the problem space from solution space. Let's use Problem-Solution Space frameworks to systematically explore before committing to solutions."
- "Based on your thinking about [problem/feature], let's use this framework to ensure you understand the problem deeply before jumping to solutions."

**Framework selection (use selection guide in framework):**
- **Double Diamond:** Focused 6-12 week exploration with clear phases (Discover → Define → Develop → Deliver)
- **Opportunity Solution Tree:** Continuous discovery practice, multiple opportunities, connect solutions to outcomes
- **Both:** OST for continuous discovery, Double Diamond for focused sprints

**Common mistakes to avoid:**
- Don't suggest Problem-Solution Space if user already has a validated problem (suggest Opportunity Assessment or PRD instead)
- Don't suggest this if user is asking "how do I build X" and has clear requirements (suggest PRD instead)
- Don't skip braindump - exploration frameworks organize thinking, they don't create it
- Don't suggest Double Diamond if user needs quick exploration (suggest Opportunity Solution Tree or Research Interviews)
- Don't jump to solutions before exploring problem (must explore problem space first)

**When NOT to use Problem-Solution Space:**
- User already has validated problem and needs to assess opportunities (use Opportunity Assessment)
- User is ready to write requirements (use PRD - problem should be understood first)
- User needs one-time research for specific questions (use Research Interviews)
- User has clear, well-understood problem (use Opportunity Assessment or PRD)

**Cross-reference:** Problem-Solution Space often feeds into Opportunity Assessment (explored problem → opportunities) or Continuous Discovery Habits (problem exploration → ongoing discovery). If user completes exploration, suggest Opportunity Assessment next.

## Framework Selection Guide

**Use Double Diamond when:**
- Starting a new product or major feature
- Need cross-functional alignment on process
- Stakeholders need visibility into exploration
- Timeline allows for structured phases (8-12 weeks)

**Use Opportunity Solution Tree when:**
- Continuous discovery practice
- Multiple opportunities to evaluate simultaneously
- Need to connect solutions back to outcomes
- Want to maintain big-picture view over time

**Use both together when:**
- Major strategic initiatives
- OST for continuous discovery, Double Diamond for focused sprints
- OST provides structure, Double Diamond provides process

## How to Maintain

- **During Exploration**: Document learnings and update opportunity/solution maps
- **After Selection**: Archive exploration artifacts for future reference
- **Quarterly Review**: Review exploration effectiveness and improve process

## Links

- Research Interviews: `../2.2.1-Research-Interviews/README.md`
- Continuous Discovery Habits: `../2.2.2-Continuous-Discovery-Habits/README.md`
- Jobs to Be Done: `../2.2.3-Jobs-To-Be-Done/README.md`
- Opportunity Assessment: `../2.2.4-Opportunity-Assessment/README.md`
- Execution: `../../2.3-Execution/README.md` (PRD Framework)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)

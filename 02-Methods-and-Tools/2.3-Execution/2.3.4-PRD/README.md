---
title: Frameworks Decision Guide
---

# Purpose
Pick the right framework fast for your current discovery phase, entry trigger, and riskiest assumption.

## Introduction

This directory contains product management frameworks organized by purpose. Each framework is self-contained with principles, processes, and templates. Use the decision guide below to find the right framework for your current situation.

## How Frameworks Work Together

The frameworks follow a natural product development flow:

**Discovery → Define → Decide → Deliver → Launch & Learn**

1. **Discover** (2.2.2-Continuous-Discovery-Habits): Interview users, observe behavior, collect stories
2. **Define** (2.2.3-Jobs-To-Be-Done, 2.2.2-Continuous-Discovery-Habits): Frame problems as jobs and opportunities
3. **Decide** (2.2.4-Opportunity-Assessment, 2.2.5-Idea-Validation): Assess opportunities and validate assumptions
4. **Deliver** (2.3.4-PRD): Write requirements and build
5. **Launch & Learn** (2.1.2-Strategic-Execution/1-OKR, 2.1.2-Strategic-Execution/2-Roadmap): Measure outcomes and iterate

**Strategic Context:**
- **2.1.1-Strategic-Foundations**: Sets strategic direction (done first, informs everything)
- **2.1.2-Strategic-Execution/1-OKR**: Operationalizes strategy into measurable outcomes
- **2.1.2-Strategic-Execution/2-Roadmap**: Plans execution timeline
- **2.2.1-Newsletter**: Communicates progress

## How to Use This Directory

1. **Identify your entry point**: Use the decision map below to find the right starting framework
2. **Follow the flow**: Use framework outputs to determine next steps
3. **Maintain traceability**: Link documents together (JTBD → Opportunity → PRD → OKR)
4. **Iterate**: Frameworks are living processes, not one-time activities

## How to Maintain

- **Quarterly Review**: Review framework effectiveness and update based on learnings
- **After Major Changes**: Update frameworks when processes evolve
- **Version Control**: Track framework changes in git
- **Team Feedback**: Gather feedback on framework usability and effectiveness

## How to use
1) Identify your entry trigger and primary risk (desirability, usability, feasibility, viability).  
2) Start with the recommended framework below; capture outputs.  
3) Move to the next framework based on what the outputs unlock.

# PRD (Product Requirements Document) Framework

## Introduction

Use this framework and template to create product requirements documents that bridge discovery and execution, aligning cross-functional teams around what to build and how success will be measured.

## Files
- `1-prd-framework.md` — Complete PRD framework with principles, structure guidance, and quality checklist
- `2-prd-template.md` — Standard PRD template with sections for context, requirements, and success metrics
- `3-prd-jtbd-template.md` — Jobs-to-Be-Done focused PRD template for job-centered product work

## Before Using This Framework

⚠️ **Don't jump straight to templates.**

### 1. Read the Golden Rule

**See:** [`/PRODUCT-SENSE-RULES.md`](../../../../PRODUCT-SENSE-RULES.md)

**The rule:** Braindump before structure. Frameworks organize thinking—they don't create it.

### 2. Braindump First (15-20 min)

**Use the prompts:** [`02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-template.md`](../../../../02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-template.md)

Specifically, the "Before Writing a PRD" section:
- Who is this really for? (actual human, not persona)
- What job are they hiring this feature to do?
- Why hasn't this been solved already?
- What assumptions am I making?
- What could go catastrophically wrong?
- Why this, why now?

**Don't organize yet. Just think deeply and honestly.**

### 3. Then Use This Framework

After your braindump, use the PRD template to organize your thinking.

---

## How to use

### Step 1: Review Framework
Review the framework in `1-prd-framework.md` to understand PRD principles and when to use them

### Step 2: Choose Template
- Use `2-prd-template.md` for standard product requirements
- Use `3-prd-jtbd-template.md` when your work is centered around customer jobs

### Step 3: Structure Your Thinking
Start with section 3 (Goals & Success Metrics) then work outward - but use your braindump to inform each section

### Step 4: Quality Check
Use the quality checklist to ensure completeness before stakeholder review

### Step 5: Maintain
Maintain as living document; track changes in version history

### Step 6: Self-Reflection
After writing the PRD, reflect:
- How did your thinking evolve from your braindump?
- What did you learn? What surprised you?
- What biases did you catch? What would you do differently?
- How did your product sense guide you?

## When to Use
- After solution validation (passed RAT tests)
- For initiatives requiring >2 weeks engineering effort
- When cross-functional alignment is critical
- When clear success metrics can be defined

## How to Maintain

- **During Development**: Update open questions and decisions as they're resolved
- **Post-Launch**: Track success metrics and update post-launch plan section
- **Quarterly Reviews**: Archive completed PRDs and extract learnings

## Links
- Product Strategy: `../../2.1-Strategy/2.1.1-Strategic-Foundations/README.md`
- Jobs To Be Done: `../../2.2-Discovery/2.2.3-Jobs-To-Be-Done/README.md`
- Opportunity Assessment: `../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md`
- Idea Validation: `../../2.2-Discovery/2.2.5-Idea-Validation/README.md`
- OKR Framework: `../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md`


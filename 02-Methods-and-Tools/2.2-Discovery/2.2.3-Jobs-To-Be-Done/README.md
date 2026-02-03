# Jobs To Be Done Framework

## Introduction

Use this framework to understand the underlying jobs customers hire your product to do, focusing on progress rather than demographics. JTBD helps you understand why customers choose your product and what progress they're trying to make.

**When to use JTBD:**
- Understanding why customers choose your product over alternatives
- Reframing feature requests as customer progress
- Identifying unmet customer needs
- Designing solutions centered on customer jobs

**When JTBD might not be needed:**
- Technical infrastructure work with no direct customer impact
- Internal tooling where the "job" is obvious
- Very early exploration before customer understanding exists

## Files
- `1-jobs-to-be-done.md` — Complete JTBD framework including interview techniques and job mapping

## Before Using This Framework

⚠️ **Don't jump straight to job statements.**

### 1. Read the Golden Rule

**See:** [`/PRODUCT-SENSE-RULES.md`](../../../../PRODUCT-SENSE-RULES.md)

### 2. Braindump First (15 min)

**Use the prompts:** [`02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md`](../../../../02-Methods-and-Tools/2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md)

Specifically, the "Before Writing a PRD" section (User Understanding):
- Who is this really for?
- What are they currently doing instead? Why does that suck?
- What's the job they're hiring this feature to do?

**JTBD frameworks organize job understanding—they don't create empathy.**

### 3. Then Use This Framework

After your braindump, use JTBD to structure your understanding.

---

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "jobs to be done", "JTBD", "what job is the user hiring this for", "customer jobs", "user needs", "why do customers choose this"
- User is in: product_sense (during discovery braindump) or execution_mode (when user asks to understand users)
- Prerequisites: User is exploring user needs or trying to understand why customers choose their product
- User has: Some initial thinking about users/customers (may be incomplete or feature-focused)

**How to introduce:**
- "You're trying to understand why customers choose your product. Let's use Jobs-To-Be-Done to reframe this from features to the progress customers are trying to make."
- "Based on your thinking about [users/features], let's structure your understanding using JTBD to focus on the job, not the solution."

**Common mistakes to avoid:**
- Don't suggest JTBD if user already has validated jobs (suggest Opportunity Assessment or PRD instead)
- Don't suggest JTBD if user is asking "how do I build X" without understanding "why" (help them understand the job first)
- Don't skip braindump - JTBD organizes understanding, it doesn't create empathy
- Don't suggest JTBD if user needs demographic personas (suggest Personas framework instead - different lens)
- Don't create feature-focused job statements (focus on progress, not solutions)

**When NOT to use JTBD:**
- User already understands the job and needs to validate solutions (use Opportunity Assessment or Idea Validation)
- User needs demographic/psychographic personas (use Personas framework - HEART or demographic approach)
- User is ready to write requirements (use PRD - JTBD should inform PRD, not replace it)
- User is doing technical infrastructure work (JTBD may not apply)

**Distinction from Personas:**
- **JTBD:** Focuses on the job/progress customers seek (outcome-driven, situation-based)
- **Personas:** Focuses on who the user is (demographic/psychographic, HEART framework)
- **When to use JTBD:** Understanding why customers choose, reframing features as jobs, outcome-driven design
- **When to use Personas:** Need demographic segments, building empathy with specific user types, stakeholder alignment

**Cross-reference:** JTBD often feeds into Opportunity Assessment (jobs → opportunities) and PRD (jobs → requirements). If user has completed JTBD, suggest Opportunity Assessment next.

## How to Use This Framework

**Product sense exercise:**
- If you had to explain the customer's job in one sentence, what would it be?
- What would make you say "this is obviously not the job"?
- What would make you say "this is obviously the job"?

### Step 1: Identify the Job
Understand what progress customers are trying to make

### Step 2: Map Job Context
Document when, where, and why the job arises

### Step 3: Understand Alternatives
Research what customers currently hire to get the job done

### Step 4: Define Job Success
Determine how customers measure successful job completion

### Step 5: Design for Progress
Create solutions that enable the desired progress

### Step 6: Self-Reflection
After mapping jobs, reflect:
- How did your understanding of the job evolve?
- What biases did you catch? (Feature bias? Solution bias?)
- What does your product sense tell you about this job?
- What would you do differently next time?

## How to Maintain

- **After Interviews**: Update job stories as you learn more from customer research
- **Quarterly Reviews**: Reassess whether you're helping customers make progress
- **After Launches**: Validate that solutions enable job completion

## Links
- Research Interviews: `../2.2.1-Research-Interviews/`
- Continuous Discovery: `../2.2.2-Continuous-Discovery-Habits/README.md`
- Opportunity Assessment: `../2.2.4-Opportunity-Assessment/README.md`
- Idea Validation: `../2.2.5-Idea-Validation/README.md`
- Execution: `../../2.3-Execution/README.md` (PRD Templates)
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)

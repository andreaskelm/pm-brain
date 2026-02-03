# Personas Framework

## Overview

This framework provides two approaches for creating personas: HEART (human-centered) and JOBS (outcome-driven). Personas help teams build empathy and make user-centered decisions.

## Step 0: Braindump & Product Sense (Do this first!)

**Use prompts from:** [2-product-sense-prompts.md](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md) → [Generic Step 0 (any framework)](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#generic-step-0-any-framework) and [Before Writing a PRD](../../../../2.0-Foundations/2.0.1-Mental-Models/6-Product-Sense-Development/2-product-sense-prompts.md#before-writing-a-prd) (user understanding). Quick start: Who are your users? What segments matter most? What assumptions about users? What biases might affect your personas? **See prompts file for full list.**

**Product sense exercise:**
- If you had to pick ONE user type to focus on, who would it be? Why?
- What would make you say "these personas are obviously wrong"?
- What would make you say "these personas are obviously right"?

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "personas", "user personas", "target users", "user segments", "who are our users", "demographic segments"
- User is in: `execution_mode` (after braindump) or when user asks to create user personas
- Prerequisites: User needs to understand who their users are (demographic/psychographic understanding)
- User has: Some initial thinking about users (may be incomplete or job-focused)

**How to introduce:**
- "You want to build empathy with your users and create user-centered personas. Let's use the Personas framework to capture who your users are, their motivations, and their context."
- "Based on your thinking about [users/segments], let's structure this using Personas to create actionable user profiles."

**Framework selection:**
- **HEART Framework** - Human-centered, lightweight, focuses on motivations and triggers (good for early scoping, UX conversations)
- **JOBS Framework** - Outcome-driven, focuses on jobs-to-be-done (good when you want to connect personas to JTBD)

**Common mistakes to avoid:**
- Don't suggest Personas if user already understands jobs and needs outcome-focused thinking (suggest JTBD instead)
- Don't create demographic-only personas without motivations/context (use HEART framework)
- Don't suggest Personas if user is exploring why customers choose (use JTBD - different lens)
- Don't skip braindump - personas organize understanding, they don't create empathy
- Don't create too many personas (focus on 2-3 primary personas)

**When NOT to use Personas:**
- User is exploring why customers choose their product (use JTBD - job-focused, not person-focused)
- User already has validated jobs and needs to assess opportunities (use Opportunity Assessment)
- User is ready to write requirements (use PRD - personas should inform PRD, not replace it)
- User needs outcome-driven understanding (use JTBD - focuses on jobs, not demographics)

**Distinction from JTBD:**
- **Personas:** Focuses on WHO the user is (demographic, psychographic, HEART: Human/Emotions/Actions/Results/Triggers)
- **JTBD:** Focuses on WHAT job/progress the user seeks (situation-based, outcome-driven)
- **When to use Personas:** Need demographic segments, building empathy with specific user types, stakeholder alignment, UX design
- **When to use JTBD:** Understanding why customers choose, reframing features as jobs, outcome-driven design, solution-agnostic thinking

**Cross-reference:** Personas often feed into PRD (personas → requirements). If user has completed Personas, they may be ready for PRD or Opportunity Assessment.

-----

## HEART Framework

**Purpose:**
- Lightweight persona framework focused on human motivations and triggers.
- Keeps personas actionable and emotionally relatable for product decisions.

**Structure:**
- H — Human: identity, role, background, experience
- E — Emotions: motivations, frustrations, success feeling
- A — Actions: daily responsibilities, decision authority, collaboration style
- R — Results: key metrics, constraints, stakes
- T — Triggers: pain points, catalysts, blockers

**When to use:**
- Early product scoping, feature prioritization, UX conversations, stakeholder alignment.

**Notes:**
- Keep entries concise (1–3 bullet points per field).
- Update with real user data after interviews or telemetry.

-----

## JOBS Framework (Jobs-to-be-Done)

**Purpose:**
- Focuses on the core "job" the user hires a solution to complete.
- Best for discovering real user needs and outcome-driven design.

**Structure:**
- Job to be Done: the goal the user wants to achieve
- Trigger: event that makes the job urgent
- Outcome: success criteria / desired result
- Obstacles: what prevents the user from succeeding
- Context: when, where, and why the job appears

**When to use:**
- Feature ideation, prioritization, experiment design, messaging.

**Notes:**
- Capture verbs and context — JOBS is action-first.

-----

## References

- Personas Template: `2-personas-template.md`
- Strategy: `../../2.1-Strategy/README.md` (Strategic Foundations)
- Discovery: `../../2.2-Discovery/README.md` (Research Interviews, Jobs to Be Done)
- PRD Framework: `../2.3.4-PRD/README.md`
- Foundations: `../../2.0-Foundations/README.md` (Self-Reflection, Mental Models, Bias)

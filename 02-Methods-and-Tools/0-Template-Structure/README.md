# Template Structure System

This directory contains reusable templates and documentation for creating consistent, high-quality frameworks, guides, templates, and playbooks across the PM Brain repository.

## Purpose

Standardized templates ensure:
- **Clarity for junior PMs** - Clear structure, examples, and guidance
- **Efficiency for senior PMs** - Consistent patterns, less cognitive overhead
- **AI/LLM optimization** - Structured prompts and clear section markers enable better AI collaboration
- **Maintainability** - Consistent structure makes updates easier

## Quick Links

- **[Template Structure Guide](1-template-structure-guide.md)** - Comprehensive documentation explaining the system, pros/cons, and customization
- **[Quickstart Template](2-quickstart-template.md)** - For rapid introduction frameworks (5-10 min read)
- **[Full Framework Template](3-full-framework-template.md)** - For comprehensive frameworks (20-30 min read)
- **[Evaluation Template](4-evaluation-template.md)** - For structured assessment frameworks
- **[Template Decision Guide](5-template-decision-guide.md)** - Quick reference for choosing which template to use
- **[Domain README Template](6-readme-template-domain.md)** - For domain/section overviews (Strategy, Discovery, Communication, Foundations, Execution)
- **[Initiative README Template](7-readme-template-initiative.md)** - For initiative folders under `04-Initiatives/`

## How to Use These Templates

### When Creating a New Framework

1. **Choose your template type** using the [Template Decision Guide](5-template-decision-guide.md)
2. **Copy the appropriate template** (`2-quickstart-template.md`, `3-full-framework-template.md`, or `4-evaluation-template.md`)
3. **Customize for your domain:**
   - Strategy frameworks: Emphasize alignment, trade-offs, decision criteria
   - Discovery frameworks: Emphasize bias awareness, evidence gathering, validation
   - Communication frameworks: Emphasize audience, clarity, stakeholder management
   - Execution frameworks: Emphasize measurement, iteration, outcomes
4. **Follow the universal elements** from the [Template Structure Guide](1-template-structure-guide.md)
5. **Add domain-specific sections** as needed

### Template Variants

**Quickstart Template** - Use when:
- Framework is simple or well-understood
- Users need rapid introduction
- Time is constrained
- Onboarding new team members

**Full Framework Template** - Use when:
- Framework is complex or strategic
- Deep understanding is required
- Teaching/onboarding context
- Framework addresses nuanced decisions

**Evaluation Template** - Use when:
- Framework needs quality gates
- Peer review is required
- Improvement tracking is needed
- Objective assessment adds value

## Universal Elements (All Templates)

Every framework should include:

1. **Step 0: Braindump & Product Sense** - Prevents premature structuring, develops intuition
2. **Overview** - What it is, why it matters, when to use it
3. **Core Philosophy** - Principles and beliefs, what it's NOT
4. **Framework Structure** - How it's organized, key components
5. **How to Use** - Step-by-step process, practical guidance
6. **When to Use / When Not to Use** - Decision criteria, alternatives
7. **Common Pitfalls** - What goes wrong and how to avoid it
8. **Best Practices** - Do's and Don'ts
9. **References** - Links to related frameworks

## Examples

**Frameworks using Quickstart:**
- Strategy Blocks (`2.1-Strategy/2.1.1-Strategic-Foundations/1-Strategy-Blocks/2-quickstart.md`)

**Frameworks using Full Framework:**
- OKR Framework (`2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/1-okr-framework.md`)
- MoSCoW Prioritization (`2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/3-MoSCoW/1-moscow-prioritization-framework.md`)

**Frameworks using Evaluation:**
- OKR Evaluation (`2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/3-okr-evaluation.md`)
- Roadmap Evaluation (`2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/3-roadmap-evaluation.md`)

**Playbook Variants (Special Case):**
- Strategy Blocks Full Guide (`2.1-Strategy/2.1.1-Strategic-Foundations/1-Strategy-Blocks/1-full-guide.md`) - Detailed process playbook with week-by-week activities, roles, and deliverables

**Note:** Playbook variants are acceptable when frameworks require detailed process documentation beyond standard framework structure. They complement Quickstart/Full Framework guides and focus on operational execution rather than framework structure.

## File Naming Convention

When creating new frameworks, follow this pattern:

- `README.md` - Overview and navigation
- `1-[framework-name]-framework.md` - Main framework guide (use Quickstart or Full Framework template)
- `2-[framework-name]-template.md` - Fill-in-the-blanks template
- `3-[framework-name]-evaluation.md` - Evaluation framework (if applicable)

## AI Collaboration

All templates are optimized for AI/LLM collaboration:

- **Structured prompts** embedded in templates
- **Clear section markers** for AI parsing
- **Explicit "help me think" vs "think for me" guidance**
- **Product sense exercises** that provide context for AI

When using templates with AI:
1. Start with braindump prompts to provide context
2. Use product sense exercises to develop intuition
3. Let AI help structure your thinking, not replace it
4. Use evaluation templates for quality checks

## References

- Main Methods & Tools README: `../README.md`
- Guidelines: `../../GUIDELINES.md`
- Setup Guide: `../../SETUP.md`

# Strategy Document Template

### Document Structure & Detailed Content Guide

#### Executive Summary (1 page)

**Purpose:** Give busy stakeholders complete picture in 60 seconds

**Template:**
```markdown
# Executive Summary

## Context
We're developing this strategy because [primary catalyst - confusion about priorities, market changes, growth challenges, etc.]. Teams are struggling with [specific symptoms - unproductive debates, unclear roadmap priorities, disconnect between vision and execution].

## Strategic Pillars (Focus Areas)
Over the next 2 years, we will focus on:

1. **[Pillar 1 Name]**: [One sentence describing what this means]
2. **[Pillar 2 Name]**: [One sentence describing what this means]  
3. **[Pillar 3 Name]**: [One sentence describing what this means]

## Winning Aspiration
By [date 2 years from now]: [Your compelling headline describing success]

## Bottom Line
This strategy will [primary business outcome] by [primary mechanism]. We expect to see [key leading indicator] within [timeframe] and [key lagging indicator] by [longer timeframe].

## What This Means
- **For Product Teams**: Focus roadmaps on pillar-supporting initiatives
- **For Engineering**: Prioritize technical investments that enable pillar success
- **For Leadership**: Measure progress via [key metrics] and adjust resources accordingly
```

**Example Executive Summary:**
```markdown
# Executive Summary

## Context
We're developing this strategy because teams are confused about why we're building specific features over others, leading to unproductive roadmap debates and misaligned execution. Despite having clear mission/vision and detailed roadmaps, the connection between daily work and strategic outcomes isn't clear.

## Strategic Pillars (Focus Areas)
Over the next 2 years, we will focus on:

1. **Discovery & Findability**: Make advanced features easily discoverable so users can access the full value they're paying for
2. **Onboarding & Activation**: Get new users to their first successful outcome within their first session
3. **Platform & Extensibility**: Enable enterprise customers to integrate our tools into their existing workflows seamlessly

## Winning Aspiration
By Q4 2026: "DesignTool becomes the platform creative teams choose first, with 90% of users activating advanced features within 30 days and enterprise customers citing seamless workflow integration as our key differentiator."

## Bottom Line
This strategy will increase user retention and expand market reach by solving the core problems preventing users from getting full value from our product. We expect to see feature adoption rates improve within 6 months and enterprise deal velocity increase within 12 months.

## What This Means
- **For Product Teams**: Prioritize discovery improvements, onboarding redesign, and integration capabilities over new feature development
- **For Engineering**: Invest in search infrastructure, API improvements, and platform architecture
- **For Leadership**: Track feature adoption rates, activation metrics, and integration usage as primary success indicators
```

#### Section-by-Section Content Guidelines

**Section 2: Context / Why Now (1-2 pages)**

**Include:**
- Current situation assessment
- Key challenges identified through research
- Market/competitive dynamics creating urgency
- Connection to company mission and vision
- Why these specific choices make sense now

**Example Content:**
```markdown
## Context / Why Now

### Current Situation
Our product has grown to [X users] and [Y revenue], but we're seeing concerning trends:
- Feature adoption rates plateau at 40% for advanced capabilities
- Enterprise prospects cite "integration complexity" in 60% of lost deals  
- New user activation has declined from 65% to 52% over 18 months

### Research Insights
Leadership interviews revealed convergent themes around [theme 1] and [theme 2]. User research with 25 customers showed [key finding]. Behavioral data confirms [data insight with specific metrics].

### Market Dynamics
Competitors are investing heavily in [area], while the market is moving toward [trend]. Our window to establish leadership in [opportunity] is narrowing.

### Strategic Imperative
These pillars address our core growth constraints while leveraging our unique advantages in [strength 1] and [strength 2]. They connect directly to our mission of [mission statement] by [connection explanation].
```

**Section 3: Strategic Pillars (2-3 pages per pillar)**

**For Each Pillar Include:**

**Definition & Scope:**
```markdown
## Pillar 1: Discovery & Findability

### What This Means
Discovery & Findability focuses on making our advanced features easily discoverable and accessible to users who need them. Currently, 60% of users are unaware of features that would solve their daily problems.

### Scope
- In scope: Search functionality, navigation design, feature highlighting, progressive disclosure
- Out of scope: New feature development, basic functionality improvements
- Time horizon: 18-month major improvements, ongoing optimization thereafter
```

**Strategic Rationale:**
```markdown
### Why This Matters Strategically
**User Impact**: Research shows users who discover advanced features have 3x higher retention rates and expand usage by 40% within 6 months.

**Business Impact**: Feature adoption directly correlates with expansion revenue—each additional feature used increases customer LTV by $2,400.

**Competitive Advantage**: Our design-first culture and user research capabilities position us to solve discoverability better than engineering-first competitors.

**Evidence Base**:
- User interviews: 8/10 enterprise users mentioned "wish I knew about that sooner"
- Usage data: 85% of users never access tools that would save them 2+ hours weekly
- Support analysis: 40% of tickets are "how do I..." questions for existing features
```

**Success Vision:**
```markdown
### What Success Looks Like (2-Year Vision)
Users naturally discover relevant features through contextual suggestions and intuitive navigation. New enterprise users activate 80% of relevant features within 30 days. Support tickets about feature location decrease by 60%.

**Behavioral Changes We'll See:**
- Users exploring features proactively rather than reactively
- Enterprise administrators confidently onboarding team members
- Feature discovery becoming a source of delight rather than frustration
```

**Illustrative Concepts:**
```markdown
### How This Comes to Life
Our design sprint produced three concept directions:

**Smart Feature Suggestions**: Contextual feature recommendations based on user workflow patterns and goals

**Progressive Discovery Journey**: Guided feature introduction that reveals capabilities as users demonstrate readiness

**Visual Feature Mapping**: Interactive overview showing how different tools connect to user workflows

[Include concept sketches or mockups from design sprint]
```

**Measurement Framework:**
```markdown
### Success Metrics

**Primary Metrics**:
- Feature adoption rate: % users who use advanced features within 30 days
- Feature discovery rate: % users who find features through product vs. support

**Secondary Metrics**:
- Search success rate and query analysis
- Feature page engagement and conversion
- Time to feature adoption after signup

**Guardrail Metrics**:
- Overall user satisfaction (maintain >4.2/5)
- Core workflow completion rates (don't break existing flows)
- Performance impact (feature discovery shouldn't slow core tasks)

**Current Baselines**: [Include specific current numbers]
**Success Targets**: [Include specific goals where possible]
```

**Major Risks:**
```markdown
### Risks & Mitigation Strategies

**Risk 1: Making Interface More Complex**
- Mitigation: Test all discovery improvements with usability studies
- Early warning: User satisfaction scores or task completion times decline

**Risk 2: Over-Promoting Features Users Don't Need**  
- Mitigation: Personalization based on user role and usage patterns
- Early warning: Increased feature suggestion dismissal rates

**Risk 3: Technical Performance Impact**
- Mitigation: Performance budgets for all discovery features
- Early warning: Page load time or search response time degradation
```

**Section 4: Non-Goals (1 page)**

**Purpose:** Explicitly state what we will NOT focus on to maintain strategic discipline

**Template:**
```markdown
## Strategic Non-Goals

These are important areas that we will explicitly NOT prioritize during our 2-year strategy period:

### New Feature Categories
**What**: Developing entirely new product capabilities or entering adjacent markets
**Why Not Now**: Our focus is maximizing value from existing capabilities before expanding scope
**What We'll Stop**: Exploring [specific new features] that don't support core pillars

### Price Competition  
**What**: Competing primarily on price or building "good enough" low-cost alternatives
**Why Not Now**: Our differentiation comes from user experience and capability depth
**What We'll Stop**: Feature parity projects aimed at matching cheaper competitors

### Technical Debt Projects
**What**: Large-scale architecture rewrites or legacy system replacements  
**Why Not Now**: Unless directly enabling pillar success, technical improvements won't drive user value
**What We'll Stop**: Infrastructure projects that don't clearly connect to user outcomes

### Geographic Expansion
**What**: Entering new international markets or localization efforts
**Why Not Now**: Focus on deepening penetration in current markets before expanding geography
**What We'll Stop**: Localization research and international go-to-market planning
```

**Section 5: Success Measurement (1 page)**

**Include:**
- Key metrics definitions and current baselines
- Success targets where possible  
- Measurement cadence and review process
- Dashboard and reporting approach
- Leading vs. lagging indicator balance

**Section 6: Dependencies & Risks (1 page)**

**Categories:**
- Cross-functional dependencies (design, engineering, marketing)
- External dependencies (partnerships, vendors, compliance)
- Resource dependencies (hiring, budget, tools)
- Technical dependencies (platform capabilities, infrastructure)

**Section 7: Next Steps & Decision Framework (0.5 pages)**

**Include:**
- Immediate post-approval actions
- How teams will use strategy for prioritization
- Decision criteria for pillar-supporting vs. non-pillar initiatives
- Escalation process for off-strategy requests

# Backlog Prioritization Framework

## Overview

This framework helps you prioritize your product backlog using a systematic approach that combines strategic alignment, customer value, and practical constraints. Backlog prioritization translates strategic priorities into an ordered list of work items that teams can execute against.

**The problem:** Backlogs grow faster than teams can execute. Without clear prioritization, teams work on the wrong things, stakeholders push pet features, and strategic goals don't get executed.

**This framework:** Provides a repeatable process for making defensible prioritization decisions that connect strategy to execution.

## Step 0: Braindump & Product Sense (Do this first!)

**Before prioritizing, braindump:**
- What's in your backlog? List everything - don't structure yet.
- What does your product sense tell you should be priorities?
- What assumptions are you making about value and effort?
- What biases might affect prioritization? (Recency bias? Stakeholder pressure? Shiny object syndrome?)

**Product sense exercise:**
- If you could only build ONE thing from the backlog, what would it be? Why?
- What would make you say "this prioritization is obviously wrong"?
- What would make you say "this prioritization is obviously right"?
- Which items are you avoiding because they're hard, not because they're wrong?

**When to use backlog prioritization:**
- Sprint planning (immediate next items)
- Quarterly planning (3-month roadmap)
- Annual planning (strategic initiatives)
- Stakeholder negotiations (defending choices)
- Continuous refinement (ongoing backlog health)

**When this framework might not be needed:**
- Tiny backlog (<5 items) where priorities are obvious
- Emergency situations requiring immediate action
- Experimental phases with no clear direction yet

## How to Use This Framework

Backlog prioritization happens at **three levels**:

1. **Strategic Level** (Quarterly): Prioritize themes/initiatives aligned to OKRs
2. **Tactical Level** (Sprint Planning): Prioritize specific features/stories for upcoming sprint
3. **Continuous Level** (Ongoing): Refine and re-prioritize as new information emerges

**The process:**
1. **Categorize** backlog items by type
2. **Score** items using appropriate method
3. **Stack rank** within categories
4. **Balance** across strategic priorities
5. **Communicate** decisions with rationale

## How to Maintain

- **Weekly**: Groom backlog, add new items, update priorities
- **Sprint Planning**: Re-prioritize top 20-30 items for next sprint
- **Quarterly**: Full backlog review aligned to OKRs and roadmap
- **As Needed**: Adjust when strategy changes or new information emerges

## Principles

- **Strategy-aligned:** Backlog reflects strategic priorities (OKRs, roadmap)
- **Evidence-based:** Prioritization uses data, research, and clear criteria
- **Transparent:** Stakeholders understand why items are prioritized
- **Flexible:** Re-prioritize as context changes
- **Actionable:** Top items are ready to execute (clear, sized, dependencies resolved)

## Types of Backlog Items

Prioritize items differently based on type:

### 1. Strategic Initiatives (Themes)
- Large bodies of work aligned to OKRs
- Typically 1-3 months of work
- Example: "Improve onboarding conversion"

### 2. Features
- User-facing capabilities
- Typically 1-4 weeks of work
- Example: "Add social login"

### 3. Improvements
- Enhancements to existing features
- Typically days to 2 weeks
- Example: "Speed up search results"

### 4. Technical Debt
- Infrastructure, refactoring, tech improvements
- Variable effort
- Example: "Migrate to new database"

### 5. Bugs
- Defects affecting users
- Variable effort
- Example: "Fix payment error on checkout"

---

## The Prioritization Process

### Step 1: Categorize & Clean

**What:** Sort backlog items by type and ensure they're well-defined

**Actions:**
1. Tag each item with type (Initiative, Feature, Improvement, Tech Debt, Bug)
2. Ensure each item has:
   - Clear description
   - Rough effort estimate (T-shirt size: S/M/L/XL)
   - Strategic alignment (which OKR/goal it supports)
   - Owner/requestor
3. Archive or delete:
   - Duplicates
   - Items no longer relevant
   - "Someday/maybe" items not aligned to strategy

**Output:** Clean, categorized backlog

**Time:** 1-2 hours initially, 30 min weekly maintenance

---

### Step 2: Score Items Using Appropriate Method

**What:** Apply scoring framework based on item type and available data

**Choose your scoring method:**

#### For Strategic Initiatives (use RICE)
- **Reach:** How many users/month? (number)
- **Impact:** How much impact per user? (0.25/0.5/1/2/3)
- **Confidence:** How sure are you? (50%/80%/100%)
- **Effort:** Person-months (number)
- **Score = (Reach × Impact × Confidence) / Effort**

#### For Features (use ICE)
- **Impact:** Business impact (1-10)
- **Confidence:** How sure are we? (1-10)
- **Ease:** How easy to build? (1-10)
- **Score = (Impact × Confidence × Ease) / 3**

#### For Improvements & Tech Debt (use Value/Effort)
- **Value:** Customer value + business value (1-10)
- **Effort:** Development effort (1-10, inverse)
- Plot on 2×2 matrix:
  - High Value, Low Effort = Do First
  - High Value, High Effort = Do Second (strategic bets)
  - Low Value, Low Effort = Do Later (fill-ins)
  - Low Value, High Effort = Don't Do

#### For Bugs (use Severity × Frequency)
- **Severity:** Impact when it happens (1-10)
  - 10 = Data loss, security breach, complete blocker
  - 5 = Feature unusable, frequent errors
  - 1 = Minor cosmetic issue
- **Frequency:** How often it happens (% of users)
  - 100% = Everyone affected
  - 10% = Some users
  - 1% = Rare edge case
- **Priority Score = Severity × Frequency**

**Actions:**
1. For each item, apply appropriate scoring method
2. Document rationale (why this score?)
3. Link to supporting evidence (data, research, customer feedback)
4. Get input from engineering on effort estimates

**Output:** Scored backlog items

**Time:** 2-4 hours for full backlog, 15-30 min for new items

---

### Step 3: Stack Rank Within Categories

**What:** Order items within each category from highest to lowest priority

**Actions:**
1. **Within each category**, sort by score (highest first)
2. **Apply qualitative adjustments** for:
   - Dependencies (must do X before Y)
   - Strategic timing (aligned to launch dates)
   - Resource constraints (specialized skills needed)
   - Risk mitigation (addressing critical risks)
3. **Use the "swap test":** If two items have similar scores, would you trade their order? If no, keep them; if yes, adjust.

**Output:** Ranked list within each category

**Time:** 1-2 hours

---

### Step 4: Balance Across Strategic Priorities

**What:** Ensure overall backlog reflects strategic balance, not just scores

**Key balancing acts:**

#### Balance 1: Strategic Themes (align to OKRs)
- If you have 3 OKRs, roughly 33% of capacity should support each
- Check: Does top 20 reflect strategic distribution?

#### Balance 2: Short-term vs. Long-term
- **70% Execution:** Delivering on committed roadmap
- **20% Strategic:** Exploring new bets, innovation
- **10% Technical:** Tech debt, infrastructure, quality

#### Balance 3: User Segments
- Are you serving all key segments?
- Or over-indexing on one at expense of others?

#### Balance 4: Risk Profile
- Mix of safe bets (low risk, incremental value)
- And strategic bets (higher risk, transformational value)

**Actions:**
1. Review top 30 items across all categories
2. Check alignment to strategic priorities
3. Adjust order to achieve balance
4. Document trade-offs (why item X comes before item Y)

**Output:** Balanced, prioritized backlog

**Time:** 1 hour

---

### Step 5: Communicate Decisions

**What:** Make prioritization transparent with clear rationale

**Create prioritization artifacts:**

#### 1. Now/Next/Later Roadmap
- **Now (0-1 month):** Top 5-10 items currently in development
- **Next (1-3 months):** Items planned for upcoming sprints
- **Later (3+ months):** Important but not yet scheduled

#### 2. Prioritization Rationale Document
For each top 10 item, document:
- **What:** Brief description
- **Why now:** Strategic rationale
- **Score:** Quantitative score with breakdown
- **Trade-offs:** What we're NOT doing to do this
- **Dependencies:** What else must happen first/alongside

#### 3. Stakeholder Communication
- Share decisions with stakeholders
- Explain scoring criteria
- Highlight strategic alignment
- Be clear about what's NOT prioritized and why

**Actions:**
1. Create/update prioritization view in your tool (Jira, Linear, etc.)
2. Write brief rationale for top 10 items
3. Schedule stakeholder review meeting
4. Prepare to defend choices with data

**Output:** Transparent, communicated priorities

**Time:** 1-2 hours

---

## Scoring Reference Tables

### RICE Scoring Table (Strategic Initiatives)

| Item | Reach (users/mo) | Impact (0.25-3) | Confidence (%) | Effort (person-mo) | Score |
|------|------------------|-----------------|----------------|-------------------|-------|
| Improve onboarding | 10,000 | 2 | 80% | 3 | 5,333 |
| Add social login | 10,000 | 0.5 | 100% | 1 | 5,000 |
| Build analytics dashboard | 500 | 1 | 50% | 4 | 63 |

**Formula:** (Reach × Impact × Confidence) / Effort

### ICE Scoring Table (Features)

| Item | Impact (1-10) | Confidence (1-10) | Ease (1-10) | Score |
|------|---------------|-------------------|-------------|-------|
| Email notifications | 8 | 9 | 7 | 8.0 |
| Dark mode | 4 | 8 | 9 | 7.0 |
| Export to PDF | 5 | 6 | 4 | 5.0 |

**Formula:** (Impact + Confidence + Ease) / 3

### Bug Priority Matrix

| Severity → Frequency ↓ | Critical (10) | High (7) | Medium (5) | Low (2) |
|------------------------|---------------|----------|------------|---------|
| **Everyone (100%)** | 1000 - P0 | 700 - P1 | 500 - P1 | 200 - P2 |
| **Many (50%)** | 500 - P1 | 350 - P1 | 250 - P2 | 100 - P3 |
| **Some (10%)** | 100 - P2 | 70 - P2 | 50 - P3 | 20 - P4 |
| **Few (1%)** | 10 - P3 | 7 - P4 | 5 - P4 | 2 - P5 |

**Priority Levels:**
- P0: Drop everything, fix now
- P1: Fix in current sprint
- P2: Fix in next sprint
- P3: Backlog, prioritize normally
- P4-P5: Fix when convenient or won't fix

---

## Common Prioritization Patterns

### Pattern 1: Sprint Planning
**Context:** Prioritizing work for 2-week sprint

**Process:**
1. Start with top 20 items from backlog
2. Filter to items marked "ready" (clear, estimated, unblocked)
3. Balance across:
   - Strategic work (aligned to OKRs)
   - Bug fixes (critical + high priority)
   - Tech debt (10-20% of capacity)
4. Check capacity: Do items fit in sprint?
5. Commit to top N items that fit

**Output:** Sprint backlog (committed work)

### Pattern 2: Quarterly Planning
**Context:** Planning roadmap for next quarter

**Process:**
1. Review OKRs for the quarter
2. Identify strategic initiatives that support OKRs
3. Score initiatives using RICE
4. Stack rank initiatives
5. Allocate capacity (70% to top initiatives, 20% to strategic bets, 10% to tech debt)
6. Break down top initiatives into features
7. Create Now/Next/Later roadmap

**Output:** Quarterly roadmap

### Pattern 3: Stakeholder Negotiation
**Context:** Stakeholder wants to prioritize their feature

**Process:**
1. Score their request using appropriate method
2. Show them current top 10 with scores
3. Ask: "Which of these should we de-prioritize to do yours?"
4. Discuss trade-offs explicitly
5. If score warrants, add to backlog at appropriate priority
6. If not, explain criteria and offer alternative (later timing, reduced scope, etc.)

**Output:** Decision + rationale documented

---

## Decision Trees

### Which Scoring Method to Use?

```
START: Need to prioritize backlog items?
│
├─ Is it a strategic initiative (months of work)?
│  └─ YES → Use RICE scoring
│     (Need reach data and effort estimates)
│
├─ Is it a feature (weeks of work)?
│  └─ YES → Use ICE scoring
│     (Qualitative assessment of impact/confidence/ease)
│
├─ Is it an improvement or tech debt?
│  └─ YES → Use Value/Effort matrix
│     (Plot on 2×2, qualitative assessment)
│
├─ Is it a bug?
│  └─ YES → Use Severity × Frequency
│     (How bad × How often = Priority)
│
└─ Not sure what it is?
   └─ Define it better first, then categorize
```

### When to Re-Prioritize?

```
Should you re-prioritize the backlog?
│
├─ Strategy changed (new OKRs, pivot)?
│  └─ YES → Full re-prioritization
│
├─ Major new information (research, data)?
│  └─ YES → Re-score affected items
│
├─ Stakeholder escalation?
│  └─ Evaluate using scoring framework
│     ├─ Scores higher than current top 10? → Adjust
│     └─ Scores lower? → Explain and hold firm
│
├─ Regular cadence (weekly grooming)?
│  └─ YES → Light updates (new items, small adjustments)
│
└─ No significant changes?
   └─ Keep current priorities, execute
```

---

## Common Pitfalls & Solutions

### Pitfall 1: Analysis Paralysis
**Problem:** Spending too long scoring and debating priorities
**Solution:** 
- Use timeboxes: 30 min for initial scoring, 1 hour for debate
- Focus on top 20 items (ignore long tail)
- Good enough > perfect
- Re-prioritize quarterly, not constantly

### Pitfall 2: HiPPO (Highest Paid Person's Opinion)
**Problem:** Senior stakeholder overrides data-driven prioritization
**Solution:**
- Make scoring transparent and documented
- Frame as trade-offs: "To do X, we won't do Y"
- Show impact on OKRs/strategy
- Offer to re-score their item with them to show it doesn't make top 10

### Pitfall 3: Everything is P0
**Problem:** Stakeholders mark everything critical, diluting priorities
**Solution:**
- Define clear P0 criteria (production down, data breach, etc.)
- Limit P0 to truly critical (aim for <5% of backlog)
- Make trade-offs explicit: "If everything is P0, nothing is"
- Use objective scoring, not stakeholder labels

### Pitfall 4: Ignoring Technical Debt
**Problem:** Only prioritizing features, letting tech debt accumulate
**Solution:**
- Reserve 10-20% capacity for tech debt
- Make tech debt costs visible (slower velocity, more bugs)
- Frame tech debt as enablers: "Refactor enables faster feature development"
- Include tech debt in strategic discussions

### Pitfall 5: Optimizing for Easy, Not Important
**Problem:** Prioritizing quick wins over strategic impact
**Solution:**
- Balance across effort (some quick wins, some big bets)
- Check: Are we shipping features or moving metrics?
- Use outcome-oriented scoring (impact, not ease)
- Question: "Are we avoiding this because it's hard or because it's wrong?"

### Pitfall 6: Not Saying No
**Problem:** Accepting all requests, backlog grows infinitely
**Solution:**
- Archive items not aligned to strategy
- Explicit "Not Doing" list with rationale
- Set capacity constraints (realistic about what team can do)
- Frame as "Not now" rather than "Never"

### Pitfall 7: Stale Backlog
**Problem:** Old items never reviewed or cleaned up
**Solution:**
- Quarterly backlog grooming
- Auto-archive items >6 months old with no activity
- If not worth prioritizing in 6 months, probably not worth keeping
- Fresh start: Delete everything, rebuild from strategy

---

## Combining with Other Frameworks

### Backlog Prioritization + OKRs
**Connection:** OKRs define outcomes, backlog defines how to achieve them
**Usage:**
1. Start with quarterly OKRs
2. For each Key Result, identify backlog items that move it
3. Prioritize items that support KRs
4. Check balance: Does backlog reflect OKR distribution?

### Backlog Prioritization + Roadmap
**Connection:** Roadmap is public commitment, backlog is full set of options
**Usage:**
1. Roadmap = top 10-20 backlog items + rough timing
2. Backlog = everything else, prioritized but not committed
3. Update roadmap from backlog after quarterly planning
4. Backlog provides flexibility when roadmap needs adjusting

### Backlog Prioritization + Continuous Discovery
**Connection:** Discovery identifies opportunities, prioritization sequences them
**Usage:**
1. Discovery generates opportunities (problems to solve)
2. Add opportunities to backlog as initiatives/features
3. Score using RICE/ICE based on research insights
4. Highest-scoring opportunities become roadmap items

### Backlog Prioritization + PRDs
**Connection:** Top backlog items need PRDs before development
**Usage:**
1. Top 5 backlog items should have PRDs
2. Next 10 need problem statements (lite PRDs)
3. Everything else is just backlog item (description + score)
4. Promote items to PRD as they rise in priority

---

## Templates & Tools

### Backlog Item Template
Use `2-backlog-item-template.md` to document individual backlog items with scoring and rationale.

### Prioritization Decision Log
Use `3-prioritization-decision-log-template.md` to document prioritization decisions, trade-offs, and rationale after each major prioritization session.

---

## Success Indicators

**You've succeeded when:**
- Team always knows what to work on next (top items are clear)
- Stakeholders understand and accept priorities (transparent rationale)
- Backlog reflects strategic priorities (alignment to OKRs)
- Top items are ready to execute (clear, estimated, unblocked)
- Decisions are defensible (data-backed, documented)
- Re-prioritization is rare (only when context significantly changes)
- Team velocity improves (working on right things, not thrashing)

**Red flags you need to revisit:**
- ❌ Constantly re-prioritizing (no stability)
- ❌ Stakeholders confused about priorities
- ❌ Team working on low-priority items
- ❌ Backlog growing faster than execution
- ❌ Strategic goals not moving despite shipping
- ❌ Frequent "urgent" interruptions

---

## Cadence & Time Investment

### Initial Setup
- **First time:** 4-6 hours
  - 1-2 hours: Clean and categorize backlog
  - 2-3 hours: Score all items
  - 1 hour: Stack rank and balance

### Ongoing Maintenance
- **Weekly grooming:** 30-60 minutes
  - Add new items
  - Update scores as context changes
  - Adjust top 20 based on progress
  
- **Sprint planning:** 1-2 hours
  - Review top 20
  - Identify ready items
  - Commit to sprint

- **Quarterly planning:** 3-4 hours
  - Full backlog review
  - Re-score based on new OKRs
  - Rebalance strategic priorities

---

## References

### Prioritization Methods (Deep Dives)
- RICE/ICE Scoring: `../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/1-RICE-ICE/1-RICE-ICE-scoring-framework.md`
- Value/Effort Matrix: `../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/2-Value-Effort-Matrix/README.md`
- MoSCoW: `../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/3-MoSCoW/README.md`
- Kano Model: `../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/4-Kano-Model/README.md`

### Related Frameworks
- OKR Framework: `../../2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/README.md` (defines outcomes to optimize for)
- Roadmap: `../../2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/README.md` (public view of top priorities)
- PRD Framework: `../2.3.4-PRD/README.md` (detailed specs for top items)
- Opportunity Assessment: `../../2.2-Discovery/2.2.4-Opportunity-Assessment/README.md`

### Mental Models
- Outcome vs. Output: `../../2.0-Foundations/2.0.1-Mental-Models/2-Product-Thinking/1-outcome-vs-output.md`
- Feature Factory: `../../2.0-Foundations/2.0.1-Mental-Models/2-Product-Thinking/3-feature-factory.md`
- Opportunity Cost: `../../2.0-Foundations/2.0.1-Mental-Models/1-Decision-Making/5-opportunity-cost.md`

### Company Context
- Product Strategy: `../../../01-Company-Context/1-company-vision.md`
- Current OKRs: `../../../01-Company-Context/2-company-strategy.md`
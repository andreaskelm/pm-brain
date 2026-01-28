# 0.1 Learning Log

**Purpose:** Synthesize daily practice into weekly insights and monthly patterns.

Your thinking over time. Not just what you did, but what you learned.

-----

## What's in This Folder

### Structure

```
0.1-Learning-Log/
├── templates/
│   ├── 1-weekly-reflection-template.md
│   └── 2-monthly-synthesis-template.md
└── [Year]-Q[#]/
    ├── week-01.md
    ├── week-02.md
    ├── week-03.md
    ├── week-04.md
    └── monthly-[month].md
```

### Templates (templates/)

#### 1-weekly-reflection-template.md
Structured template for Sunday evening reflections.

**Sections:**
- Practice summary (what exercises you did)
- Decisions made (from daily log)
- Key insights (patterns noticed)
- What worked / didn't work
- Next week focus

**Time:** 30 minutes

#### 2-monthly-synthesis-template.md
Structured template for end-of-month synthesis.

**Sections:**
- Month overview
- Practice consistency
- Decision quality (retrospectives)
- Patterns across weeks
- Growth trajectory
- Next month focus

**Time:** 60 minutes

### Your Logs ([Year]-Q[#]/)

Quarterly folders containing your actual reflections.

**Example: `2026-Q1/`**
- `week-01.md` through `week-13.md`
- `monthly-jan.md`, `monthly-feb.md`, `monthly-mar.md`

-----

## Workflow

### Daily → Weekly → Monthly → Quarterly

```
Daily Log (5 min)
   ↓
Weekly Reflection (30 min)
   ↓
Monthly Synthesis (60 min)
   ↓
Quarterly Review (90 min)
```

**The pattern:** Compress daily noise into weekly signal into monthly patterns.

-----

## Weekly Reflection (Sunday Evening, 30 min)

### Process

1. **Review your daily log for the week**
   ```bash
   # Read last 7 days
   tail -50 ../1-daily-log-2026-Q1.md
   ```

2. **Copy the weekly template**
   ```bash
   cp templates/1-weekly-reflection-template.md 2026-Q1/week-04.md
   ```

3. **Fill it out:**
   - What practice did you do? (Tally from daily log)
   - What decisions did you make? (Copy from daily log)
   - What patterns did you notice? (Synthesize)
   - What worked well? What didn't?
   - What's your focus for next week?

4. **Commit (optional):**
   ```bash
   git add 2026-Q1/
   git commit -m "reflection: Week 4 synthesis"
   ```

### What Makes a Good Weekly Reflection

**Good:**
- "I noticed I avoid user research when I'm uncertain about my hypothesis"
- "3 decisions this week, all reversible, shipped all 3 - good bias toward action"
- "Cross-domain exercise sparked idea that's now in sprint planning"

**Bad:**
- "Did 3 exercises this week" (just reporting, not reflecting)
- "Week was busy" (not specific enough)
- "Everything was fine" (not honest enough)

**The goal:** Surface patterns you wouldn't see day-to-day.

-----

## Monthly Synthesis (Last Sunday, 60 min)

### Process

1. **Review all weekly reflections for the month**
   ```bash
   ls 2026-Q1/week-*.md
   cat 2026-Q1/week-{01,02,03,04}.md
   ```

2. **Copy the monthly template**
   ```bash
   cp templates/2-monthly-synthesis-template.md 2026-Q1/monthly-jan.md
   ```

3. **Fill it out:**
   - Month overview (what happened?)
   - Practice consistency (how many days/weeks?)
   - Decision retrospectives (check review dates from daily log)
   - Patterns across weeks (themes emerging?)
   - Growth trajectory (compare to previous months)
   - Next month focus (what to work on?)

4. **Update related files:**
   - Self-assessment (`../self-assessment-2026-Q1.md`, if you create one)
   - Growth portfolio (`../0.2-Growth-Portfolio/`)

5. **Commit:**
   ```bash
   git add 2026-Q1/ ../0.2-Growth-Portfolio/
   git commit -m "reflection: January monthly synthesis and portfolio update"
   ```

### What Makes a Good Monthly Synthesis

**Good:**
- "Customer insight rating increased from 3.0 to 3.5 - evidence: 4 user observations, caught 2 assumptions before building"
- "Recurring blind spot: I underestimate technical complexity - 3 projects this month took 2x longer than estimated"
- "Best decision: Killed feature X early - saved 4 weeks of work - confidence calibration improving"

**Bad:**
- "Did 20 exercises this month" (counting, not learning)
- "Still working on getting better" (vague)
- "Good month" (no specifics)

**The goal:** Connect dots across weeks. Identify trajectory. Calibrate judgment.

-----

## Git Strategy

### Depends on Your Mode

Your PM-Brain can run in three modes: **Public**, **Private**, or **Team**. What gets committed depends on your mode.

**🌍 Public Mode (Default):**
- ✓ Everything tracked: daily logs, reflections, syntheses, growth portfolio
- Best for: Building public learning portfolio

**🔒 Private Mode:**
- ✗ Personal content ignored: logs, reflections, syntheses all private
- ✓ Only templates and frameworks tracked
- Best for: Confidential company work

**👥 Team Mode:**
- ✗ Personal content ignored: logs, reflections, syntheses private
- ✓ Templates and frameworks tracked for team sharing
- Best for: Collaborative framework development

**To check or change your mode:** See `00-Meta/README.md` or run `bash 00-Meta/SETUP.sh`

### General Guidance

Regardless of mode:
- Weekly reflections are synthesized (less raw than daily logs)
- Monthly syntheses show growth trajectory
- Templates help your team (always shareable)

**Rule of thumb:** If it helps your team or future you, and your mode allows it, commit it. Otherwise, keep it local.

-----

## Making This Work

### Schedule It

- [ ] **Sunday 7pm:** Weekly reflection (30 min)
- [ ] **Last Sunday of month:** Monthly synthesis (60 min)

**Put these on your calendar. Treat them like 1:1s with yourself.**

### Don't Skip

**Weekly reflections are the most valuable part of this system.**

Daily practice → without weekly synthesis → just activity, not learning

Weekly synthesis → connects dots → actual insight

**If you only do one thing from this entire system, do weekly reflections.**

### Be Honest

These reflections are private (unless you choose to share).

No one is grading you.

The more honest you are, the faster you improve.

**Patterns you don't acknowledge are patterns you can't fix.**

-----

## Common Questions

### "What if I miss a week?"

**It's fine.** Don't try to backfill perfectly.

When you resume:
- Skim your daily log for what you missed
- Note any major insights or decisions
- Move forward

**Consistency > perfection.**

### "Should I share my reflections with my manager?"

**Maybe.**

**Do share:**
- Monthly syntheses when they show growth
- Decision retrospectives that demonstrate learning
- Patterns that inform your development plan

**Don't share:**
- Raw daily logs (too noisy)
- Every weekly reflection (too much detail)
- Reflections that are purely personal

**Share the signal, not the noise.**

### "How long until I see patterns?"

**Timelines:**
- **1 month:** You'll notice immediate habits (good and bad)
- **3 months:** Patterns become clear across decisions
- **6 months:** You can see trajectory and growth
- **1 year:** The compounding is obvious

**The longer you do this, the more valuable it becomes.**

-----

## Examples

### Week-level insight

```
## Week 4 - January 2026

**Practice:** 4/5 days (10-min exercises)
**Weekly deep work:** Product teardown of Notion

**Decisions Made:**
1. Shipped feature X using approach B (reversible, fast iteration)
2. Killed feature Y exploration (low impact, high complexity)
3. Escalated Z decision to leadership (couldn't align stakeholders)

**Pattern Noticed:**
I'm getting better at killing things early. 6 months ago I would have 
explored feature Y for 2 weeks before realizing it wasn't worth it.

**Next Week Focus:**
Do 2 user observation sessions. I've been designing without watching users.
```

### Month-level insight

```
## January 2026 Synthesis

**Overview:** Shipped 3 features, killed 2, started new initiative

**Practice Consistency:** 18/23 workdays (78%) - good rhythm established

**Decision Retrospectives:**
- Feature X (from week 1): Shipped, performing well, decision was right
- Feature Y (from week 2): Killed early, saved time, good call
- Initiative Z (from week 4): Too early to tell, check back in March

**Patterns Across Weeks:**
- I'm biasing toward action on reversible decisions (good)
- I still avoid user research when uncertain (need to fix)
- My "why" explanations are getting deeper (stakeholders noticed)

**Growth Trajectory:**
Customer Insight: 3.0 → 3.5 (evidence: 6 observations, 2 interviews)
Strategic Judgment: 3.5 → 4.0 (evidence: 2 early kills, faster decisions)

**February Focus:**
- Force 1 user observation per week (calendar block)
- Practice contrarian thinking (weekly exercise rotation)
```

-----

## Remember

**Reflection turns experience into learning.**

Without reflection, you repeat the same mistakes.

With reflection, you compound improvements.

**30 minutes on Sunday evening = dramatically better product sense.**

-----

## Quick Links

- **Weekly template:** `templates/1-weekly-reflection-template.md`
- **Monthly template:** `templates/2-monthly-synthesis-template.md`
- **Your daily log:** `../1-daily-log-YYYY-QX.md`
- **Self-assessment:** `../self-assessment-YYYY-QX.md` (if you choose to keep one here)
- **Growth portfolio:** `../0.2-Growth-Portfolio/`

**Block Sunday evening. Do your weekly reflection. Watch your product sense compound.**

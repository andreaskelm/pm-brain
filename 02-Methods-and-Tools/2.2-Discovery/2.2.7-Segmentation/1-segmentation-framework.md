# Segmentation Framework

## For Agents: When to Suggest This Framework

**Trigger conditions:**
- User mentions: "segment our market", "segment customers", "who should we serve first", "different customer groups", "JTBD then what", "after job interviews"
- User is in: product_sense (after braindump) or execution_mode (when user has done JTBD research and wants to structure segments)
- Prerequisites: User has JTBD research (job stories from interviews) or is planning discovery and wants to know the full flow
- User has: Job stories or interview output; may have many job variants and need to group them

**How to introduce:**
- "You've got job stories from JTBD research. The next step is to group similar jobs into segments so you can decide who to serve first and how to build and message for them. The Segmentation framework helps you go from 20–30 job stories to 3–5 actionable segments."
- "Before building personas, define segments. Segments are strategic (what to build, who to serve); personas are execution (how to market and design). This framework bridges JTBD and Personas."

**Common mistakes to avoid:**
- Don't suggest segmentation if user hasn't done any job research (suggest JTBD or Research-Interviews first)
- Don't let users segment by demographics alone; steer toward job-based segmentation
- Don't suggest creating 10+ segments; 3–5 max, with 1–2 prioritized
- Don't skip validation; segments should be testable (qualitative and, if possible, quantitative)

**When NOT to use this framework:**
- User only needs prioritization between known options (use 2.1.2/4-Prioritization)
- User has no job research yet (use JTBD first)
- User is optimizing an existing product by usage patterns only (mention behavioral segmentation briefly; see 2.3.6-Metrics for usage/cohort analysis)

---

## Goal

Group customers by the **job they are trying to do**, not by who they are. Use segments to decide what to build, how to position, and who to serve first. Segments drive strategy; personas (created from priority segments) drive execution.

> **Before using this framework:** Braindump first. What do you think your main customer groups are? What jobs keep coming up in interviews? What would "different enough to matter" look like? Then use this framework to structure your thinking.

## Core Principle: Segment by Jobs, Not Demographics

The same person can be in different segments depending on the job they're in. Different people in different demographics can be in the same segment if they share the same job.

- **Bad:** "Small business owners" (demographic, not actionable)
- **Good:** "Solopreneurs who need to look professional without admin overhead" (job + context)

Segment by:
1. **Job** — What progress they're trying to make (When / I want to / So I can)
2. **Context** — Frequency, urgency, environment (solo vs team, critical vs nice-to-have)
3. **Forces** — Push, Pull, Anxiety, Habit profiles (different force profiles = different segments)
4. **Outcomes** — How they measure success (speed, quality, risk, status)

## When to Use

**Use when:**
- You have (or will have) 15–30+ JTBD job stories and need to group them
- You're deciding which customer groups to serve first
- You're building personas and want them grounded in validated segments
- You need different messaging, features, or pricing by group

**Don't use when:**
- You have no job research yet (do JTBD first)
- You're only optimizing by usage (e.g. power vs casual users); use behavioral signals and 2.3.6-Metrics; mention in framework below
- You need one-off prioritization between initiatives (use 2.1.2/4-Prioritization)

## The Process

### 1. Job clustering (from JTBD stories to 3–5 segments)

- **Input:** Job stories from JTBD (2.2.3) — When / I want to / So I can, plus forces and context.
- **Steps:**
  - Extract dimensions per job: desired outcome type, frequency, urgency, context, primary push/pull, current solution, willingness to pay.
  - Group jobs that share the same core outcome, similar forces, and could be served with similar features.
  - Name 5–10 job families, then consolidate to **3–5 market segments** (combine families that could use ~80% same features, similar WTP, similar channels).
- **Output:** 3–5 segment clusters ready for definition.
- **Template:** Use [2-segment-definition-template.md](2-segment-definition-template.md) (job clustering dimensions and consolidation criteria are in the template).

### 2. Segment definition

- For each cluster, fill one segment definition (job statement, context, forces, success criteria, market sizing, who has this job, competitive set, product/GTM implications).
- **Output:** One segment definition per segment (use the same template).
- **Quality:** Segments should be mutually exclusive, collectively exhaustive for your scope, and meaningfully different (different features, messaging, or pricing).

### 3. Validation

- **Qualitative:** 5–10 interviews per segment (or 10–15 if you have bandwidth). Do they recognize themselves in the segment description? Same competitive set? Same success criteria?
- **Quantitative:** Survey (e.g. 50–100+ respondents) with job-screening and force questions. Do segment sizes and patterns match your hypotheses?
- **Behavioral (optional):** If you have product/usage data, check whether behavior aligns with segment (e.g. different feature use, retention by segment).
- **Output:** Validated / Revise / Merge / Split / Reject per segment. Update definitions and iterate.

### 4. Integration with personas

- **Segments = strategy** (which markets to serve, what to build, how to price).
- **Personas = execution** (how to market, how to design, who to target).
- Create 1–2 personas **per priority segment** using 2.3.5-Personas. Same segment can have multiple personas (e.g. different channels, copy tone); same persona type can appear in different segments when the job changes.
- **Workflow:** Define segments (this framework) → Prioritize which 1–2 segments to serve (2.1.2/4-Prioritization) → Create personas for those segments (2.3.5-Personas).

## Connection to Other Frameworks

| Framework | Role |
|-----------|------|
| **JTBD (2.2.3)** | Provides job stories and forces; segmentation clusters those jobs into segments. |
| **Problem-Solution Space (2.2.6)** | Validates which problems matter to which segments; different segments can have different problem priorities. |
| **Personas (2.3.5)** | Personas are derived from priority segments; segments define *what* to build, personas define *how* to execute. |
| **PMF (2.2.8)** | Assess PMF by segment when possible; one segment may have strong PMF while another does not. |
| **Prioritization (2.1.2/4)** | Use to choose which 1–2 segments to serve first; don't invent a separate segment-prioritization system. |

## Example: Note-Taking App (3 segments)

**Segment 1: "Capture Chaos"**
- **Job:** When ideas hit me randomly, I want to capture them instantly, so I don't lose important thoughts.
- **Context:** Multiple times daily, immediate urgency, solo, often mobile.
- **Forces:** Push = ideas lost before writing; Pull = frictionless capture; Anxiety = new app not fast enough; Habit = phone notes always there.
- **Success:** Captured in under 5 seconds.
- **Competitive set:** Apple Notes, Google Keep, voice memos.
- **Implication:** Build fastest capture (mobile, voice); free or low price; app-store discovery.

**Segment 2: "Build Knowledge"**
- **Job:** When researching a complex topic, I want to connect ideas across sources, so I can develop deeper understanding.
- **Context:** Weekly deep work, not urgent, solo, desktop.
- **Forces:** Push = can't see relationships; Pull = linking, graph view; Anxiety = setup/learning time; Habit = existing folder structure.
- **Success:** Insights emerge from connections; easy to revisit.
- **Competitive set:** Roam, Obsidian, Notion.
- **Implication:** Linking, graph, search; mid-tier price; content/community acquisition.

**Segment 3: "Share Understanding"**
- **Job:** When collaborating with my team, I want to align on decisions and context, so we execute consistently.
- **Context:** Multiple times per week, blocks progress, team.
- **Forces:** Push = "where did we decide that?"; Pull = single source of truth; Anxiety = team won't adopt; Habit = docs familiar to everyone.
- **Success:** Team finds decisions independently; easy to keep updated.
- **Competitive set:** Notion, Confluence, Google Docs.
- **Implication:** Collaboration, permissions, export; higher WTP; sales-assisted or team-led GTM.

## Behavioral segmentation (brief)

When you have an **existing product** and usage data, you can also segment by behavior (e.g. power vs casual, RFM, feature adoption). Use that to optimize activation, retention, and expansion. Combine with job-based segments when possible: job segment = *what* to build, behavioral segment = *how* to deliver (onboarding, messaging, features). For usage metrics and cohort analysis, see **2.3.6-Metrics**. This framework stays focused on job-based segmentation; behavioral is complementary.

## Red flags (anti-patterns)

- **Segments sound like personas** — You're segmenting by demographics. Refocus on the job and context.
- **You'd market the same way to all segments** — They're not meaningfully different; merge or redefine.
- **Can't articulate the job per segment** — Go back to JTBD research; segments must be job-based.
- **Segments need completely different products** — May be different markets; consider separate scope.
- **Can't identify which segment a user is in** — Segments must be behaviorally or contextually identifiable (e.g. job screening, usage proxy).
- **Too many segments (e.g. 10+)** — Consolidate to 3–5; focus on 1–2 to serve first.
- **Segments you can't measure** — You must be able to track or survey by segment.

## Quick Quality Checks (during creation)

- [ ] Each segment has a clear job statement (When / I want to / So I can).
- [ ] Segments are mutually exclusive and meaningfully different (different features, messaging, or pricing).
- [ ] You have 3–5 segments (not 1, not 10+).
- [ ] You can explain how you'd identify someone in each segment (behavior, survey, or context).
- [ ] At least qualitative validation (or a plan for it) is in place.
- [ ] Connection to personas is clear: segments = strategy, personas = execution; personas come from priority segments.

## Output and handoffs

- **Format:** Markdown (`.md`)
- **Location:** `03-Research-Artifacts/segments/` or initiative folder
- **Filename:** `segment-[segment-name]-[YYYY-MM-DD].md` or one doc with all segments
- **Handoffs:** JTBD (2.2.3) → this framework → Prioritization (2.1.2/4) for which segment(s) to serve → Personas (2.3.5) for priority segments → PMF (2.2.8) to assess fit by segment.

## Links

- JTBD: [2.2.3-Jobs-To-Be-Done](../2.2.3-Jobs-To-Be-Done/README.md)
- Problem-Solution Space: [2.2.6-Problem-Solution-Space](../2.2.6-Problem-Solution-Space/README.md)
- Personas: [2.3.5-Personas](../../2.3-Execution/2.3.5-Personas/README.md)
- PMF: [2.2.8-Product-Market-Fit](../2.2.8-Product-Market-Fit/README.md)
- Prioritization: [2.1.2-Strategic-Execution/4-Prioritization](../../2.1-Strategy/2.1.2-Strategic-Execution/4-Prioritization/)
- Segment Definition Template: [2-segment-definition-template.md](2-segment-definition-template.md)

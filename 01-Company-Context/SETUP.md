# Company Context Setup Guide

## Introduction

Every company is unique. Your organizational structure, how decisions are made, how strategic planning is organized (OKRs, goals, or none), and how teams are organized all shape how you should structure your `01-Company-Context/` directory.

This guide helps you:
- **Discover** your organizational structure through probing questions
- **Plan** the right document structure for your company
- **Implement** your company context incrementally (no need to do everything at once)
- **Maintain** your structure as your organization evolves

**Why this matters:** A well-structured company context helps you:
- Make faster, better-aligned decisions
- Navigate organizational complexity
- Keep stakeholders aligned
- Enable AI agents to provide better, context-aware assistance

**Time commitment:** You can complete this in stages. Each step has a checkpoint where you can pause and return later.

**Before you start:** Fill out [`CONTEXT.md`](CONTEXT.md) with your name, company name, and team/BU names. This personalizes the setup and helps AI agents provide better assistance.

---

## Step 0: Personalize Your Context

**First step:** Open [`CONTEXT.md`](CONTEXT.md) and fill in:
- Your name
- Company name
- Team/BU names (if applicable)

This information will be referenced throughout your PM Brain to personalize AI assistance and make documents more relevant.

**Relationship to other personalization files:**
- **`CONTEXT.md`** (this file) = Organizational context (company name, teams, BUs, your role in the organization)
- **`.cursor/rules/thinking.personal.mdc`** = Personal working style and preferences (how you like to work, communication style, cognitive preferences)
- Both files may include your name - keep them consistent. `CONTEXT.md` focuses on organizational context; `thinking.personal.mdc` focuses on how you work.

**Time:** 2-3 minutes

---

## Step 1: Braindump - What Do You Already Know?

Before diving into questions, take 5 minutes to braindump what you know about your organization:

**Quick braindump prompts:**
- How big is your company? (startup, mid-size, enterprise)
- Do you have business units or divisions? How many?
- How many product/engineering teams are there?
- How is strategic planning organized? (company-level, BU-level, team-level, or none - OKRs, goals, etc.)
- Who are the key stakeholders you work with regularly?
- How are decisions made? (top-down, bottom-up, consensus)

**Don't structure yet** - just dump what comes to mind. This helps you answer the questions below more quickly.

---

## Step 2: Organizational Structure Discovery

Answer these questions to understand your company's structure. **Don't create files yet** - we're just discovering.

### 2.1 Company Size & Stage

**Question:** What stage is your company at?

- [ ] **Startup** (< 50 people, single product focus)
- [ ] **Mid-size** (50-500 people, multiple products/teams)
- [ ] **Enterprise** (500+ people, multiple business units)
- [ ] **Other** (describe: _______________)

**Why this matters:** Smaller companies need simpler structures; larger companies may need BU-level organization.

### 2.2 Business Units

**Question:** Does your company have distinct business units, divisions, or product lines?

- [ ] **No business units** - Single product or unified organization
- [ ] **Yes, business units exist** - Multiple distinct units (e.g., Consumer, Enterprise, Platform)
- [ ] **Not sure** - Organization is complex/unclear

**If yes, answer:**
- How many business units? _______
- Which business units are relevant to your work? (list them - update `CONTEXT.md` with these names)
  - _________________________________
  - _________________________________
  - _________________________________
- Do business units have their own strategies/roadmaps/OKRs?
  - [ ] Yes, each BU has its own
  - [ ] No, everything is company-wide
  - [ ] Mixed (some BUs have their own, others don't)

**Why this matters:** If BUs exist, you may need subfolders like `1.1-Business-Unit-A/` for BU-specific documents.

### 2.3 Product/Engineering Organization

**Question:** How is Product and Engineering organized?

- [ ] **Centralized** - Single PM/Eng organization, teams work across products
- [ ] **Decentralized** - PM/Eng embedded in business units
- [ ] **Matrix** - PM/Eng report to both functional and BU leadership
- [ ] **Hybrid** - Mix of centralized and decentralized
- [ ] **Other** (describe: _______________)

**Why this matters:** Affects how you organize stakeholders and roadmaps.

### 2.4 Team Structure

**Question:** How many teams do you work with or manage?

- [ ] **Single team** - You work with one team
- [ ] **Multiple teams** - You work with 2-5 teams
- [ ] **Many teams** - You work with 6+ teams
- [ ] **Cross-functional pods** - Teams are organized as pods/squads

**If multiple teams:**
- Are teams organized by product, feature, or function?
- Do teams have their own roadmaps/OKRs?
- Do you need team-specific context documents?

**Why this matters:** Determines whether you need team-level subfolders or if everything fits at the company/BU level.

---

## Step 3: Operating Model Discovery

Now let's understand how your organization operates.

### 3.1 Decision-Making Model

**Question:** How are product/strategic decisions made?

- [ ] **Top-down** - Leadership sets direction, teams execute
- [ ] **Bottom-up** - Teams propose, leadership approves
- [ ] **Consensus** - Decisions require broad agreement
- [ ] **Hybrid** - Mix depending on decision type
- [ ] **Other** (describe: _______________)

**Why this matters:** Affects how you document strategy and roadmap ownership.

### 3.2 Strategic Planning Structure

**Question:** How is strategic planning organized in your company? (OKRs, goals, objectives, etc.)

- [ ] **Company-level only** - Single set of strategic goals/OKRs for the whole company
- [ ] **Company + BU-level** - Company goals cascade to BU goals/OKRs
- [ ] **Company + BU + Team-level** - Goals cascade through all levels
- [ ] **No formal strategic planning** - Company doesn't use OKRs or formal goal-setting
- [ ] **Other** (describe: _______________)

**If strategic planning exists:**
- What system does your company use? (OKRs, KPIs, goals, objectives, etc.)
- Where are these documented? (company wiki, separate tool, etc.)
- Do you need to track strategic goals in your PM Brain? (Yes/No/Maybe)

**Why this matters:** Determines whether you need separate strategic planning documents at different levels. Not all companies use OKRs - some use other goal-setting frameworks or informal planning.

### 3.3 Roadmap & Planning Documents

**Question:** How are roadmaps and planning documents organized?

- [ ] **Single company roadmap** - One roadmap/plan for everything
- [ ] **BU-specific roadmaps** - Each BU has its own roadmap/plan
- [ ] **Team-specific roadmaps** - Each team has its own roadmap/plan
- [ ] **Product-specific roadmaps** - Each product has its own roadmap/plan
- [ ] **Mixed** - Combination of the above
- [ ] **No formal roadmap** - Roadmaps are informal or don't exist

**Note:** Not all companies have formal roadmaps. Some use other planning documents (release plans, project plans, etc.) or keep planning informal.

**Why this matters:** Determines whether you need multiple roadmap/planning documents at different organizational levels.

### 3.4 Stakeholder Organization

**Question:** How are stakeholders organized?

- [ ] **Centralized PM** - PMs report to a central PM organization
- [ ] **Distributed PM** - PMs report to different BUs/functions
- [ ] **Embedded PM** - PMs are embedded in engineering teams
- [ ] **Hybrid** - Mix of the above
- [ ] **Other** (describe: _______________)

**Question:** How many key stakeholders do you regularly work with?

- [ ] **Few** (1-5 people)
- [ ] **Some** (6-15 people)
- [ ] **Many** (16+ people)

**Why this matters:** Determines how detailed your stakeholder document needs to be and whether you need BU/team-level stakeholder docs.

### 3.5 Stakeholder avatars (optional)

If you want the PM Brain agent to simulate "what would my manager say?" or run politics checks when key people aren't in the room, you can set up a **stakeholder avatars** (brainfeed) cast. This lives in the **`1.1-Stakeholder-Avatars/`** subfolder: one file per person (e.g. `1-jane-manager.md`, `2-alex-eng-lead.md`). Naming: **single digit**, **name**, **role**, optional **company/organization**.

- **Folder and naming:** [1.1-Stakeholder-Avatars/README.md](1.1-Stakeholder-Avatars/README.md)
- **How to set up (guided quiz):** [02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/](../02-Methods-and-Tools/2.4-Communication/2.4.8-Stakeholder-Avatars/README.md)

You can do this during company context setup or anytime later. It's optional but useful if you work with a recurring cast of stakeholders and want to pressure-test plans and communication before live conversations.

---

## Step 4: Document Structure Planning

Based on your answers, here's how to structure your `01-Company-Context/` directory.

### 4.1 Core Documents (Always Needed)

These documents should exist at the company level:

- ✅ **`1-company-vision.md`** - Company mission, vision, values
- ✅ **`2-company-strategy.md`** - Strategic priorities and initiatives
- ✅ **`3-company-product-principles.md`** - Product principles and development process
- ✅ **`4-company-product-explanation.md`** - Product portfolio and customer segments
- ✅ **`6-company-stakeholders.md`** - Key stakeholders directory

### 4.2 Roadmap & Planning Documents

Based on your roadmap organization (Step 3.3):

**If single company roadmap/plan:**
- ✅ **`5-company-roadmap.md`** - Single company-wide roadmap or planning document

**If BU-specific roadmaps:**
- ✅ **`5-company-roadmap.md`** - High-level company roadmap
- Create subfolders: `1.1-Business-Unit-A/`, `1.2-Business-Unit-B/`, etc.
- Each BU folder: `2-bu-[name]-roadmap.md`

**If team-specific roadmaps:**
- ✅ **`5-company-roadmap.md`** - Company-level roadmap
- Consider team-level roadmaps in `04-Initiatives/` or create team subfolders if needed

**Note:** If your company doesn't use formal roadmaps, you can skip this document or use it for high-level strategic planning/priorities instead.

### 4.3 Business Unit Structure

**If you have business units (Step 2.2):**

Create subfolders for each relevant BU:
```
01-Company-Context/
├── 1.1-Business-Unit-A/
│   ├── README.md (use template from 02-Methods-and-Tools/0-Template-Structure/)
│   ├── 1-bu-a-strategy.md
│   ├── 2-bu-a-roadmap.md (if BU has its own roadmap)
│   └── 3-bu-a-stakeholders.md (if BU has distinct stakeholders)
├── 1.2-Business-Unit-B/
│   └── ...
```

**Naming convention:** Use `1.x-Business-Unit-Name/` where x is sequential (1.1, 1.2, 1.3...)

**When creating BU subfolders:**
- Reference `02-Methods-and-Tools/0-Template-Structure/6-readme-template-domain.md` for README structure
- Only create BU folders for BUs relevant to your work
- You can add more BU folders later as needed

### 4.4 Strategic Planning Documents (OKRs, Goals, etc.)

**If you have strategic planning (Step 3.2):**

**Company-level only:**
- Add strategic goals/OKRs to `2-company-strategy.md` or create `2.1-company-goals.md` (or `2.1-company-okrs.md` if using OKRs)

**Company + BU-level:**
- Company goals: `2-company-strategy.md` or `2.1-company-goals.md`
- BU goals: In each BU folder as `1-bu-[name]-goals.md` or part of `1-bu-[name]-strategy.md`

**Company + BU + Team-level:**
- Company: `2-company-strategy.md` or `2.1-company-goals.md`
- BU: In BU folders
- Team: Consider tracking in `04-Initiatives/` or team-specific folders

**If no formal strategic planning:**
- Skip goal/OKR-specific documents
- Focus on strategy and roadmap documents (or use strategy document for high-level priorities)

### 4.5 Common Scenarios

**Scenario A: Single Team, No BUs (Startup)**
```
01-Company-Context/
├── CONTEXT.md
├── 1-company-vision.md
├── 2-company-strategy.md
├── 3-company-product-principles.md
├── 4-company-product-explanation.md
├── 5-company-roadmap.md
└── 6-company-stakeholders.md
```
**Action:** Create all 6 core documents. No subfolders needed.

**Scenario B: Multiple Teams, No BUs (Mid-size)**
```
01-Company-Context/
├── CONTEXT.md
├── 1-company-vision.md
├── 2-company-strategy.md
├── 3-company-product-principles.md
├── 4-company-product-explanation.md
├── 5-company-roadmap.md (company-level)
└── 6-company-stakeholders.md (all teams)
```
**Action:** Create core documents. If teams need separate roadmaps, consider team subfolders or track in `04-Initiatives/`.

**Scenario C: Business Units Exist (Enterprise)**
```
01-Company-Context/
├── CONTEXT.md
├── 1-company-vision.md
├── 2-company-strategy.md
├── 3-company-product-principles.md
├── 4-company-product-explanation.md
├── 5-company-roadmap.md (high-level)
├── 6-company-stakeholders.md
├── 1.1-Business-Unit-A/
│   ├── README.md
│   ├── 1-bu-a-strategy.md
│   ├── 2-bu-a-roadmap.md
│   └── 3-bu-a-stakeholders.md
└── 1.2-Business-Unit-B/
    └── ...
```
**Action:** Create core documents + BU subfolders for relevant BUs.

**Scenario D: Complex Matrix Organization**
```
01-Company-Context/
├── [Company-level documents]
├── [BU-level folders]
└── [Consider team-level folders if teams have distinct strategies]
```
**Action:** Start with company + BU level. Add team level only if teams have distinct strategies/roadmaps.

---

## Step 5: Implementation

Now let's create your structure step-by-step. **You don't need to do everything at once.**

### 5.1 Phase 1: Personalization & Core Company Documents (Start Here)

**Time:** 35-65 minutes

1. **Fill out CONTEXT.md:**
   - Your name
   - Company name (will replace `[Company]` placeholders)
   - Team/BU names

2. **Start with Vision & Strategy:**
   - Create `1-company-vision.md` (use existing template structure, replace `[Company]` with your company name from CONTEXT.md)
   - Create `2-company-strategy.md`
   - Use frameworks from `02-Methods-and-Tools/2.1-Strategy/2.1.1-Strategic-Foundations/`

3. **Add Principles & Portfolio:**
   - Create `3-company-product-principles.md`
   - Create `4-company-product-explanation.md`

4. **Create Stakeholder Directory:**
   - Create `6-company-stakeholders.md`
   - Add key stakeholders you work with regularly

**Checkpoint:** ✅ You can pause here. Core documents are in place.

### 5.2 Phase 2: Roadmap (If Needed)

**Time:** 20-30 minutes

1. **Create company roadmap:**
   - Create `5-company-roadmap.md`
   - Use roadmap framework from `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/`

**Checkpoint:** ✅ Company-level structure is complete.

### 5.3 Phase 3: Business Unit Structure (If Applicable)

**Time:** 30-45 minutes per BU

**For each relevant business unit:**

1. **Create BU folder:**
   - Create folder: `1.x-Business-Unit-Name/` (use names from CONTEXT.md)
   - Create `README.md` using template from `02-Methods-and-Tools/0-Template-Structure/6-readme-template-domain.md`

2. **Create BU documents:**
   - `1-bu-[name]-strategy.md` - BU-specific strategy
   - `2-bu-[name]-roadmap.md` - BU-specific roadmap (if applicable)
   - `3-bu-[name]-stakeholders.md` - BU-specific stakeholders (if applicable)

3. **Link to company-level:**
   - Update `2-company-strategy.md` to reference BU strategies
   - Update `5-company-roadmap.md` to reference BU roadmaps

**Checkpoint:** ✅ BU structure is in place. You can add more BUs later.

### 5.4 Phase 4: Strategic Planning Documents (If Applicable)

**Time:** 20-30 minutes per level

**If company-level strategic planning:**
- Add to `2-company-strategy.md` or create `2.1-company-goals.md` (or `2.1-company-okrs.md` if using OKRs)
- If using OKRs, use OKR framework from `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/`

**If BU-level strategic planning:**
- Add to BU strategy documents or create separate goal/OKR files in BU folders

**Checkpoint:** ✅ Strategic planning documents are documented at appropriate levels.

---

## Step 6: Validation Checklist

Use this checklist to verify your setup is complete:

### Personalization
- [ ] `CONTEXT.md` filled out with your name, company name, and team/BU names

### Company-Level Documents
- [ ] `1-company-vision.md` exists and has content (not just placeholders), `[Company]` replaced with actual company name
- [ ] `2-company-strategy.md` exists and reflects current priorities
- [ ] `3-company-product-principles.md` exists
- [ ] `4-company-product-explanation.md` exists
- [ ] `5-company-roadmap.md` exists (if roadmaps are used)
- [ ] `6-company-stakeholders.md` exists with key stakeholders

### Business Unit Structure (If Applicable)
- [ ] BU folders created for all relevant BUs
- [ ] Each BU folder has README.md
- [ ] BU strategy documents exist
- [ ] BU roadmaps exist (if applicable)
- [ ] Company-level documents reference BU documents

### OKRs (If Applicable)
- [ ] OKRs documented at company level (if applicable)
- [ ] OKRs documented at BU level (if applicable)
- [ ] OKRs are current and reflect actual OKRs

### Structure Quality
- [ ] Document structure matches your organizational reality
- [ ] You can find information quickly
- [ ] Documents are linked/cross-referenced appropriately
- [ ] README.md in `01-Company-Context/` reflects your structure
- [ ] All `[Company]` placeholders replaced with actual company name

---

## Maintenance: Keeping Your Structure Current

### When to Update

**Quarterly:**
- Review all documents for accuracy
- Update strategy and roadmap documents
- Refresh stakeholder directory
- Update CONTEXT.md if team/BU names change

**After Organizational Changes:**
- New business unit → Create new BU folder, update CONTEXT.md
- BU reorganization → Update BU folder structure, update CONTEXT.md
- New teams → Update stakeholder directory or create team folders, update CONTEXT.md
- Strategic planning structure changes → Update strategic planning documents

**When Agent Detects Changes:**
- If the PM Brain agent mentions new organizational structures (BUs, teams, different strategic planning levels), review `SETUP.md` to see if your structure needs updating

### How to Add New Structures

**Adding a new business unit:**
1. Update `CONTEXT.md` with new BU name
2. Create folder: `1.x-Business-Unit-Name/` (use next sequential number)
3. Create README.md using template from `02-Methods-and-Tools/0-Template-Structure/`
4. Create BU-specific documents (strategy, roadmap, stakeholders)
5. Update company-level documents to reference new BU

**Adding team-level structure:**
1. Update `CONTEXT.md` with new team name
2. Consider if team needs separate folder or if `04-Initiatives/` is sufficient
3. If folder needed, create `1.x-Team-Name/` or `2.x-Team-Name/` (depending on hierarchy)
4. Follow same pattern as BU folders

**Reference:** Always use `02-Methods-and-Tools/0-Template-Structure/` when creating new structures.

---

## Getting Help

**Stuck?** Ask the PM Brain agent:
- "Help me set up my company context structure"
- "I have business units - how should I organize them?"
- "How do I add a new business unit folder?"

**Need examples?** See:
- `02-Methods-and-Tools/0-Template-Structure/` - Template structure guide
- `02-Methods-and-Tools/2.1-Strategy/` - Strategy frameworks
- `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/1-OKR/` - OKR framework
- `02-Methods-and-Tools/2.1-Strategy/2.1.2-Strategic-Execution/2-Roadmap/` - Roadmap framework

---

## Quick Reference

For a quick checklist version, see: [`SETUP-QUICK-REFERENCE.md`](SETUP-QUICK-REFERENCE.md)

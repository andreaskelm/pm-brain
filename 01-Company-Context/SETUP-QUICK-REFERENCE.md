# Company Context Setup - Quick Reference

**Full guide:** See [`SETUP.md`](SETUP.md) for detailed step-by-step instructions.

## Quick Decision Tree

### 0. Personalize First
- [ ] Fill out `CONTEXT.md` with your name, company name, and team/BU names

### 1. Do you have business units?
- **No** → Flat structure: All 6 core documents at root level
- **Yes** → Create BU subfolders: `1.1-Business-Unit-A/`, `1.2-Business-Unit-B/`, etc.

### 2. How is strategic planning organized? (OKRs, goals, etc.)
- **Company-level only** → Add to `2-company-strategy.md`
- **Company + BU-level** → Company goals in strategy doc, BU goals in BU folders
- **No formal planning** → Skip goal/OKR-specific documents

### 3. How are roadmaps organized?
- **Single roadmap** → `5-company-roadmap.md` only
- **BU-specific** → Company roadmap + BU roadmaps in BU folders
- **Team-specific** → Consider team folders or track in `04-Initiatives/`

## Core Documents Checklist

**Always create these:**
- [ ] `CONTEXT.md` (personalization - your name, company, teams/BUs)
- [ ] `1-company-vision.md`
- [ ] `2-company-strategy.md`
- [ ] `3-company-product-principles.md`
- [ ] `4-company-product-explanation.md`
- [ ] `5-company-roadmap.md` (if roadmaps exist)
- [ ] `6-company-stakeholders.md`

## Business Unit Structure (If Applicable)

**For each relevant BU:**
- [ ] Update `CONTEXT.md` with BU name
- [ ] Create folder: `1.x-Business-Unit-Name/`
- [ ] Create `README.md` (use template from `02-Methods-and-Tools/0-Template-Structure/`)
- [ ] Create `1-bu-[name]-strategy.md`
- [ ] Create `2-bu-[name]-roadmap.md` (if BU has own roadmap)
- [ ] Create `3-bu-[name]-stakeholders.md` (if BU has distinct stakeholders)

## Common Scenarios

### Startup (Single Team, No BUs)
```
01-Company-Context/
├── CONTEXT.md
├── [6 core documents]
└── No subfolders needed
```

### Mid-size (Multiple Teams, No BUs)
```
01-Company-Context/
├── CONTEXT.md
├── [6 core documents]
└── Consider team folders if teams need separate roadmaps
```

### Enterprise (Business Units Exist)
```
01-Company-Context/
├── CONTEXT.md
├── [6 core documents]
├── 1.1-Business-Unit-A/
│   ├── README.md
│   ├── 1-bu-a-strategy.md
│   ├── 2-bu-a-roadmap.md
│   └── 3-bu-a-stakeholders.md
└── 1.2-Business-Unit-B/
    └── ...
```

## Implementation Phases

**Phase 0:** Personalization (2-3 min)
- Fill out CONTEXT.md

**Phase 1:** Core documents (30-60 min)
- Vision, Strategy, Principles, Portfolio, Stakeholders

**Phase 2:** Roadmap (20-30 min)
- Company roadmap

**Phase 3:** BU structure (30-45 min per BU)
- BU folders and documents

**Phase 4:** Strategic planning (20-30 min per level)
- Company/BU/Team OKRs

## Key Questions to Answer

1. **Company size?** Startup / Mid-size / Enterprise
2. **Business units?** Yes / No
3. **Strategic planning structure?** Company / BU / Team / None
4. **Roadmap structure?** Single / BU-specific / Team-specific
5. **Stakeholder organization?** Centralized / Distributed / Embedded

## When to Update

- **Quarterly:** Review all documents, update CONTEXT.md if needed
- **After organization changes:** New BUs, teams, strategic planning structure changes → Update CONTEXT.md
- **When agent suggests:** If agent detects new organizational structures

## Getting Help

- Full guide: [`SETUP.md`](SETUP.md)
- Template structure: `02-Methods-and-Tools/0-Template-Structure/`
- Ask agent: "Help me set up my company context structure"

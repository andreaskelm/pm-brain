# 4-Research — Research Artifacts

## Introduction

This directory stores research outputs and artifacts from discovery activities. This is **storage for research results**, not a process framework. Use the discovery methods in [2-Methods/3-Discovery/](../2-Methods/3-Discovery/README.md) to conduct research, then store your outputs here.

**For agents:** This folder is one of the context sources the PM Brain agent asks about early in product_sense (and when starting execution_mode for non-trivial docs). If the user has not added relevant research context, suggest adding or @-mentioning key artifacts from here; having them in context speeds up thinking and grounds answers in evidence. 

**Critical agent guidance:** When users share research/discovery insights (from interviews, qualitative research, analysis, etc.), **always guide them to save a document** capturing the insight. Ask: "Should this be saved in `4-Research/` (for general research) or in the initiative folder under `3-Work/[initiative-name]/research/` (if it's specific to an active initiative)?" Help them create or update the appropriate analysis document. For raw data (transcripts, recordings, large files), guide users to store externally (Google Drive, SharePoint, Teams) and link to that source from the analysis doc. Paths below are from repo root.

**This is for:** Storing research artifacts, interview notes, synthesis outputs, and research findings  
**This is NOT:** A process framework or sequential step in product development

## How This Relates to Frameworks

**Research Process (Use Frameworks):**
- Conduct interviews using discovery guides in [2-Methods/3-Discovery/1-Research-Interviews/](../2-Methods/3-Discovery/1-Research-Interviews/README.md)
- Synthesize patterns using discovery steps in [2-Methods/3-Discovery/2-Continuous-Discovery-Habits/](../2-Methods/3-Discovery/2-Continuous-Discovery-Habits/README.md)
- Create opportunities using [2-Continuous-Discovery-Habits/3-create-opportunities.md](../2-Methods/3-Discovery/2-Continuous-Discovery-Habits/3-create-opportunities.md)

**Research Storage (This Directory):**
- Store **analysis and insights** as markdown documents (interview snapshots, synthesis summaries, key findings, patterns)
- Archive synthesis outputs and patterns
- Keep research findings and insights
- Maintain research history and learnings
- **Link to external raw data** (transcripts, recordings, raw notes stored in Google Drive, SharePoint, Teams, etc.)

**Storage Pattern:**
- **In this repo (4-Research or 3-Work)**: Analysis documents, insights, synthesis summaries, interview snapshots, key findings
- **External (Google Drive/SharePoint/Teams)**: Raw transcripts, audio/video recordings, large datasets, sensitive data — link to these sources from your analysis docs

**Difference from [3-Work](../3-Work/README.md):**
- **This directory (4-Research)**: Archive for completed research outputs (analysis docs, snapshots, synthesis documents) that are **general or reusable** across initiatives
- **3-Work**: Active workspace where you plan research, document opportunities, and work on initiatives; **initiative-specific research** can be stored in `3-Work/[initiative-name]/research/`
- **Decision rule**: If research is specific to one active initiative, store analysis in that initiative's folder. If it's general/reusable, store here in `4-Research/`. Either way, **always save analysis as a document**; raw data (transcripts, recordings) goes external with links.

## Directory Structure

```
4-Research/
 +-- 1-User-Interviews/ # Interview notes, transcripts, insights
 +-- 2-Qualitative-Research/ # Qualitative findings and analysis
 +-- [Future research categories] # Add as needed
```

## How to Use This Directory

1. **Before Conducting Research**: Review the interview guide in [1-Research-Interviews](../2-Methods/3-Discovery/1-Research-Interviews/README.md) for principles and best practices
2. **After Conducting Research**: Store outputs from discovery frameworks here
3. **Organize by Research Type**: Use subdirectories to organize different research activities
4. **Link from Initiatives**: Reference research artifacts in your initiative folders ([3-Work/](../3-Work/README.md))
5. **Maintain Research History**: Keep historical research for future reference

---

## Quick start: self-quiz + AI collaboration for research artifacts

Use this prompt when you've done research (or are about to) and want help organizing artifacts in this folder:

```markdown
Act as a research archivist and synthesis partner. Help me store and structure my research artifacts in `4-Research/`.

1) Ask me:
- What kind of work I just did or plan to do (e.g. user interviews, usability tests, discovery calls, synthesis workshop).
- Which initiative or problem this research belongs to (if any).

2) Based on my answer:
- **Decide storage location**: Is this research specific to one initiative? Store in `3-Work/[initiative-name]/research/`. Is it general/reusable? Store in `4-Research/` (e.g. `1-User-Interviews/`, `2-Qualitative-Research/`, or a new category).
- **Create analysis document**: Help me create/update a markdown document capturing insights, findings, patterns, synthesis (not raw data).
- **Handle raw data**: If I have transcripts, recordings, or large files, guide me to store them externally (Google Drive, SharePoint, Teams) and add a link in the analysis doc.
- Offer to help convert my raw notes into snapshots or synthesis summaries, and suggest links back to [3-Work/](../3-Work/README.md) and [2-Methods/3-Discovery/](../2-Methods/3-Discovery/README.md).

3) At the end of each pass:
- List: (a) which files we created/updated under `4-Research/`, (b) which initiative(s) they should be linked from, and (c) any open questions or follow-up research ideas.

I'll start by telling you what research I just did or am planning to do.
```

## How to Maintain

- **After Each Research Activity**: **Save analysis as a document** (insights, findings, synthesis) in appropriate subdirectory; link to external raw data sources
- **Link to Initiatives**: Reference research artifacts in opportunity assessments and PRDs
- **Quarterly Reviews**: Archive old research and extract key learnings
- **Version Control**: Track research analysis documents in git (not raw data files)

## Links
- Discovery methods: [2-Methods/3-Discovery/](../2-Methods/3-Discovery/README.md)
- Initiatives: [3-Work/](../3-Work/README.md)
- Jobs To Be Done: [3-Jobs-To-Be-Done](../2-Methods/3-Discovery/3-Jobs-To-Be-Done/README.md)


---
name: review-prd
description: Multi-perspective PRD review with parallel subagent reviewers representing User, Technical, Business, and QA roles. Produces a structured confidence report and actionable revision requests. Use when: (1) a PRD has just been written and needs quality validation, (2) user asks to "review PRD", "validate PRD", "check PRD quality", (3) write-prd workflow reaches Step 7 and automated review is desired. Outputs a confidence score (0–1); PRDs scoring below the configured threshold are returned for revision.
---

# review-prd — Multi-Perspective PRD Review

## Overview

After a PRD is written, spawn **4 independent reviewer subagents** in parallel, each embodying a distinct stakeholder perspective. Collect their structured feedback, compute a weighted confidence score, and decide pass/revise.

```
PRD input
   │
   ├─► [User Reviewer]      → score + issues
   ├─► [Tech Reviewer]      → score + issues
   ├─► [Business Reviewer]  → score + issues
   └─► [QA Reviewer]        → score + issues
         │
         ▼
   Aggregate Report
   Confidence Score ≥ threshold? → PASS : REVISE
```

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `PASS_THRESHOLD` | `0.75` | Minimum weighted confidence to pass |
| `MAX_REVISION_LOOPS` | `2` | Max auto-revision cycles before escalating to user |

## Workflow

### Step 1 — Locate PRD

Identify the PRD to review. Accept:
- A file path (e.g. `prd/my-feature/prd.md`)
- A directory (read `prd.md` inside it)
- Inline PRD text passed directly

Read the PRD content before spawning reviewers.

### Step 2 — Spawn Parallel Reviewers

Spawn all 4 reviewer subagents simultaneously (no sequential dependency). Pass each reviewer:
1. The full PRD text
2. Their role persona and scoring rubric (see `references/reviewer-personas.md`)
3. The structured output format (see below)

Use `sessions_spawn` with `runtime: "subagent"`, `mode: "run"`.

**Reviewer roles:**
- `user-reviewer` — End-user / customer perspective
- `tech-reviewer` — Engineering / technical feasibility perspective  
- `business-reviewer` — Business value / ROI / strategy perspective
- `qa-reviewer` — Testability / acceptance criteria / edge cases perspective

### Step 3 — Collect & Aggregate Results

Wait for all 4 subagents to complete. Each returns:

```json
{
  "role": "user-reviewer",
  "score": 0.82,
  "passed": true,
  "critical_issues": [],
  "major_issues": ["Missing error state for login failure"],
  "minor_issues": ["Acceptance criteria could be more specific"],
  "summary": "..."
}
```

**Weighted confidence formula:**
```
confidence = (user×0.30 + tech×0.30 + business×0.20 + qa×0.20)
```

### Step 4 — Generate Review Report

Write the report to `{prd-directory}/review-report.md`. See `references/report-template.md` for the exact format.

Report sections:
1. **Confidence Score** — weighted score + pass/fail verdict
2. **Per-Reviewer Summary** — each role's score, critical/major/minor issues
3. **Consolidated Issue List** — deduplicated, sorted by severity
4. **Revision Requests** — specific, actionable items for the PRD author

### Step 5 — Pass or Revise

**If PASS** (`confidence ≥ PASS_THRESHOLD`):
- Announce pass with score and report path
- Suggest next steps (share with team, implement, etc.)

**If REVISE** (`confidence < PASS_THRESHOLD`):
- List critical and major issues clearly
- If called from `write-prd` workflow and `revision_loop < MAX_REVISION_LOOPS`:
  - Feed revision requests back to the PRD author agent
  - Increment loop counter, re-run from Step 1 after revision
- Otherwise: surface issues to user and ask how to proceed

## Integration with write-prd

Add this call at the end of `write-prd` Step 7 (Quality Check):

> After self-check passes, invoke `review-prd` skill on the generated `prd.md`.
> Only mark the PRD as complete after `review-prd` returns PASS.

## Standalone Usage

Users can invoke this skill directly:
- "Review the PRD at `prd/feature-x/prd.md`"
- "Run a multi-perspective review on this PRD"
- "Validate PRD quality before we share it with the team"

# Review Report Template

Save as `{prd-directory}/review-report.md`.

---

```markdown
# PRD Review Report

**PRD:** {prd-file-path}  
**Reviewed:** {datetime}  
**Revision Loop:** {n} / {MAX_REVISION_LOOPS}

---

## Confidence Score

| Reviewer | Score | Weight | Weighted |
|----------|-------|--------|---------|
| User | {score} | 30% | {weighted} |
| Technical | {score} | 30% | {weighted} |
| Business | {score} | 20% | {weighted} |
| QA | {score} | 20% | {weighted} |
| **Total** | | | **{confidence}** |

### Verdict: {✅ PASS | ❌ REVISE}

> Threshold: {PASS_THRESHOLD} · Score: {confidence}

---

## Per-Reviewer Summary

### 👤 User Reviewer — {score}
{summary}

**Critical:** {list or "None"}  
**Major:** {list or "None"}  
**Minor:** {list or "None"}

### ⚙️ Technical Reviewer — {score}
{summary}

**Critical:** {list or "None"}  
**Major:** {list or "None"}  
**Minor:** {list or "None"}

### 📊 Business Reviewer — {score}
{summary}

**Critical:** {list or "None"}  
**Major:** {list or "None"}  
**Minor:** {list or "None"}

### 🧪 QA Reviewer — {score}
{summary}

**Critical:** {list or "None"}  
**Major:** {list or "None"}  
**Minor:** {list or "None"}

---

## Consolidated Issues

### 🔴 Critical (must fix before pass)
1. {issue} _(raised by: {roles})_

### 🟡 Major (should fix)
1. {issue} _(raised by: {roles})_

### 🟢 Minor (nice to fix)
1. {issue} _(raised by: {roles})_

---

## Revision Requests

> Specific, actionable items for the PRD author. Each item references the PRD section to update.

1. **[Section X]** {what to add/change and why}
2. **[Section Y]** {what to add/change and why}

---

## Next Steps

{If PASS:}
- ✅ PRD is ready for team review / implementation planning
- Consider sharing with: engineering lead, design, QA

{If REVISE:}
- Address critical and major issues above
- Re-run `review-prd` after revisions
```

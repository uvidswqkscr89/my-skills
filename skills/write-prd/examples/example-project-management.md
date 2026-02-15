# Complete Example: Project Progress Reporting | 完整示例：项目进度汇报

This is a complete worked example of the PRD workflow for a project management tool.

这是项目管理工具的 PRD 工作流完整示例。

---

## JTBD Definition | JTBD 定义

### Core Statement | 核心句式

> When I **need to report project progress to my manager every week**,
> I want to **generate a "key tasks completion + risks" report in 10 minutes**,
> So that I can **quickly explain if the project will be delayed and secure resource support**.

> 当我**每周要向老板汇报项目进度**时，
> 我想要**在 10 分钟内生成一份"关键任务完成情况+风险"的报告**，
> 以便于**快速说明项目是否会延期，并争取资源支持**。

### Design Anchors | 设计锚点

- **Context | 情境**: Weekly project status meeting with manager, need to prepare report beforehand
- **Task | 任务**: Generate comprehensive progress report showing task completion and risk areas
- **Outcome | 结果**: Manager understands project health, can make informed decisions about resource allocation

### Design Validation Standard | 后续设计检验标准

> Every feature/flow/interface must answer:
> "Does this help project managers generate accurate progress reports faster?"

---

## User Story Map | 用户故事地图

### Backbone Flow | 主干流程

1. **Login** → 2. **Select Project** → 3. **Choose Time Range** → 4. **View Progress Overview** → 5. **Drill into Delayed Tasks** → 6. **Mark Key Items** → 7. **Export/Share Report**

### Feature Layering Details | 功能分层明细

#### Step 1: Login

**MVP**:
- SSO authentication with company credentials
- Remember last logged-in state

**Enhanced**:
- Biometric login (fingerprint/face)
- Multi-account switching

**Delighter**:
- Auto-login based on device recognition

---

#### Step 2: Select Project

**MVP**:
- List of all projects user manages
- Basic search by project name
- Show project status indicator (on track/at risk/delayed)

**Enhanced**:
- Filter by project status, team, or date
- Recently accessed projects at top
- Favorite/pin important projects

**Delighter**:
- AI-suggested project based on meeting calendar
- Voice search for project selection

---

#### Step 3: Choose Time Range

**MVP**:
- Quick select: This week, Last week, This month
- Custom date range picker
- Default to current week

**Enhanced**:
- Save custom date ranges as presets
- Compare to previous period
- Fiscal calendar support

**Delighter**:
- Auto-detect reporting period from meeting invite
- Smart suggestions based on reporting patterns

---

#### Step 4: View Progress Overview ⚠️

**MVP**:
- Task completion percentage (completed/total)
- Count of delayed tasks with red indicator
- Count of at-risk tasks with yellow indicator
- Overall project health score

**Enhanced**:
- Progress trend chart (last 4 weeks)
- Breakdown by task priority (high/medium/low)
- Team member contribution summary
- Milestone progress visualization

**Delighter**:
- AI-generated executive summary
- Predictive completion date
- Comparison to similar projects
- Automated insights and recommendations

---

#### Step 5: Drill into Delayed Tasks ⚠️

**MVP**:
- List of all delayed tasks
- Show task name, assignee, original due date, days delayed
- Sort by days delayed (most delayed first)
- Click to see task details

**Enhanced**:
- Filter by assignee, priority, or delay severity
- Show delay reason (if documented)
- Show dependency chain (what's blocked by this)
- Bulk actions (reassign, extend deadline)

**Delighter**:
- AI-suggested resolution strategies
- Historical delay patterns for similar tasks
- Automated escalation recommendations
- Impact analysis (what will be affected)

---

#### Step 6: Mark Key Items

**MVP**:
- Select tasks to highlight in report
- Add notes/comments to selected items
- Save selections for this reporting period

**Enhanced**:
- Tag items by category (achievement/risk/blocker)
- Attach supporting documents or screenshots
- Collaborate with team on item selection

**Delighter**:
- AI-suggested items based on importance
- Voice notes for context
- Auto-generate talking points

---

#### Step 7: Export/Share Report

**MVP**:
- Export as PDF with standard format
- Email report directly to manager
- Include all marked items and overview

**Enhanced**:
- Multiple export formats (PDF/PPT/Excel)
- Customizable report template
- Schedule recurring reports
- Share link with view-only access

**Delighter**:
- Auto-populate meeting agenda
- Integration with presentation tools
- Real-time collaborative report editing
- Voice-over narration for report

---

## User Journey Overlay | 用户旅程叠加

| Step | User Goal | Current/Expected Emotion | Main Pain Points/Risks | Priority |
|------|-----------|--------------------------|------------------------|----------|
| ① Login | Quickly enter system | Neutral → Frustrated if slow | SSO fails 15% of time, 5-10 second wait | Medium |
| ② Select Project | Find my project fast | Routine → Anxious if many projects | Managing 20+ projects, no good search, takes 30+ seconds | Medium |
| ③ Choose Time Range | Set reporting period | Routine | Defaults to last month instead of current week, extra clicks needed | Low |
| ④ View Overview ⚠️ | Know if project is healthy | Confident if clear → Anxious if unclear | 10+ metrics shown, no clear "healthy/at-risk" indicator, takes 2-3 minutes to interpret | **High** |
| ⑤ Drill into Details ⚠️ | Identify specific blockers | Focused → Frustrated if slow | 3-5 second load time, can't filter effectively, 50+ tasks to scan manually | **High** |
| ⑥ Mark Key Items | Highlight for meeting | Efficient → Annoyed if lost | Selections don't persist, have to re-select if page refreshes | Medium |
| ⑦ Export/Share | Send to manager | Relieved → Disappointed if poor format | PDF format not editable, manager prefers PPT, manual reformatting needed | Medium |

**Experience Key Points Summary | 体验关键点总结**:

- **Step ④ (View Overview)**: This is where users determine if they have a problem. If unclear, they waste time investigating or miss critical issues. Need clear, actionable summary.

- **Step ⑤ (Drill into Details)**: Users are under time pressure. Slow loading and poor filtering cause frustration and may lead to incomplete analysis.

---

## User Stories | 用户故事

### For Step 4: View Progress Overview

#### US-001: Quick Project Health Assessment

> As a **Project Manager**,
> When I **open the project overview page before my weekly status meeting**,
> I want to **see a clear project health indicator and key metrics at a glance**,
> So that I can **immediately know if I need to prepare explanations for delays or risks**.

**Acceptance Criteria**:
- [ ] Page loads in < 3 seconds
- [ ] Health indicator is prominently displayed (Green/Yellow/Red)
- [ ] Shows task completion percentage (e.g., "75% complete, 15 of 20 tasks")
- [ ] Shows count of delayed tasks with red badge
- [ ] Shows count of at-risk tasks with yellow badge
- [ ] All metrics visible without scrolling

**Priority**: MVP
**Story Map Reference**: Step 4 - View Progress Overview
**Journey Map Reference**: Addresses pain point "10+ metrics, no clear indicator"

---

#### US-002: Progress Trend Visualization

> As a **Project Manager**,
> When I **review the progress overview**,
> I want to **see a trend chart showing progress over the last 4 weeks**,
> So that I can **explain to my manager whether we're improving or declining**.

**Acceptance Criteria**:
- [ ] Chart shows weekly completion percentage for last 4 weeks
- [ ] Trend line indicates improving/declining/stable
- [ ] Hover shows exact values for each week
- [ ] Chart loads within 2 seconds

**Priority**: Enhanced
**Story Map Reference**: Step 4 - View Progress Overview

---

### For Step 5: Drill into Delayed Tasks

#### US-003: Delayed Task Identification

> As a **Project Manager**,
> When I **see that there are delayed tasks in the overview**,
> I want to **jump directly to a filtered list of delayed tasks sorted by severity**,
> So that I can **quickly identify which tasks need immediate attention for my meeting**.

**Acceptance Criteria**:
- [ ] One-click navigation from overview to delayed tasks
- [ ] List loads in < 3 seconds
- [ ] Default sort by days delayed (most delayed first)
- [ ] Shows task name, assignee, original due date, days delayed
- [ ] Red indicator for tasks delayed > 3 days
- [ ] Can filter by assignee or priority

**Priority**: MVP
**Story Map Reference**: Step 5 - Drill into Delayed Tasks
**Journey Map Reference**: Addresses pain point "3-5 second load, can't filter, 50+ tasks to scan"

---

#### US-004: Delay Impact Analysis

> As a **Project Manager**,
> When I **review a delayed task**,
> I want to **see what other tasks are blocked by this delay**,
> So that I can **explain the full impact to my manager and prioritize unblocking**.

**Acceptance Criteria**:
- [ ] Click on delayed task shows dependency chain
- [ ] Highlights tasks that are blocked (can't start until this completes)
- [ ] Shows count of blocked tasks
- [ ] Indicates if any blocked tasks are on critical path

**Priority**: Enhanced
**Story Map Reference**: Step 5 - Drill into Delayed Tasks

---

## Complete PRD Structure | 完整 PRD 结构

*[This would be the full PRD document combining all sections above with additional details on interactions, metrics, risks, etc. For brevity, the structure is shown in the templates.md file]*

---

## Key Insights from This Example | 此示例的关键洞察

### 1. JTBD Drives Everything | JTBD 驱动一切

Every feature can be traced back to helping project managers "generate accurate progress reports in 10 minutes":
- Quick health indicator → Saves time determining if there's a problem
- Delayed task filtering → Saves time finding what to discuss
- Export to PDF → Enables sharing with manager

### 2. Journey Map Identifies Priorities | 旅程图识别优先级

Steps ④ and ⑤ are marked ⚠️ because:
- High emotional impact (anxiety if unclear)
- Severe pain points (slow, unclear, manual work)
- Critical for JTBD success (can't report without understanding status)

These steps get more MVP features and more detailed UX specifications.

### 3. MVP is Truly Minimal | MVP 真正最小化

MVP features are sufficient to complete the JTBD but nothing more:
- Can login, select project, see health, find delays, export
- No fancy charts, no AI, no customization
- Achieves the 10-minute goal

Enhanced and Delighter features improve efficiency but aren't essential.

### 4. User Stories Connect Everything | 用户故事连接一切

Each user story:
- References specific story map step
- Addresses specific journey map pain point
- Helps achieve JTBD outcome
- Has testable acceptance criteria

This creates complete traceability from JTBD → Features → Requirements.

---

## Validation Against Methodology | 针对方法论的验证

✅ **JTBD Completeness**: Has Context/Task/Outcome, specific and actionable

✅ **Story Map Structure**: 7-step backbone, features layered by priority

✅ **Journey Map Overlay**: Goals, emotions, pain points for each step, ⚠️ marked

✅ **Feature-to-JTBD Traceability**: All features help complete JTBD faster

✅ **User Story Quality**: Follow standard format, map to story map steps

✅ **Acceptance Criteria**: Every user story has testable criteria

✅ **Journey-to-UX Optimization**: ⚠️ steps have detailed MVP features

✅ **Priority Layer Clarity**: Clear MVP/Enhanced/Delighter distinction

**Quality Score**: 8/8 ✅

---

## Next Steps for This Example | 此示例的后续步骤

1. **Validate with Users**: Show story map and journey map to 3-5 project managers
2. **Refine Priorities**: Adjust MVP/Enhanced based on user feedback
3. **Create Prototypes**: Design key interfaces for steps ④ and ⑤
4. **Write Detailed PRD**: Expand into full PRD with all sections
5. **Plan Implementation**: Break into sprints, estimate effort

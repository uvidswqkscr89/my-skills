# PRD Workflow Templates | PRD 工作流模板

This file contains all templates used in the PRD creation workflow.

本文件包含 PRD 创建工作流中使用的所有模板。

---

## Template 1: JTBD Definition | 模板 1：JTBD 定义

```markdown
## JTBD Definition | JTBD 定义

### Core Statement | 核心句式

> When I am in [SPECIFIC CONTEXT],
> I want to [COMPLETE A TASK],
> So that I can [ACHIEVE OUTCOME / AVOID RISK].

> 当我在【具体情境】时，
> 我想要【完成某个任务】，
> 以便于【获得某个结果/避免某个风险】。

### Design Anchors | 设计锚点

- **Context | 情境**: [Describe the specific situation, timing, or trigger]
- **Task | 任务**: [Describe the concrete action the user needs to complete]
- **Outcome | 结果**: [Describe the value gained or risk avoided]

### Design Validation Standard | 后续设计检验标准

> Every feature/flow/interface must answer:
> "Does this step help users complete this JTBD more smoothly?"

> 任何功能/流程/界面设计都要能回答：
> "这一步，是在帮用户更顺利完成这个 JTBD 吗？"
```

---

## Template 2: User Story Map | 模板 2：用户故事地图

```markdown
## User Story Map | 用户故事地图

### Backbone Flow | 主干流程

1. [Step 1] → 2. [Step 2] → 3. [Step 3] → 4. [Step 4] → 5. [Step 5]

### Feature Layering Details | 功能分层明细

#### Step 1: [Step Name]

**MVP (Must-Have) | MVP（必须有）**:
- [Feature A]: [Brief description]
- [Feature B]: [Brief description]

**Enhanced (Should-Have) | 增强（应该有）**:
- [Feature C]: [Brief description]

**Delighter (Nice-to-Have) | 锦上添花（可选）**:
- [Feature D]: [Brief description]

#### Step 2: [Step Name]

[Repeat structure...]

---

### Priority Rationale | 优先级理由

**Why these features are MVP:**
- [Rationale for MVP features]

**Why these features are Enhanced:**
- [Rationale for enhanced features]

**Why these features are Delighter:**
- [Rationale for delighter features]
```

---

## Template 3: User Journey Overlay | 模板 3：用户旅程叠加

```markdown
## User Journey Overlay | 用户旅程叠加

| Step | User Goal | Current/Expected Emotion | Main Pain Points/Risks | Priority |
|------|-----------|--------------------------|------------------------|----------|
| ① [Step 1] | [What user wants to achieve] | [Emotion if smooth / Emotion if problematic] | [Specific pain points] | [High/Med/Low] |
| ② [Step 2] | [User goal] | [Emotions] | [Pain points] | [Priority] |
| ③ [Step 3] ⚠️ | [User goal] | [Emotions] | [Pain points] | [Priority] |
| ④ [Step 4] | [User goal] | [Emotions] | [Pain points] | [Priority] |
| ⑤ [Step 5] ⚠️ | [User goal] | [Emotions] | [Pain points] | [Priority] |

**Legend | 图例**:
- ⚠️ = Experience key point (high emotional impact or critical pain point)
- ⚠️ = 体验关键点（高情绪影响或关键痛点）

**Experience Key Points Summary | 体验关键点总结**:
- **Step [X]**: [Why this is critical and what needs special attention]
- **Step [Y]**: [Why this is critical and what needs special attention]
```

---

## Template 4: User Story | 模板 4：用户故事

```markdown
### User Story [ID]: [Short Title]

**Story | 故事**:
> As a [USER TYPE],
> When [IN SPECIFIC CONTEXT / AT STORY MAP STEP],
> I want to [COMPLETE AN ACTION IN SOME WAY],
> So that I can [ACHIEVE JTBD OUTCOME / ALLEVIATE PAIN POINT].

> 作为【某类用户】，
> 当【处于某个情境/来到故事地图上的某一步】时，
> 我希望【通过某种方式完成某个动作】，
> 以便于【达成 JTBD 中的结果 / 缓解某个痛点】。

**Acceptance Criteria | 验收标准**:
- [ ] [Specific, testable criterion 1]
- [ ] [Specific, testable criterion 2]
- [ ] [Specific, testable criterion 3]

**Story Map Reference | 故事地图引用**:
- Maps to: Step [X] - [Step Name]
- Priority Layer: [MVP / Enhanced / Delighter]

**Journey Map Reference | 旅程图引用**:
- Addresses pain point: [Specific pain point from journey map]
- Target emotion: [Desired emotional outcome]
```

---

## Template 5: Complete PRD | 模板 5：完整 PRD

```markdown
# Requirement Name: [Feature Name]

**围绕 JTBD**: [Brief JTBD statement]

---

## 1. Background & JTBD | 背景与 JTBD

### 1.1 JTBD Description | JTBD 描述

> When I am in [context],
> I want to [task],
> So that I can [outcome].

### 1.2 User Roles & Scenarios | 用户角色与场景

**Primary User | 主要用户**: [User type, role, responsibilities]

**Usage Scenarios | 使用场景**:
- [Scenario 1]
- [Scenario 2]

### 1.3 Current Pain Points | 现状痛点

Based on user research and journey mapping:
- [Pain point 1 with evidence]
- [Pain point 2 with evidence]
- [Pain point 3 with evidence]

---

## 2. User Journey & Main Flow | 用户旅程与主流程

### 2.1 Backbone Flow | 主干流程

1. [Step 1] → 2. [Step 2] → 3. [Step 3] → 4. [Step 4] → 5. [Step 5]

### 2.2 Journey Map Summary | 旅程图总结

| Step | User Goal | Emotion | Key Pain Points |
|------|-----------|---------|-----------------|
| ① [Step 1] | [Goal] | [Emotion] | [Pain points] |
| ② [Step 2] ⚠️ | [Goal] | [Emotion] | [Pain points] |
| ... | ... | ... | ... |

**Experience Key Points | 体验关键点**: Steps marked with ⚠️ require special UX attention.

---

## 3. Functional Requirements | 功能需求

### 3.1 [Module/Step Name]

#### User Story 3.1.1: [Title]

> As a [user],
> When [context],
> I want to [action],
> So that I can [outcome].

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Priority**: [MVP / Enhanced / Delighter]

#### User Story 3.1.2: [Title]

[Repeat structure...]

### 3.2 [Module/Step Name]

[Repeat structure...]

---

## 4. Interaction & Interface Key Points | 交互与界面要点

### 4.1 Key Interface Specifications | 关键界面规格

**For Step [X] - [Step Name]**:
- **Layout**: [Description or link to mockup]
- **Key Elements**: [List of critical UI elements]
- **Interactions**: [User interactions and system responses]
- **Feedback**: [What feedback users receive]

**For Experience Key Points (⚠️)**:
- **Step [Y]**: [Detailed UX optimization for this critical step]

### 4.2 Prototype Links | 原型链接

- [Link to Figma/Sketch/etc.]

---

## 5. Acceptance Criteria & Metrics | 验收标准与指标

### 5.1 Acceptance Criteria Summary | 验收标准汇总

All user stories must meet their individual acceptance criteria (see Section 3).

### 5.2 Behavioral Metrics | 行为指标

**Success Metrics | 成功指标**:
- [Metric 1]: [Target value]
- [Metric 2]: [Target value]

**Example**:
- Average time to complete [task]: < [X] minutes
- Feature usage rate: > [Y]%
- Error rate: < [Z]%
- User satisfaction score: > [N]/5

---

## 6. Scope & Priority | 范围与优先级

### 6.1 MVP Scope (This Release) | MVP 范围（本期必做）

**Features included**:
- [Feature 1]
- [Feature 2]
- [Feature 3]

**Rationale**: These features are minimum viable to complete the JTBD.

### 6.2 Enhanced Features (Next Iteration) | 增强功能（下期迭代）

**Features deferred**:
- [Feature 4]
- [Feature 5]

**Rationale**: These improve efficiency but are not essential for JTBD completion.

### 6.3 Delighters (TBD) | 锦上添花（待定）

**Features for future consideration**:
- [Feature 6]
- [Feature 7]

**Rationale**: These exceed expectations but can be deferred.

---

## 7. Risks & Dependencies | 风险与依赖

### 7.1 Technical Dependencies | 技术依赖

- [Dependency 1]: [Description and status]
- [Dependency 2]: [Description and status]

### 7.2 Business Risks | 业务风险

- [Risk 1]: [Description and mitigation plan]
- [Risk 2]: [Description and mitigation plan]

### 7.3 Questions to Clarify | 待澄清问题

- [ ] [Question 1]
- [ ] [Question 2]

---

## 8. Appendix | 附录

### 8.1 User Research References | 用户研究参考

- [Link to user interviews]
- [Link to survey results]
- [Link to analytics data]

### 8.2 Competitive Analysis | 竞品分析

- [Competitor 1]: [Key features and approach]
- [Competitor 2]: [Key features and approach]

### 8.3 Change Log | 变更日志

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| [Date] | 0.1 | Initial draft | [Name] |
| [Date] | 0.2 | [Changes] | [Name] |
```

---

## Template 6: Workshop Agenda | 模板 6：工作坊议程

```markdown
# PRD Creation Workshop Agenda | PRD 创建工作坊议程

**Duration | 时长**: 2-3 hours
**Participants | 参与者**: [List of attendees]
**Facilitator | 引导者**: [Name]
**Date | 日期**: [Date]

---

## Pre-Workshop Preparation | 工作坊前准备

**Materials Needed | 所需材料**:
- [ ] Whiteboard or large wall space
- [ ] Sticky notes (3 colors for priority layers)
- [ ] Markers
- [ ] JTBD statement printed and visible
- [ ] User research/pain points reference
- [ ] Laptop for documentation

**Pre-Read | 预读材料**:
- [ ] JTBD methodology overview
- [ ] User research summary
- [ ] Competitive analysis (if available)

---

## Workshop Agenda | 工作坊议程

### Part 1: JTBD Definition (30 minutes) | 第一部分：定义 JTBD（30 分钟）

**10:00 - 10:10** | Introduction & Context
- Review workshop goals
- Present user research findings

**10:10 - 10:25** | JTBD Creation
- Brainstorm JTBD statements
- Refine to final statement
- Decompose into design anchors

**10:25 - 10:30** | Validation
- Check JTBD against criteria
- Get team alignment

---

### Part 2: User Story Mapping (60 minutes) | 第二部分：用户故事地图（60 分钟）

**10:30 - 11:00** | Create Backbone
- Identify user journey steps (5-10 steps)
- Arrange chronologically
- Validate completeness

**11:00 - 11:30** | Brainstorm Features
- For each step, list possible features
- Focus on user needs, not solutions
- Capture all ideas (no filtering yet)

---

### Break (10 minutes) | 休息（10 分钟）

**11:30 - 11:40** | Break

---

### Part 3: Prioritization & Journey Mapping (50 minutes) | 第三部分：优先级与旅程图（50 分钟）

**11:40 - 12:10** | Prioritize Features
- Assign features to MVP/Enhanced/Delighter layers
- Discuss rationale for each decision
- Ensure MVP is truly minimal

**12:10 - 12:30** | Add Journey Layer
- For each step, identify:
  - User goals
  - Emotions
  - Pain points
- Mark experience key points (⚠️)

---

### Part 4: Wrap-Up & Next Steps (10 minutes) | 第四部分：总结与后续步骤（10 分钟）

**12:30 - 12:40** | Review & Next Steps
- Summarize what was created
- Assign action items:
  - [ ] Document story map and journey map
  - [ ] Create user stories with acceptance criteria
  - [ ] Write formal PRD
  - [ ] Schedule validation session
- Set timeline for PRD completion

---

## Post-Workshop Actions | 工作坊后行动

- [ ] Digitize story map and journey map
- [ ] Generate user stories from workshop output
- [ ] Draft PRD document
- [ ] Share with stakeholders for feedback
- [ ] Schedule PRD review meeting
```

---

## Quick Reference | 快速参考

### File Naming Convention | 文件命名约定

```
{output-directory}/
├── jtbd.md           # JTBD definition
├── story_map.md      # Story map + journey overlay
└── prd.md            # Complete PRD
```

### Priority Layer Definitions | 优先级层定义

- **MVP**: Without this, cannot complete JTBD
- **Enhanced**: With this, efficiency significantly improves
- **Delighter**: Exceeds expectations, truly optional

### Experience Key Point Marker | 体验关键点标记

Use ⚠️ to mark steps with:
- High emotional impact
- Severe pain points
- Critical for JTBD success
- Competitive differentiation opportunity

# User Story Mapping Guide | 用户故事地图指南

## Overview | 概述

User Story Mapping is a technique for organizing user stories along two dimensions:
- **Horizontal (时间轴)**: The sequence of activities users perform
- **Vertical (优先级)**: The priority/depth of features for each activity

用户故事地图是一种沿两个维度组织用户故事的技术：
- **水平（时间轴）**：用户执行活动的顺序
- **垂直（优先级）**：每个活动的功能优先级/深度

## Story Map Structure | 故事地图结构

```
Backbone (主干)
├─ Step 1 ─────┬─ Step 2 ─────┬─ Step 3 ─────┬─ Step 4
│              │              │              │
MVP Layer      │ Feature 2.1  │ Feature 3.1  │ Feature 4.1
│ Feature 1.1  │ Feature 2.2  │ Feature 3.2  │ Feature 4.2
│ Feature 1.2  │              │              │
│              │              │              │
Enhanced       │ Feature 2.3  │ Feature 3.3  │ Feature 4.3
│ Feature 1.3  │              │              │
│              │              │              │
Delighter      │ Feature 2.4  │ Feature 3.4  │ Feature 4.4
│ Feature 1.4  │              │              │
```

## Creating the Backbone | 创建主干

### Step 1: Identify User Activities | 识别用户活动

Ask: "From 0 to completing the JTBD, what key steps will users go through?"

问："从 0 到完成 JTBD，用户会经历哪些关键步骤？"

**Example for Project Reporting JTBD:**
1. Open product
2. Select project
3. Choose time range
4. View progress overview
5. Drill into delayed tasks
6. Mark key items
7. Export/share report

### Step 2: Arrange Chronologically | 按时间顺序排列

Place activities from left to right in the order users experience them.

从左到右按用户体验顺序放置活动。

**Tips:**
- 5-10 steps is ideal
- Too few = missing important steps
- Too many = need to group/consolidate
- Each step should be a distinct phase

## Adding Features | 添加功能

### Step 3: List Activities Under Each Step | 在每个步骤下列出活动

For each backbone step, brainstorm:
- What can users do here?
- What information do they need?
- What decisions do they make?
- What actions can they take?

**Example for "View Progress Overview":**
- See task completion percentage
- View delayed task count
- See risk indicators
- View progress chart
- Filter by priority
- Compare to previous week

### Step 4: Prioritize Vertically | 垂直优先级排序

Organize features into three layers:

将功能组织成三层：

#### Layer 1: MVP (Must-Have) | 第一层：MVP（必须有）

**Criteria:**
- Without this, users cannot complete the JTBD
- Minimum viable to achieve the outcome
- Core functionality only

**Example:**
- ✅ See task completion percentage
- ✅ View delayed task count
- ✅ See risk indicators

#### Layer 2: Enhanced (Should-Have) | 第二层：增强（应该有）

**Criteria:**
- With this, efficiency significantly improves
- Makes the experience notably better
- Addresses common pain points

**Example:**
- ✅ View progress chart
- ✅ Filter by priority
- ✅ Sort by various criteria

#### Layer 3: Delighter (Nice-to-Have) | 第三层：锦上添花（可选）

**Criteria:**
- Exceeds expectations
- Provides delight but not essential
- Can be deferred to later releases

**Example:**
- ✅ Compare to previous week
- ✅ AI-suggested focus areas
- ✅ Predictive delay warnings

## Story Map Best Practices | 故事地图最佳实践

### DO: | 做：

✅ Start with backbone before adding features
✅ Use sticky notes or digital tools for flexibility
✅ Involve whole team in mapping session
✅ Focus on user perspective, not system architecture
✅ Keep MVP layer truly minimal
✅ Validate with real users

### DON'T: | 不要：

❌ Skip backbone and jump to features
❌ Organize by system components instead of user flow
❌ Make everything MVP priority
❌ Include features that don't serve the JTBD
❌ Create the map alone without team input

## Story Map Templates | 故事地图模板

### Template 1: Table Format | 模板 1：表格格式

```markdown
## User Story Map

### Backbone Flow
1. [Step 1] → 2. [Step 2] → 3. [Step 3] → 4. [Step 4]

### Feature Details

| Step | MVP | Enhanced | Delighter |
|------|-----|----------|-----------|
| 1. [Step Name] | - Feature A<br>- Feature B | - Feature C | - Feature D |
| 2. [Step Name] | - Feature E<br>- Feature F | - Feature G | - Feature H |
```

### Template 2: Hierarchical Format | 模板 2：层级格式

```markdown
## User Story Map

### Step 1: [Step Name]
**MVP:**
- Feature A: [Description]
- Feature B: [Description]

**Enhanced:**
- Feature C: [Description]

**Delighter:**
- Feature D: [Description]

### Step 2: [Step Name]
[...]
```

## Connecting to JTBD | 连接到 JTBD

Every step in the backbone should help users progress toward completing the JTBD.

主干中的每一步都应帮助用户朝着完成 JTBD 前进。

**Validation questions:**
- Does this step move users closer to the JTBD outcome?
- What happens if we remove this step?
- Is this step necessary for JTBD completion?

**验证问题：**
- 这一步是否让用户更接近 JTBD 结果？
- 如果删除这一步会发生什么？
- 这一步对于完成 JTBD 是否必要？

## Workshop Facilitation | 工作坊引导

### Timing | 时间安排

- **Backbone creation**: 30-45 minutes
- **Feature brainstorming**: 45-60 minutes
- **Prioritization**: 30-45 minutes
- **Total**: 2-3 hours

### Materials Needed | 所需材料

- Whiteboard or large wall space
- Sticky notes (3 colors for 3 priority layers)
- Markers
- JTBD statement visible to all
- User research/pain points reference

### Facilitation Steps | 引导步骤

1. **Review JTBD** (10 min) - Ensure everyone understands the job
2. **Create Backbone** (30 min) - Collaboratively identify steps
3. **Brainstorm Features** (45 min) - Generate ideas for each step
4. **Prioritize** (30 min) - Assign features to MVP/Enhanced/Delighter
5. **Validate** (15 min) - Check against JTBD and user needs

## Common Patterns | 常见模式

### Pattern 1: Discovery → Decision → Action | 模式 1：发现 → 决策 → 行动

```
1. Find information → 2. Evaluate options → 3. Make decision → 4. Take action → 5. Verify result
```

### Pattern 2: Setup → Use → Maintain | 模式 2：设置 → 使用 → 维护

```
1. Configure → 2. Perform task → 3. Review results → 4. Adjust settings
```

### Pattern 3: Create → Collaborate → Deliver | 模式 3：创建 → 协作 → 交付

```
1. Draft → 2. Share → 3. Get feedback → 4. Revise → 5. Publish
```

## Further Reading | 延伸阅读

- **"User Story Mapping"** by Jeff Patton
- **"Mapping Experiences"** by James Kalbach

## Quick Reference | 快速参考

### Story Mapping Checklist | 故事地图检查清单

- [ ] Backbone represents complete user journey
- [ ] Steps are in chronological order
- [ ] Each step has at least 1 MVP feature
- [ ] MVP layer is truly minimal
- [ ] Enhanced layer provides clear value
- [ ] Delighters are genuinely optional
- [ ] All features trace back to JTBD
- [ ] Team has validated the map

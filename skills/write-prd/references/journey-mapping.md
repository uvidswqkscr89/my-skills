# User Journey Mapping Guide | 用户旅程图指南

## Overview | 概述

User Journey Mapping adds emotional and experiential context to the story map by documenting:
- User goals at each step
- Emotional states and feelings
- Pain points and frustrations
- Opportunities for optimization

用户旅程图通过记录以下内容为故事地图添加情感和体验背景：
- 每个步骤的用户目标
- 情绪状态和感受
- 痛点和挫折
- 优化机会

## Journey Map Dimensions | 旅程图维度

### 1. User Goal | 用户目标

**What the user wants to achieve at this step**

**用户在此步骤想要实现什么**

**Questions to ask:**
- What is the user trying to accomplish here?
- What decision are they making?
- What information do they need?
- What's the success criteria for this step?

**Example:**
- Step: "View Progress Overview"
- Goal: "Quickly determine if project is on track or at risk"

### 2. Current/Expected Emotion | 当前/预期情绪

**The user's psychological state**

**用户的心理状态**

**Emotion Categories:**
- **Positive**: Confident, relieved, excited, satisfied, empowered
- **Neutral**: Focused, methodical, routine
- **Negative**: Anxious, frustrated, confused, overwhelmed, stressed

**Example:**
- If information is clear: Confident, in control
- If information is scattered: Anxious, uncertain

### 3. Pain Points/Risks | 痛点/风险

**Where things go wrong or cause friction**

**哪里出错或造成摩擦**

**Types of pain points:**
- **Time**: Takes too long, causes delays
- **Effort**: Requires too much work, too complex
- **Clarity**: Confusing, unclear, ambiguous
- **Reliability**: Errors, failures, inconsistency
- **Accessibility**: Hard to find, hard to use

**Example:**
- Pain: "Report has too much data, hard to find key insights"
- Risk: "Might miss critical delayed tasks in the noise"

## Journey Map Format | 旅程图格式

### Table Format (Recommended) | 表格格式（推荐）

```markdown
## User Journey Overlay

| Step | User Goal | Current/Expected Emotion | Main Pain Points/Risks |
|------|-----------|--------------------------|------------------------|
| ① Login | Quickly enter system | Frustrated if slow | High SSO failure rate |
| ② Select Project | Find project to report | Anxious if many projects | Slow search, messy list |
| ③ Choose Time Range | Set reporting period | Routine, quick | Defaults don't match needs |
| ④ View Overview ⚠️ | Judge project health | Confident if clear, anxious if unclear | Too much data, no conclusion |
| ⑤ Drill into Details ⚠️ | Identify specific issues | Focused, investigative | Hard to filter, slow loading |
| ⑥ Mark Key Items | Highlight for meeting | Efficient, prepared | Can't save selections |
| ⑦ Export/Share | Send to manager | Relieved, done | Export format not suitable |
```

**Note:** ⚠️ marks experience key points (high emotional impact or critical pain points)

**注意：** ⚠️ 标记体验关键点（高情绪影响或关键痛点）

## Creating Journey Maps | 创建旅程图

### Step 1: Start with Story Map Backbone | 从故事地图主干开始

Use the backbone steps from your story map as the journey map structure.

使用故事地图的主干步骤作为旅程图结构。

### Step 2: Add User Goals | 添加用户目标

For each step, identify what the user wants to accomplish.

对于每个步骤，确定用户想要完成什么。

**Tips:**
- Goals should be specific, not generic
- Focus on outcomes, not actions
- Use user language, not technical terms

### Step 3: Map Emotions | 映射情绪

Identify the user's emotional state at each step.

识别用户在每个步骤的情绪状态。

**Sources for emotion data:**
- User interviews: "How did you feel when...?"
- Observation: Watch for facial expressions, body language
- Surveys: Emotion rating scales
- Analytics: Where do users abandon? (frustration indicator)

### Step 4: Document Pain Points | 记录痛点

List specific problems, frustrations, or risks at each step.

列出每个步骤的具体问题、挫折或风险。

**Pain point format:**
- Be specific: "Search takes 5+ seconds" not "Search is slow"
- Include impact: "Causes users to give up and use spreadsheet instead"
- Prioritize by frequency and severity

### Step 5: Mark Experience Key Points | 标记体验关键点

Use ⚠️ to highlight steps where:
- Emotions are strongly positive or negative
- Pain points are severe or frequent
- User success/failure is determined
- Competitive differentiation is possible

## Emotion Mapping Techniques | 情绪映射技术

### Technique 1: Emotion Curve | 技术 1：情绪曲线

Plot emotional intensity across the journey:

```
High +5 ┤     ╭─╮
        │    ╱   ╰╮
Neutral 0┼───╯     ╰─╮
        │            ╰╮
Low  -5 ┤             ╰─
        └─┬──┬──┬──┬──┬──┬─
          1  2  3  4  5  6  7
```

### Technique 2: Emotion Words | 技术 2：情绪词汇

Use specific emotion words, not just positive/negative:

**Positive emotions:**
- Confident, empowered, in control
- Relieved, satisfied, accomplished
- Excited, delighted, surprised
- Focused, engaged, absorbed

**Negative emotions:**
- Anxious, worried, uncertain
- Frustrated, annoyed, angry
- Confused, lost, overwhelmed
- Bored, disengaged, apathetic

### Technique 3: Quotes | 技术 3：引用

Include actual user quotes to bring emotions to life:

```
Step 4: View Overview
Emotion: Anxious
Quote: "I never know if I'm looking at the right thing. There's so much data, but I can't tell if we're in trouble or not."
```

## Pain Point Analysis | 痛点分析

### Pain Point Severity Matrix | 痛点严重程度矩阵

```
High Impact    │ ⚠️ Fix Now    │ ⚠️ Fix Soon
               │ (Frequent)    │ (Rare)
───────────────┼───────────────┼──────────────
Low Impact     │ Monitor       │ Ignore
               │ (Frequent)    │ (Rare)
               └───────────────┴──────────────
                 High Frequency  Low Frequency
```

**Priority:**
1. **Fix Now**: High impact + high frequency (⚠️⚠️)
2. **Fix Soon**: High impact + low frequency (⚠️)
3. **Monitor**: Low impact + high frequency
4. **Ignore**: Low impact + low frequency

### Pain Point Categories | 痛点类别

**Time-based:**
- "Takes too long to load"
- "Requires too many steps"
- "Causes delays in workflow"

**Effort-based:**
- "Too complex to understand"
- "Requires manual work that should be automated"
- "Need to switch between multiple tools"

**Clarity-based:**
- "Unclear what to do next"
- "Confusing terminology"
- "Can't tell if action succeeded"

**Reliability-based:**
- "Frequently fails or errors"
- "Data is inconsistent"
- "Can't trust the results"

## Connecting Journey to Story Map | 连接旅程到故事地图

### Mapping Pain Points to Features | 将痛点映射到功能

For each pain point, identify features that address it:

```
Pain Point: "Report has too much data, hard to find key insights"
↓
Story Map Features:
- MVP: Summary section with key metrics
- Enhanced: Customizable dashboard
- Delighter: AI-generated insights
```

### Prioritizing Based on Emotions | 基于情绪优先级排序

Steps with ⚠️ (high emotional impact) should have:
- More MVP features
- More detailed UX specifications
- More testing and validation
- More user feedback loops

## Journey Map Best Practices | 旅程图最佳实践

### DO: | 做：

✅ Base emotions on real user research
✅ Be specific about pain points
✅ Include both positive and negative emotions
✅ Mark experience key points (⚠️)
✅ Connect pain points to story map features
✅ Update journey map as you learn more

### DON'T: | 不要：

❌ Guess emotions without user data
❌ Only focus on negative emotions
❌ Use vague pain points ("it's confusing")
❌ Ignore positive moments
❌ Create journey map in isolation from story map

## Workshop Facilitation | 工作坊引导

### Timing | 时间安排

- **Add goals**: 15-20 minutes
- **Map emotions**: 20-30 minutes
- **Document pain points**: 20-30 minutes
- **Mark key points**: 10-15 minutes
- **Total**: 60-90 minutes

### Materials Needed | 所需材料

- Story map (already created)
- Different colored sticky notes for emotions
- User research/interview notes
- Pain point data from support tickets, surveys

### Facilitation Steps | 引导步骤

1. **Review story map** (5 min)
2. **Add user goals** (15 min) - One goal per step
3. **Map emotions** (25 min) - Use emotion words, not just +/-
4. **Document pain points** (25 min) - Be specific, include evidence
5. **Mark key points** (10 min) - Identify ⚠️ steps
6. **Connect to features** (10 min) - Link pain points to story map

## Example Journey Map | 示例旅程图

### Project Reporting JTBD

| Step | User Goal | Emotion | Pain Points | Priority |
|------|-----------|---------|-------------|----------|
| ① Login | Enter quickly | Neutral → Frustrated if slow | SSO fails 15% of time | Medium |
| ② Select Project | Find my project | Routine → Anxious if many | 50+ projects, no search | Low |
| ③ Time Range | Set this week | Routine | Defaults to last month | Low |
| ④ Overview ⚠️ | Know if healthy | Confident if clear → Anxious if unclear | 10+ metrics, no summary | **High** |
| ⑤ Details ⚠️ | Find blockers | Focused → Frustrated if slow | 3+ second load, can't filter | **High** |
| ⑥ Mark Items | Highlight for meeting | Efficient | Selections don't save | Medium |
| ⑦ Export | Send to manager | Relieved | PDF format not editable | Low |

**Experience Key Points:** Steps ④ and ⑤ (marked ⚠️) are critical for JTBD success.

## Further Reading | 延伸阅读

- **"Mapping Experiences"** by James Kalbach
- **"The Customer Journey"** by Aimee Lucas

## Quick Reference | 快速参考

### Journey Mapping Checklist | 旅程图检查清单

- [ ] Every story map step has journey information
- [ ] User goals are specific and actionable
- [ ] Emotions are based on real user data
- [ ] Pain points are concrete and measurable
- [ ] Experience key points (⚠️) are marked
- [ ] High-impact pain points have corresponding features
- [ ] Journey map validated with users

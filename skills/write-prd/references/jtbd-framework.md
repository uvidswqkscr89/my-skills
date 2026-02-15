# JTBD Framework Deep Dive | JTBD 框架深入解析

## What is JTBD? | 什么是 JTBD？

**Jobs-to-be-Done (JTBD)** is a framework for understanding customer needs by focusing on the "job" they're trying to accomplish, rather than the product features they might want.

**Jobs-to-be-Done (JTBD)** 是一个理解客户需求的框架，专注于他们试图完成的"任务"，而不是他们可能想要的产品功能。

### Core Principle | 核心原则

> "People don't want a quarter-inch drill. They want a quarter-inch hole."
>
> "人们不想要四分之一英寸的钻头。他们想要四分之一英寸的孔。"

— Theodore Levitt

The job is the hole, not the drill. JTBD helps us focus on the outcome users want, not the solution we think they need.

任务是孔，不是钻头。JTBD 帮助我们专注于用户想要的结果，而不是我们认为他们需要的解决方案。

---

## JTBD Statement Format | JTBD 陈述格式

### Standard Template | 标准模板

```
When I am in [SPECIFIC CONTEXT],
I want to [COMPLETE A TASK],
So that I can [ACHIEVE OUTCOME / AVOID RISK].

当我在【具体情境】时，
我想要【完成某个任务】，
以便于【获得某个结果/避免某个风险】。
```

### Three Components | 三个组成部分

1. **Context (情境)**: The situation that triggers the need
   - Must be specific, not generic
   - Includes timing, location, or circumstance
   - Example: "When I need to report project progress to my manager every week"

2. **Task (任务)**: The action the user wants to complete
   - Must be concrete and actionable
   - Focuses on what, not how
   - Example: "I want to generate a 'key tasks + risks' report in 10 minutes"

3. **Outcome (结果)**: The value gained or risk avoided
   - Must be meaningful to the user
   - Explains why the task matters
   - Example: "So that I can quickly explain if the project will be delayed and secure resources"

---

## Good vs Bad JTBD Examples | 好的与坏的 JTBD 示例

### ❌ Bad Example 1: Too Vague

```
When I use the app,
I want to manage my tasks,
So that I can be productive.
```

**Problems:**
- Context is too generic ("use the app")
- Task is too broad ("manage tasks")
- Outcome is vague ("be productive")

### ✅ Good Example 1: Specific

```
When I arrive at the office each morning,
I want to see which tasks are due today and which are blocked,
So that I can prioritize my work and unblock teammates before standup.
```

**Why it's good:**
- Context is specific (morning arrival at office)
- Task is concrete (see due and blocked tasks)
- Outcome is actionable (prioritize and unblock before standup)

---

### ❌ Bad Example 2: Solution-Focused

```
When I need to track time,
I want to use a timer with start/stop buttons,
So that I can log my hours.
```

**Problems:**
- Prescribes solution (timer with buttons)
- Doesn't explain why time tracking matters
- Focuses on feature, not job

### ✅ Good Example 2: Outcome-Focused

```
When I finish client work each day,
I want to quickly record what I worked on and for how long,
So that I can accurately bill clients and avoid revenue loss.
```

**Why it's good:**
- Doesn't prescribe solution
- Explains real outcome (accurate billing, avoid loss)
- Focuses on the job, not the tool

---

## JTBD Templates by Domain | 按领域分类的 JTBD 模板

### Project Management | 项目管理

```
When I [need to report status / plan sprint / allocate resources],
I want to [see/create/update specific information],
So that I can [make decision / avoid risk / achieve goal].
```

**Example:**
> When I need to plan next sprint,
> I want to see team velocity and upcoming dependencies,
> So that I can commit to realistic scope and avoid overcommitment.

---

### E-commerce | 电子商务

```
When I [shopping situation / decision point],
I want to [find/compare/purchase something],
So that I can [get value / avoid regret / save time or money].
```

**Example:**
> When I'm shopping for a gift with limited time,
> I want to filter by recipient type and see highly-rated options,
> So that I can find something they'll love without spending hours browsing.

---

### SaaS Tools | SaaS 工具

```
When I [work situation / collaboration need],
I want to [accomplish task / share information],
So that I can [improve efficiency / reduce errors / enable team].
```

**Example:**
> When I need to onboard a new team member,
> I want to share our team's knowledge base and grant appropriate access,
> So that they can become productive quickly without repeatedly asking questions.

---

### Healthcare | 医疗保健

```
When I [health situation / care need],
I want to [access care / get information / manage condition],
So that I can [improve health / reduce anxiety / avoid complications].
```

**Example:**
> When I experience new symptoms,
> I want to check if they require urgent care or can wait for regular appointment,
> So that I can get appropriate care without unnecessary ER visits.

---

## Design Anchors | 设计锚点

After creating a JTBD statement, decompose it into three design anchors that guide all subsequent design decisions.

创建 JTBD 陈述后，将其分解为三个设计锚点，指导所有后续设计决策。

### Anchor 1: Context | 锚点 1：情境

**Questions to ask:**
- What triggers this need?
- When does this happen?
- Where is the user?
- What's happening around them?
- What constraints exist?

**Example:**
- Context: "Every Monday morning before standup meeting"
- Triggers: Weekly cadence, team meeting
- Constraints: Limited time (15 minutes before meeting)
- Environment: At desk, need to multitask

### Anchor 2: Task | 锚点 2：任务

**Questions to ask:**
- What specific action is needed?
- What information is required?
- What decisions must be made?
- What artifacts are created?
- What's the success criteria?

**Example:**
- Task: "Identify which team members are blocked and why"
- Information needed: Task status, dependencies, assignees
- Decision: Who to talk to first
- Success: Unblock at least 2 people before standup

### Anchor 3: Outcome | 锚点 3：结果

**Questions to ask:**
- What value is gained?
- What risk is avoided?
- What becomes possible?
- What pain is relieved?
- What goal is achieved?

**Example:**
- Outcome: "Team can start work immediately after standup"
- Value: No wasted time waiting for unblocking
- Risk avoided: Sprint delays due to blockers
- Pain relieved: Frustration of discovering blockers mid-sprint

---

## Validation Questions | 验证问题

Use these questions to validate your JTBD:

使用这些问题验证您的 JTBD：

### Is the Context Specific Enough? | 情境是否足够具体？

- ❌ "When I use the product"
- ✅ "When I arrive at the office each morning"

### Is the Task Concrete? | 任务是否具体？

- ❌ "I want to be more productive"
- ✅ "I want to see which tasks are due today"

### Is the Outcome Meaningful? | 结果是否有意义？

- ❌ "So that I can use the feature"
- ✅ "So that I can prioritize work and unblock teammates"

### Does it Avoid Prescribing Solutions? | 是否避免了规定解决方案？

- ❌ "I want a dashboard with charts"
- ✅ "I want to see project health at a glance"

### Can You Trace Features Back to It? | 能否将功能追溯回它？

For every feature you design, ask:
- "Does this help users complete this JTBD?"
- "Does this address the context, task, or outcome?"
- "Would removing this feature prevent JTBD completion?"

对于您设计的每个功能，问：
- "这是否帮助用户完成此 JTBD？"
- "这是否解决了情境、任务或结果？"
- "删除此功能是否会阻止 JTBD 完成？"

---

## Common Mistakes | 常见错误

### Mistake 1: Feature Disguised as JTBD | 错误 1：伪装成 JTBD 的功能

❌ "When I use the app, I want to see a dashboard, so that I can view data"

This describes a feature (dashboard), not a job.

✅ "When I start my workday, I want to know if any critical issues occurred overnight, so that I can address them before they impact customers"

This describes the job (know about critical issues), not the solution.

### Mistake 2: Too Many Jobs in One Statement | 错误 2：一个陈述中包含太多任务

❌ "When I manage projects, I want to plan, track, report, and collaborate, so that projects succeed"

This is actually 4+ different jobs.

✅ Break into separate JTBDs:
- Planning job
- Tracking job
- Reporting job
- Collaboration job

### Mistake 3: Internal Process, Not User Job | 错误 3：内部流程，而非用户任务

❌ "When data is entered, I want it to be validated, so that the database stays clean"

This is a system requirement, not a user job.

✅ "When I enter customer information, I want to know immediately if something is wrong, so that I can fix it before the customer leaves"

This is the user's job (enter correct information quickly).

---

## JTBD Research Methods | JTBD 研究方法

### Method 1: Jobs Interview | 方法 1：任务访谈

Ask users about recent experiences:
- "Tell me about the last time you [did this task]"
- "What were you trying to accomplish?"
- "What happened before and after?"
- "What made it hard or easy?"
- "What would have made it better?"

### Method 2: Observation | 方法 2：观察

Watch users in their natural environment:
- What triggers the need?
- What workarounds do they use?
- What do they struggle with?
- What do they skip or avoid?

### Method 3: Timeline Mapping | 方法 3：时间线映射

Map the user's journey:
- What happens first, second, third?
- Where do they get stuck?
- Where do they feel anxious or frustrated?
- Where do they feel confident or relieved?

---

## JTBD in PRD Workflow | PRD 工作流中的 JTBD

In the PRD workflow, JTBD serves as the **North Star**:

在 PRD 工作流中，JTBD 作为**北极星**：

1. **Step 2**: Define JTBD → Establishes why we're building
2. **Step 3**: Story Map → Maps how users complete the JTBD
3. **Step 4**: Journey Map → Identifies where to optimize for JTBD completion
4. **Step 5**: User Stories → Each story helps complete the JTBD
5. **Step 6**: PRD → Every feature traces back to JTBD
6. **Step 7**: Quality Check → Validate all features serve the JTBD

Every design decision must answer: **"Does this help users complete the JTBD more smoothly?"**

每个设计决策都必须回答：**"这是否帮助用户更顺利地完成 JTBD？"**

---

## Further Reading | 延伸阅读

- **"Competing Against Luck"** by Clayton Christensen
- **"The Jobs To Be Done Playbook"** by Jim Kalbach
- **"When Coffee and Kale Compete"** by Alan Klement

---

## Quick Reference | 快速参考

### JTBD Checklist | JTBD 检查清单

- [ ] Context is specific (not "when I use the product")
- [ ] Task is concrete (not "be productive")
- [ ] Outcome is meaningful (not "use the feature")
- [ ] Doesn't prescribe solution (not "I want a dashboard")
- [ ] Can trace features back to it
- [ ] Validated with real users
- [ ] Decomposed into 3 design anchors
- [ ] Team understands and agrees on it

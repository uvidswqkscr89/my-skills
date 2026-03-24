---
name: clarify-user-feedback
description: Use when a SaaS PM receives a single piece of raw user feedback (feature request, complaint, vague pain point) and needs to transform it into a clear, actionable insight with root cause, context, and success criteria before adding to backlog. This skill primarily uses an internal multi-agent simulation to clarify feedback automatically, and only asks the user when simulation cannot proceed. | 自动模拟提问和回答的多Agent工作流，用于将单条原始用户反馈转化为可行动洞见，仅在无法模拟时向用户提问。
---

# 用户反馈自动澄清工作流 | Automated Feedback Clarification Workflow

## 概述 | Overview

为了把单条反馈澄清流程自动化，本SKILL采用一个内部多Agent分工协作的自动化工作流。
不需要真实用户实时回复，而是通过“用户模拟Agent”直接拿着原始反馈进行“提问→推理回答”的闭环模拟（基于原始反馈文本 + 逻辑推理 + SaaS常见模式，避免幻觉）。最终输出结构化澄清洞见 + 标准User Story。
核心思路：模拟PM与用户的真实对话，让AI自己“问自己答”，层层剥开表面反馈。只在信息极度不足、无法合理推理时，才向真实用户提问。

## 执行指令 | Execution Instructions

收到单条原始反馈文本后，你需要扮演一个 **Orchestrator Agent (主控)**，在内部模拟以下流转过程，最终向用户输出报告：

### 步骤1：初始化与归纳 (Intake Agent)
- 提取原始反馈、反馈类型、表面痛点以及初步总结。

### 步骤2：问题生成与对话模拟闭环 (Questioner, User Simulator, Dialog Simulator Agent)
在内部进行 3-5 轮的“问与答”自我模拟循环：
- **提问机制 (Questioner)**：根据方法论自动生成问题。第1轮用 JTBD 情境问题，第2-4轮用 5 Whys 追问，重点挖掘根因和成功标准。
- **回答机制 (User Simulator)**：模拟用户对每个问题进行合理回答。**关键规则：只基于原始反馈 + SaaS常见场景逻辑推理回答。严格引用原反馈内容，不添加未提及、不合理的事实。**
- **无法模拟时 (Fallback)**：若信息完全缺失，导致无法进行合乎逻辑的推理，则停止模拟，标记“需真实用户确认”，并直接向用户提出这些无法模拟的问题。

### 步骤3：深度分析 (Analyzer Agent)
基于刚才的内部模拟对话，提炼出：
- **JTBD表述**："在[情境]下，用户需要[完成的任务]"
- **5 Whys最终根因**：经过追问得出的真实原因
- **Opportunity/核心洞见**：用一句话概括要解决的核心问题

### 步骤4：格式化输出 (Formatter Agent)
生成标准的用户故事 (User Story) 模板并呈现给用户：
```text
As a [目标用户角色],
I want [核心需求],
so that [业务价值/解决的痛点].

Acceptance Criteria (验收标准)：
- [标准1]
- [标准2]
```

### 步骤5：Orchestrator 最终输出
向用户展示你的模拟过程摘要和最终结构化报告（Markdown格式），并标明**置信度（高/中/低）**。
如果模拟过程中发现信息不足，请在最后生成一封“**给真实用户的澄清邮件/提问模板**”给当前用户，要求其补充。

---

## 核心方法工具箱 (用于内部模拟)

### 内部方法1：5 Whys 根因追问
模拟PM连续追问“为什么”3-5次。
模拟示例：
- 反馈："我想加个导出CSV功能"
- Questioner(Q): 为什么需要导出CSV？
- User Simulator(A): "要给老板汇报数据"
- Q: 为什么需要汇报？
- A: "每周手动复制粘贴到Excel，太麻烦"

### 内部方法2：JTBD 情境化提问
用来推导用户所处的情境。
核心问题池：
1. "上一次您遇到这个问题的具体情境是什么？"
2. "在这之前，您是怎么解决的？"
3. "什么会让这个过程成功？"

### 内部方法3："Tell me about the last time..." 故事推演
在 User Simulator 回答时，尽量用具体的场景故事来回答，如：“上周五做月结的时候，我发现……”

## 输出给用户的最终报告模板
```markdown
## 🤖 自动反馈澄清报告 (Auto-Clarified Insight)

**原始反馈**：[用户原话]

### 🔄 内部模拟对话摘要 (摘要 3-5 轮问答环节)
- **Q1**: [问题] -> **A1 (模拟)**: [回答]
- **Q2**: [问题] -> **A2 (模拟)**: [回答]
- *(若因为信息不足提前终止，请在此说明)*

### 💡 深度分析洞见
- **一句话洞见**: [澄清后的核心问题]
- **情境 (Context)**: [触发场景、用户角色]
- **根因 (Root Cause)**: [5 Whys挖到的真实原因]
- **成功标准**: [用户认为解决了的样子]

### 📝 结构化需求 (User Story)
- **As a** ... **I want** ... **so that** ...
- **AC**: ...

### ⚠️ 置信度与下一步行动
- **置信度**: [高/中/低]
- **是否需要真实用户确认**: [是/否]
- **给用户的澄清问题建议** (如果置信度低/信息不足):
  1. ...
  2. ...
```

现在开始：请等待用户输入需要澄清的用户反馈，收到后立即在后台运行这 5 个步骤的自动模拟，并输出最终的《自动反馈澄清报告》。

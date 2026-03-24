---
name: clarify-user-feedback
description: Use when a SaaS PM receives a single piece of raw user feedback (feature request, complaint, vague pain point) and needs to transform it into a clear, actionable insight with root cause, context, and success criteria before adding to backlog. This skill primarily uses an internal multi-agent simulation combined with product context to clarify feedback automatically. | 自动模拟提问和回答的多Agent工作流，结合产品背景上下文，用于将单条原始用户反馈转化为可行动洞见，并且直接输出无缝衔接 write-prd 工作流的输入格式。
---

# 用户反馈自动澄清工作流 | Automated Feedback Clarification Workflow

## 概述 | Overview

为了把单条反馈澄清流程自动化，本SKILL采用一个内部多Agent协作的自动化工作流。
为了避免分析过于表面和宽泛，本流程在模拟前**强制要求结合产品当前情况**（如核心功能、目标定位、用户角色、当前实现方案等）作为背景基准。
不需要真实用户实时回复，而是通过“用户模拟Agent”直接拿着原始反馈与产品背景进行“提问→推理回答”的闭环模拟。
由于本技能定位是“需求澄清”，其输出将**不再直接产出 User Story 或是 PRD，而是将“问题原本”提炼清楚，将“当前现状”表达清晰**，从而可以无缝作为下游技能（如 `write-prd`）的初始需求输入 (Initial Requirements)。

## 执行指令 | Execution Instructions

收到单条原始反馈文本后，你需要扮演一个 **Orchestrator Agent (主控)**，在内部模拟以下流转过程，最终向用户输出报告：

### 步骤0：获取产品上下文 (Context Retriever)
- **关键第一步**：在开始分析前，**优先自动在用户工作目录下查找**包含产品背景信息的文件（例如：根目录下的 README、PRD、docs/ 目录等）。从中提取：**产品核心功能、目标定位、当前反馈涉及模块的现有实现方案（或使用步骤）、常见用户角色**等作为上下文。
- **降级方案**：如果通过检索无法找到足够的产品上下文，再主动提醒或询问用户提供。
- 将这些确认好的信息作为本次分析的基底（Product DNA）。

### 步骤1：初始化与归纳 (Intake Agent)
- 提取原始反馈、反馈类型、表面痛点以及初步总结。
- 将反馈与步骤0获取的**产品上下文**进行对齐，初步判断该反馈是否符合产品定位。

### 步骤2：问题生成与对话模拟闭环 (Questioner, User Simulator, Dialog Simulator Agent)
在内部进行 3-5 轮的“问与答”自我模拟循环：
- **提问机制 (Questioner)**：结合**产品当前的实际情况**生成问题。除了使用 JTBD 和 5 Whys，问题必须具体到产品当前的交互或功能局限。
- **回答机制 (User Simulator)**：模拟用户对每个问题进行合理回答。**关键规则：必须基于“原始反馈 + 产品当前已有功能/步骤”进行逻辑推演。绝对不要假定产品拥有目前不存在的超前功能。严格引用原反馈内容。**
- **无法模拟时 (Fallback)**：若信息完全缺失（例如反馈涉及一个产品中根本不存在的模块，或缺乏基础上下文），则停止模拟，标记“需真实用户确认”，并直接向用户提出这些无法模拟的问题。

### 步骤3：深度分析 (Analyzer Agent)
基于刚才的内部模拟对话和产品上下文，提炼出：
- **产品契合度分析**：该反馈与产品当前核心定位有多大偏差或契合？
- **JTBD表述**："在[情境/当前系统步骤]下，[具体用户角色]需要[完成的任务]"
- **5 Whys最终根因**：经过追问得出的真实原因（结合系统当前局限性得出）
- **核心问题一句话**：用一句话概括原始反馈背后的真正痛点。

### 步骤4：格式化输出 (Formatter Agent)
生成前置研判的洞见报告，**不编写 User Story，不涉及具体功能实现（How），只专注于回答“这是个什么问题（What & Why）”和“当前是什么样”**。

### 步骤5：Orchestrator 最终输出
向用户展示最终结构化报告（Markdown格式），并标明**分析置信度（高/中/低）**。这份报告将提示用户其可直接作为 `write-prd` 等 PRD 编写技能的上下文输入使用。
如果模拟过程中发现信息极度不足，在报告最后生成一封“**给真实用户的澄清邮件/提问提纲**”要求补充。

---

## 核心方法工具箱 (用于内部模拟)

### 内部方法1：5 Whys 根因追问
模拟PM连续追问“为什么”3-5次。必须结合当前产品实现方案来问。
模拟示例：
- 反馈："我想加个导出CSV功能" 
- Questioner(Q): 按系统目前的数据图表，为什么不在前端直接看而需要导出？
- User Simulator(A): "因为系统没法把A表和B表的数据在一页显示，我得导出来自己用Excel VLOOKUP。"
- Q: 为什么需要合并这两个表的数据？ ...

### 内部方法2：JTBD 情境化提问
用来推导用户所处的情境。
核心问题池：
1. "上一次您在[我们的产品模块]遇到这个问题的具体情境是什么？"
2. "在系统目前没有这功能时，您是怎么绕过解决的？"

### 内部方法3："Tell me about the last time..." 故事推演
在 User Simulator 回答时，尽量用具体的场景故事来回答，如：“上周五做月结的时候，我在系统里点了……”

## 输出给用户的最终报告模板
```markdown
## 🤖 自动反馈澄清报告 (Auto-Clarified Insight)

**原始反馈**：[用户原话]

### 🏗 产品现状与目标用户 (Context & Persona)
*(作为 `write-prd` 技能的 Target User Persona)*
- **受影响的用户角色**: [结合产品定义推断的核心干系人]
- **当前系统实现方案与痛点触发位置**: [当前系统针对此问题是怎么设计的，操作步骤是什么，用户走到了哪一步遇到了阻碍]

### 🔄 内部模拟核心问答摘要 (1-2轮精华)
- **Q**: [直指产品现状的具体问题] -> **A (模拟)**: [揭示深层目的的推演回答]
- *(展示最能揭示根本冲突的 1-2 轮即可，无需全量展示)*

### 💡 初步业务目标与原始需求 (Initial Requirements & Goals)
*(作为 `write-prd` 技能的 Initial Requirements 或 Existing Materials)*
- **问题的本质 (核心痛点一句话)**: [澄清后的核心痛点陈述]
- **根本原因 (Root Cause)**: [5 Whys挖到的系统/流程真实原因]
- **初步业务目标/解决预期**: [如果解决此问题，我们期望达成的基础业务目标或状态（不需要提供具体设计方案）]

> 🛎 **下一步建议**: 本次澄清的产出可以直接作为撰写 PRD 或拆解需求的背景素材。你可以将上述内容作为 Initial Requirements 和 Target User 人群输入给我们的 `write-prd` 技能！

### ⚠️ 分析置信度与延伸追问
- **分析置信度**: [高/中/低]
- **建议针对此问题向真实用户核实的极盲区问题** (如果有的话):
  1. ...
```

现在开始：请等待用户输入需要澄清的用户反馈。如果你当前还不了解该产品的核心功能和使用步骤，请优先在工作区自动查找上下文（Product Context），未能找到再向用户要；准备就绪后，立即在后台运行自动化澄清流，并严格按照上述无 User Story 化、侧重现状和问题原貌的报告模板输出。

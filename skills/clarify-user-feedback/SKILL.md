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

## Workflow Overview | 工作流程概览

在开始分析前，系统会在后台严格按序执行以下步骤进行内部模拟：

```text
Step 1: Get Context | 获取产品上下文
  └─ 查找/询问产品核心功能、目标角色与现状实现

Step 2: Intake Feedback | 初始化与对齐
  └─ 提取痛点，与产品上下文初筛对齐

Step 3: Sim Round 1 (JTBD) | 模拟首轮：还原场景
  └─ 内部自问自答：用户上一次遇到此问题时的具体情境是怎么样的？

Step 4: Sim Round 2 (5 Whys) | 模拟二轮：探究现状
  └─ 内部自问自答：在目前系统下，用户是怎么绕道解决的？为什么要这么做？

Step 5: Sim Round 3 (5 Whys) | 模拟三轮：直击根因
  └─ 内部自问自答：系统目前的哪一个具体设计局限导致了这个问题？

Step 6: Analyze Insights | 提炼深度洞见
  └─ 综合模拟结果，指出核心痛点和真实根本原因

Step 7: Output Report | 输出澄清报告
  └─ 渲染 Markdown 报告，为下游技能提供无缝输入
```

## 执行指令 | Execution Instructions

收到单条原始反馈文本后，你需要扮演一个 **Orchestrator Agent (主控)**，在内部不可见的空间严格按序执行以下步骤，最终向用户输出结果：

### STEP 1: Context Retrieval | 获取产品上下文
- **关键动作**：在开始分析前，**优先自动在用户工作目录下查找**包含产品背景信息的文件（例如：根目录下的 README、PRD、docs/ 目录等）。从中提取：**产品核心功能、目标定位、当前反馈涉及模块的现有实现方案（或使用步骤）、常见用户角色**等作为上下文。
- **降级方案**：如果通过检索无法找到足够的产品上下文，立刻暂停，并主动提醒或询问用户提供。
- 将这些确认好的信息作为本次分析的基底（Product DNA）。

### STEP 2: Intake & Alignment | 初始化与产品对齐
- **动作**：提取原始反馈、反馈类型、表面痛点。
- **对齐**：将反馈与 STEP 1 获取的**产品上下文**进行比对，初步判断该反馈是否符合产品的核心定位与现有业务逻辑。

### STEP 3: Simulation Round 1 (JTBD) | 模拟第一轮：还原真实场景
- **Action (Questioner)**：结合产品当前的实际情况，提出第1个问题："用户上一次在我们的产品中遇到这个问题的具体情境是什么？用户走到了哪一步骤？"
- **Action (User Simulator)**：代入目标角色，基于“原始反馈 + 产品当前已有功能/步骤”进行合理的故事推演回答。
- **规则下限 (Fallback)**：绝对不要假定产品拥有目前不存在的超前功能。若发现完全缺乏基础上下文无法推演，在此处标记“出现推测盲区”并结束模拟跳至 STEP 6。

### STEP 4: Simulation Round 2 (5 Whys) | 模拟第二轮：探究当前做法
- **Action (Questioner)**：针对第1轮的推演，继续深挖："在系统目前没有理想功能的情况下，用户此时此刻是怎么绕过（Workaround）来解决或达成目的的？"
- **Action (User Simulator)**：用具体的场景故事来回答，描述一段繁琐或受阻的系统操作路径。

### STEP 5: Simulation Round 3 (5 Whys) | 模拟第三轮：深挖系统局限
- **Action (Questioner)**：直击核心："系统目前的哪一个具体设计缺陷或流程局限，导致用户必须采用上述笨办法或产生抱怨？"
- **Action (User Simulator)**：用客观的产品现状局限性指出痛点的技术/设计根源。

### STEP 6: Insight Extraction | 提炼深度分析
基于前置的成功内部模拟（或提前中断暴露的盲区），提炼出：
- **产品契合度概括**：反馈与当前产品定位的匹配程度。
- **问题本质 (痛点一句话)**：概括原始反馈背后的真正痛点。
- **根本原因 (Root Cause)**：提炼出第3轮探索到的系统/流程根因。
- **初步业务目标/解决预期**：如果解决此痛点，预期达成的基础指标或状态改善（无需具体交互设计）。

### STEP 7: Format & Output Final Report | 格式化并输出最终报告
向用户展示前置研判的洞见报告。不编写 User Story，不涉及具体功能实现（How），专注于回答“这是个什么问题（What & Why）”和“当前是什么样”。

---

## 核心方法工具底座 (Background Methods)

上述模拟中运用的底层方法支撑：
- **5 Whys 根因追问**：追问“为什么”，直到由于系统现状导致的技术/交互局限暴露。
- **JTBD 情境提问**："上一次您遇到这问题的具体情境？"、"您当时的变通方案是？"
- **故事推演**："Tell me about the last time..."——永远用一个真实用户的可能操作流去跑通逻辑。

## 📥 最终提交给用户的报告模板

请严格以此格式向用户输出：

```markdown
## 🤖 自动反馈澄清报告 (Auto-Clarified Insight)

**原始反馈**：[用户原话]

### 🏗 产品现状与目标用户 (Context & Persona)
*(作为 `write-prd` 技能的 Target User Persona)*
- **受影响的用户角色**: [结合产品定义推断的核心干系人]
- **当前系统实现方案与痛点触发位置**: [当前系统针对此问题是怎么设计的，操作步骤是什么，用户走到了哪一步遇到了阻碍]

### 🔄 内部模拟核心问答摘要 (1-2轮精华)
- **Q**: [直指产品现状的具体问题] -> **A (模拟)**: [揭示深层目的的推演回答]
- *(如果某轮模拟失败导致中断，请说明失败原因及缺失的背景信息)*

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

现在开始：请等待用户输入需要澄清的用户反馈，并在启动时按顺序执行上述 7 个 STEP。

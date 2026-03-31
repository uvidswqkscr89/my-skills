---
name: feedback-to-design
description: End-to-end orchestration skill that transforms raw user feedback into a validated PRD and UI/UX design spec. Runs four stages in sequence: (1) clarify-user-feedback — extract root cause and structured insight, (2) write-prd — generate jtbd.md / story_map.md / prd.md using JTBD methodology, (3) prd-validator — quality check against 8 criteria, (4) ui-ux-designer — produce wireframes, component specs, and interaction patterns. Use when: user provides raw feedback or a feature request and wants to go all the way from insight to design-ready spec. Requires product context (README, existing PRDs, or description). | 端到端编排：从原始用户反馈到 UI/UX 设计规范的完整流程，串联需求澄清 → PRD 编写 → 质量验证 → UI/UX 设计四个阶段。
---

# Feedback-to-Design 编排 Skill

将一条原始用户反馈，经过四个阶段，输出可直接交付开发的 UI/UX 设计规范。

## 流程总览

```
[输入] 原始用户反馈 + 产品上下文
    ↓
Stage 1: clarify-user-feedback
  → 输出: clarified-insight（结构化洞见，含根因 + 业务目标）
    ↓
Stage 2: write-prd
  → 输入: clarified-insight 作为 Initial Requirements
  → 输出: {output-dir}/jtbd.md + story_map.md + prd.md
    ↓
[人工 Checkpoint A] 确认 PRD 方向后继续
    ↓
Stage 3: prd-validator
  → 输出: 8项质量评分 + 修复建议
  → 自动修复可修复问题，重新评分直到 ≥ 6/8
    ↓
Stage 4: ui-ux-designer
  → 输入: prd.md + story_map.md + jtbd.md
  → 输出: {output-dir}/ui_ux_design.md
    ↓
[人工 Checkpoint B] 最终交付确认
```

## 执行指令

### 启动条件

收到以下任意触发时执行本流程：
- 用户提供原始反馈 + 要求生成设计规范
- 用户说"跑完整流程"、"从反馈到设计"、"run feedback-to-design"

启动前收集：
1. **原始反馈文本** — 用户的原话，越原始越好
2. **产品上下文** — 优先自动查找（README、现有 PRD、docs/），找不到则询问
3. **输出目录** — 建议格式：`prd/{feature-name}-{YYYY-MM-DD}/`，未指定则自动生成

---

### Stage 1: 需求澄清（clarify-user-feedback）

读取并遵循 `skills/clarify-user-feedback/SKILL.md` 的完整执行流程。

**关键输出**（内存中保留，传递给 Stage 2）：
- 受影响的用户角色
- 当前系统实现与痛点触发位置
- 问题本质（核心痛点一句话）
- 根本原因（Root Cause）
- 初步业务目标

**置信度处理**：
- 高/中：直接进入 Stage 2
- 低：向用户补充说明盲区，询问是否继续或补充信息

---

### Stage 2: PRD 编写（write-prd）

读取并遵循 `skills/write-prd/SKILL.md` 的完整 9 步工作流。

**输入映射**（将 Stage 1 输出映射到 write-prd 的 Step 1 上下文）：

| write-prd 字段 | 来源 |
|----------------|------|
| Target User Persona | Stage 1: 受影响的用户角色 |
| Initial Requirements | Stage 1: 问题本质 + 根本原因 + 业务目标 |
| Existing Materials | Stage 1: 当前系统实现描述 |
| Output Directory | 启动时确定的输出目录 |

**Checkpoint A**：完成 Step 6（PRD 结构化）后，向用户展示 PRD 摘要（JTBD + MVP 范围），等待确认后继续 Step 7-9。

---

### Stage 3: 质量验证（prd-validator）

按照 `agents/prd-validator.md` 的 8 项标准逐一验证。

**自动修复规则**：
- 文件间不一致（jtbd.md / story_map.md / prd.md 描述不同步）→ 以 prd.md 为准自动修复
- 缺少验收标准 → 基于 User Story 内容自动补充
- 优先级分层不一致 → 以 prd.md 范围章节为准同步

**阻断规则**（需人工介入，不自动修复）：
- JTBD 本身模糊或缺失 → 返回 Stage 2 Step 2 重新定义
- User Story 格式严重不符 → 提示用户确认后重写

**通过标准**：评分 ≥ 6/8 继续；< 6/8 列出关键问题，修复后重新评分。

---

### Stage 4: UI/UX 设计（ui-ux-designer）

读取并遵循 `skills/ui-ux-designer/SKILL.md` 的完整 5 步流程。

**输入**：Stage 2 输出的三个文件（jtbd.md / story_map.md / prd.md）

**输出**：`{output-dir}/ui_ux_design.md`

**Checkpoint B**：生成完成后，向用户展示设计摘要（屏幕列表 + 关键组件），确认是否需要调整。

---

## 阶段间数据传递

各阶段通过**文件**传递数据（不依赖内存），确保每阶段可独立重跑：

```
{output-dir}/
├── jtbd.md              ← Stage 2 输出，Stage 3/4 读取
├── story_map.md         ← Stage 2 输出，Stage 3/4 读取
├── prd.md               ← Stage 2 输出，Stage 3/4 读取
└── ui_ux_design.md      ← Stage 4 输出
```

Stage 1 的澄清报告**不单独写文件**，直接作为 Stage 2 的 Initial Requirements 输入（减少文件噪音）。如需保留，可写入 `{output-dir}/clarified-insight.md`。

---

## 断点续跑

用户可以从任意阶段重新开始，只需说明：
- "从 Stage 3 继续" → 跳过 Stage 1/2，直接验证现有 PRD
- "重新跑 UI 设计" → 跳过 Stage 1/2/3，直接执行 Stage 4
- "PRD 有改动，重新验证和设计" → 从 Stage 3 开始

---

## 参考资源

各阶段详细执行指令见对应 skill 文件：
- `skills/clarify-user-feedback/SKILL.md`
- `skills/write-prd/SKILL.md`
- `skills/ui-ux-designer/SKILL.md`（含 references/）
- `my-skills/agents/prd-validator.md`（验证标准）

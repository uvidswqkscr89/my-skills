---
name: ui-ux-designer
description: Transform a completed PRD (prd.md + story_map.md + jtbd.md) into detailed UI/UX design specifications. Outputs screen-by-screen wireframe descriptions, interaction patterns, component specs, and design tokens. Use when: (1) a PRD has been written and validated, (2) user asks to design the UI/UX for a feature, (3) user asks for wireframes, interaction specs, or design guidelines based on requirements. Input: path to a PRD directory containing prd.md and story_map.md. Output: ui_ux_design.md with full design spec. | 将已完成的 PRD 转化为详细的 UI/UX 设计规范，输出逐屏线框图描述、交互模式、组件规范和设计令牌。
---

# UI/UX Designer Skill

将 PRD 转化为可直接交付给开发的 UI/UX 设计规范。

## 输入要求

执行前确认以下文件存在：
- `prd.md` — 包含 User Stories、验收标准、交互关键点
- `story_map.md` — 包含用户旅程和功能分层
- `jtbd.md` — 包含 JTBD 和设计锚点

如果路径未指定，在当前目录或用户提到的目录下查找。

## 执行流程（5步）

### STEP 1: 读取 PRD 上下文

读取三个输入文件，提取：
- JTBD 核心句式和设计检验标准
- 用户旅程主干流程（步骤列表）
- 所有 User Stories 和验收标准
- 已有的交互关键点描述（prd.md 第 4 节）
- MVP 范围（哪些功能本期做）

### STEP 2: 确定设计范围

基于 MVP 范围，列出需要设计的**屏幕/区域**清单。每个 User Story 对应至少一个设计区域。

格式：
```
设计范围：
- Screen A: [名称] — 对应 US-XXX
- Screen B: [名称] — 对应 US-XXX
- Component C: [名称] — 跨屏复用
```

向用户确认范围后继续（或直接执行，若用户已明确要求）。

### STEP 3: 逐屏输出线框图描述

对每个屏幕/区域，输出：

1. **屏幕目的** — 一句话说明这个屏幕解决什么问题
2. **布局结构** — 用 ASCII 或文字描述区域划分
3. **核心元素** — 列出每个 UI 元素（组件类型、内容、状态）
4. **交互行为** — 描述用户操作触发的状态变化
5. **边界状态** — 空状态、加载态、错误态、降级态

参考 `references/wireframe-patterns.md` 获取常用布局模式。

### STEP 4: 输出组件规范 & 设计令牌

对新增或改动的组件，输出：
- 组件名称和用途
- Props/状态列表
- 视觉规范（颜色、间距、字体）
- 与现有设计系统的关系（复用/新增/改动）

参考 `references/design-tokens.md` 获取规范格式。

### STEP 5: 生成输出文件

将所有内容写入 `{prd目录}/ui_ux_design.md`。

文件结构：
```
# UI/UX Design Spec: [功能名称]

## 设计原则（来自 JTBD）
## 设计范围
## 屏幕设计
  ### Screen 1: ...
  ### Screen 2: ...
## 组件规范
## 设计令牌
## 开发交付说明
```

## 质量检验标准

每个设计决策都要能回答 JTBD 的检验标准。完成后自检：
- [ ] 每个 MVP User Story 都有对应的设计区域
- [ ] 每个 ⚠️ 旅程痛点都有对应的 UX 优化设计
- [ ] 所有边界状态（空/加载/错误）都已覆盖
- [ ] 组件规范足够开发直接实现，无需猜测

## 参考资源

- `references/wireframe-patterns.md` — 常用布局模式和 ASCII 线框图模板
- `references/design-tokens.md` — 颜色、间距、字体规范格式
- `references/interaction-patterns.md` — 常用交互模式（hover、展开、滚动、加载等）

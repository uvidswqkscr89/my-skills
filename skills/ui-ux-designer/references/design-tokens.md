# Design Tokens | 设计令牌规范

UI/UX 设计规范中使用的颜色、间距、字体标准格式。

---

## 颜色令牌（Color Tokens）

### 语义色

| Token | 用途 | 示例值 |
|-------|------|--------|
| `color.success` | 成功、通过 | `#52C41A` |
| `color.error` | 失败、错误 | `#FF4D4F` |
| `color.error.bg` | 错误背景（浅） | `#FFF1F0` |
| `color.error.border` | 错误边框/竖线 | `#FF4D4F` |
| `color.warning` | 警告 | `#FA8C16` |
| `color.warning.bg` | 警告背景（浅） | `#FFF7E6` |
| `color.info` | 信息、进行中 | `#1890FF` |
| `color.neutral` | 未执行、禁用 | `#D9D9D9` |
| `color.neutral.text` | 次要文字 | `#8C8C8C` |

### 文字色

| Token | 用途 |
|-------|------|
| `color.text.primary` | 主要文字 `#262626` |
| `color.text.secondary` | 次要文字 `#595959` |
| `color.text.disabled` | 禁用文字 `#BFBFBF` |
| `color.text.error` | 错误文字 `#FF4D4F` |

---

## 间距令牌（Spacing Tokens）

基础单位：4px

| Token | 值 | 用途 |
|-------|-----|------|
| `spacing.xs` | 4px | 图标与文字间距 |
| `spacing.sm` | 8px | 组件内部间距 |
| `spacing.md` | 12px | 列表项间距 |
| `spacing.lg` | 16px | 区块间距 |
| `spacing.xl` | 24px | 页面区域间距 |
| `spacing.2xl` | 32px | 页面级间距 |

---

## 字体令牌（Typography Tokens）

| Token | 大小 | 行高 | 用途 |
|-------|------|------|------|
| `text.heading.lg` | 20px | 28px | 页面标题 |
| `text.heading.md` | 16px | 24px | 区块标题 |
| `text.body.md` | 14px | 22px | 正文 |
| `text.body.sm` | 12px | 20px | 辅助文字、说明 |
| `text.code` | 12px | 20px | 代码、错误信息（monospace） |

---

## 组件规范格式模板

描述一个新增或改动组件时，使用以下格式：

```markdown
### ComponentName

**用途**：[一句话说明]

**Props / 状态**：
| Prop | 类型 | 说明 |
|------|------|------|
| status | 'success' \| 'failed' \| 'pending' | 步骤状态 |
| errorMessage | string \| null | 错误原因文字 |
| isExpanded | boolean | 错误详情是否展开 |

**视觉规范**：
- 失败状态：背景色 `color.error.bg`，左侧 2px 竖线 `color.error.border`
- 错误文字：`text.code`，颜色 `color.text.error`
- 展开/折叠动画：200ms ease

**交互行为**：
- 页面加载时，失败步骤自动展开
- 点击步骤行可手动折叠/展开错误详情

**与设计系统关系**：
- 基于现有 StepItem 组件扩展，新增 errorMessage prop 和展开状态
```

---

## 边界状态规范

每个组件/区域都需要覆盖以下状态：

| 状态 | 触发条件 | 设计处理 |
|------|----------|----------|
| 正常态 | 数据正常加载 | 主设计 |
| 加载态 | 数据请求中 | 骨架屏或 Spinner |
| 空状态 | 无数据 | Empty State 组件 |
| 错误态 | 请求失败 | 错误提示 + 重试 |
| 降级态 | 部分数据缺失 | 隐藏对应元素，不影响主流程 |

# Test Case Format Reference

## Directory Naming Conventions

- Domain directories: lowercase, hyphen-separated (e.g., `user-auth`, `payment`)
- Module directories: lowercase, hyphen-separated (e.g., `login`, `checkout`)
- Feature files: lowercase, hyphen-separated, `.md` extension (e.g., `basic-login.md`, `oauth-login.md`)
- No spaces, no uppercase, no underscores in paths

## Feature File Format (`{feature}.md`)

```markdown
# {功能名称} 测试用例

> PRD来源: {prd_id或文件名} | 最后更新: {YYYY-MM-DD}

## 正向流程
- [ ] TC-001: {自然语言描述测试意图}
- [ ] TC-002: ...

## 异常流程
- [ ] TC-100: ...

## 边界值
- [ ] TC-200: ...
```

## TC ID Numbering Rules

- Format: `TC-{NNN}` where NNN is a zero-padded 3-digit integer
- Category ranges:
  - 正向流程 (Happy path): TC-001 to TC-099
  - 异常流程 (Error/exception): TC-100 to TC-199
  - 边界值 (Boundary): TC-200 to TC-299
- When appending: read the highest existing ID in that category, increment by 1
- Range overflow: if a category is full (e.g., TC-099 used), continue from TC-300 sequentially and append `<!-- overflow -->` to the line
- IDs are file-scoped (not globally unique). Uniqueness key = module path + TC ID
- On file split: original file keeps original IDs; new file starts from TC-001

## Index File Format (`_index.md`)

```markdown
# {层级名称}

## 子模块
- [{模块名}](./{模块路径}/_index.md) — {一句话描述}

## 用例文件
- [{功能名}](./{feature}.md) — {一句话描述}
```

## `_index.md` Update Rules

- Adding a sub-module: append one line to the "子模块" list
- Adding a feature file: append one line to the "用例文件" list
- First-time initialization (no `test-cases/` directory): create root `_index.md` with empty lists under both headings
- Missing intermediate directories: show the full path to be created, wait for user confirmation before creating

## Root Index Bootstrap Template

```markdown
# 测试用例库

## 子模块

## 用例文件
```

# CRUD Classification Rules (Sub-flow 3)

## Three-State Classification

When comparing existing test cases against PRD_V2, classify each affected case into one of three states:

### UPDATE
The test scenario still exists in PRD_V2, but the intent or scope has changed.
- The feature being tested still exists
- The expected behavior, preconditions, or scope has changed
- Action: modify the natural language description in place, keep the TC ID

Example:
- Old: "验证用户名密码登录"
- PRD_V2 change: login now requires 2FA
- New: "验证用户名密码及二次验证码登录"

### DELETE / DEPRECATE
The test scenario no longer applies in PRD_V2.
- The feature has been removed
- The business rule has been eliminated
- Action: mark the line with `~~` strikethrough and append `(已废弃 YYYY-MM-DD)`, do NOT delete the line

Example:
- `- [x] ~~TC-007: 验证记住密码功能~~ (已废弃 2026-03-17)`

### CREATE
A new scenario exists in PRD_V2 that has no corresponding existing test case.
- New feature or business rule introduced
- Action: add as a new test case following tc-format.md rules

## Boundary Cases

| Situation | Classification |
|-----------|---------------|
| Intent partially changed (same feature, different scope) | UPDATE |
| Feature renamed but behavior unchanged | UPDATE (update description only) |
| Feature split into two separate features | DELETE original + CREATE two new cases |
| Feature merged from two into one | DELETE both originals + CREATE one new case |
| Behavior completely reversed | UPDATE (not DELETE+CREATE) |

## Output Format Template

When presenting the CRUD analysis to the user, use this format:

```
即将执行以下变更，请确认：

[UPDATE] {relative/path/to/feature.md}
  TC-{NNN}: "{old description}" → "{new description}"

[DELETE] {relative/path/to/feature.md}
  TC-{NNN}: "{description}" (已废弃)

[CREATE] {relative/path/to/feature.md} {(新文件) if new file}
  TC-{NNN}: "{new description}"

输入 "确认" 执行，或指出需要修改的部分：
```

Partial confirmation is supported. User may respond: "确认 UPDATE 和 CREATE，跳过 DELETE"

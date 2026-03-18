# Semantic Deduplication Reference

## When to Apply

Run deduplication in:
- Sub-flow 1 (new PRD ingestion): before writing any new test case
- Sub-flow 2 (incremental supplement): before writing any supplemental test case

## Scope

Compare only within the same module. Do not compare across modules.
This keeps token usage bounded and avoids false positives from similar-sounding but contextually different cases.

## Similarity Scoring Prompt Template

For each candidate new test case, evaluate against each existing test case in the target module:

```
你是一个测试用例相似度评估专家。请评估以下两条测试用例的语义相似度。

候选用例：{new_case}
已有用例：{existing_case}

请按以下格式输出：
相似度分数：{0-100的整数}
判断理由：{一句话说明相似或不同的核心原因}
建议：{SKIP（跳过）/ CONFIRM（需用户确认）/ ADD（直接新增）}

评分参考：
- 90+：测试意图完全相同，仅措辞不同
- 70-89：测试同一功能点，但覆盖范围有差异
- 40-69：测试相关功能，但关注点不同
- 0-39：测试不同功能或场景
```

## Decision Table

| Score | Action |
|-------|--------|
| > 85 | SKIP — record as "already exists: {existing_case}" |
| 40–85 | CONFIRM — flag as "possible duplicate", show both to user |
| < 40 | ADD — proceed without user input |

## Calibration Examples

### High similarity — SKIP (score > 85)

**Example A**
- Candidate: "验证用户使用正确的用户名和密码可以成功登录"
- Existing: "验证用户输入有效凭据后能够登录系统"
- Score: 92 — same intent, different wording

**Example B**
- Candidate: "verify user can log in with valid credentials"
- Existing: "验证用户使用有效凭据可以登录"
- Score: 95 — same intent, cross-language

**Example C**
- Candidate: "验证管理员账号可以正常登录后台"
- Existing: "验证管理员使用正确密码登录管理系统"
- Score: 88 — same scenario (admin login), minor scope difference

### Medium similarity — CONFIRM (score 40–85)

**Example A**
- Candidate: "验证用户登录后跳转到首页"
- Existing: "验证登录成功后的页面跳转行为"
- Score: 68 — related but candidate is more specific about destination

**Example B**
- Candidate: "验证用户名超过50个字符时无法提交"
- Existing: "验证用户名字段的长度限制"
- Score: 72 — same field, but candidate specifies a concrete boundary value

**Example C**
- Candidate: "验证用户在登录页面点击忘记密码链接"
- Existing: "验证忘记密码功能入口可以正常访问"
- Score: 75 — same feature, slightly different focus (click action vs. accessibility)

### Low similarity — ADD (score < 40)

**Example A**
- Candidate: "验证用户连续输错密码5次后账号被锁定"
- Existing: "验证用户使用正确密码可以登录"
- Score: 15 — different scenario (lockout vs. success)

**Example B**
- Candidate: "验证未登录用户访问受保护页面时被重定向到登录页"
- Existing: "验证用户名密码登录"
- Score: 10 — different scenario (redirect guard vs. login form)

**Example C**
- Candidate: "验证第三方OAuth登录（Google）"
- Existing: "验证用户名密码登录"
- Score: 20 — different authentication method

## Cross-Language Handling

When comparing Chinese and English test cases, evaluate semantic meaning, not literal text.
Example: "verify user can log in with valid credentials" and "验证用户使用有效凭据可以登录" should score 95+.

# Tree Navigation Reference

## Core Principle

`_index.md` files are navigation-only. They contain directory structure, not test case content.
Never load test case content until the target module is confirmed.

## On-Demand Loading Algorithm

### Step 1: Always start at root
Read `{test_cases_root}/_index.md` to get the list of top-level domains.

### Step 2: LLM domain inference
Given the PRD content and the domain list from root `_index.md`, infer which domain(s) the PRD belongs to.
- If one domain clearly matches → proceed to Step 3 for that domain
- If multiple domains match → proceed to Step 3 for each candidate
- If no domain matches → STOP, present domain list to user, ask them to select or create a new domain

### Step 3: Module-level navigation (depth 2)
Read `{test_cases_root}/{domain}/_index.md` to get the module list.
Infer which module the PRD belongs to.
- If one module clearly matches → this is the target module, proceed to content loading
- If uncertain → proceed to Step 4

### Step 4: Sub-module navigation (depth 3, maximum)
Read `{test_cases_root}/{domain}/{module}/_index.md` to get sub-module list.
Infer which sub-module matches.
- If match found → this is the target module
- If still uncertain → STOP, show the current tree structure to the user, ask them to specify the exact mount path

### Depth Reference

```
Depth 1: {root}/_index.md                          ← always read
Depth 2: {root}/{domain}/_index.md                 ← read if domain identified
Depth 3: {root}/{domain}/{module}/_index.md        ← read if module uncertain (MAX depth)
```

Never auto-navigate beyond depth 3. Always ask the user if depth 3 is insufficient.

## Content Loading (after target module confirmed)

Read all direct `.md` files in the target module directory (not recursive).
Sub-module directories have their own `_index.md` and are treated as separate modules.

## Path Does Not Exist

If the target path does not exist:
1. Show the user the full directory path that would be created
2. Wait for explicit confirmation
3. Create directories and `_index.md` files level by level after confirmation

## Malformed `_index.md`

If an `_index.md` is missing the "子模块" or "用例文件" headings:
1. Inform the user the file is malformed
2. Show the expected format (from tc-format.md)
3. Ask the user to fix it before retrying

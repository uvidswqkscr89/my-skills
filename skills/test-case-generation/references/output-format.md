# Test Case Output Format

Complete Markdown template structure for test case documentation.

## Document Structure

```markdown
# [Feature Name] - Test Cases

> **Generation Date**: YYYY-MM-DD
> **Source Page**: [Page URL]
> **PRD Reference**: [PRD file path] (if applicable)
> **Analysis Method**: UI Reverse Engineering + PRD Analysis (if applicable)

## 1. Feature Overview

### Pseudo User Stories

- As [role], I want [action], so that [goal]
- As [role], I want [action], so that [goal]
- As [role], I want [action], so that [goal]

### Core Acceptance Criteria

- AC-1: [Acceptance criterion description]
- AC-2: [Acceptance criterion description]
- AC-3: [Acceptance criterion description]

## 2. Test Cases

### TC-001: [Test Case Title] [happy_path] [P0]

**Preconditions**:
- [Condition that must be met before test starts]
- [Another precondition if needed]

**Test Steps**:
1. Open "[Page Name]" page
2. Enter "[test value]" in "[Field Name]" field
3. Select "[option]" from "[Dropdown Name]" dropdown
4. Click "[Button Text]" button
5. Wait for page to load
6. Verify page displays "[Expected Text]" message
7. Verify "[Field Name]" value is "[Expected Value]"
8. Verify list contains N items

**Expected Result**:
- [Final state or outcome that should be achieved]
- [Another expected outcome if applicable]

---

### TC-002: [Test Case Title] [validation] [P1]

**Preconditions**:
- [Precondition description]

**Test Steps**:
1. [Step description]
2. [Step description]
3. [Step description]

**Expected Result**:
- [Expected outcome description]

---

### TC-003: [Test Case Title] [edge_case] [P1]

**Preconditions**:
- [Precondition description]

**Test Steps**:
1. [Step description]
2. [Step description]

**Expected Result**:
- [Expected outcome description]

---

### TC-004: [Test Case Title] [negative] [P1]

**Preconditions**:
- [Precondition description]

**Test Steps**:
1. [Step description]
2. [Step description]

**Expected Result**:
- [Expected outcome description]

---

(Additional test cases following same format...)

## 3. Items Requiring Confirmation

- [ ] [Needs Confirmation] [Description of unclear requirement or assumption]
- [ ] [PRD Discrepancy] [Description of difference between PRD and UI]
- [ ] [Needs Confirmation] [Another item requiring clarification]

## 4. Coverage Summary

| Type | Count | Description |
|:-----|:------|:------------|
| happy_path | N | Core positive flows |
| validation | N | Input validation |
| edge_case | N | Boundary conditions |
| negative | N | Error paths |
| **Total** | **N** | |

### Priority Distribution

| Priority | Count | Description |
|:---------|:------|:------------|
| P0 | N | Must cover - critical flows |
| P1 | N | Should cover - important scenarios |
| P2 | N | Can defer - low priority |
| **Total** | **N** | |
```

## Field Descriptions

### Header Section

- **Generation Date**: Date when test cases were generated (YYYY-MM-DD format)
- **Source Page**: Full URL of the analyzed page
- **PRD Reference**: Path to PRD file if one was used in analysis
- **Analysis Method**: Methodology used (always "UI Reverse Engineering" + "PRD Analysis" if applicable)

### Feature Overview Section

**Pseudo User Stories**:
- Format: "As [role], I want [action], so that [goal]"
- One story per major user workflow identified
- Derived from UI element analysis
- Should cover all primary use cases

**Core Acceptance Criteria**:
- Format: "AC-N: [Description]"
- High-level acceptance criteria for the feature
- Derived from UI controls and PRD (if available)
- Should be testable and specific

### Test Cases Section

Each test case must include:

**Test Case Header**:
- Format: `### TC-XXX: [Title] [type] [priority]`
- **TC-XXX**: Sequential test case ID (TC-001, TC-002, etc.)
- **Title**: Clear, descriptive title (verb + object, e.g., "Create new user account")
- **Type**: One of: `happy_path`, `validation`, `edge_case`, `negative`, `security`
- **Priority**: One of: `P0`, `P1`, `P2`

**Preconditions**:
- Bullet list of conditions that must be true before test starts
- Examples: "User is logged in", "Database contains test data", "Page is in edit mode"
- Leave empty if no preconditions needed

**Test Steps**:
- Numbered list of actions and verifications
- Each step is one complete sentence
- Use natural language with visible UI text
- Follow step patterns from `step-patterns.md`
- Typical range: 3-15 steps

**Expected Result**:
- Bullet list of final outcomes
- Describes the end state after all steps complete
- Should be specific and verifiable
- Examples: "User account is created", "Error message is displayed", "Data is saved to database"

### Items Requiring Confirmation Section

- Checkbox list of items needing clarification
- Two types of markers:
  - `[Needs Confirmation]`: Uncertain requirements or assumptions
  - `[PRD Discrepancy]`: Differences between PRD and actual UI
- Each item should be specific and actionable
- Leave empty if no items need confirmation

### Coverage Summary Section

**Type Distribution Table**:
- Counts test cases by type
- Shows balance of test coverage
- Helps identify gaps (e.g., no negative tests)

**Priority Distribution Table**:
- Counts test cases by priority
- Shows testing effort allocation
- Helps with test execution planning

## Formatting Guidelines

### Markdown Syntax

- Use `#` for main sections (1-4)
- Use `###` for test case headers
- Use `**bold**` for field labels (Preconditions, Test Steps, Expected Result)
- Use `-` for bullet lists
- Use `1.` for numbered lists (test steps)
- Use `---` horizontal rules between test cases
- Use `>` for blockquotes (header metadata)
- Use `|` for tables (coverage summary)

### Naming Conventions

**Test Case IDs**:
- Format: `TC-XXX` where XXX is zero-padded number (TC-001, TC-002, ..., TC-099, TC-100)
- Sequential numbering starting from 001
- No gaps in numbering

**Test Case Titles**:
- Start with action verb (Create, Verify, Update, Delete, Submit, etc.)
- Include object (user, order, report, etc.)
- Be specific but concise (max 10 words)
- Examples:
  - Good: "Create new user with valid data"
  - Good: "Verify email format validation"
  - Bad: "Test the form" (too vague)
  - Bad: "Verify that the system correctly validates email addresses according to RFC 5322" (too long)

**Field Names**:
- Use exact text from UI (e.g., "Email Address" not "email" or "Email")
- Include field type if ambiguous (e.g., "Start Date" field, "Status" dropdown)
- Use quotes around field names in steps

**Button Names**:
- Use exact button text (e.g., "Submit", "Save Changes", "Create Account")
- Include "button" after the name (e.g., "Submit button")
- Use quotes around button text in steps

### Language Consistency

- Use same language throughout document (all English or all Chinese)
- Match user's input language
- Use consistent terminology (don't alternate between "user" and "account holder")
- Use consistent verb tense (present tense for steps: "Click", "Enter", "Verify")

### Step Writing Style

**Action Steps**:
- Start with action verb: Open, Click, Enter, Select, Upload, etc.
- Include target element with visible text
- Include value if entering data
- Examples:
  - "Open 'User Management' page"
  - "Click 'Add User' button"
  - "Enter 'john@example.com' in 'Email' field"
  - "Select 'Active' from 'Status' dropdown"

**Wait Steps**:
- Use when timing is important
- Be specific about what to wait for
- Examples:
  - "Wait for page to load"
  - "Wait for 'Success' message to appear"
  - "Wait for list to refresh"

**Verification Steps**:
- Start with "Verify"
- State what should be true
- Be specific about expected values
- Examples:
  - "Verify page displays 'User created successfully' message"
  - "Verify 'Email' field value is 'john@example.com'"
  - "Verify user list contains 5 items"
  - "Verify navigation to 'User Details' page"

## Example Test Case

Here's a complete example following all guidelines:

```markdown
### TC-001: Create new user with valid data [happy_path] [P0]

**Preconditions**:
- User is logged in as administrator
- User Management page is accessible

**Test Steps**:
1. Open "User Management" page
2. Click "Add User" button
3. Wait for "New User" modal to appear
4. Enter "John Doe" in "Full Name" field
5. Enter "john.doe@example.com" in "Email" field
6. Select "Active" from "Status" dropdown
7. Select "Editor" from "Role" dropdown
8. Click "Save" button
9. Wait for modal to close
10. Verify page displays "User created successfully" message
11. Verify user list contains new user "John Doe"
12. Verify new user's email is "john.doe@example.com"

**Expected Result**:
- New user account is created in the system
- User appears in the user list with correct details
- Success confirmation message is displayed
```

## Common Mistakes to Avoid

### ❌ Wrong

```markdown
### TC-001: Test login

**Test Steps**:
1. Go to the page
2. Type username
3. Type password
4. Click submit
5. Check if logged in
```

**Problems**:
- Vague title (what about login?)
- Missing type and priority tags
- No preconditions
- Steps don't use visible UI text
- Steps don't specify values
- No expected result section
- Verification step is vague

### ✅ Correct

```markdown
### TC-001: Login with valid credentials [happy_path] [P0]

**Preconditions**:
- User account exists with username "testuser" and password "Test123!"
- User is not currently logged in

**Test Steps**:
1. Open "Login" page
2. Enter "testuser" in "Username" field
3. Enter "Test123!" in "Password" field
4. Click "Login" button
5. Wait for page to load
6. Verify navigation to "Dashboard" page
7. Verify page displays "Welcome, testuser" message

**Expected Result**:
- User is successfully authenticated
- User is redirected to Dashboard page
- Welcome message displays correct username
```

**Why it's correct**:
- Specific title with action and scenario
- Includes type and priority tags
- Clear preconditions
- Steps use exact UI text
- Steps specify test values
- Verification steps are specific
- Expected result summarizes outcomes

## Template Usage

When generating test cases:

1. **Copy the structure** from the template above
2. **Fill in all sections** - don't skip any
3. **Follow formatting rules** exactly
4. **Use consistent language** throughout
5. **Be specific** in all descriptions
6. **Verify completeness** before finalizing

The template ensures:
- ✅ Consistent structure across all test case documents
- ✅ Complete information for test execution
- ✅ Easy parsing for CSV conversion
- ✅ Professional documentation quality
- ✅ Clear communication with stakeholders

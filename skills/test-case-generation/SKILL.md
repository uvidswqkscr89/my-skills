---
name: test-case-generation
description: This skill should be used when the user asks to "generate test cases", "create test cases from UI", "analyze page for testing", "write test cases", or mentions test case generation from web interfaces. Provides UI reverse engineering methodology for automated test case creation.
---

# Test Case Generation Skill

## Purpose

Generate comprehensive, natural language test cases from web interfaces using UI reverse engineering methodology. This skill transforms web page analysis into structured test cases with executable steps, combining browser-based UI exploration with optional PRD (Product Requirements Document) analysis.

## When to Use This Skill

Use this skill when:
- Generating test cases from web applications or pages
- Analyzing UI elements to infer test scenarios
- Creating natural language test steps without technical selectors
- Combining PRD requirements with actual UI implementation
- Producing test cases in both Markdown and CSV formats

## Core Methodology: 5-Step Process

Execute these steps in strict sequence, completing each before proceeding to the next.

### Step 1: UI Exploration - Infer User Stories

**Objective**: Analyze the web page through browser automation to understand user intent.

**Process**:
1. Use Chrome DevTools MCP to open the target page URL
2. Complete login if credentials provided
3. Systematically scan page elements (top-to-bottom, left-to-right):
   - Page titles (H1/H2, browser tab title)
   - Action buttons (Create, Save, Submit, Delete, Export)
   - Form fields (inputs, dropdowns, checkboxes, date pickers)
   - Data tables/lists (column headers, pagination, search, filters)
   - Navigation elements (tabs, status filters, step indicators)
   - Help text and placeholders
4. Trigger interactive elements (modals, drawers, expandable panels)
5. If PRD provided, read and compare with observed UI elements

**Output Format**:
```
Page Information:
- Title: [Page title]
- URL: [Page URL]
- Purpose: [Inferred purpose]

Element Inventory:
- Buttons: [List button texts]
- Form Fields: [{label: X, type: input/dropdown/...}, ...]
- Table Columns: [Column names]
- Other Interactive Elements: [...]

Pseudo User Stories:
- As [role], I want [action], so that [goal]
- As [role], I want [action], so that [goal]

PRD Comparison (if applicable):
- Missing in UI: [Features in PRD but not on page]
- Extra in UI: [Features on page but not in PRD]
- Inconsistencies: [Differences between PRD and UI]
```

### Step 2: Infer Acceptance Criteria from Controls

**Objective**: Derive validation rules from UI elements.

**Inference Rules**:

| Control Type | Default Acceptance Criteria |
|:-------------|:---------------------------|
| **Text Input** | 1. Required? (check for * or required marker)<br>2. Format constraints? (email, phone, number range)<br>3. Length limits? (min/max characters)<br>4. Special character handling? |
| **Dropdown/Select** | 1. Default option?<br>2. Available options?<br>3. Search/multi-select support? |
| **Button** | 1. Pre-conditions? (form validation?)<br>2. Expected result? (navigation? message? data change?)<br>3. Confirmation dialog? |
| **List/Table** | 1. Empty state behavior?<br>2. Pagination logic?<br>3. Search/filter/sort functionality? |
| **Status/Label** | 1. Possible status values?<br>2. Actions available per status?<br>3. Status transition rules? |
| **File Upload** | 1. Supported file types?<br>2. Size limits?<br>3. Success/failure feedback? |
| **Checkbox/Toggle** | 1. Default state?<br>2. Impact of toggling? |

**Output Format**:
```
Feature Acceptance Criteria:

Feature 1: [Feature description]
  - AC-1: [Acceptance condition]
  - AC-2: [Acceptance condition]

Feature 2: [Feature description]
  - AC-1: [Acceptance condition]
```

### Step 3: Generate Test Cases and Steps

**Objective**: Transform user stories and acceptance criteria into structured test cases.

**Test Case Classification**:

| Type | Description | Priority |
|:-----|:------------|:---------|
| `happy_path` | Core positive flows, most common user paths | High (P0) |
| `validation` | Input validation, format checks, required field checks | Medium (P1) |
| `edge_case` | Boundary conditions, extreme scenarios | Medium (P1-P2) |
| `negative` | Error paths, invalid inputs | Medium (P1) |
| `security` | Permissions, authorization | Context-dependent |

**Test Step Guidelines**:

1. **Pure natural language**: Each step is a complete operation or verification instruction
2. **Use visible text**: Reference elements by their visible labels, not technical identifiers
3. **Atomic steps**: One action per step
4. **Step count**: 3-15 steps per test case (split if longer)

**Step Sentence Patterns**:

- **Actions**: "Open '[page name]' page" / "Enter '[value]' in '[field name]'" / "Click '[button text]' button" / "Select '[option]' from '[dropdown name]'"
- **Waits**: "Wait for page to load" / "Wait for list to refresh"
- **Verifications**: "Verify page displays '[text]'" / "Verify '[field]' value is '[expected]'" / "Verify list contains N items" / "Verify navigation to '[page]'"

**Prohibited in Steps**:
- ❌ CSS selectors, XPath, element IDs
- ❌ Hardcoded wait times ("wait 5 seconds")
- ❌ Code snippets
- ❌ BDD keywords (Given/When/Then)
- ❌ Position-based references ("click 3rd button")

### Step 4: Lightweight Review - Identify Gaps

**Objective**: Self-check for completeness and clarity.

**Review Checklist**:

1. **Coverage Check**:
   - Each user story has ≥1 happy_path test case?
   - Each key input field has ≥1 validation test case?
   - Empty data/list boundary scenarios covered?

2. **Executability Check**:
   - Steps use actual visible page text?
   - Step sequence matches real workflow?
   - Verification expectations are specific?

3. **Ambiguity Identification**:
   - Mark uncertain acceptance criteria as `[Needs Confirmation]`
   - Mark PRD-UI inconsistencies as `[PRD Discrepancy]`

### Step 5: Prioritize and Output

**Objective**: Rank test cases and generate final output.

**Priority Rules**:
- **P0 (Must Cover)**: happy_path scenarios, core business flows
- **P1 (Should Cover)**: Key field validation, common negative scenarios
- **P2 (Can Defer)**: Boundary conditions, low-frequency operations, UX tests

**Output Format**: See `references/output-format.md` for complete Markdown template structure.

## Language Adaptation

Detect user's language from their input and generate all output (test cases, steps, documentation) in that language. Support both Chinese and English seamlessly.

## Browser Automation

Use Chrome DevTools MCP for all browser operations:
- Automatic page navigation and interaction
- Element inspection and text extraction
- Screenshot capture for documentation
- Retry logic: Attempt once, retry once on failure, then report error

## CSV Export

After generating Markdown output, automatically convert to CSV format using the bundled conversion script. CSV includes columns: ID, Title, Type, Priority, Preconditions, Steps, Expected Result.

## Execution Reminders

1. **Observe first**: Always open and analyze the page before writing test cases
2. **Use real text**: Reference actual button names and field labels from the page
3. **Natural language only**: All steps in plain language, no technical selectors
4. **Incremental approach**: Prioritize P0 and P1 cases first, mark P2 for later
5. **Mark uncertainties**: Use `[Needs Confirmation]` for any unclear requirements
6. **Reusable patterns**: Use consistent sentence structures for better AI execution
7. **Atomic test cases**: One scenario per test case, one action per step

## Additional Resources

### Reference Files

For detailed information, consult:
- **`references/control-inference-rules.md`** - Complete control type inference table with examples
- **`references/output-format.md`** - Full Markdown output template structure
- **`references/step-patterns.md`** - Comprehensive test step sentence patterns and examples

### Example Files

Working examples in `examples/`:
- **`sample-test-cases.md`** - Complete test case document example
- **`sample-test-cases.csv`** - Corresponding CSV output

### Scripts

Utility scripts in `scripts/`:
- **`convert_tc_md_to_csv.py`** - Markdown to CSV conversion (Python 3.12+)

## Quality Standards

Generated test cases must meet these criteria:
- ✅ Natural language steps without technical identifiers
- ✅ Clear, specific verification expectations
- ✅ Logical step sequence matching real user workflow
- ✅ Appropriate test case classification and prioritization
- ✅ Complete coverage of core functionality (P0/P1)
- ✅ Identified gaps and uncertainties marked clearly
- ✅ Both Markdown and CSV outputs generated successfully

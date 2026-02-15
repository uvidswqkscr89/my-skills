---
name: gen-tc
description: Generate natural language test cases from web UI using reverse engineering methodology
argument-hint: (interactive - will prompt for inputs)
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Bash
  - mcp__chrome-devtools__*
---

# Generate Test Cases Command

Generate comprehensive test cases from web interfaces using UI reverse engineering methodology.

## Overview

This command orchestrates the complete test case generation workflow:
1. Gather inputs interactively (URL, PRD, credentials, output path)
2. Use Chrome DevTools MCP to analyze the web page
3. Apply the 5-step test case generation methodology
4. Generate Markdown test case document
5. Automatically convert to CSV format

## Execution Flow

### Step 1: Gather Inputs

Use AskUserQuestion to collect required information:

**Required inputs**:
- **Page URL**: The web page to analyze for test case generation
- **Output filename**: Name for the test case files (without extension)

**Optional inputs**:
- **PRD file path**: Path to Product Requirements Document (Markdown format only)
- **Login required**: Whether the page requires authentication
- **Login credentials**: If login required, collect username and password

**Interactive prompts**:
```
Question 1: "What is the URL of the page you want to generate test cases for?"
Question 2: "Do you have a PRD (Product Requirements Document) file to reference?"
  - If yes: "What is the path to the PRD file?"
Question 3: "Does this page require login?"
  - If yes: "What are the login credentials?" (username and password)
Question 4: "What should the output filename be? (without extension)"
  - Default suggestion: Extract from URL or use "test_cases"
```

### Step 2: Browser Automation Setup

Use Chrome DevTools MCP tools for browser interaction:

**Tools to use**:
- `mcp__chrome-devtools__browser_navigate`: Navigate to the page URL
- `mcp__chrome-devtools__browser_snapshot`: Capture page structure
- `mcp__chrome-devtools__browser_click`: Interact with elements
- `mcp__chrome-devtools__browser_type`: Fill in forms (for login)
- `mcp__chrome-devtools__browser_take_screenshot`: Capture visuals if needed

**Login handling** (if required):
1. Navigate to login page
2. Fill in credentials using browser_type
3. Click login button using browser_click
4. Wait for navigation to complete
5. Verify successful login

**Retry logic**:
- Attempt browser operation once
- If fails, retry one time
- If still fails, report error to user and ask how to proceed

### Step 3: Apply Test Case Generation Methodology

The test-case-generation skill will be automatically activated. Follow its 5-step process:

1. **UI Exploration**: Analyze page elements systematically
2. **Acceptance Criteria Inference**: Derive validation rules from controls
3. **Test Case Generation**: Create structured test cases with natural language steps
4. **Review**: Identify gaps and ambiguities
5. **Prioritization**: Rank test cases by importance

**Language detection**:
- Detect user's language from their inputs
- Generate all output in the detected language (Chinese or English)

**PRD integration** (if provided):
- Read the PRD file using Read tool
- Compare PRD requirements with observed UI elements
- Note discrepancies in the output

### Step 4: Generate Markdown Output

Create test case document following the template from `references/output-format.md`:

**Output structure**:
```markdown
# [Feature Name] - Test Cases

> Generation Date: [Current date]
> Source Page: [URL]
> PRD Reference: [Path if provided]
> Analysis Method: UI Reverse Engineering [+ PRD Analysis]

## 1. Feature Overview
[Pseudo user stories and acceptance criteria]

## 2. Test Cases
[All generated test cases with TC-001, TC-002, etc.]

## 3. Items Requiring Confirmation
[Any uncertainties or PRD discrepancies]

## 4. Coverage Summary
[Statistics table]
```

**File location**:
- Save to current working directory
- Filename: `{user_provided_name}_test_cases.md`

Use Write tool to create the file.

### Step 5: Convert to CSV

Automatically convert the Markdown file to CSV format:

**Conversion process**:
1. Verify Python 3.6+ is available:
   ```bash
   python3 --version
   ```
2. If Python not found, inform user and skip CSV generation
3. If Python available, run conversion script:
   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/scripts/convert_tc_md_to_csv.py "{markdown_file}" "{csv_file}"
   ```

**CSV output**:
- Filename: `{user_provided_name}_test_cases.csv`
- Location: Same directory as Markdown file
- Columns: ID, Title, Type, Priority, Preconditions, Steps, Expected Result

### Step 6: Report Results

Provide summary to user:

```
✓ Test case generation complete!

Generated files:
- Markdown: {path_to_md_file}
- CSV: {path_to_csv_file}

Summary:
- Total test cases: {count}
- P0 (Critical): {count}
- P1 (Important): {count}
- P2 (Optional): {count}

Test case types:
- Happy Path: {count}
- Validation: {count}
- Edge Case: {count}
- Negative: {count}

Items requiring confirmation: {count}
```

## Error Handling

**Browser automation failures**:
- Retry once automatically
- If still fails, report error and ask user:
  - "Browser automation failed. Would you like to: (1) Retry, (2) Continue without browser (manual analysis), (3) Cancel"

**PRD file not found**:
- Inform user and continue without PRD analysis

**Python not available**:
- Inform user that CSV conversion requires Python 3.6+
- Provide Markdown output only
- Suggest manual conversion or Python installation

**Page requires authentication but no credentials**:
- Ask user if they want to provide credentials or continue with public page analysis

## Best Practices

1. **Always use the test-case-generation skill**: It contains the methodology
2. **Be systematic**: Follow the 5-step process in order
3. **Use real UI text**: Reference actual button names and field labels
4. **Natural language only**: No technical selectors in test steps
5. **Mark uncertainties**: Use [Needs Confirmation] for unclear requirements
6. **Verify outputs**: Check that both MD and CSV files are created successfully

## Tips for Claude

- The test-case-generation skill will guide the methodology
- Use Chrome DevTools MCP for all browser operations
- Detect user language and generate output in that language
- Be thorough in UI exploration - scan all elements systematically
- Generate 10-20 test cases typically (adjust based on page complexity)
- Prioritize P0 and P1 test cases
- Always attempt CSV conversion after Markdown generation

## Example Usage

User runs: `/gen-tc`

Command flow:
1. Ask for page URL → User provides "https://example.com/users"
2. Ask about PRD → User says "No"
3. Ask about login → User says "Yes" and provides credentials
4. Ask for filename → User provides "user_management"
5. Navigate to page and login using Chrome DevTools MCP
6. Analyze page systematically (buttons, forms, tables, etc.)
7. Generate test cases following methodology
8. Write "user_management_test_cases.md"
9. Convert to "user_management_test_cases.csv"
10. Report results with summary statistics

The entire process should be smooth and automated after initial input gathering.

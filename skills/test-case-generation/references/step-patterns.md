# Test Step Sentence Patterns

Comprehensive guide to writing natural language test steps with consistent patterns.

## Core Principles

1. **One action per step**: Each step performs a single, atomic operation
2. **Use visible text**: Reference UI elements by their displayed text, not technical identifiers
3. **Be specific**: Include exact values, field names, and button texts
4. **Present tense**: Use present tense verbs (Click, Enter, Verify)
5. **Complete sentences**: Each step is a full sentence with proper punctuation

## Action Step Patterns

### Navigation Actions

**Pattern**: `Open "[Page Name]" page`

**Examples**:
- Open "User Management" page
- Open "Dashboard" page
- Open "Settings" page
- Open "Order Details" page

**Variations**:
- Navigate to "[Page Name]" page
- Go to "[Page Name]" page

**When to use**: Starting a test case or moving between pages

---

### Text Input Actions

**Pattern**: `Enter "[value]" in "[Field Name]" field`

**Examples**:
- Enter "john@example.com" in "Email" field
- Enter "John Doe" in "Full Name" field
- Enter "12345" in "Postal Code" field
- Enter "Test description" in "Description" field

**Variations**:
- Type "[value]" in "[Field Name]" field
- Input "[value]" in "[Field Name]" field
- Fill "[Field Name]" field with "[value]"

**Special cases**:
- Enter "password123" in "Password" field (for password fields)
- Enter "1000" in "Amount" field (for number fields)
- Enter "2024-01-15" in "Start Date" field (for date fields)

**When to use**: Filling in text inputs, textareas, number inputs, date inputs

---

### Button Click Actions

**Pattern**: `Click "[Button Text]" button`

**Examples**:
- Click "Submit" button
- Click "Save Changes" button
- Click "Add User" button
- Click "Delete" button
- Click "Cancel" button

**Variations**:
- Press "[Button Text]" button
- Select "[Button Text]" button

**Special cases**:
- Click "Save" button in modal (when multiple Save buttons exist)
- Click "Submit" button in "New User" form (for specificity)

**When to use**: Clicking any button element

---

### Dropdown/Select Actions

**Pattern**: `Select "[Option]" from "[Dropdown Name]" dropdown`

**Examples**:
- Select "Active" from "Status" dropdown
- Select "Administrator" from "Role" dropdown
- Select "United States" from "Country" dropdown
- Select "January" from "Month" dropdown

**Variations**:
- Choose "[Option]" from "[Dropdown Name]" dropdown
- Pick "[Option]" from "[Dropdown Name]" dropdown

**Special cases**:
- Select "Option 1" and "Option 2" from "Categories" dropdown (multi-select)
- Clear selection in "Status" dropdown (deselect)

**When to use**: Selecting from dropdown menus, select elements, comboboxes

---

### Checkbox Actions

**Pattern**: `Check "[Checkbox Label]" checkbox`

**Examples**:
- Check "I agree to terms" checkbox
- Check "Remember me" checkbox
- Check "Send notifications" checkbox

**Pattern**: `Uncheck "[Checkbox Label]" checkbox`

**Examples**:
- Uncheck "Remember me" checkbox
- Uncheck "Send notifications" checkbox

**Variations**:
- Select "[Checkbox Label]" checkbox
- Deselect "[Checkbox Label]" checkbox
- Toggle "[Checkbox Label]" checkbox

**When to use**: Checking or unchecking checkbox elements

---

### Radio Button Actions

**Pattern**: `Select "[Option]" radio button`

**Examples**:
- Select "Male" radio button
- Select "Credit Card" radio button
- Select "Yes" radio button

**Variations**:
- Choose "[Option]" radio button
- Pick "[Option]" radio button

**When to use**: Selecting radio button options

---

### Toggle/Switch Actions

**Pattern**: `Toggle "[Switch Label]" switch to [On/Off]`

**Examples**:
- Toggle "Email Notifications" switch to On
- Toggle "Dark Mode" switch to Off
- Toggle "Auto-save" switch to On

**Variations**:
- Turn "[Switch Label]" switch On
- Turn "[Switch Label]" switch Off
- Enable "[Switch Label]"
- Disable "[Switch Label]"

**When to use**: Toggling switch/toggle elements

---

### File Upload Actions

**Pattern**: `Upload "[filename]" to "[Upload Field]" field`

**Examples**:
- Upload "document.pdf" to "Attachment" field
- Upload "profile.jpg" to "Profile Picture" field
- Upload "data.csv" to "Import File" field

**Variations**:
- Select file "[filename]" for "[Upload Field]" field
- Choose "[filename]" for upload

**When to use**: Uploading files through file input elements

---

### Link Click Actions

**Pattern**: `Click "[Link Text]" link`

**Examples**:
- Click "Forgot Password?" link
- Click "View Details" link
- Click "Edit" link
- Click "Download Report" link

**Variations**:
- Select "[Link Text]" link
- Follow "[Link Text]" link

**When to use**: Clicking hyperlinks or text links

---

### Tab Selection Actions

**Pattern**: `Click "[Tab Name]" tab`

**Examples**:
- Click "Profile" tab
- Click "Settings" tab
- Click "History" tab

**Variations**:
- Select "[Tab Name]" tab
- Switch to "[Tab Name]" tab

**When to use**: Switching between tabs in a tabbed interface

---

### Modal/Dialog Actions

**Pattern**: `Close "[Modal Name]" modal`

**Examples**:
- Close "New User" modal
- Close "Confirmation" dialog
- Close "Settings" modal

**Variations**:
- Dismiss "[Modal Name]" modal
- Cancel "[Modal Name]" dialog

**When to use**: Closing modal dialogs or popups

---

### Scroll Actions

**Pattern**: `Scroll to "[Element]"`

**Examples**:
- Scroll to "Footer" section
- Scroll to "Comments" section
- Scroll to bottom of page

**Variations**:
- Scroll down to "[Element]"
- Scroll up to "[Element]"

**When to use**: When element is not visible without scrolling

---

### Hover Actions

**Pattern**: `Hover over "[Element]"`

**Examples**:
- Hover over "Help" icon
- Hover over "User Menu" button
- Hover over "Tooltip" icon

**Variations**:
- Move mouse over "[Element]"

**When to use**: When hover triggers a tooltip, dropdown, or other UI change

---

### Drag and Drop Actions

**Pattern**: `Drag "[Item]" to "[Target]"`

**Examples**:
- Drag "Task 1" to "In Progress" column
- Drag "File" to "Upload Area"
- Drag "Item A" above "Item B"

**When to use**: Drag and drop interactions

---

### Search Actions

**Pattern**: `Search for "[search term]" in "[Search Field]"`

**Examples**:
- Search for "John Doe" in "User Search" field
- Search for "Order #12345" in "Order Search" field

**Variations**:
- Enter "[search term]" in search box
- Type "[search term]" in "[Search Field]" and press Enter

**When to use**: Performing searches

---

### Clear Actions

**Pattern**: `Clear "[Field Name]" field`

**Examples**:
- Clear "Email" field
- Clear "Search" field
- Clear all filters

**Variations**:
- Delete content from "[Field Name]" field
- Remove text from "[Field Name]" field

**When to use**: Clearing input fields or filters

## Wait Step Patterns

### Page Load Waits

**Pattern**: `Wait for page to load`

**Examples**:
- Wait for page to load
- Wait for "Dashboard" page to load
- Wait for page to fully load

**When to use**: After navigation or page refresh

---

### Element Appearance Waits

**Pattern**: `Wait for "[Element]" to appear`

**Examples**:
- Wait for "Success" message to appear
- Wait for "Loading" spinner to disappear
- Wait for "User List" to appear
- Wait for modal to open

**Variations**:
- Wait until "[Element]" is visible
- Wait for "[Element]" to be displayed

**When to use**: When waiting for dynamic content to load

---

### Data Load Waits

**Pattern**: `Wait for [data] to load`

**Examples**:
- Wait for list to refresh
- Wait for table data to load
- Wait for search results to appear

**When to use**: When waiting for data to populate

---

### Action Completion Waits

**Pattern**: `Wait for [action] to complete`

**Examples**:
- Wait for file upload to complete
- Wait for save operation to complete
- Wait for deletion to complete

**When to use**: When waiting for asynchronous operations

## Verification Step Patterns

### Text Display Verification

**Pattern**: `Verify page displays "[text]" message`

**Examples**:
- Verify page displays "User created successfully" message
- Verify page displays "Invalid email format" error
- Verify page displays "Welcome, John" greeting

**Variations**:
- Verify "[text]" message is displayed
- Verify "[text]" appears on page
- Confirm page shows "[text]"

**When to use**: Verifying success messages, error messages, notifications

---

### Field Value Verification

**Pattern**: `Verify "[Field Name]" value is "[expected value]"`

**Examples**:
- Verify "Email" field value is "john@example.com"
- Verify "Status" dropdown value is "Active"
- Verify "Total" field value is "$100.00"

**Variations**:
- Verify "[Field Name]" contains "[expected value]"
- Confirm "[Field Name]" shows "[expected value]"
- Check "[Field Name]" equals "[expected value]"

**When to use**: Verifying form field values, input values

---

### Element State Verification

**Pattern**: `Verify "[Element]" is [state]`

**Examples**:
- Verify "Submit" button is disabled
- Verify "Email" field is empty
- Verify "Success" message is visible
- Verify "Loading" spinner is not visible

**States**: enabled, disabled, visible, hidden, checked, unchecked, selected, empty

**Variations**:
- Confirm "[Element]" is [state]
- Check that "[Element]" is [state]

**When to use**: Verifying element states and properties

---

### List/Table Verification

**Pattern**: `Verify list contains [N] items`

**Examples**:
- Verify list contains 5 items
- Verify table contains 10 rows
- Verify "Users" list contains 3 items

**Pattern**: `Verify list contains "[item]"`

**Examples**:
- Verify list contains "John Doe"
- Verify table contains row with "Order #12345"
- Verify "Users" list contains "john@example.com"

**Variations**:
- Confirm list has [N] items
- Check table shows [N] rows
- Verify "[item]" appears in list

**When to use**: Verifying list or table contents

---

### Navigation Verification

**Pattern**: `Verify navigation to "[Page Name]" page`

**Examples**:
- Verify navigation to "Dashboard" page
- Verify navigation to "User Details" page
- Verify redirect to "Login" page

**Variations**:
- Verify page is "[Page Name]"
- Confirm current page is "[Page Name]"
- Check URL is "[Page Name]" page

**When to use**: Verifying page navigation and redirects

---

### Count Verification

**Pattern**: `Verify [element] count is [N]`

**Examples**:
- Verify error count is 0
- Verify selected items count is 3
- Verify notification count is 5

**Variations**:
- Confirm [element] count equals [N]
- Check number of [element] is [N]

**When to use**: Verifying counts of elements or items

---

### Existence Verification

**Pattern**: `Verify "[Element]" exists`

**Examples**:
- Verify "Edit" button exists
- Verify "User Profile" section exists
- Verify "Error Message" does not exist

**Variations**:
- Confirm "[Element]" is present
- Check "[Element]" appears
- Verify "[Element]" is not present (for negative verification)

**When to use**: Verifying presence or absence of elements

---

### Order Verification

**Pattern**: `Verify items are ordered by [criteria]`

**Examples**:
- Verify items are ordered by "Name" ascending
- Verify list is sorted by "Date" descending
- Verify table rows are ordered by "Priority"

**When to use**: Verifying sort order

---

### Style/Appearance Verification

**Pattern**: `Verify "[Element]" is [color/style]`

**Examples**:
- Verify "Status" badge is green
- Verify "Error" message is red
- Verify "Submit" button is highlighted

**When to use**: Verifying visual styling (use sparingly, focus on functional verification)

## Complex Step Patterns

### Conditional Actions

**Pattern**: `If "[condition]", then [action]`

**Examples**:
- If "Remember Me" checkbox is checked, then uncheck it
- If modal is open, then close it

**Note**: Try to avoid conditional steps by setting up proper preconditions instead

---

### Repeated Actions

**Pattern**: `Repeat [N] times: [action]`

**Examples**:
- Repeat 3 times: Click "Add Item" button
- For each row in table: Verify "Status" is "Active"

**Note**: Use sparingly; prefer specific steps for clarity

---

### Multi-Step Actions

**Pattern**: Break into atomic steps rather than combining

**❌ Wrong**:
- Enter user details and submit form

**✅ Correct**:
- Enter "John Doe" in "Name" field
- Enter "john@example.com" in "Email" field
- Click "Submit" button

## Language-Specific Patterns

### Chinese Patterns

**Navigation**:
- 打开"[页面名称]"页面
- 导航到"[页面名称]"页面

**Input**:
- 在"[字段名]"中输入"[值]"
- 在"[字段名]"字段中填写"[值]"

**Click**:
- 点击"[按钮文本]"按钮
- 单击"[链接文本]"链接

**Select**:
- 从"[下拉框名]"中选择"[选项]"
- 在"[下拉框名]"下拉框中选择"[选项]"

**Verify**:
- 验证页面显示"[文本]"消息
- 验证"[字段名]"的值为"[期望值]"
- 确认列表包含 N 条数据

**Wait**:
- 等待页面加载完成
- 等待"[元素]"出现

## Best Practices

### DO:
- ✅ Use exact UI text in quotes
- ✅ Be specific about values and elements
- ✅ Use consistent verb tense (present)
- ✅ Write complete sentences
- ✅ Keep steps atomic (one action each)
- ✅ Use consistent patterns throughout document

### DON'T:
- ❌ Use technical identifiers (IDs, classes, XPath)
- ❌ Combine multiple actions in one step
- ❌ Use vague descriptions ("click the button")
- ❌ Include hardcoded wait times ("wait 5 seconds")
- ❌ Use BDD keywords (Given/When/Then)
- ❌ Reference element positions ("click 3rd button")

## Pattern Selection Guide

| User Action | Pattern to Use |
|:------------|:---------------|
| Navigate to page | `Open "[Page]" page` |
| Type in field | `Enter "[value]" in "[Field]" field` |
| Click button | `Click "[Button]" button` |
| Select from dropdown | `Select "[Option]" from "[Dropdown]" dropdown` |
| Check checkbox | `Check "[Label]" checkbox` |
| Upload file | `Upload "[file]" to "[Field]" field` |
| Wait for load | `Wait for page to load` |
| Verify message | `Verify page displays "[text]" message` |
| Verify field value | `Verify "[Field]" value is "[value]"` |
| Verify element state | `Verify "[Element]" is [state]` |
| Verify list content | `Verify list contains [N] items` |
| Verify navigation | `Verify navigation to "[Page]" page` |

## Examples of Complete Test Cases

### Example 1: Login Test

```markdown
**Test Steps**:
1. Open "Login" page
2. Enter "testuser@example.com" in "Email" field
3. Enter "password123" in "Password" field
4. Check "Remember Me" checkbox
5. Click "Login" button
6. Wait for page to load
7. Verify navigation to "Dashboard" page
8. Verify page displays "Welcome, Test User" message
```

### Example 2: Form Validation Test

```markdown
**Test Steps**:
1. Open "User Registration" page
2. Click "Submit" button
3. Verify page displays "Email is required" error
4. Verify page displays "Password is required" error
5. Enter "invalid-email" in "Email" field
6. Click "Submit" button
7. Verify page displays "Invalid email format" error
8. Enter "test@example.com" in "Email" field
9. Enter "pass" in "Password" field
10. Click "Submit" button
11. Verify page displays "Password must be at least 8 characters" error
```

### Example 3: Data Table Test

```markdown
**Test Steps**:
1. Open "Users" page
2. Wait for table to load
3. Verify table contains 10 rows
4. Click "Name" column header
5. Wait for table to refresh
6. Verify items are ordered by "Name" ascending
7. Enter "John" in "Search" field
8. Wait for search results to appear
9. Verify table contains 2 rows
10. Verify list contains "John Doe"
11. Verify list contains "John Smith"
```

Use these patterns consistently to create clear, executable, natural language test steps.

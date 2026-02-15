# Control Type Inference Rules

Detailed rules for inferring acceptance criteria from UI control types.

## Text Input Fields

### Standard Text Input

**Observable Indicators**:
- Input field with text placeholder
- May have character counter
- May show format hints (e.g., "example@email.com")

**Inferred Acceptance Criteria**:
1. **Required Field Check**: Look for asterisk (*), "required" label, or red border
2. **Format Validation**:
   - Email: Check for @ symbol requirement
   - Phone: Check for number format (digits, dashes, parentheses)
   - URL: Check for http:// or https:// requirement
3. **Length Constraints**:
   - Minimum length (often shown as "at least X characters")
   - Maximum length (character counter or maxlength attribute)
4. **Special Characters**:
   - Allowed characters (alphanumeric, symbols)
   - Forbidden characters (SQL injection prevention)
5. **Real-time Validation**: Error messages appearing during typing

**Test Case Types to Generate**:
- Happy path: Valid input within constraints
- Validation: Empty (if required), too short, too long, invalid format
- Edge case: Boundary lengths, special characters
- Negative: SQL injection attempts, XSS attempts

### Number Input

**Observable Indicators**:
- Input field with number spinner controls
- Min/max value hints
- Step increment indicators

**Inferred Acceptance Criteria**:
1. **Range Validation**: Minimum and maximum allowed values
2. **Step Increment**: Allowed increment (e.g., integers only, or 0.01 steps)
3. **Decimal Places**: Precision requirements
4. **Negative Numbers**: Whether negative values are allowed
5. **Zero Handling**: Whether zero is valid

**Test Case Types to Generate**:
- Happy path: Valid number within range
- Validation: Below min, above max, non-numeric input
- Edge case: Exact min/max values, zero, negative (if allowed)
- Negative: Text input, special characters

### Password Input

**Observable Indicators**:
- Masked input field
- Password strength indicator
- Show/hide password toggle

**Inferred Acceptance Criteria**:
1. **Minimum Length**: Usually 8+ characters
2. **Complexity Requirements**:
   - Uppercase letters required?
   - Lowercase letters required?
   - Numbers required?
   - Special characters required?
3. **Forbidden Patterns**: Common passwords, sequential characters
4. **Confirmation Match**: If password confirmation field exists

**Test Case Types to Generate**:
- Happy path: Strong password meeting all requirements
- Validation: Too short, missing required character types, mismatch confirmation
- Edge case: Exactly minimum length, maximum length (if any)
- Negative: Common passwords, all same character

## Dropdown/Select Controls

### Single Select Dropdown

**Observable Indicators**:
- Dropdown arrow icon
- Placeholder text ("Select an option...")
- List of options when clicked

**Inferred Acceptance Criteria**:
1. **Default Selection**: What's selected initially (blank, first option, specific default)
2. **Available Options**: Complete list of selectable values
3. **Required Selection**: Whether selection is mandatory
4. **Option Ordering**: Alphabetical, categorical, or custom order
5. **Disabled Options**: Any options that are grayed out

**Test Case Types to Generate**:
- Happy path: Select valid option
- Validation: Leave unselected (if required), verify all options available
- Edge case: First option, last option, default option
- Negative: Attempt to submit without selection (if required)

### Multi-Select Dropdown

**Observable Indicators**:
- Checkboxes next to options
- "Select all" / "Clear all" buttons
- Selected items displayed as chips/tags

**Inferred Acceptance Criteria**:
1. **Selection Limits**: Minimum and maximum selections allowed
2. **Select All Behavior**: Whether "select all" is available
3. **Deselection**: How to remove selected items
4. **Display Format**: How selected items are shown
5. **Search Functionality**: Whether options can be filtered

**Test Case Types to Generate**:
- Happy path: Select multiple valid options
- Validation: Select below minimum, exceed maximum (if limits exist)
- Edge case: Select all, select none, select one
- Negative: Attempt invalid selection count

### Searchable Dropdown

**Observable Indicators**:
- Search input within dropdown
- Filtered results as user types
- "No results found" message

**Inferred Acceptance Criteria**:
1. **Search Behavior**: Partial match, exact match, case sensitivity
2. **Minimum Characters**: Minimum input before search activates
3. **Result Ordering**: How results are sorted
4. **No Results Handling**: Message and behavior when no matches
5. **Clear Search**: How to reset search

**Test Case Types to Generate**:
- Happy path: Search and select valid option
- Validation: Search with no results, partial matches
- Edge case: Single character search, very long search term
- Negative: Special characters in search, SQL injection attempts

## Button Controls

### Submit/Save Button

**Observable Indicators**:
- Primary button styling (often blue/green)
- Text like "Submit", "Save", "Create", "Update"
- May be disabled until form is valid

**Inferred Acceptance Criteria**:
1. **Enabled State**: When button becomes clickable (form validation passed)
2. **Click Action**: What happens (navigation, modal, success message)
3. **Loading State**: Button shows spinner or "Saving..." text
4. **Success Feedback**: Success message, toast notification, or redirect
5. **Error Handling**: Error messages if submission fails
6. **Duplicate Prevention**: Button disabled during submission

**Test Case Types to Generate**:
- Happy path: Valid form submission with success
- Validation: Click when form invalid (should be disabled)
- Edge case: Rapid double-click (duplicate prevention)
- Negative: Network error during submission, server error response

### Delete/Destructive Button

**Observable Indicators**:
- Red or warning color styling
- Text like "Delete", "Remove", "Cancel"
- Often secondary or outlined style

**Inferred Acceptance Criteria**:
1. **Confirmation Dialog**: Whether confirmation is required
2. **Confirmation Message**: Specific warning text
3. **Undo Capability**: Whether action can be reversed
4. **Success Feedback**: Confirmation of deletion
5. **Data Removal**: What gets deleted (item, related data)

**Test Case Types to Generate**:
- Happy path: Delete with confirmation
- Validation: Cancel deletion, verify data removed
- Edge case: Delete last item, delete with dependencies
- Negative: Delete without permission, delete non-existent item

### Action Button (Secondary)

**Observable Indicators**:
- Secondary styling (outlined, gray)
- Text like "Export", "Download", "Print", "Share"
- May trigger file download or modal

**Inferred Acceptance Criteria**:
1. **Action Trigger**: What happens when clicked
2. **Pre-conditions**: When button is enabled (data selected, etc.)
3. **Output Format**: File type, modal content, etc.
4. **Success Indication**: Download starts, modal opens, etc.
5. **Error Handling**: What happens if action fails

**Test Case Types to Generate**:
- Happy path: Successful action execution
- Validation: Click when pre-conditions not met
- Edge case: Large data export, empty data export
- Negative: Action failure, timeout

## List/Table Controls

### Data Table

**Observable Indicators**:
- Column headers
- Rows of data
- Pagination controls
- Sort indicators (arrows in headers)
- Search/filter inputs

**Inferred Acceptance Criteria**:
1. **Empty State**: Message and UI when no data
2. **Pagination**:
   - Items per page (10, 25, 50, 100)
   - Page navigation (previous, next, page numbers)
   - Total count display
3. **Sorting**:
   - Sortable columns (indicated by arrows)
   - Sort direction (ascending, descending)
   - Default sort order
4. **Filtering**:
   - Filter inputs per column
   - Filter operators (equals, contains, greater than)
   - Multiple filter combination (AND/OR)
5. **Search**:
   - Global search across all columns
   - Search behavior (partial match, case sensitivity)
6. **Row Actions**:
   - Edit, delete, view buttons per row
   - Bulk actions (select multiple rows)
7. **Column Visibility**: Show/hide columns

**Test Case Types to Generate**:
- Happy path: View data, paginate, sort, filter
- Validation: Empty table, single item, full page
- Edge case: Maximum items per page, sort with equal values
- Negative: Invalid filter values, search with no results

### Simple List

**Observable Indicators**:
- Vertical list of items
- May have icons or avatars
- May have item actions (edit, delete)

**Inferred Acceptance Criteria**:
1. **Empty State**: Message when list is empty
2. **Item Display**: What information is shown per item
3. **Item Actions**: Available actions per item
4. **Ordering**: How items are ordered (chronological, alphabetical)
5. **Loading State**: Skeleton or spinner while loading

**Test Case Types to Generate**:
- Happy path: View list with items
- Validation: Empty list, single item, many items
- Edge case: Very long item names, special characters in names
- Negative: Load failure, item action failure

## Status/Label Controls

### Status Badge

**Observable Indicators**:
- Colored badge or pill
- Text like "Active", "Pending", "Completed", "Failed"
- Different colors for different statuses

**Inferred Acceptance Criteria**:
1. **Status Values**: All possible status values
2. **Status Colors**: Color coding for each status
3. **Status Transitions**: Valid transitions between statuses
4. **Status-Dependent Actions**: What actions are available per status
5. **Status Change Triggers**: What causes status to change

**Test Case Types to Generate**:
- Happy path: Verify status display, valid status transitions
- Validation: Status-dependent action availability
- Edge case: Rapid status changes, concurrent status updates
- Negative: Invalid status transition attempts

### Tag/Label

**Observable Indicators**:
- Small colored chips
- Multiple tags per item
- May have remove (X) button

**Inferred Acceptance Criteria**:
1. **Tag Creation**: How tags are added
2. **Tag Removal**: How tags are removed
3. **Tag Limits**: Maximum number of tags
4. **Tag Validation**: Allowed characters, length limits
5. **Duplicate Handling**: Can same tag be added twice?

**Test Case Types to Generate**:
- Happy path: Add and remove tags
- Validation: Maximum tags, duplicate tags
- Edge case: Very long tag names, special characters
- Negative: Invalid tag characters, exceed maximum

## File Upload Controls

### File Input

**Observable Indicators**:
- "Choose file" or "Upload" button
- Drag-and-drop area
- File type restrictions shown
- File size limit shown
- Upload progress indicator

**Inferred Acceptance Criteria**:
1. **Allowed File Types**: Extensions or MIME types (PDF, JPG, PNG, etc.)
2. **File Size Limit**: Maximum file size (MB)
3. **Multiple Files**: Whether multiple files can be uploaded
4. **Upload Method**: Click to browse or drag-and-drop
5. **Progress Indication**: Progress bar or percentage
6. **Success Feedback**: File name displayed, success message
7. **Error Handling**: Error messages for invalid files
8. **File Preview**: Whether uploaded file can be previewed

**Test Case Types to Generate**:
- Happy path: Upload valid file within size limit
- Validation: Invalid file type, file too large, no file selected
- Edge case: Exactly maximum size, minimum size (if any), multiple files
- Negative: Malicious file types, corrupted files, network interruption

## Checkbox/Toggle Controls

### Checkbox

**Observable Indicators**:
- Square box with checkmark when selected
- Label text next to checkbox
- May be part of a group

**Inferred Acceptance Criteria**:
1. **Default State**: Checked or unchecked initially
2. **Required Selection**: Whether checkbox must be checked (e.g., terms acceptance)
3. **Dependent Fields**: Fields that appear/disappear based on checkbox state
4. **Group Behavior**: If part of checkbox group, selection rules
5. **Disabled State**: When checkbox is disabled

**Test Case Types to Generate**:
- Happy path: Check and uncheck
- Validation: Required checkbox validation, dependent field behavior
- Edge case: Rapid toggling, all checked, none checked (in group)
- Negative: Submit without required checkbox

### Toggle Switch

**Observable Indicators**:
- Sliding switch control
- On/Off or Yes/No labels
- May have color change (green for on, gray for off)

**Inferred Acceptance Criteria**:
1. **Default State**: On or off initially
2. **Toggle Effect**: What changes when toggled (feature enabled/disabled)
3. **Confirmation**: Whether confirmation is needed for toggle
4. **Immediate Effect**: Whether change takes effect immediately or requires save
5. **Disabled State**: When toggle is disabled

**Test Case Types to Generate**:
- Happy path: Toggle on and off
- Validation: Verify effect of toggle, confirmation if required
- Edge case: Rapid toggling, toggle with unsaved changes
- Negative: Toggle when disabled, toggle without permission

## Date/Time Controls

### Date Picker

**Observable Indicators**:
- Calendar icon
- Date input field
- Calendar popup when clicked
- Date format hint (MM/DD/YYYY)

**Inferred Acceptance Criteria**:
1. **Date Format**: Required format (MM/DD/YYYY, DD/MM/YYYY, etc.)
2. **Date Range**: Minimum and maximum allowed dates
3. **Disabled Dates**: Dates that cannot be selected (weekends, holidays)
4. **Default Date**: Pre-selected date (today, specific date, empty)
5. **Manual Entry**: Whether date can be typed or only selected from calendar
6. **Validation**: Real date validation (no Feb 30, etc.)

**Test Case Types to Generate**:
- Happy path: Select valid date from calendar
- Validation: Invalid date format, date outside range, disabled date
- Edge case: Today, minimum date, maximum date, leap year dates
- Negative: Invalid date (Feb 30), text input, future date (if not allowed)

### Time Picker

**Observable Indicators**:
- Clock icon
- Time input field
- Time format hint (HH:MM AM/PM)
- Dropdown or spinner for time selection

**Inferred Acceptance Criteria**:
1. **Time Format**: 12-hour or 24-hour format
2. **Time Intervals**: Allowed intervals (1 min, 5 min, 15 min, 30 min)
3. **Time Range**: Minimum and maximum allowed times
4. **Default Time**: Pre-selected time
5. **Manual Entry**: Whether time can be typed

**Test Case Types to Generate**:
- Happy path: Select valid time
- Validation: Invalid time format, time outside range
- Edge case: Midnight, noon, boundary times
- Negative: Invalid time (25:00), text input

## Modal/Dialog Controls

### Modal Dialog

**Observable Indicators**:
- Overlay that dims background
- Close button (X) in corner
- Action buttons (Save, Cancel)
- May have form fields inside

**Inferred Acceptance Criteria**:
1. **Trigger**: What opens the modal (button click, automatic)
2. **Close Methods**: X button, Cancel button, click outside, Escape key
3. **Form Validation**: If modal contains form, validation rules
4. **Save Behavior**: What happens when Save clicked
5. **Cancel Behavior**: Whether unsaved changes are lost
6. **Backdrop Click**: Whether clicking outside closes modal

**Test Case Types to Generate**:
- Happy path: Open modal, complete action, close modal
- Validation: Form validation within modal, required fields
- Edge case: Multiple modals, modal with long content
- Negative: Close without saving, invalid form submission

## Search Controls

### Search Input

**Observable Indicators**:
- Search icon (magnifying glass)
- Placeholder text ("Search...")
- Clear button (X) when text entered
- Search results appear below or in dropdown

**Inferred Acceptance Criteria**:
1. **Search Trigger**: When search executes (on Enter, on type, on button click)
2. **Minimum Characters**: Minimum input before search activates
3. **Search Scope**: What fields/data are searched
4. **Search Type**: Exact match, partial match, fuzzy match
5. **Case Sensitivity**: Whether search is case-sensitive
6. **Result Display**: How results are shown (list, table, dropdown)
7. **No Results**: Message when no matches found
8. **Clear Search**: How to reset search

**Test Case Types to Generate**:
- Happy path: Search with results
- Validation: Search with no results, partial matches, exact matches
- Edge case: Single character search, very long search term, special characters
- Negative: SQL injection attempts, XSS attempts, empty search

## Navigation Controls

### Tab Navigation

**Observable Indicators**:
- Horizontal or vertical tabs
- Active tab highlighted
- Content changes when tab clicked

**Inferred Acceptance Criteria**:
1. **Default Tab**: Which tab is active initially
2. **Tab Count**: Number of tabs
3. **Tab Labels**: Text on each tab
4. **Content Loading**: Whether content loads immediately or on tab click
5. **Disabled Tabs**: Any tabs that are disabled
6. **URL Update**: Whether URL changes with tab selection

**Test Case Types to Generate**:
- Happy path: Navigate between tabs
- Validation: Verify content changes per tab, default tab
- Edge case: Rapid tab switching, many tabs
- Negative: Access disabled tab, invalid tab URL

### Breadcrumb Navigation

**Observable Indicators**:
- Horizontal path with separators (> or /)
- Clickable links to parent pages
- Current page not clickable

**Inferred Acceptance Criteria**:
1. **Path Accuracy**: Breadcrumb reflects actual navigation path
2. **Clickable Links**: All parent pages are clickable
3. **Current Page**: Current page shown but not clickable
4. **Separator Style**: Consistent separator between items
5. **Truncation**: How long paths are handled

**Test Case Types to Generate**:
- Happy path: Navigate using breadcrumb links
- Validation: Verify path accuracy, current page not clickable
- Edge case: Very deep navigation path, long page names
- Negative: Invalid breadcrumb link

## Usage Guidelines

When analyzing a page:

1. **Identify all control types** present on the page
2. **For each control**, apply the relevant inference rules from this reference
3. **Document observed indicators** that led to each inference
4. **Generate acceptance criteria** based on the rules
5. **Create test cases** covering all inferred criteria
6. **Mark uncertainties** with `[Needs Confirmation]` when indicators are ambiguous

Remember: These are inference rules based on common patterns. Always verify inferences against actual page behavior when possible.

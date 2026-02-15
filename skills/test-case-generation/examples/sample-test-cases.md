# User Management - Test Cases

> **Generation Date**: 2024-01-15
> **Source Page**: https://example.com/admin/users
> **PRD Reference**: N/A
> **Analysis Method**: UI Reverse Engineering

## 1. Feature Overview

### Pseudo User Stories

- As an administrator, I want to create new user accounts, so that new team members can access the system
- As an administrator, I want to view a list of all users, so that I can manage user accounts effectively
- As an administrator, I want to edit user details, so that I can keep user information up-to-date
- As an administrator, I want to deactivate user accounts, so that former team members cannot access the system

### Core Acceptance Criteria

- AC-1: User list displays all users with their name, email, role, and status
- AC-2: New users can be created with required fields: name, email, role
- AC-3: Email addresses must be unique and follow valid email format
- AC-4: User roles can be selected from predefined options: Admin, Editor, Viewer
- AC-5: User status can be Active or Inactive
- AC-6: Changes to user details are saved and reflected immediately in the list

## 2. Test Cases

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
13. Verify new user's role is "Editor"

**Expected Result**:
- New user account is created in the system
- User appears in the user list with correct details
- Success confirmation message is displayed

---

### TC-002: Verify email format validation [validation] [P1]

**Preconditions**:
- User is logged in as administrator
- User Management page is accessible

**Test Steps**:
1. Open "User Management" page
2. Click "Add User" button
3. Wait for "New User" modal to appear
4. Enter "Test User" in "Full Name" field
5. Enter "invalid-email" in "Email" field
6. Select "Active" from "Status" dropdown
7. Select "Viewer" from "Role" dropdown
8. Click "Save" button
9. Verify page displays "Invalid email format" error message
10. Verify "Email" field is highlighted in red
11. Verify modal remains open
12. Verify user is not created in the list

**Expected Result**:
- Invalid email format is rejected
- Clear error message is displayed
- User is not created until valid email is provided

---

### TC-003: Verify required field validation [validation] [P1]

**Preconditions**:
- User is logged in as administrator
- User Management page is accessible

**Test Steps**:
1. Open "User Management" page
2. Click "Add User" button
3. Wait for "New User" modal to appear
4. Click "Save" button without entering any data
5. Verify page displays "Full Name is required" error message
6. Verify page displays "Email is required" error message
7. Verify "Full Name" field is highlighted in red
8. Verify "Email" field is highlighted in red
9. Verify "Save" button remains enabled
10. Verify modal remains open

**Expected Result**:
- All required fields are validated
- Clear error messages are displayed for each missing field
- User cannot be created without required information

---

### TC-004: Verify duplicate email prevention [validation] [P1]

**Preconditions**:
- User is logged in as administrator
- User "existing@example.com" already exists in the system

**Test Steps**:
1. Open "User Management" page
2. Click "Add User" button
3. Wait for "New User" modal to appear
4. Enter "Another User" in "Full Name" field
5. Enter "existing@example.com" in "Email" field
6. Select "Active" from "Status" dropdown
7. Select "Viewer" from "Role" dropdown
8. Click "Save" button
9. Verify page displays "Email already exists" error message
10. Verify "Email" field is highlighted in red
11. Verify modal remains open
12. Verify duplicate user is not created

**Expected Result**:
- Duplicate email addresses are rejected
- Clear error message indicates email is already in use
- Existing user data is not affected

---

### TC-005: Edit existing user details [happy_path] [P0]

**Preconditions**:
- User is logged in as administrator
- User "john.doe@example.com" exists in the system

**Test Steps**:
1. Open "User Management" page
2. Locate user "john.doe@example.com" in the list
3. Click "Edit" button for that user
4. Wait for "Edit User" modal to appear
5. Verify "Full Name" field contains "John Doe"
6. Verify "Email" field contains "john.doe@example.com"
7. Enter "John Smith" in "Full Name" field
8. Select "Admin" from "Role" dropdown
9. Click "Save" button
10. Wait for modal to close
11. Verify page displays "User updated successfully" message
12. Verify user list shows updated name "John Smith"
13. Verify user's role is now "Admin"

**Expected Result**:
- User details are successfully updated
- Changes are reflected immediately in the user list
- Success confirmation message is displayed

---

### TC-006: Deactivate user account [happy_path] [P0]

**Preconditions**:
- User is logged in as administrator
- Active user "john.doe@example.com" exists in the system

**Test Steps**:
1. Open "User Management" page
2. Locate user "john.doe@example.com" in the list
3. Click "Edit" button for that user
4. Wait for "Edit User" modal to appear
5. Select "Inactive" from "Status" dropdown
6. Click "Save" button
7. Wait for modal to close
8. Verify page displays "User updated successfully" message
9. Verify user's status badge shows "Inactive"
10. Verify user's status badge is gray (not green)

**Expected Result**:
- User status is changed to Inactive
- Status change is reflected in the user list
- User account is deactivated (cannot login)

---

### TC-007: Cancel user creation [edge_case] [P2]

**Preconditions**:
- User is logged in as administrator
- User Management page is accessible

**Test Steps**:
1. Open "User Management" page
2. Click "Add User" button
3. Wait for "New User" modal to appear
4. Enter "Test User" in "Full Name" field
5. Enter "test@example.com" in "Email" field
6. Click "Cancel" button
7. Verify modal closes
8. Verify user list does not contain "test@example.com"
9. Verify no success or error messages are displayed

**Expected Result**:
- Modal closes without saving
- No user is created
- User list remains unchanged

---

### TC-008: Search for users [happy_path] [P1]

**Preconditions**:
- User is logged in as administrator
- Multiple users exist in the system

**Test Steps**:
1. Open "User Management" page
2. Verify user list displays multiple users
3. Enter "John" in "Search" field
4. Wait for list to refresh
5. Verify list contains only users with "John" in their name or email
6. Verify users not matching "John" are hidden
7. Clear "Search" field
8. Wait for list to refresh
9. Verify all users are displayed again

**Expected Result**:
- Search filters user list in real-time
- Only matching users are displayed
- Clearing search restores full list

---

### TC-009: Sort users by name [edge_case] [P2]

**Preconditions**:
- User is logged in as administrator
- Multiple users exist in the system

**Test Steps**:
1. Open "User Management" page
2. Click "Name" column header
3. Wait for list to refresh
4. Verify users are sorted by name in ascending order (A-Z)
5. Click "Name" column header again
6. Wait for list to refresh
7. Verify users are sorted by name in descending order (Z-A)

**Expected Result**:
- Clicking column header sorts the list
- Sort direction toggles between ascending and descending
- Sort indicator (arrow) shows current direction

---

### TC-010: View empty user list [edge_case] [P2]

**Preconditions**:
- User is logged in as administrator
- No users exist in the system (or all users are deleted)

**Test Steps**:
1. Open "User Management" page
2. Verify page displays "No users found" message
3. Verify empty state illustration or icon is shown
4. Verify "Add User" button is still visible and enabled

**Expected Result**:
- Empty state is clearly communicated
- User can still add new users
- No errors or broken UI elements

## 3. Items Requiring Confirmation

- [ ] [Needs Confirmation] Can administrators delete users permanently, or only deactivate them?
- [ ] [Needs Confirmation] What happens to a user's data when their account is deactivated?
- [ ] [Needs Confirmation] Is there a maximum length for the Full Name field?
- [ ] [Needs Confirmation] Can users have multiple roles, or only one role at a time?

## 4. Coverage Summary

| Type | Count | Description |
|:-----|:------|:------------|
| happy_path | 4 | Core positive flows |
| validation | 3 | Input validation |
| edge_case | 3 | Boundary conditions |
| negative | 0 | Error paths |
| **Total** | **10** | |

### Priority Distribution

| Priority | Count | Description |
|:---------|:------|:------------|
| P0 | 3 | Must cover - critical flows |
| P1 | 4 | Should cover - important scenarios |
| P2 | 3 | Can defer - low priority |
| **Total** | **10** | |

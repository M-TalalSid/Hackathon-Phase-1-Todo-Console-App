# CLI Contracts: Console Todo App

## Command Interface Specification

### Add Todo Command
- **Command**: `add "description text"`
- **Input**: String containing the todo description (in quotes if spaces)
- **Output**: Success message with assigned ID
- **Error Cases**:
  - Empty description → Error message
  - Invalid format → Error message
- **Success Scenario**: New todo added with unique ID, displayed to user

### View Todos Command
- **Command**: `view` or `list`
- **Input**: None
- **Output**: Formatted list of all todos with ID, description, and status
- **Error Cases**: None
- **Success Scenario**: All todos displayed in readable format

### Update Todo Command
- **Command**: `update <id> "new description"`
- **Input**: Integer ID and new description string
- **Output**: Success confirmation
- **Error Cases**:
  - Invalid ID → Error message
  - Non-existent ID → Error message
  - Empty description → Error message
- **Success Scenario**: Todo description updated and confirmed

### Delete Todo Command
- **Command**: `delete <id>`
- **Input**: Integer ID
- **Output**: Success confirmation
- **Error Cases**:
  - Invalid ID → Error message
  - Non-existent ID → Error message
- **Success Scenario**: Todo removed and confirmation displayed

### Complete Todo Command
- **Command**: `complete <id>` or `done <id>`
- **Input**: Integer ID
- **Output**: Success confirmation
- **Error Cases**:
  - Invalid ID → Error message
  - Non-existent ID → Error message
- **Success Scenario**: Todo marked as completed and status updated

## Application Flow Contract

### Main Loop
1. Display prompt to user
2. Accept user input
3. Parse command and arguments
4. Execute appropriate operation
5. Display result or error
6. Return to prompt (continue loop)

### Input Validation
- Commands must match expected format
- IDs must be positive integers
- Descriptions must not be empty
- Invalid inputs result in error messages and return to prompt

### Error Handling
- All errors display user-friendly messages
- Application continues running after errors
- Error messages explain what went wrong and how to fix
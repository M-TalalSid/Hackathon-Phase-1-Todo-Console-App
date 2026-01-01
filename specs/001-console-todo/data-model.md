# Data Model: Console Todo App

## Todo Entity

### Fields
- **id**: Integer - Unique identifier for the todo item (auto-incremented)
- **description**: String - The text content of the todo task (required)
- **completed**: Boolean - Status indicating if the task is completed (default: False)

### Invariants
- ID must be unique within the application session
- Description must not be empty or contain only whitespace
- Completed status is either True (completed) or False (pending)
- ID must be a positive integer

### State Transitions
- Creation: `id` assigned, `description` set, `completed` = False
- Update: `description` modified, other fields unchanged
- Complete: `completed` = True, other fields unchanged
- Delete: Item removed from collection

## Todo Collection

### Structure
- **Storage**: Dictionary mapping integer IDs to Todo objects
- **ID Generation**: Auto-incrementing integer starting from 1
- **Access Pattern**: O(1) lookup by ID

### Operations
- **Create**: Add new todo with auto-generated ID
- **Read**: Retrieve todo by ID
- **Update**: Modify existing todo by ID
- **Delete**: Remove todo by ID
- **List**: Retrieve all todos
- **Filter**: Retrieve completed or pending todos separately

### Validation Rules
- Duplicate IDs are not allowed
- Description must be provided and not empty
- Invalid IDs return appropriate errors
- Empty collections return empty lists when listed
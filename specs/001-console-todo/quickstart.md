# Quickstart: Console Todo App

## Getting Started

### Prerequisites
- Python 3.13+ installed
- UV package manager installed

### Setup
1. Clone or create the project directory
2. Navigate to the project root
3. Install dependencies (if any): `uv sync` (though this project uses only built-in libraries)

### Running the Application
```bash
cd src/cli
python main.py
```

## Basic Usage

### Available Commands

1. **Add a todo**:
   ```
   add "Buy groceries"
   ```

2. **View all todos**:
   ```
   view
   ```

3. **Update a todo**:
   ```
   update 1 "Buy groceries and cook dinner"
   ```

4. **Complete a todo**:
   ```
   complete 1
   ```

5. **Delete a todo**:
   ```
   delete 1
   ```

### Example Workflow
```
> add "Buy milk"
Added todo #1: Buy milk

> add "Walk the dog"
Added todo #2: Walk the dog

> view
1. [ ] Buy milk
2. [ ] Walk the dog

> complete 1
Todo #1 marked as complete

> view
1. [x] Buy milk
2. [ ] Walk the dog

> update 2 "Walk the dog in the morning"
Todo #2 updated to: Walk the dog in the morning

> delete 2
Todo #2 deleted

> view
1. [x] Buy milk
```

## Expected Behavior
- Application runs in console and maintains state in memory
- All operations complete quickly (under 100ms)
- Invalid commands show helpful error messages
- Application continues running until manually exited
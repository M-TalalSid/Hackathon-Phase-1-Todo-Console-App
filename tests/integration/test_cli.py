"""
Integration tests for the CLI application.
Tests the complete user workflows by simulating user interactions.
"""

from src.cli.main import TodoCLI


class TestCLIIntegration:
    """Integration tests for the CLI application."""

    def test_complete_workflow_add_view_complete_update_delete(self):
        """Test the complete workflow: add, view, complete, update, delete."""
        cli = TodoCLI()

        # Add a todo
        cli._add_todo('"First task"')

        # Verify the todo was added
        todos = cli.service.get_all_todos()
        assert len(todos) == 1
        assert todos[0].description == "First task"
        assert todos[0].completed is False

        # Complete the todo
        todo_id = todos[0].id
        cli._complete_todo(str(todo_id))

        # Verify the todo was completed
        completed_todo = cli.service.get_todo(todo_id)
        assert completed_todo is not None
        assert completed_todo.completed is True

        # Update the todo
        cli._update_todo(f'{todo_id} "Updated task"')

        # Verify the todo was updated
        updated_todo = cli.service.get_todo(todo_id)
        assert updated_todo is not None
        assert updated_todo.description == "Updated task"

        # Delete the todo
        cli._delete_todo(str(todo_id))

        # Verify the todo was deleted
        deleted_todo = cli.service.get_todo(todo_id)
        assert deleted_todo is None
        assert len(cli.service.get_all_todos()) == 0

    def test_multiple_todos_workflow(self):
        """Test workflow with multiple todos."""
        cli = TodoCLI()

        # Add multiple todos
        cli._add_todo('"First task"')
        cli._add_todo('"Second task"')
        cli._add_todo('"Third task"')

        # Verify all todos were added
        todos = cli.service.get_all_todos()
        assert len(todos) == 3

        # Get the IDs of the todos
        todo_ids = [todo.id for todo in todos]
        assert len(todo_ids) == 3

        # Complete the second todo
        second_id = todo_ids[1]
        cli._complete_todo(str(second_id))

        # Verify the second todo is completed
        completed_todo = cli.service.get_todo(second_id)
        assert completed_todo is not None
        assert completed_todo.completed is True

        # Update the first todo
        first_id = todo_ids[0]
        cli._update_todo(f'{first_id} "Updated first task"')

        # Verify the first todo was updated
        updated_todo = cli.service.get_todo(first_id)
        assert updated_todo is not None
        assert updated_todo.description == "Updated first task"

        # Delete the third todo
        third_id = todo_ids[2]
        cli._delete_todo(str(third_id))

        # Verify the third todo was deleted and others remain
        remaining_todos = cli.service.get_all_todos()
        assert len(remaining_todos) == 2
        assert cli.service.get_todo(third_id) is None

    def test_error_handling_for_invalid_commands(self):
        """Test that invalid commands are handled gracefully."""
        cli = TodoCLI()

        # Add a todo first
        cli._add_todo('"Test task"')
        todos = cli.service.get_all_todos()
        assert len(todos) == 1
        todo_id = todos[0].id

        # Try to complete a non-existent todo
        cli._complete_todo("999")
        # No exception should be raised, and the service method returns False

        # Try to update a non-existent todo
        cli._update_todo("999 \"New description\"")
        # No exception should be raised

        # Try to delete a non-existent todo
        cli._delete_todo("999")
        # No exception should be raised

        # Try to get a non-existent todo
        result = cli.service.get_todo(999)
        assert result is None

    def test_input_validation(self):
        """Test input validation for various commands."""
        cli = TodoCLI()

        # Test adding a todo with empty description
        cli._add_todo('""')
        # Should show error message but not crash

        # Add a valid todo
        cli._add_todo('"Valid task"')
        todos = cli.service.get_all_todos()
        assert len(todos) == 1

        # Update with valid description
        todo_id = todos[0].id
        cli._update_todo(f'{todo_id} "Updated valid task"')
        updated_todo = cli.service.get_todo(todo_id)
        assert updated_todo.description == "Updated valid task"
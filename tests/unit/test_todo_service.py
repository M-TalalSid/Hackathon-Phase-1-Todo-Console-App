"""
Unit tests for the TodoService.
"""

import pytest
from src.services.todo_service import TodoService


class TestTodoService:
    """Test cases for the TodoService."""

    def test_initial_state(self):
        """Test the initial state of the service."""
        service = TodoService()
        assert len(service.get_all_todos()) == 0
        assert service.get_next_id() == 1

    def test_add_todo(self):
        """Test adding a new todo."""
        service = TodoService()
        todo = service.add_todo("Test task")

        assert todo.id == 1
        assert todo.description == "Test task"
        assert todo.completed is False

        todos = service.get_all_todos()
        assert len(todos) == 1
        assert todos[0].id == 1
        assert todos[0].description == "Test task"

    def test_add_todo_with_special_characters(self):
        """Test adding a todo with special characters."""
        service = TodoService()
        description = "Test task with special chars: !@#$%^&*()"
        todo = service.add_todo(description)

        assert todo.description == description

    def test_add_multiple_todos(self):
        """Test adding multiple todos."""
        service = TodoService()
        todo1 = service.add_todo("First task")
        todo2 = service.add_todo("Second task")
        todo3 = service.add_todo("Third task")

        assert todo1.id == 1
        assert todo2.id == 2
        assert todo3.id == 3

        todos = service.get_all_todos()
        assert len(todos) == 3

    def test_add_todo_empty_description(self):
        """Test adding a todo with empty description raises error."""
        service = TodoService()
        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            service.add_todo("")

    def test_add_todo_whitespace_description(self):
        """Test adding a todo with whitespace-only description raises error."""
        service = TodoService()
        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            service.add_todo("   ")

    def test_add_todo_trailing_leading_spaces(self):
        """Test adding a todo trims trailing and leading spaces."""
        service = TodoService()
        todo = service.add_todo("  Test task  ")
        assert todo.description == "Test task"

    def test_get_todo_by_id(self):
        """Test getting a todo by its ID."""
        service = TodoService()
        added_todo = service.add_todo("Test task")

        retrieved_todo = service.get_todo(added_todo.id)
        assert retrieved_todo is not None
        assert retrieved_todo.id == added_todo.id
        assert retrieved_todo.description == added_todo.description

    def test_get_nonexistent_todo(self):
        """Test getting a non-existent todo returns None."""
        service = TodoService()
        todo = service.get_todo(999)
        assert todo is None

    def test_get_all_todos_empty(self):
        """Test getting all todos when none exist."""
        service = TodoService()
        todos = service.get_all_todos()
        assert len(todos) == 0

    def test_complete_todo(self):
        """Test completing a todo."""
        service = TodoService()
        todo = service.add_todo("Test task")

        assert todo.completed is False

        success = service.complete_todo(todo.id)
        assert success is True

        updated_todo = service.get_todo(todo.id)
        assert updated_todo is not None
        assert updated_todo.completed is True

    def test_complete_nonexistent_todo(self):
        """Test completing a non-existent todo returns False."""
        service = TodoService()
        success = service.complete_todo(999)
        assert success is False

    def test_complete_already_completed_todo(self):
        """Test completing an already completed todo."""
        service = TodoService()
        todo = service.add_todo("Test task")

        # Complete it first time
        success1 = service.complete_todo(todo.id)
        assert success1 is True

        # Check it's completed
        retrieved_todo = service.get_todo(todo.id)
        assert retrieved_todo.completed is True

        # Try to complete it again
        success2 = service.complete_todo(todo.id)
        assert success2 is True  # Should still return True

        # Check it's still completed
        retrieved_todo2 = service.get_todo(todo.id)
        assert retrieved_todo2.completed is True

    def test_update_todo(self):
        """Test updating a todo's description."""
        service = TodoService()
        original_todo = service.add_todo("Original task")

        success = service.update_todo(original_todo.id, "Updated task")
        assert success is True

        updated_todo = service.get_todo(original_todo.id)
        assert updated_todo is not None
        assert updated_todo.description == "Updated task"
        assert updated_todo.id == original_todo.id  # ID should remain the same
        assert updated_todo.completed is False  # Completion status should remain the same

    def test_update_todo_completion_status_preserved(self):
        """Test that updating a todo preserves its completion status."""
        service = TodoService()
        todo = service.add_todo("Original task")
        service.complete_todo(todo.id)  # Mark as completed first

        # Verify it's completed
        retrieved_todo = service.get_todo(todo.id)
        assert retrieved_todo.completed is True

        # Update the description
        success = service.update_todo(todo.id, "Updated task")
        assert success is True

        # Verify it's still completed after update
        updated_todo = service.get_todo(todo.id)
        assert updated_todo is not None
        assert updated_todo.completed is True
        assert updated_todo.description == "Updated task"

    def test_update_nonexistent_todo(self):
        """Test updating a non-existent todo returns False."""
        service = TodoService()
        success = service.update_todo(999, "New description")
        assert success is False

    def test_update_todo_empty_description(self):
        """Test updating a todo with empty description raises error."""
        service = TodoService()
        todo = service.add_todo("Original task")

        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            service.update_todo(todo.id, "")

    def test_update_todo_whitespace_description(self):
        """Test updating a todo with whitespace-only description raises error."""
        service = TodoService()
        todo = service.add_todo("Original task")

        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            service.update_todo(todo.id, "   ")

    def test_delete_todo(self):
        """Test deleting a todo."""
        service = TodoService()
        todo = service.add_todo("Test task")

        # Verify the todo exists
        retrieved_todo = service.get_todo(todo.id)
        assert retrieved_todo is not None

        # Delete the todo
        success = service.delete_todo(todo.id)
        assert success is True

        # Verify the todo no longer exists
        retrieved_todo_after = service.get_todo(todo.id)
        assert retrieved_todo_after is None

        # Verify the todo count is reduced
        all_todos = service.get_all_todos()
        assert len(all_todos) == 0

    def test_delete_nonexistent_todo(self):
        """Test deleting a non-existent todo returns False."""
        service = TodoService()
        success = service.delete_todo(999)
        assert success is False

    def test_delete_todo_and_add_new(self):
        """Test deleting a todo doesn't affect adding new todos."""
        service = TodoService()
        first_todo = service.add_todo("First task")

        # Delete the first todo
        success = service.delete_todo(first_todo.id)
        assert success is True

        # Add a new todo
        second_todo = service.add_todo("Second task")

        # Verify the new todo exists and has the next available ID
        all_todos = service.get_all_todos()
        assert len(all_todos) == 1
        assert all_todos[0].id == 2  # Should be 2 since 1 was deleted
        assert all_todos[0].description == "Second task"

    def test_delete_multiple_todos(self):
        """Test deleting multiple todos."""
        service = TodoService()
        todo1 = service.add_todo("First task")
        todo2 = service.add_todo("Second task")
        todo3 = service.add_todo("Third task")

        # Verify all todos exist
        assert service.get_todo(todo1.id) is not None
        assert service.get_todo(todo2.id) is not None
        assert service.get_todo(todo3.id) is not None
        assert len(service.get_all_todos()) == 3

        # Delete the second todo
        success = service.delete_todo(todo2.id)
        assert success is True

        # Verify only the second todo is gone
        assert service.get_todo(todo1.id) is not None
        assert service.get_todo(todo2.id) is None
        assert service.get_todo(todo3.id) is not None
        assert len(service.get_all_todos()) == 2
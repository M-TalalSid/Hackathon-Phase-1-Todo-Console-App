"""
Unit tests for the Todo model.
"""

import pytest
from src.models.todo import Todo


class TestTodo:
    """Test cases for the Todo model."""

    def test_todo_creation(self):
        """Test creating a valid todo."""
        todo = Todo(id=1, description="Test task")
        assert todo.id == 1
        assert todo.description == "Test task"
        assert todo.completed is False

    def test_todo_creation_with_completion_status(self):
        """Test creating a todo with completed status."""
        todo = Todo(id=1, description="Test task", completed=True)
        assert todo.id == 1
        assert todo.description == "Test task"
        assert todo.completed is True

    def test_todo_mark_completed(self):
        """Test marking a todo as completed."""
        todo = Todo(id=1, description="Test task")
        assert todo.completed is False
        todo.mark_completed()
        assert todo.completed is True

    def test_todo_update_description(self):
        """Test updating a todo's description."""
        todo = Todo(id=1, description="Old task")
        assert todo.description == "Old task"
        todo.update_description("New task")
        assert todo.description == "New task"

    def test_todo_update_description_empty(self):
        """Test updating a todo's description with empty string raises error."""
        todo = Todo(id=1, description="Old task")
        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            todo.update_description("")

    def test_todo_update_description_whitespace(self):
        """Test updating a todo's description with whitespace raises error."""
        todo = Todo(id=1, description="Old task")
        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            todo.update_description("   ")

    def test_todo_creation_empty_description(self):
        """Test creating a todo with empty description raises error."""
        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            Todo(id=1, description="")

    def test_todo_creation_whitespace_description(self):
        """Test creating a todo with whitespace description raises error."""
        with pytest.raises(ValueError, match="Todo description cannot be empty"):
            Todo(id=1, description="   ")

    def test_todo_creation_negative_id(self):
        """Test creating a todo with negative ID raises error."""
        with pytest.raises(ValueError, match="Todo ID must be a positive integer"):
            Todo(id=-1, description="Test task")

    def test_todo_creation_zero_id(self):
        """Test creating a todo with zero ID raises error."""
        with pytest.raises(ValueError, match="Todo ID must be a positive integer"):
            Todo(id=0, description="Test task")

    def test_todo_str_representation(self):
        """Test the string representation of a todo."""
        todo = Todo(id=1, description="Test task")
        assert str(todo) == "[ ] 1. Test task"

        todo.mark_completed()
        assert str(todo) == "[x] 1. Test task"
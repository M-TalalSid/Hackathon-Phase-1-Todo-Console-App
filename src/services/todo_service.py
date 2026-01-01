"""
Todo service for managing todo operations in memory.
"""

from typing import List, Optional
from src.models.todo import Todo


class TodoService:
    """
    Service class for managing todo operations.
    Handles all business logic for todo management in memory.
    """

    def __init__(self):
        """Initialize the service with an empty todo list."""
        self._todos = {}
        self._next_id = 1

    def add_todo(self, description: str) -> Todo:
        """
        Add a new todo with the given description.

        Args:
            description: The description of the todo

        Returns:
            The created Todo object with assigned ID
        """
        if not description or not description.strip():
            raise ValueError("Todo description cannot be empty")

        todo = Todo(id=self._next_id, description=description.strip())
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        return self._todos.get(todo_id)

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos.

        Returns:
            A list of all Todo objects
        """
        return list(self._todos.values())

    def update_todo(self, todo_id: int, new_description: str) -> bool:
        """
        Update the description of an existing todo.

        Args:
            todo_id: The ID of the todo to update
            new_description: The new description for the todo

        Returns:
            True if the todo was updated, False if it didn't exist
        """
        if todo_id not in self._todos:
            return False

        if not new_description or not new_description.strip():
            raise ValueError("Todo description cannot be empty")

        self._todos[todo_id].update_description(new_description.strip())
        return True

    def complete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as completed.

        Args:
            todo_id: The ID of the todo to mark as completed

        Returns:
            True if the todo was marked as completed, False if it didn't exist
        """
        if todo_id not in self._todos:
            return False

        self._todos[todo_id].mark_completed()
        return True

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if it didn't exist
        """
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo.

        Returns:
            The next available ID
        """
        return self._next_id
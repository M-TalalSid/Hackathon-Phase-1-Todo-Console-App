"""
Todo data model representing a single todo item.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with an ID, description, and completion status.
    """
    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate the todo after initialization."""
        if not self.description or not self.description.strip():
            raise ValueError("Todo description cannot be empty")
        if self.id <= 0:
            raise ValueError("Todo ID must be a positive integer")

    def mark_completed(self):
        """Mark the todo as completed."""
        self.completed = True

    def update_description(self, new_description: str):
        """Update the todo description."""
        if not new_description or not new_description.strip():
            raise ValueError("Todo description cannot be empty")
        self.description = new_description.strip()

    def __str__(self) -> str:
        """String representation of the todo."""
        status = "x" if self.completed else " "
        return f"[{status}] {self.id}. {self.description}"
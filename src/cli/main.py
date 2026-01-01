from src.services.todo_service import TodoService


class TodoCLI:
    """
    Menu-driven CLI for the todo application.
    Simple, beginner-friendly interface with numbered options.
    """

    def __init__(self):
        """Initialize the CLI with a todo service."""
        self.service = TodoService()

    def run(self):
        """Run the main application loop."""
        print("=" * 40)
        print("  Welcome to the Todo CLI Application !")
        print("=" * 40)
        print()

        while True:
            self._show_menu()
            try:
                choice = input("Enter your choice (1-6): ").strip()

                if choice == "1":
                    self._add_todo_menu()
                elif choice == "2":
                    self._list_todos()
                elif choice == "3":
                    self._update_todo_menu()
                elif choice == "4":
                    self._complete_todo_menu()
                elif choice == "5":
                    self._delete_todo_menu()
                elif choice in ["6", "q", "quit", "exit"]:
                    print("\n👋 Goodbye!")
                    break
                else:
                    print("\nInvalid choice. Please enter a number between 1 and 6.\n")

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\nError: {e}")
                input("\nPress Enter to continue...")
                print()

    def _show_menu(self):
        """Display the main menu."""
        menu = """
Main Menu:
---------
1. Add a todo
2. View all todos
3. Update a todo
4. Complete a todo
5. Delete a todo
6. Exit
        """
        print(menu)

    def _add_todo_menu(self):
        """Menu for adding a new todo."""
        print("\n--- Add Todo ---")
        description = input("Enter task description: ").strip()

        if not description:
            print("\nError: Task description cannot be empty!")
            return

        try:
            todo = self.service.add_todo(description)
            print(f"\nAdded: [{todo.id}] {todo.description}")
        except ValueError as e:
            print(f"\nError: {e}")

    def _list_todos(self):
        """Display all todos."""
        print("\n--- Your Todos ---")
        todos = self.service.get_all_todos()

        if not todos:
            print("\nNo todos yet!")
            return

        for todo in todos:
            status = "X" if todo.completed else "O"
            print(f"  {status} [{todo.id}] {todo.description}")

    def _update_todo_menu(self):
        """Menu for updating a todo."""
        print("\n--- Update Todo ---")
        self._list_todos()

        try:
            todo_id = int(input("\nEnter todo ID to update: ").strip())
        except ValueError:
            print("\nError: Please enter a valid number!")
            return

        new_description = input("Enter new description: ").strip()

        if not new_description:
            print("\nError: New description cannot be empty!")
            return

        success = self.service.update_todo(todo_id, new_description)
        if success:
            print(f"\nUpdated todo [{todo_id}]")
        else:
            print(f"\nError: Todo [{todo_id}] not found!")

    def _complete_todo_menu(self):
        """Menu for completing a todo."""
        print("\n--- Complete Todo ---")
        self._list_todos()

        try:
            todo_id = int(input("\nEnter todo ID to complete: ").strip())
        except ValueError:
            print("\nError: Please enter a valid number!")
            return

        success = self.service.complete_todo(todo_id)
        if success:
            print(f"\nCompleted todo [{todo_id}]")
        else:
            print(f"\nError: Todo [{todo_id}] not found!")

    def _delete_todo_menu(self):
        """Menu for deleting a todo."""
        print("\n--- Delete Todo ---")
        self._list_todos()

        try:
            todo_id = int(input("\nEnter todo ID to delete: ").strip())
        except ValueError:
            print("\nError: Please enter a valid number!")
            return

        # Confirm deletion
        confirm = input(f"\nAre you sure you want to delete todo [{todo_id}]? (y/n): ").strip().lower()
        if confirm != "y":
            print("\nDeletion cancelled.")
            return

        success = self.service.delete_todo(todo_id)
        if success:
            print(f"\nDeleted todo [{todo_id}]")
        else:
            print(f"\nError: Todo [{todo_id}] not found!")


def main():
    """Main entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()

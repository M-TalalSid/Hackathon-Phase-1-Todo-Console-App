"""
Console Todo Application - Main CLI Interface
Clean, extensible, and user-friendly.
"""

import re
from typing import Callable
from src.services.todo_service import TodoService


class TodoCLI:
    PROMPT = "todo > "

    COMMANDS = {
        "add": {
            "aliases": [],
            "handler": "_add_todo",
            "help": 'add "task description"'
        },
        "list": {
            "aliases": ["ls", "view"],
            "handler": "_list_todos",
            "help": "list | ls | view"
        },
        "update": {
            "aliases": [],
            "handler": "_update_todo",
            "help": 'update <id> "new description"'
        },
        "complete": {
            "aliases": ["done", "finish"],
            "handler": "_complete_todo",
            "help": "complete <id>"
        },
        "delete": {
            "aliases": ["del", "remove"],
            "handler": "_delete_todo",
            "help": "delete <id>"
        },
        "help": {
            "aliases": [],
            "handler": "_show_help",
            "help": "help"
        },
        "quit": {
            "aliases": ["exit", "q"],
            "handler": "_quit",
            "help": "quit | exit | q"
        },
    }

    def __init__(self):
        self.service = TodoService()
        self.running = True

    # ================== CORE LOOP ==================

    def run(self):
        self._print_banner()

        while self.running:
            try:
                raw = input(self.PROMPT).strip()
                if not raw:
                    continue

                command, args = self._parse_input(raw)
                self._dispatch(command, args)

            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

    # ================== DISPATCH ==================

    def _dispatch(self, command: str, args: str):
        for name, meta in self.COMMANDS.items():
            if command == name or command in meta["aliases"]:
                handler: Callable = getattr(self, meta["handler"])
                handler(args)
                return

        print(f"Unknown command: '{command}'. Type `help`.")

    def _parse_input(self, raw: str):
        parts = raw.split(maxsplit=1)
        return parts[0].lower(), parts[1] if len(parts) > 1 else ""

    # ================== COMMANDS ==================

    def _add_todo(self, args: str):
        desc = self._strip_quotes(args)
        if not desc:
            print("Usage: add \"task description\"")
            return

        todo = self.service.add_todo(desc)
        print(f"Added [#{todo.id}] {todo.description}")

    def _list_todos(self, _=None):
        todos = self.service.get_all_todos()
        if not todos:
            print("No todos yet.")
            return

        print("\nYour Todos")
        print("-" * 30)
        for t in todos:
            status = "✔" if t.completed else "○"
            print(f"{status} [{t.id}] {t.description}")
        print()

    def _update_todo(self, args: str):
        todo_id, desc = self._parse_id_and_text(args)
        if todo_id is None or not desc:
            print("Usage: update <id> \"new description\"")
            return

        if self.service.update_todo(todo_id, desc):
            print(f"Updated todo #{todo_id}")
        else:
            print(f"Todo #{todo_id} not found")

    def _complete_todo(self, args: str):
        todo_id = self._parse_id(args)
        if todo_id is None:
            print("Usage: complete <id>")
            return

        if self.service.complete_todo(todo_id):
            print(f"Completed todo #{todo_id}")
        else:
            print(f"Todo #{todo_id} not found")

    def _delete_todo(self, args: str):
        todo_id = self._parse_id(args)
        if todo_id is None:
            print("Usage: delete <id>")
            return

        if self.service.delete_todo(todo_id):
            print(f"Deleted todo #{todo_id}")
        else:
            print(f"Todo #{todo_id} not found")

    def _quit(self, _=None):
        print("👋 Goodbye!")
        self.running = False

    # ================== HELPERS ==================

    def _show_help(self, _=None):
        print("\nAvailable Commands")
        print("-" * 30)
        for cmd, meta in self.COMMANDS.items():
            print(f"{meta['help']}")
        print()

    def _strip_quotes(self, text: str) -> str:
        text = text.strip()
        if (text.startswith('"') and text.endswith('"')) or \
           (text.startswith("'") and text.endswith("'")):
            return text[1:-1].strip()
        return text

    def _parse_id(self, text: str):
        match = re.match(r"(\d+)", text.strip())
        return int(match.group(1)) if match else None

    def _parse_id_and_text(self, text: str):
        match = re.match(r"(\d+)\s+(.*)", text.strip())
        if not match:
            return None, None
        return int(match.group(1)), self._strip_quotes(match.group(2))

    def _print_banner(self):
        print("\nWelcome to the Todo CLI Application !")
        print("Type `help` to see commands\n")


def main():
    TodoCLI().run()


if __name__ == "__main__":
    main()

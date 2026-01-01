---
description: "Task list for console todo app implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included based on the feature requirements for verification and validation.
**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 [P] Create src/models/, src/services/, src/cli/, and src/lib/ directories
- [X] T003 [P] Initialize Python project with basic requirements (no external dependencies needed)

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Todo data model in src/models/todo.py
- [X] T005 Create TodoService class in src/services/todo_service.py
- [X] T006 Create basic CLI structure in src/cli/main.py
- [X] T007 Set up in-memory storage mechanism in TodoService

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo tasks to the application with a unique identifier

**Independent Test**: User can run the application, enter an "add" command with a task description, and see the task added to the list with a unique ID and "pending" status

### Tests for User Story 1
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T008 [P] [US1] Create unit test for Todo model in tests/unit/test_todo.py
- [X] T009 [P] [US1] Create unit test for add functionality in tests/unit/test_todo_service.py

### Implementation for User Story 1

- [X] T010 [P] [US1] Implement Todo class with id, description, and completed fields in src/models/todo.py
- [X] T011 [US1] Implement add_todo method in TodoService class in src/services/todo_service.py
- [X] T012 [US1] Implement CLI command parsing for add functionality in src/cli/main.py
- [X] T013 [US1] Connect CLI add command to TodoService in src/cli/main.py
- [X] T014 [US1] Add input validation for add command in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: Enable users to see all their current todo tasks displayed in the console with their status

**Independent Test**: User can run the application, add some tasks, then enter a "view" command to see all tasks displayed with their ID, description, and completion status

### Tests for User Story 2
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T015 [P] [US2] Create unit test for list functionality in tests/unit/test_todo_service.py

### Implementation for User Story 2

- [X] T016 [US2] Implement get_all_todos method in TodoService class in src/services/todo_service.py
- [X] T017 [US2] Implement CLI command parsing for view functionality in src/cli/main.py
- [X] T018 [US2] Connect CLI view command to TodoService in src/cli/main.py
- [X] T019 [US2] Add formatting for displaying todos in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P2)

**Goal**: Enable users to mark specific tasks as complete after finishing them using the task ID

**Independent Test**: User can run the application, add a task, then enter a "complete" command with the task ID, and see the task status updated to "completed"

### Tests for User Story 3
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T020 [P] [US3] Create unit test for complete functionality in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [X] T021 [US3] Implement complete_todo method in TodoService class in src/services/todo_service.py
- [X] T022 [US3] Implement CLI command parsing for complete functionality in src/cli/main.py
- [X] T023 [US3] Connect CLI complete command to TodoService in src/cli/main.py
- [X] T024 [US3] Add validation for complete command in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---
## Phase 6: User Story 4 - Update Todo (Priority: P3)

**Goal**: Enable users to modify the description of an existing task using the task ID

**Independent Test**: User can run the application, add a task, then enter an "update" command with the task ID and new description, and see the task description updated

### Tests for User Story 4
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T025 [P] [US4] Create unit test for update functionality in tests/unit/test_todo_service.py

### Implementation for User Story 4

- [X] T026 [US4] Implement update_todo method in TodoService class in src/services/todo_service.py
- [X] T027 [US4] Implement CLI command parsing for update functionality in src/cli/main.py
- [X] T028 [US4] Connect CLI update command to TodoService in src/cli/main.py
- [X] T029 [US4] Add validation for update command in src/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---
## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Enable users to remove a specific task from their list using the task ID

**Independent Test**: User can run the application, add a task, then enter a "delete" command with the task ID, and see the task removed from the system

### Tests for User Story 5
> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T030 [P] [US5] Create unit test for delete functionality in tests/unit/test_todo_service.py

### Implementation for User Story 5

- [X] T031 [US5] Implement delete_todo method in TodoService class in src/services/todo_service.py
- [X] T032 [US5] Implement CLI command parsing for delete functionality in src/cli/main.py
- [X] T033 [US5] Connect CLI delete command to TodoService in src/cli/main.py
- [X] T034 [US5] Add validation for delete command in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T035 [P] Add comprehensive error handling across all CLI commands in src/cli/main.py
- [X] T036 [P] Add input validation across all functions in src/services/todo_service.py
- [X] T037 Add help command to CLI in src/cli/main.py
- [X] T038 [P] Add integration tests for complete user workflows in tests/integration/test_cli.py
- [X] T039 Run quickstart.md validation to ensure all functionality works as expected

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
T008 [P] [US1] Create unit test for Todo model in tests/unit/test_todo.py
T009 [P] [US1] Create unit test for add functionality in tests/unit/test_todo_service.py

# Launch all models for User Story 1 together:
T010 [P] [US1] Implement Todo class with id, description, and completed fields in src/models/todo.py
```

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
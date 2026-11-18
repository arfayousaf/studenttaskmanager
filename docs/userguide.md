
# Student Task Manager - User Guide

## 1. Introduction

Student Task Manager is a simple Python console
application designed to help students manage
their academic tasks.

## 2. Starting the Application

Open the terminal in the project directory.

Execute:

```bash
python task_manager.py
```

The main menu will appear.

## 3. Adding a Task

Select option 1.

Enter the task title when prompted.

Example:

```text
Enter task title: Complete Database Assignment
Task added successfully! ID: 1
```

Empty task titles are not accepted.

## 4. Displaying Tasks

Select option 2.

The application displays all tasks with their IDs,
titles, and completion statuses.

## 5. Completing a Task

Select option 3.

Enter the ID of the task you want to complete.

The task status changes from Pending to Completed.

## 6. Deleting a Task

Select option 4.

Enter the ID of the task you want to delete.

The selected task is removed from the list.

## 7. Exiting

Select option 5 to close the application.

## 8. Running Tests

Execute:

```bash
python -m unittest discover -s tests -v
```

The application includes automated tests for
task creation, completion, deletion, validation,
and invalid task identifiers.

## 9. Important Notes

- Tasks are stored in memory.
- Task IDs are assigned automatically.
- Empty titles are rejected.
- Invalid IDs are handled safely.

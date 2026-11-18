
# Student Task Manager

A Python-based console application that helps students
organize and manage their academic tasks.

## Features

- Add new tasks.
- Validate task titles.
- Display all tasks.
- Mark tasks as completed.
- Delete tasks using unique task IDs.
- Handle invalid task IDs.
- Automated unit testing using unittest.
- Continuous Integration using GitHub Actions.

## Technologies Used

- Python 3.12
- Git
- GitHub
- Python unittest
- GitHub Actions

## Project Structure

```text
studenttaskmanager/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── docs/
│   └── userguide.md
├── tests/
│   └── test_task_manager.py
├── task_manager.py
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/studenttaskmanager.git
```

2. Navigate to the project:

```bash
cd studenttaskmanager
```

3. Ensure Python is installed:

```bash
python --version
```

No external dependencies are required.

## Usage

Run the application:

```bash
python task_manager.py
```

Select an option from the menu:

1. Add Task
2. Display Tasks
3. Complete Task
4. Delete Task
5. Exit

Each task is assigned a unique identifier.

## Running Automated Tests

Run the tests using:

```bash
python -m unittest discover -s tests -v
```

The test suite checks task creation, completion,
deletion, validation, and invalid task IDs.

## GitHub Actions

GitHub Actions automatically runs unit tests when:

- Code is pushed to the main branch.
- A pull request targets the main branch.

## Documentation

See [User Guide](docs/userguide.md) for
detailed application instructions.

## Version

v1.0.0

## License

This project is licensed under the MIT License.

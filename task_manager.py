# Student Task Manager application
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    def validate_title(self, title):
        return bool(title and title.strip())

    def add_task(self, title):

        if not self.validate_title(title):
            raise ValueError("Task title cannot be empty.")

        task = {
        "id": self.next_id,
        "title": title.strip(),
        "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1

        return task

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(
                f'{task["id"]}. {task["title"]} - {status}'
            )

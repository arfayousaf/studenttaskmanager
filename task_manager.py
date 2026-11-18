# Student Task Manager application
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {
            "id": self.next_id,
            "title": title,
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

    def delete_task(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        return True
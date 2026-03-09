from task import Task

class TaskManager:
    def _init_(self):
        self.tasks = []

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in writes")
            return

            for task in self.tasks:
                print(f"{task.id}. {task.title} ({task.description}) - {task.status}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task.id:
                task.complete()
                return True
        return False

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

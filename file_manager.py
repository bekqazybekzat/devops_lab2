import json
from task import Task

class FileManager:
    def save(self, tasks, filename):
        data = [tasks.to_dict() for tasks in tasks]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load (self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                return [Task.from_dict(task) for task in data]
        except:
            return []

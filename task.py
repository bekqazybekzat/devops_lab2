class Task:
    def _init_ (self, id, title, description, status = "Waiting"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def complete (self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }


    @staticmethod
    def from_dict (data):
        return Task (data["id"], data["title"], data["description"], data["status"])

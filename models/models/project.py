from datetime import datetime


from datetime import datetime


class Project:
    """
    Represents a project owned by a user.
    """

    # Class attribute
    next_id = 1

    def __init__(self, title, description, due_date):
        self.id = Project.next_id
        Project.next_id += 1

        self.title = title
        self.description = description
        self.due_date = due_date

        # Every project starts with no tasks
        self.tasks = []

    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):

        value = value.strip()

        if not value:
            raise ValueError("Project title cannot be empty.")

        self._title = value.title()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):

        value = value.strip()

        if not value:
            raise ValueError("Description cannot be empty.")

        self._description = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):

        try:
            datetime.strptime(value, "%Y-%m-%d")
            self._due_date = value
        except ValueError:
            raise ValueError(
                "Due date must be in YYYY-MM-DD format."
            )

    
    
    def add_task(self, task):
        """
        Add a task to this project.
        """
        self.tasks.append(task)

    def remove_task(self, task_title):
        """
        Remove a task by title.
        """

        for task in self.tasks:

            if task.title.lower() == task_title.lower():
                self.tasks.remove(task)
                return True

        return False

    def get_tasks(self):
        """
        Return all tasks.
        """
        return self.tasks

    # ------------------------
    # JSON Methods
    # ------------------------

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [
                task.to_dict()
                for task in self.tasks
            ]
        }

    @classmethod
    def from_dict(cls, data):

        project = cls(
            data["title"],
            data["description"],
            data["due_date"]
        )

        project.id = data["id"]

        if project.id >= cls.next_id:
            cls.next_id = project.id + 1

        return project


    def __str__(self):

        return (
            f"Project ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Tasks: {len(self.tasks)}"
        )
class Task:
    """
    Represents a task in a project.
    """

    # Class attribute for automatic IDs
    next_id = 1

    def __init__(self, title, assigned_to):
        self.id = Task.next_id
        Task.next_id += 1

        self.title = title
        self.assigned_to = assigned_to

        # Every new task starts as Pending
        self.status = "Pending"

    # -------------------------
    # Properties
    # -------------------------

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):

        value = value.strip()

        if not value:
            raise ValueError("Task title cannot be empty.")

        self._title = value.title()

    @property
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, value):

        value = value.strip()

        if not value:
            raise ValueError("Assigned user cannot be empty.")

        self._assigned_to = value.title()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):

        allowed = ["Pending", "Completed"]

        if value not in allowed:
            raise ValueError("Status must be Pending or Completed.")

        self._status = value

    # -------------------------
    # Instance Methods
    # -------------------------

    def mark_complete(self):
        """
        Marks a task as completed.
        """
        self.status = "Completed"

    # -------------------------
    # JSON Methods
    # -------------------------

    def to_dict(self):

        return {
            "id": self.id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):

        task = cls(
            data["title"],
            data["assigned_to"]
        )

        task.id = data["id"]
        task.status = data["status"]

        if task.id >= cls.next_id:
            cls.next_id = task.id + 1

        return task

    # -------------------------
    # String Representation
    # -------------------------

    def __str__(self):

        return (
            f"Task ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Assigned To: {self.assigned_to}\n"
            f"Status: {self.status}"
        )
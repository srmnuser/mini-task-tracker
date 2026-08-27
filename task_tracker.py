class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.title}"


class TaskTracker:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        return task


if __name__ == "__main__":
    tracker = TaskTracker()

    task = tracker.add_task("Learn Git")
    print(task)
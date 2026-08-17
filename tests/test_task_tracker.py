from task_tracker import TaskTracker


def test_add_task():
    tracker = TaskTracker()

    task = tracker.add_task("Learn Git")

    assert task.id == 1
    assert task.title == "Learn Git"
    assert task.completed is False


def test_multiple_tasks_get_unique_ids():
    tracker = TaskTracker()

    task1 = tracker.add_task("Learn Git")
    task2 = tracker.add_task("Learn Docker")

    assert task1.id == 1
    assert task2.id == 2
    assert len(tracker.tasks) == 2
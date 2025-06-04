import pytest
from taskman import Task
from datetime import date


class TestTask:
    def test_task_id_getter(self):
        task = Task(0, "Zero'th task")
        assert task.task_id == 0

    def test_task_id_immutability(self):
        task = Task(1, "First task")
        with pytest.raises(AttributeError):
            task.task_id = 2

    def test_default_date_created(self):
        task = Task(2, "Second task")
        assert task.date_created == date.today()

from datetime import date


class Task:
    def __init__(self, task_id: int, title: str, date_created: date | None = None, done: bool = False) -> None:
        self.__task_id = task_id
        self.title = title
        self.done = done

        if date_created is None:
            self.__date_created = date.today()
        else:
            self.__date_created = date_created

    @property
    def task_id(self):
        return self.__task_id

    @property
    def date_created(self):
        return self.__date_created

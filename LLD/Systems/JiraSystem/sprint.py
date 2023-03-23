
class Sprint:

    def __init__(self, begin, end, name=''):
        self._tasks = []
        self.begin = begin
        self.end = end
        self.name = name

    def add_tasks(self, task):
        self._tasks.append(task)

    def remove_tasks(self, task):
        for index, _task in enumerate(self._tasks):
            if _task == task:
                del self._tasks[index]
                return True
        return False

    def print_details(self):
        print(self)

    def __str__(self):
        return f'Sprint: {self.name} is starting from {self.begin} and ending on {self.end}'

    def __eq__(self, other):
        if self.begin == other.begin and self.end == other.end and self.name == other.name:
            return True
        return False

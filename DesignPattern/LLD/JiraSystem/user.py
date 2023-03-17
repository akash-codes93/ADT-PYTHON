import uuid
from task import Task
from sprint import Sprint

class User:

    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())
        self.task_list = []
        self.sprint_list = []

    def create_task(self, task_type, subtract=None):
        task = Task(task_type)
        task.subtract = subtract
        task.user = self
        self.task_list.append(task)
        return task

    def create_sprint(self, begin, end, name=''):
        sprint = Sprint(begin, end, name)
        self.sprint_list.append(sprint)
        return sprint

    def add_to_sprint(self, sprint, task):
        # check if the sprint is created by the user
        found = False
        for _sprint in self.sprint_list:
            if sprint == _sprint:
                found = True

        if not found:
            return False

        sprint.add_tasks(task)
        return True

    def remove_from_sprint(self, sprint, task):
        for _sprint in self.sprint_list:
            if sprint == _sprint:
                if sprint.remove_tasks(task):
                    return True
        return False

    def change_status(self, task, status):
        for _task in self.task_list:
            if _task == task:
                task.status = status
                return True
        return False

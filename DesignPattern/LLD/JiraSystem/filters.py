from abc import ABC, abstractmethod


class Specification(ABC):

    @abstractmethod
    def is_satisfied(self, task):
        pass


class Filter(ABC):

    @abstractmethod
    def filter(self, tasks, spec):
        pass


class UserSpecification(Specification):

    def __init__(self, user):
        self.user = user

    def is_satisfied(self, task):
        if task.user == self.user:
            return True
        else:
            return False


class DelayedSpecification(Specification):

    def is_satisfied(self, task):
        if task.is_delayed:
            return True
        else:
            return False


class TaskFilter(Filter):

    def filter(self, tasks, spec):
        for task in tasks:
            if spec.is_satisfied(task):
                yield task

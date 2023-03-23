import uuid
from abc import ABC, abstractmethod
from enum import Enum


class TaskStatus(Enum):
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    DELAYED = 'delayed'


class TaskType(Enum):
    STORY = 'story'
    FEATURE = 'feature'
    BUG = 'bug'


class Task(ABC):

    def __init__(self, task_type):
        self._status = TaskStatus.NOT_STARTED
        self._user = None
        self.id = uuid.uuid4()
        self.task_type = task_type

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    def __eq__(self, other):
        if self.id == other.id:
            return True
        return False


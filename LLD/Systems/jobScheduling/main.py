from enum import Enum


class UserType(Enum):
    Root = 0
    Admin = 1
    User = 2

    def __lt__(self, other):
        return self.value > other.value

    def __gt__(self, other):
        return self.value < other.value


class Priority(Enum):
    P0 = 0
    P1 = 1
    P2 = 2

    def __lt__(self, other):
        return self.value > other.value

    def __gt__(self, other):
        return self.value < other.value


class Job:

    def __init__(self, name, duration, priority, deadline, usertype):
        self.name = name
        self.duration = duration
        self.priority = priority
        self.deadline = deadline
        self.usertype = usertype


class Jobs(list):
    pass


class JobScheduler:

    @staticmethod
    def create_schedule(threads):
        schedule = {}
        for i in range(threads):
            schedule[i] = []
        return schedule

    @staticmethod
    def process_threads(thread_process):
        p = min(thread_process)
        for i in range(len(thread_process)):
            thread_process[i] -= p

    def common_schedule_logic(self, jobs, threads):
        thread_process = [0] * threads
        schedule = self.create_schedule(threads)

        while jobs:
            for i in range(threads):
                if thread_process[i] == 0:
                    job = jobs.pop(0)
                    thread_process[i] += job.duration
                    schedule[i].append(job.__dict__)

            self.process_threads(thread_process)
        return schedule

    def shortest_job_first(self, jobs, threads):
        jobs = sorted(jobs, key=lambda job: (job.duration, job.priority))
        return self.common_schedule_logic(jobs, threads)

    def first_come_first_serve(self, jobs, threads):
        return self.common_schedule_logic(jobs, threads)


def driver():
    j1 = Job("j1", 10, Priority.P0, 12, UserType.Root)
    j2 = Job("j2", 4, Priority.P1, 5, UserType.Root)
    j3 = Job("j3", 1, Priority.P0, 3, UserType.Root)
    j4 = Job("j4", 10, Priority.P0, 5, UserType.Root)
    j5 = Job("j5", 1, Priority.P0, 2, UserType.Root)

    print(UserType.Root < UserType.Admin)

    jobs = Jobs([j1, j2, j3, j4, j5])
    #
    scheduler = JobScheduler()
    schedule = scheduler.shortest_job_first(jobs, 3)
    #
    print(schedule)


driver()

"""
Priority Queue could be used but custom comparator not present
"""
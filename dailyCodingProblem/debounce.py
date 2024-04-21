"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""


import threading
import heapq
import time


class Scheduler():

    def __init__(self):
        self.functions = []

        thread = threading.Thread(target=self.execute)
        thread.start()
        # self.execute()

    def execute(self):

        while True:
            curr_time = time.time() * 1000
            if len(self.functions) > 0:
                t, f, name = self.functions[0]
                if t <= curr_time:
                    f(name)
                    heapq.heappop(self.functions)

            time.sleep(0.01)

    def schedule(self, f, n: int, name):
        time_to_execute = time.time() * 1000 + n
        heapq.heappush(self.functions, (time_to_execute, f, name))


def f1(name):
    print("code executed: ", name)


scheduler = Scheduler()

scheduler.schedule(f1, 10, 10)
scheduler.schedule(f1, 2, 2)
scheduler.schedule(f1, 5, 5)
scheduler.schedule(f1, 3, 3)
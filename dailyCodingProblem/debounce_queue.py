"""
below example will fail if there are two consumer threads running
could potentially lead to a deadlock
"""

import threading
import time
import random


class BoundedQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.condition = threading.Condition()

    def produce(self, item):
        with self.condition:
            while len(self.queue) >= self.capacity:
                print("Queue full, producer is waiting...")
                self.condition.wait()

            self.queue.append(item)
            print(f"Produced: {item}")
            self.condition.notify()  # Notify one consumer

    def consume(self):
        with self.condition:
            while not self.queue:
                print("Queue empty, consumer is waiting...")
                self.condition.wait()

            item = self.queue.pop(0)
            print(f"Consumed: {item}")
            self.condition.notify()  # Notify one producer
            return item


# Producer thread
def producer(q):
    for i in range(10):
        q.produce(i)
        time.sleep(random.uniform(1, 60))


# Consumer thread
def consumer(q):
    for _ in range(10):
        q.consume()
        time.sleep(random.uniform(0.1, 0.6))


if __name__ == "__main__":
    queue = BoundedQueue(capacity=3)
    t1 = threading.Thread(target=producer, args=(queue,))
    t2 = threading.Thread(target=consumer, args=(queue,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

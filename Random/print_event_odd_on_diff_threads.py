# import asyncio
#
# loop = asyncio.new_event_loop()
#
# task1 = loop.create_task(cor)
#
# loop.run_until_complete(asyncio.wait([task1]))
#
# task1.result()
#
# loop.close()

import threading


event_even = threading.Event()
event_odd = threading.Event()


def print_even():

    for i in range(0, 30, 2):
        print("Thread 1: ", i)

        event_odd.set()
        event_even.clear()
        event_even.wait()

    event_odd.set()


def print_odd():
    event_odd.wait()

    for i in range(1, 30, 2):
        print("Thread 2: ", i)

        event_even.set()
        event_odd.clear()
        event_odd.wait()

    event_even.set()


if __name__ == "__main__":

    t1 = threading.Thread(target=print_even)
    t2 = threading.Thread(target=print_odd)

    t1.start()
    t2.start()

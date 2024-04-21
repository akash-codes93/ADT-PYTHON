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


if __name__ == "__main__":

    t1 = threading.Thread(target=print_even)
    t2 = threading.Thread(target=print_odd)

    t1.start()
    t2.start()

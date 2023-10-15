import threading


# class Singleton(type):
#     """ Metaclass that creates a Singleton base type when called. """
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls)\
#                 .__call__(*args, **kwargs)
#         return cls._instances[cls]

class Singleton(type):
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # double-checking for instance not created
        if cls._instance is None:  # cls._instance could be overload by __bool__
            with cls._lock:
                # Another thread could have created the instance
                # before we acquired the lock. So check that the
                # instance is still nonexistent.
                if not cls._instance:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')





if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


"""
Since implementing a singleton is easy, you have a different challenge: write a function called is_singleton() .
This method takes a factory method that returns an object and it's up to you to determine whether or not that object is a singleton instance.
"""


def is_singleton(factory):
    f1 = factory()
    f2 = factory()

    return f1 == f2

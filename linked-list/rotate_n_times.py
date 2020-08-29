"""
in/p : 10, 20, 30, 40, 50, 60
k = 4
o/p : 50, 60, 10, 20, 30, 40
"""
from typing import Union


class Node:

    def __init__(self, value, _next=None):

        if not isinstance(_next, Node):
            if _next is not None:
                raise ValueError('_next should be node/ None type')

        self.value = value
        self.next = _next


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):

        if isinstance(value, Node):
            node = value
        else:
            node = Node(value)

        if self.head is None:

            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_nodes(self, values):

        if not isinstance(values, list):
            raise TypeError('values must be a list type')

        for value in values:
            self.add_node(value)

    def __iter__(self):
        self.travel = self.head
        return self

    def __next__(self):

        if self.travel is not None:
            previous = self.travel
            self.travel = self.travel.next

            return previous
        else:
            raise StopIteration


def rotate_n_times(head: Node, k: int) -> Union[Node, None]:

    travel = head

    while travel.next is not None:
        travel = travel.next

    travel.next = head

    new_travel = head

    while k != 1:
        new_travel = new_travel.next
        k -= 1

    new_head = new_travel.next

    new_travel.next = None

    return new_head


def driver():

    ll = SingleLinkedList()

    ll.add_nodes([10, 20, 30])

    new_head = rotate_n_times(ll.head, 1)
    ll.head = new_head

    print("o/p: ", end=' ')

    for node in ll:
        print(node.value, end='->')


if __name__ == '__main__':
    driver()

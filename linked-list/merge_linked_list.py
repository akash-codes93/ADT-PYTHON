"""
This code is to show to merge two linked list
l1: 1 -> 2 -> 3 -> 4
l2: 2 -> 8 -> 9
o/p: 1 -> 2 -> 2 -> 8 -> 3 -> 9 -> 4
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


def merge_lists(l1: Node, l2: Node) -> Union[Node, None]:

    travel = l1
    travel_2 = l2

    if travel is None:
        return travel_2
    elif travel_2 is None:
        return travel

    while (travel is not None) and (travel_2 is not None):

        p = travel.next
        k = travel_2.next

        travel.next = travel_2
        if p is not None:
            travel_2.next = p

        travel = p
        travel_2 = k

    return l1


def driver():
    l1 = SingleLinkedList()
    l2 = SingleLinkedList()

    l1.add_nodes([1])
    l2.add_nodes([5, 6, 7, 8])

    merge_lists(l1.head, l2.head)

    for node in l1:
        print(node.value, end=' -> ')


if __name__ == '__main__':
    driver()
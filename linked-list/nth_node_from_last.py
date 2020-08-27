"""
To find the nth node from last in linked list
Approach1: find the len of linked-list and subtract n from it
            node from start len - n + 1
Approach2: reverse the linked list and find the nth list
"""
from typing import Union


class Node:

    def __init__(self, value, _next=None):

        self.value = value

        if not isinstance(_next, Node):
            if _next is not None:
                raise ValueError("next just be node type")

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
            raise ValueError('values must be list type')

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


def reverse(head: Node) -> Union[Node, None]:
    travel = head
    previous = head

    if travel is None:
        return None

    elif travel.next is None:
        return travel

    travel = travel.next

    while travel is not None:
        p = travel.next

        travel.next = previous
        previous = travel

        travel = p

    head.next = None
    return previous


def get_nth_from_last(head: Node, n: int) -> Node:
    new_head = reverse(head)
    travel = new_head

    count = 1

    while (count != n) and (travel is not None):
        travel = travel.next
        count += 1

    if travel is None:
        return Node(-1)

    return travel


def driver():
    ll = SingleLinkedList()

    ll.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])

    node = get_nth_from_last(ll.head, 5)

    print("o/p: ", node.value)


if __name__ == '__main__':
    driver()

"""
Skip m nodes and then delete m nodes
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


def delete_m_after_n(head: Node, m: int, n: int) -> Union[Node, None]:
    m_count = m
    n_count = n

    travel = head

    if travel is None:
        return travel

    while travel is not None:

        while m_count > 1:
            travel = travel.next
            m_count -= 1

        m_node = travel

        while n_count > 0:
            travel = travel.next
            n_count -= 1

        n_node = travel

        m_node.next = n_node.next

        travel = travel.next

        m_count = m
        n_count = n

    return head


def driver():
    ll = SingleLinkedList()
    ll.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    new_head = delete_m_after_n(ll.head, 1, 1)

    ll.head = new_head
    print('o/p: ', end='')
    for node in ll:
        print(node.value, end=' -> ')


if __name__ == '__main__':
    driver()

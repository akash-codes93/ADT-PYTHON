"""
To check if a linked list is palindrome
app1 : use stack
app2: find middle -> reverse from middle to end  -> check
"""

from typing import Union


class Node:

    def __init__(self, value, _next=None):

        if not isinstance(_next, Node):
            if _next is not None:
                raise ValueError('_next must be node/node type')

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
            raise ValueError("values must be list type")

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


def find_middle(head: Node) -> Node:
    travel = head
    travel_prev = head

    while travel is not None:

        if travel.next is None:
            travel = travel.next

        elif travel.next.next is None:
            travel = travel.next

            if travel != head:
                travel_prev = travel_prev.next
        else:
            travel = travel.next.next
            travel_prev = travel_prev.next

    return travel_prev


def reverse(head: Node) -> Union[Node, None]:
    travel = head
    travel_prev = head

    if travel is None:
        return None

    if travel.next is None:
        return travel

    travel = travel.next

    while travel is not None:
        p = travel.next

        travel.next = travel_prev

        travel_prev = travel
        travel = p

    head.next = None

    return travel_prev


def check_palindrome(head: Node) -> bool:
    status = True

    middle_node = find_middle(head)

    new_head = reverse(middle_node)

    travel = head
    travel_other = new_head

    p = new_head
    while p.next is not None:
        p = p.next

    while (travel is not None) and (travel != p):

        if travel.value != travel_other.value:
            status = False
            break

        travel = travel.next
        travel_other = travel_other.next

    return status


def driver():
    ll = SingleLinkedList()

    ll.add_nodes([3, 3, 1, 3, 3])

    print(check_palindrome(ll.head))

    # newhead = reverse(ll.head)
    # ll.head = newhead
    #
    # for node in ll:
    #     print(node.value)


if __name__ == '__main__':
    driver()

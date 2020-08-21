class Node:

    def __init__(self, value, _next=None):

        if not isinstance(_next, Node):
            if _next is not None:
                raise ValueError("Node must be node type/ None")

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

    def delete_middle(self):
        first = self.head
        second = self.head

        while first is not None:

            if first.next is None:
                """Last node reached"""
                first = first.next

            elif first.next.next is None:
                """jump by one node"""

                first = first.next

                if first != self.head:
                    """Case check if there are only two nodes in the linked list"""
                    second = second.next
            else:
                """Jump by two node"""
                first = first.next.next
                second = second.next

        middle = second
        first = self.head
        while (first.next != middle) and (first.next is not None):
            first = first.next

        if middle == self.head:
            """Case two cover if there is only one node in the linked list"""
            self.head = None
        else:
            first.next = middle.next


def delete_middle_elem():
    import random

    for _ in range(0, 10):
        no_of_values = random.randint(1, 3)
        node_values = [random.randint(0, 99) for __ in range(0, no_of_values)]

        print("Node values -- ", node_values)
        linked_list = SingleLinkedList()
        linked_list.add_nodes(node_values)

        linked_list.delete_middle()

        print('Output: ', end=' ')
        for node in linked_list:
            print(node.value, end=' -> ')

        print(end='\n')


if __name__ == '__main__':
    delete_middle_elem()

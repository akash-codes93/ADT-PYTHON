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


def reverse_list(head_node: Node):

    travel = head_node
    previous = None

    if travel is None:
        return travel

    if travel.next is None:
        return travel

    while travel is not None:
        p = travel.next

        travel.next = previous
        previous = travel

        travel = p

    return previous


def driver():
    import random

    for _ in range(0, 10):
        no_of_values = random.randint(0, 20)
        node_values = [random.randint(0, 99) for __ in range(0, no_of_values)]

        print("Node values -- ", node_values)
        linked_list = SingleLinkedList()
        linked_list.add_nodes(node_values)

        new_head = reverse_list(linked_list.head)

        linked_list.tail = linked_list.head
        linked_list.head = new_head

        print('Output: ', end=' ')
        for node in linked_list:
            print(node.value, end=' -> ')

        print(end='\n')


if __name__ == '__main__':

    driver()

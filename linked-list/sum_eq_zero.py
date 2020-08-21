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

        if not isinstance(value, Node):
            node = Node(value)
        else:
            node = value

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_nodes(self, values):

        if not isinstance(values, list):
            return ValueError('Values must be a list type')

        for value in values:
            self.add_node(value)

    def __iter__(self):
        self.travel = self.head
        return self

    def __next__(self):

        if self.travel is not None:
            release = self.travel
            self.travel = self.travel.next

            return release
        else:
            raise StopIteration


class Stack(SingleLinkedList):

    def __init__(self):

        super(Stack, self).__init__()

    def add_node(self, value):

        if not isinstance(value, Node):
            node = Node(value)
        else:
            node = value

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):

        node = self.head
        self.head = self.head.next

        return node


def driver():
    single_linked_list = SingleLinkedList()
    # single_linked_list.add_nodes([6, -6, 8, 4, -12, 9, 8, -8])
    single_linked_list.add_nodes([4, 6, -10, 8, 9, 10, -19, 10, -18, 20, 25])

    stack = Stack()

    for node in single_linked_list:

        if node.value >= 0:
            stack.add_node(node.value)
        else:
            _sum = -1 * node.value
            while _sum > 0:
                np = stack.pop()

                _sum -= np.value

    single_linked_list.head = None

    for node in stack:
        single_linked_list.add_node(node.value)

    # printing the output
    for node in single_linked_list:
        print(node.value)


if __name__ == '__main__':
    driver()

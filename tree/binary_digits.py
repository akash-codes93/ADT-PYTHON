class Node:

    def __init__(self, value, _next=None):
        if value not in [0, 1]:
            raise ValueError('Value can be 0/1')
        self.value = value
        self.next = _next


class SingleLinkedList:

    def __init__(self):

        self.has_head = False
        self.head_node = None

    def add_node(self, value):

        node = Node(value)

        if not isinstance(node, Node):
            raise ValueError('Node must a node type')

        if self.has_head is False:

            self.head_node = node
            self.has_head = True

        else:
            prev_node = None

            for current_node in self:
                prev_node = current_node

            prev_node.next = node

    def add_nodes(self, values):

        if not isinstance(values, list):
            return ValueError('Values must be a list type')

        for value in values:
            self.add_node(value)

    def __iter__(self):
        self.travel = self.head_node
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

        node = Node(value)

        if self.has_head is False:
            self.head_node = node
            self.has_head = True

        else:
            node.next = self.head_node
            self.head_node = node


if __name__ == '__main__':
    linked_list = SingleLinkedList()

    linked_list.add_nodes([1, 0, 1, 1, 0])
    stack = Stack()

    for node1 in linked_list:
        # print(node1.value)
        stack.add_node(node1.value)

    number = 0
    count = 0
    for node1 in stack:
        # print(node1.value)
        number += pow(2, count)*node1.value
        count += 1

    print(number)

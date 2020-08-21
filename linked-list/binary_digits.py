class Node:

    def __init__(self, value, _next=None):
        # if value not in [0, 1]:
        #     raise ValueError('Value can be 0/1')
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

        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            node.next = self.head
            self.head = node


def binary_digit_to_number():
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
        number += pow(2, count) * node1.value
        count += 1

    print(number)


class SingleMiddleList(SingleLinkedList):

    def __init__(self):
        super(SingleMiddleList, self).__init__()

    def find_middle(self):
        """
        One pointer will move by one and other by two
        This code will not work in case of two nodes
        inp: 1 -> 2
        out: 2
        expected: 1
        ----------------
        update the issue has been fixed
        :return:
        """

        travel = self.head
        travel_prev = self.head

        while travel is not None:

            if travel.next is None:
                """Last node reached"""
                travel = travel.next

            elif travel.next.next is None:
                """jump by one node"""
                travel = travel.next

                if travel != self.head:
                    """Two cover if the linked list has only two nodes"""
                    travel_prev = travel_prev.next
            else:
                """Jump by two node"""
                travel = travel.next.next
                travel_prev = travel_prev.next

        return travel_prev


def middle_number_of_list(approach=2):
    if approach == 1:
        """approach count the total and divide by 2"""
        linked_list = SingleLinkedList()

        linked_list.add_nodes([1, 0, 1, 1, 0, 0, 0, 1])
        count = 0
        for _ in linked_list:
            count += 1

        middle = int(count/2)
        for cnt, node in enumerate(linked_list):
            if cnt == middle:
                print(node.value)

    elif approach == 2:
        import random

        for _ in range(0, 10):
            no_of_values = random.randint(0, 20)
            node_values = [random.randint(0, 99) for __ in range(0, no_of_values)]

            print("Node values -- ", node_values)
            linked_list = SingleMiddleList()
            linked_list.add_nodes(node_values)

            middle_node = linked_list.find_middle()
            if middle_node is None:
                print("This linked list is empty")
            else:
                print("Middle value - ", middle_node.value)


if __name__ == '__main__':

    # binary_digit_to_number()

    middle_number_of_list(1)

class Node:

    def __init__(self, value, _next=None, down=None):

        self.value = value
        self.next = _next
        self.down = down


class LinkedList:

    def __init__(self):
        self.head = None

    @staticmethod
    def add_node(value, prev_node, alignment):

        if not isinstance(value, Node):
            node = Node(value)
        else:
            node = value

        if not isinstance(prev_node, Node):
            raise ValueError('Prev node must be node type')

        if alignment not in ('next', 'down'):
            raise ValueError('Alignment can be next/down')

        if alignment == 'next':
            if prev_node.next is None:
                prev_node.next = node
            else:
                node.next = prev_node.next
                prev_node.next = node
        else:
            if prev_node.down is None:
                prev_node.down = node
            else:
                node.down = prev_node.down
                prev_node.down = node

    def __iter__(self):

        if self.alignment == 'next':

            while self.travel is not None:
                release = self.travel
                self.travel = self.travel.next

                yield release

        else:
            while self.travel is not None:
                release = self.travel
                self.travel = self.travel.down

                yield release

    def __call__(self, node, alignment):
        self.travel = node

        if alignment not in ('next', 'down'):
            raise ValueError('Alignment can be next/down')

        self.alignment = alignment

        return self

    def assign_head(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        self.head = node


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


def create_linked_list():

    linked_list = LinkedList()

    node_a = Node(5)
    node_a_1 = Node(7)
    node_a_2 = Node(8)
    node_a_3 = Node(30)

    node_b = Node(10)
    node_b_1 = Node(20)

    node_c = Node(19)
    node_c_1 = Node(22)
    node_c_2 = Node(50)

    node_d = Node(28)
    node_d_1 = Node(35)
    node_d_2 = Node(40)
    node_d_3 = Node(45)

    linked_list.add_node(node_a_1, node_a, 'down')
    linked_list.add_node(node_a_2, node_a_1, 'down')
    linked_list.add_node(node_a_3, node_a_2, 'down')

    linked_list.add_node(node_b_1, node_b, 'down')

    linked_list.add_node(node_c_1, node_c, 'down')
    linked_list.add_node(node_c_2, node_c_1, 'down')

    linked_list.add_node(node_d_1, node_d, 'down')
    linked_list.add_node(node_d_2, node_d_1, 'down')
    linked_list.add_node(node_d_3, node_d_2, 'down')

    linked_list.add_node(node_b, node_a, 'next')
    linked_list.add_node(node_c, node_b, 'next')
    linked_list.add_node(node_d, node_c, 'next')

    linked_list.assign_head(node_a)

    # un-comment below to print the linked list from a given node 'down' and 'next'
    # for node in linked_list(linked_list.head, 'next'):
    #     print(node.value)
    return linked_list


def flatten(linked_list):
    """
    Learnings: 1.) Two for loops for the same class objects is not possible
    because we use the instance variable to iterate and they get re-initialized
    for the next loop.
    2.) iterator without using the next method. call() is used and yield is placed
    inside the iter
    3.) Mutable object passed as parameter in a function so do not pass node as parameter
    instead pass value of node as parameter
    :param linked_list:
    :return:
    """

    single_linkedlist = SingleLinkedList()

    for node in linked_list(linked_list.head, 'down'):
        single_linkedlist.add_node(node.value)

    for node in linked_list(linked_list.head.next, 'next'):

        travel = single_linkedlist.head
        prev = travel

        sub_node = node

        while sub_node is not None:

            while travel is not None:

                if sub_node.value < travel.value:
                    break

                prev = travel
                travel = travel.next

            new_node = Node(sub_node.value)
            if travel is None:
                prev.next = new_node
            else:
                new_node.next = prev.next
                prev.next = new_node
            # because the list is sorted the next values will always be greater
            travel = new_node
            # travel down
            sub_node = sub_node.down

    for node in single_linkedlist:
        print(node.value, end='->')


if __name__ == '__main__':
    structure = create_linked_list()
    flatten(structure)

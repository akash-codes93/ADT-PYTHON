"""
This code will drop duplicates in a linked list
"""


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
            raise ValueError('Values must be a list type')

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


def remove_duplicates(head_node: Node):
    """
    To remove duplicates
    :param head_node: Node
    :return:
    """
    travel = head_node
    previous = head_node

    if travel.next is None:
        return head_node
    else:

        travel = travel.next

        while travel is not None:

            if travel.value != previous.value:
                previous.next = travel

                previous = travel
                travel = travel.next
            else:
                travel = travel.next

        previous.next = None

    return head_node


def driver():
    """
    This function will drive the code
    :return:
    """
    single_linked_list = SingleLinkedList()
    # single_linked_list.add_nodes([2, 2, 4, 5])
    # single_linked_list.add_nodes([2, 2, 2, 2, 2])
    # single_linked_list.add_nodes([1, 2, 2, 2, 3, 3])
    # single_linked_list.add_nodes([1, 2, 2, 2, 3, 3, 4])
    single_linked_list.add_nodes([1, 2, 3, 4, 5, 6, 7])

    print('Input: ', end=' ')
    for node in single_linked_list:
        print(node.value, end=' -> ')
    print()

    remove_duplicates(single_linked_list.head)

    print('Output: ', end=' ')
    for node in single_linked_list:
        print(node.value, end=' -> ')


if __name__ == '__main__':
    driver()

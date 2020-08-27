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


def reverse_list(head_node):

    if head_node is None:
        return None

    travel = head_node
    previous = head_node

    if head_node.next is None:
        return head_node

    travel = travel.next

    while travel is not None:
        p = travel.next

        travel.next = previous

        previous = travel
        travel = p

    head_node.next = None
    return previous


def add_one_to_list(head_node):

    new_node = reverse_list(head_node)

    travel = new_node
    previous = new_node
    carry = 1

    while travel is not None:

        _sum = travel.value + carry

        if _sum > 9:
            travel.value = 0
            carry = 1
        else:
            travel.value = _sum
            carry = 0

        previous = travel
        travel = travel.next

    if carry == 1:
        previous.next = Node(carry)

    new_node = reverse_list(new_node)

    return new_node


def driver():
    import random

    for _ in range(0, 10):
        no_of_values = random.randint(0, 20)
        node_values = [random.randint(1, 9) for __ in range(0, no_of_values)]

        print("Node values -- ", node_values)
        linked_list = SingleLinkedList()
        linked_list.add_nodes(node_values)

        new_head = add_one_to_list(linked_list.head)
        linked_list.head = new_head

        print('Output: ', end=' ')
        for node in linked_list:
            print(node.value, end=' -> ')

        print(end='\n')


if __name__ == '__main__':
    driver()

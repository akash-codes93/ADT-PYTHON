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


def remove_last_occurrence(head: Node, value):
    travel = head
    occurrence_node_prev = None

    if travel is None:
        return None

    if travel.next is None:

        if travel.value == value:
            return None
        else:
            return travel

    while travel.next is not None:

        if travel.next.value == value:
            occurrence_node_prev = travel

        travel = travel.next

    # check for first node as last occurrence e.g. 2, 1, 3, 4
    if head.value == value:
        head = head.next
        return head

    if occurrence_node_prev is not None:
        occurrence_node_prev.next = occurrence_node_prev.next.next

    return head


def driver():
    ll = SingleLinkedList()

    ll.add_nodes([1, 1, 2, 3, 4, 2])

    new_head = remove_last_occurrence(ll.head, 2)
    ll.head = new_head

    for node in ll:
        print(node.value)


if __name__ == '__main__':
    driver()
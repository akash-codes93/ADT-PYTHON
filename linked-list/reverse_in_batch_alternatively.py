"""
This will reverse the linked list
in groups of given sizes
k=3
i/n: 1 -> 2 -> 3 -> 4 -> 5
o/p: 3 -> 2 -> 1 -> 5 -> 4
"""


class Node:

    def __init__(self, value, _next=None):

        if not isinstance(_next, Node):
            if _next is not None:
                raise ValueError('_next can only be None/ node')

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


def reversing(start, end):
    if start.next is None:
        return start

    previous = start
    start = start.next

    previous.next = end

    while start != end:
        p = start.next
        start.next = previous

        previous = start
        start = p

    return previous


def reverse_in_alt_batch(head: Node, batch_size: int):
    k = batch_size
    travel = head
    previous = head

    new_head = head

    alt = 1

    batch_end_node = []

    # empty linked list
    if travel is None:
        return None

    # single node linked list
    if travel.next is None:
        return head

    while k > 0 and travel is not None:

        # second condition in below "if" is because if last batch does not have full batch size
        if (k == 1) or (travel.next is None):

            # reverse each batch
            if alt == 1:

                # this is to maintain the start and end of each batch so that they can be linked together
                batch_end_node.append([travel, previous])
                travel = travel.next

                # so that only the alt batch get reversed
                sub_head = reversing(previous, travel)

                # to get the new head
                if previous == head:
                    new_head = sub_head

            else:
                # start and end remains the same
                batch_end_node.append([previous, travel])
                travel = travel.next

            previous = travel
            k = batch_size
            alt = alt * -1
        else:
            travel = travel.next
            k -= 1

    for count, batch in enumerate(batch_end_node):
        if count+1 == len(batch_end_node):
            batch[1].next = None
        else:
            batch[1].next = batch_end_node[count+1][0]

    return new_head


def driver():
    # ll = SingleLinkedList()
    # nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #
    # ll.add_nodes(nodes)
    #
    # print("Input: ", end='')
    # for node in ll:
    #     print(node.value, end=" -> ")
    #
    # print()
    # head = reverse_in_batch(ll.head, 3)
    # ll.head = head
    #
    # print("Output: ", end='')
    # for node in ll:
    #     print(node.value, end=" -> ")

    import random

    for _ in range(0, 10):
        no_of_values = random.randint(0, 10)
        node_values = [random.randint(1, 9) for __ in range(0, no_of_values)]

        print("Node values -- ", node_values)
        linked_list = SingleLinkedList()
        linked_list.add_nodes(node_values)

        head = reverse_in_alt_batch(linked_list.head, 3)
        linked_list.head = head

        print('Output: ', end=' ')
        for node in linked_list:
            print(node.value, end=' -> ')

        print(end='\n')


if __name__ == '__main__':
    driver()

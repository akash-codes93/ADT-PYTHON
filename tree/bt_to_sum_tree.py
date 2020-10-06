"""
convert the binary tree to its sum tree
"""
from typing import Union


class Node:

    def __init__(self, value, left=None, right=None):

        for pointer in [left, right]:

            if not isinstance(pointer, Node):
                if pointer is not None:
                    raise ValueError("left/right node must a Node/None type")

        self.value = value
        self.left = left
        self.right = right


class BT:

    def __init__(self):

        self.head = None

    def add_node(self, value):

        if isinstance(value, Node):
            node = value
        else:
            node = Node(value)

        if self.head is None:
            self.head = node
        else:
            for each_node in self:
                if each_node.left is None:
                    each_node.left = node
                    break
                elif each_node.right is None:
                    each_node.right = node
                    break

    def add_nodes(self, values):

        if not isinstance(values, list):
            raise ValueError('Values must be list')

        for value in values:
            self.add_node(value)

    def __iter__(self):

        self.queue = [self.head]
        return self

    def __next__(self):

        if self.queue:

            node = self.queue.pop(0)

            if node.left is not None:
                self.queue.append(node.left)

            if node.right is not None:
                self.queue.append(node.right)

            return node

        else:
            raise StopIteration


def binary_to_sum(node: Union[Node, None]) -> int:
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return node.value

    value = binary_to_sum(node.left) + binary_to_sum(node.right)

    node.value = value

    return 2 * value


def driver():
    # bt = BT()
    # bt.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    # binary_to_sum(bt.head)

    # print("Values after converting to sum tree - ")

    # for node in bt:
    #     print(node.value, end=' -> ')

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    binary_to_sum(root)
    print("Values after converting to sum tree - ")

    print(root.value)
    print(root.left.value)
    print(root.right.value)
    print(root.left.right.value)
    print(root.right.left.value)
    print(root.right.right.value)
    print(root.right.left.left.value)
    print(root.right.left.right.value)


if __name__ == '__main__':
    driver()

"""
to find out if two nodes are cousins or not
"""
from typing import Union


class Node:

    def __init__(self, value, left=None, right=None):

        for pointer in [left, right]:
            if pointer is not None:
                raise ValueError("left/right should be Node/None")

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


def check_if_cousins(head: Union[Node, None], node1: int, node2: int) -> bool:

    queue1 = [head]
    queue2 = []

    status_brother = True
    status_level = False

    while queue1:
        node = queue1.pop(0)

        if node.left.value == node1 and node.right.value == node2:
            status_brother = False
        elif node.right.value == node1 and node.left.value == node2:
            status_brother = False
            break

        if node.left is not None:
            queue2.append(node.left)

        if node.right is not None:
            queue2.append(node.right)

        if len(queue1):
            if node1 in queue2 and node2 in queue2:
                status_level = True
            queue1 = queue2

    if status_brother is False:
        return False
    else:
        if status_level is False:
            return False

    return True


def driver():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if check_if_cousins(root, 5, 1):
        print("Given nodes are cousins")
    else:
        print("Given nodes are not cousins")


if __name__ == '__main__':
    driver()


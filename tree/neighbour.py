"""
Code to find the next node at same level
"""


class Node:

    def __init__(self, value, left=None, right=None):

        for pointer in [left, right]:

            if not isinstance(pointer, Node):
                if pointer is not None:
                    raise ValueError("Left/ right can be Node/ None")

        self.value = value
        self.left = left
        self.right = right


def find_right_neighbour(head, value):

    queue1 = [head]

    queue2 = []

    while queue1:
        node = queue1.pop(0)

        if node.value == value:
            try:
                new_node = queue1.pop(0)
            except IndexError:
                return None
            return new_node
        else:
            if node.left is not None:
                queue2.append(node.left)

            if node.right is not None:
                queue2.append(node.right)

        if len(queue1) == 0:
            queue1 = queue2

    return None


def driver():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    node = find_right_neighbour(root, 6)

    if node is None:
        print("Right neighbour: does not exists")
    else:
        print("Right neighbour: ", node.value)


if __name__ == '__main__':
    driver()

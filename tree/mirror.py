"""
Check if a node is a mirror
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


def check_mirror(left_node, right_node):

    if left_node is None and right_node is None:
        return True

    if left_node.value == right_node.value:

        if (left_node.left is None and right_node.right is not None) or (left_node.left is not None and right_node.right is None):
            return False

        if (left_node.right is None and right_node.left is not None) or (left_node.right is not None and right_node.left is None):
            return False

        if check_mirror(left_node.left, right_node.right) and check_mirror(left_node.right, right_node.left):
            return True

    return False


def driver():
    bt = BT()
    bt.add_nodes([1, 2, 2, 3, 4, 4, 3])

    # print("Level order traversal: ", end=" ")
    # for node in bt:
    #     print(node.value, end=" -> ")
    print(check_mirror(bt.head.left, bt.head.right))


if __name__ == '__main__':
    driver()

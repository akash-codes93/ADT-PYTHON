"""
Code to print the top view of the tree
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


def top_view(node, dist, level, _dict=None):

    if _dict is None:
        _dict = {}

    if node is None or node.value is None:
        return

    if dist in _dict:
        if level not in _dict[dist]:
            _dict[dist][level] = []

    else:
        _dict[dist] = {}
        _dict[dist][level] = []

    _dict[dist][level].append(node.value)

    top_view(node.left, dist-1, level+1, _dict)
    top_view(node.right, dist+1, level+1, _dict)


def driver():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    _dict = {}
    top_view(root, 0, 0, _dict)

    print("Top view: ", end=" ")
    sorted_key = list(sorted(list(_dict.keys())))
    for key in sorted_key:
        sub_dict = _dict[key]
        max_key = min(list(sub_dict.keys()))

        print(sub_dict[max_key][0], end=" -> ")


if __name__ == '__main__':
    driver()

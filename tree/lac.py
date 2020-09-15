"""
The code is to find the least common ancestor
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

    def dfs(self, s, value, path=None):

        if path is None:
            path = []

        if s is None:
            return False

        path.append(s.value)

        if s.value == value:
            return True

        if (
            ((s.left is not None) and self.dfs(s.left, value, path))
            or
            ((s.right is not None) and self.dfs(s.right, value, path))
        ):
            return True

        path.pop()
        return False


def driver():
    bt = BT()
    bt.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print("Level order traversal: ", end=" ")
    for node in bt:
        print(node.value, end=" -> ")

    print()
    path1 = []
    bt.dfs(bt.head, 1, path1)
    print("Path1: ", end=" ")
    print(path1)

    path2 = []
    bt.dfs(bt.head, 8, path2)
    print("Path2: ", end=" ")
    print(path2)

    if path2 == [] or path1 == []:
        print("LAC: Nothing!")
        exit(0)

    i = 0
    min_len = min(len(path1), len(path2))

    while i < min_len:

        if path2[i] != path1[i]:
            break

        i += 1

    print()
    print("LAC: ", path1[i-1])


if __name__ == '__main__':
    driver()

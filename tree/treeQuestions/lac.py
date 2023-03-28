class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Lac:

    def get_node_path(self, root, value, path=None):

        if path is None:
            path = []

        path.append(root.value)

        if root.value == value:
            return True

        if root.left:
            if self.get_node_path(root.left, value, path):
                return True

        if root.right:
            if self.get_node_path(root.right, value, path):
                return True

        path.pop()

        return False

    def least_common_ancestor(self, root):
        pass


def driver():
    root = Node(1,
                Node(2,
                     Node(4), Node(5)),
                Node(3,
                     Node(6), Node(7))
                )

    path1 = []
    node1_present = Lac().get_node_path(root, 5, path1)

    path2 = []
    node2_present = Lac().get_node_path(root, 3, path2)
    print(path1, path2)

    if (not node1_present) or (not node2_present):
        print("Common ancestor not present")
    else:
        start = -1
        while True:
            start += 1
            if path1[start] != path2[start]:
                print(path1[start-1])
                break


driver()

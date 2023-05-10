
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs(root, path):

    if len(path) == 0:
        return True

    if len(path) != 0 and root is None:
        return False

    value = path.pop(0)

    if value == root.value:
        if dfs(root.left, path):
            return True

        if dfs(root.right, path):
            return True

    path.insert(0, value)
    return False


root1 = Node(1,
            Node(2,
                 Node(4, Node(8)), Node(5)),
            Node(3,
                 Node(6), Node(7))
            )


is_possible = dfs(root1, [1,2,4,8])
print(is_possible)


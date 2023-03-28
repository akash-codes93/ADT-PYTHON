class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class Traversal:

    def _dfs_utils(self, root, visited):

        print(root.value)

        if root.left and root.left not in visited:
            visited.add(root.left)
            self._dfs_utils(root.left, visited)

        if root.right and root.right not in visited:
            visited.add(root.right)
            self._dfs_utils(root.right, visited)

    def dfs(self, root):
        visited = {root}
        self._dfs_utils(root, visited)


a = TreeNode(8)
_root = TreeNode(1
                 ,
                 TreeNode(2,
                          TreeNode(4, a), TreeNode(5)
                          ),
                 TreeNode(3, a
                          #      # ,Node(6), Node(7)
                          )
                 )

Traversal().dfs(_root)

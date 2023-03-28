class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Traversal:

    def in_order(self, node):

        if node.left:
            self.in_order(node.left)

        print(node.value)

        if node.right:
            self.in_order(node.right)

    def pre_order(self, node):

        print(node.value)

        if node.left:
            self.pre_order(node.left)

        if node.right:
            self.pre_order(node.right)

    def post_order(self, node):

        if node.left:
            self.post_order(node.left)

        if node.right:
            self.post_order(node.right)

        print(node.value)


_root = TreeNode(1
                 ,
                 TreeNode(2,
                          TreeNode(4, TreeNode(8)), TreeNode(5)
                          ),
                 TreeNode(3,
                          # TreeNode(6), TreeNode(7)
                          )
                 )

Traversal().in_order(_root)
print("------------------")
Traversal().pre_order(_root)
print("------------------")
Traversal().post_order(_root)

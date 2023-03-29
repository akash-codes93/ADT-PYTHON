"""
Idea is to do a bfs at two level
before moving to the next level you know that first node will be viewed from left
and other from right
"""


class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class Traversal:

    def left_right_view(self, root):

        left_view = [root.value]
        right_view = [root.value]

        queue = [root]
        next_queue = []

        while queue:
            node = queue.pop(0)

            if node.left:
                next_queue.append(node.left)

            if node.right:
                next_queue.append(node.right)

            if len(queue) == 0:

                if next_queue:
                    left_view.append(next_queue[0].value)
                    right_view.append(next_queue[-1].value)

                queue = next_queue
                next_queue = []

        print("left_view: ", left_view)
        print("right_view: ", right_view)


_root = TreeNode(1
                 ,
                 TreeNode(2,
                          TreeNode(4, TreeNode(8)), TreeNode(5)
                          ),
                 TreeNode(3
                          , TreeNode(6), TreeNode(7)
                          )
                 )

traversal = Traversal()
traversal.left_right_view(_root)

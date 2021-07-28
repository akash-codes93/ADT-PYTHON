from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView1(self, root: TreeNode) -> List[int]:
        """
        Using bfs
        :param root:
        :return:
        """

        if root is None:
            return []

        output, sub_output = [], []
        queue = [root]
        queue_len = 1
        count = 0
        while queue:
            # print(queue)

            if count == queue_len:
                output.append(sub_output[-1])
                sub_output = []
                queue_len = len(queue)
                count = 0

            node = queue.pop(0)

            sub_output.append(node.val)
            count += 1
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        output.append(sub_output[-1])
        return output

    def rightSideView2(self, root: TreeNode, level: int, output: List[int]):

        if root is None:
            return

        if level >= len(output):
            output.append(root.val)

        level += 1

        self.rightSideView2(root.right, level, output)
        self.rightSideView2(root.left, level, output)

        return

    def rightSideView(self, root: TreeNode) -> List[int]:
        output = []
        self.rightSideView2(root, 0, output)
        return output


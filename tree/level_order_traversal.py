from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        output, sub_output = [], []
        queue = [root]
        queue_len = 1
        count = 0
        while queue:
            # print(queue)

            if count == queue_len:
                output.append(sub_output)
                sub_output = []
                queue_len = len(queue)
                count = 0

            node = queue.pop(0)

            sub_output.append(node.val)
            count += 1
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        output.append(sub_output)
        return output


"""
Time : O(N) :: because we touch every node once
Space: O(N)

No. of nodes at leaf : N/2 + 1

"""

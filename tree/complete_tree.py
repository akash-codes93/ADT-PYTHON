"""
@url: https://leetcode.com/problems/count-complete-tree-nodes/
no. of nodes in a tree of height h
2^(h) -1
No. of node at a level = 2^(h-1)
"""
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find_tree_height(self, root):
        traverse = root
        height = 0
        while traverse:
            height += 1
            traverse = traverse.left

        return height

    def check_node_exists(self, index, height, root):
        left = 0
        right = 2 ** (height - 1) - 1
        count = 0
        traverse = root

        while count < height-1:

            mid = math.ceil((left + right) / 2)
            if mid > index:
                traverse = traverse.left
                right = mid - 1
            else:
                traverse = traverse.right
                left = mid

            count += 1
        return traverse is not None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = self.find_tree_height(root)

        if height == 1:
            return 1

        total_nodes = 2 ** (height - 1)
        left = 0
        right = total_nodes - 1

        while left < right:

            mid = math.ceil((left + right) / 2)  # ceil because we need upper value which will lead to wrong calculation

            if self.check_node_exists(mid, height, root):
                left = mid
            else:
                right = mid - 1

        return total_nodes + left + 1

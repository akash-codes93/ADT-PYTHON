"""
@url: https://leetcode.com/problems/validate-binary-search-tree/submissions/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValid(self, root, upper_bound, lower_bound):
        # print(root, upper_bound, lower_bound)
        if root is None:
            return True

        if root.val >= upper_bound or root.val <= lower_bound:
            return False

        if not self.isValid(root.left, root.val, lower_bound) or not self.isValid(root.right, upper_bound, root.val):
            return False

        return True

    def isValidBST(self, root: TreeNode) -> bool:

        return self.isValid(root, float('inf'), float('-inf'))

"""
@url: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
logic: inorder traversal
"""
from tkinter.tix import Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = k

        self.res = None

        self.inorder(root)

        return self.res

    def inorder(self, root):

        if not root:
            return

        self.inorder(root.left)

        self.k -= 1
        if self.k == 0:
            self.res = root.val

        self.inorder(root.right)
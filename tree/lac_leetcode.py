"""
@url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def path_to_node(self, start, end, path):

        if start == end:
            return

        path.append(start)

        for child in [start.left, start.right]:
            if child is not None:
                path.append(child)
                if self.path_to_node(child, end, path):
                    return path
                path.pop()

        return path

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            path_to_p = self.path_to_node(root, p, [])
            path_to_q = self.path_to_node(root, q, [])

            lca = path_to_p[0]
            for i in range(1, min(len(path_to_p), len(path_to_q))):

                if path_to_p[i] != path_to_q[i]:
                    lca = path_to_p[i-1]

            return lca



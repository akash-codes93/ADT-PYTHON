"""
code to find out is tree complete or not
"""
# More simpler available in leetcode repo

# from typing import Optional
#
#
# class Node:
#
#     def __init__(self, value, left=None, right=None):
#
#         for pointer in [left, right]:
#
#             if not isinstance(pointer, Node):
#                 if pointer is not None:
#                     raise ValueError('left/right must be Node/ None')
#
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# def is_complete_tree(node: Optional[Node, None]) -> bool:
#     queue = [node]
#
#     flag = False
#     status = True
#
#     while queue:
#         n = queue.pop(0)
#
#         if n is not None:
#
#             if flag is True:
#                 if n.left is not None or n.right is not None:
#                     status = False
#             else:
#                 if n.left is not None and n.right is None:
#                     flag = True
#                 elif n.left is None and n.right is not None:
#                     status = False
#                 else:
#                     queue.append(n.left)
#                     queue.append(n.right)
#
#     return status
#
#
# def driver():
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.left = Node(6)
#     root.right.right = Node(7)
#
#     if is_complete_tree(root):
#         print("Given Binary Tree is a Complete Binary Tree")
#     else:
#         print("Given Binary Tree is not a Complete Binary Tree")
#
#
# if __name__ == '__main__':
#     driver()

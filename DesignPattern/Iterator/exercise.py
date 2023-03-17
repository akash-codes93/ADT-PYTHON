class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        # todo - return inorder values (not Nodes)
        yield self.value

        if self.left:
            yield from self.left.traverse_preorder()

        if self.right:
            yield from self.right.traverse_preorder()


# root = Node(1,
#             Node(2),
#             Node(3))
root = Node('a',
            Node('b',
                 Node('c'),
                 Node('d')),
            Node('e'))

root.traverse_preorder()

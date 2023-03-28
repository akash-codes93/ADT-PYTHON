"""
To write the level order traversal of the binary tree
First it will contain the implementation of a tree
Followed by different traversal
"""


class Node:

    def __init__(self, value, left, right):
        self.value = value

        self.left = left
        self.right = right


class BT:

    def __init__(self):

        self.head = None

    def add_node(self, value):

        node = Node(value, None, None)

        if self.head is None:
            self.head = node
        else:
            # traversal = self.head
            for each_node in self:
                if each_node.left is None:
                    each_node.left = node
                    break
                elif each_node.right is None:
                    each_node.right = node
                    break

    def add_nodes(self, values):

        if not isinstance(values, list):
            raise ValueError('Values must be list')

        for value in values:
            self.add_node(value)

    def __iter__(self):
        self.queue = [self.head]

        return self

    def __next__(self):

        if self.queue:
            item = self.queue.pop(0)

            if item.left is not None:
                self.queue.append(item.left)

            if item.right is not None:
                self.queue.append(item.right)

            return item
        else:
            raise StopIteration

    def pre_order(self, node=None):
        """
        root -> left -> right
        :param node:
        :return:
        """

        if node is None:
            node = self.head

        if not isinstance(node, Node):
            raise ValueError('node must be Node type')

        print(node.value)

        if node.left is not None:
            self.pre_order(node.left)

        if node.right is not None:
            self.pre_order(node.right)

    def post_order(self, node=None):
        """
        left -> right -> node
        :param node:
        :return:
        """

        if node is None:
            node = self.head

        if not isinstance(node, Node):
            raise ValueError('node must be Node type')

        if node.left is not None:
            self.post_order(node.left)

        if node.right is not None:
            self.post_order(node.right)

        print(node.value)

    def in_order(self, node=None):
        """
        left - > root -> right
        :param node:
        :return:
        """
        if node is None:
            node = self.head

        if not isinstance(node, Node):
            raise ValueError('node must be Node type')

        if node.left is not None:
            self.in_order(node.left)

        print(node.value)

        if node.right is not None:
            self.in_order(node.right)

    def zig_zag(self):

        queue = [[self.head], []]
        # improvement -- you can use only two levels, current and next and the frame q simpler logic
        n = 0
        order = 1
        k = 0

        while len(queue[n]) != 0:
            # print('n - ', n)
            # print('queue - ', queue)
            node = queue[n].pop(0)
            print(node.value)

            if order == 1:
                if node.left is not None:
                    queue[n + 1].insert(0, node.left)

                if node.right is not None:
                    queue[n + 1].insert(0, node.right)
            else:
                if node.right is not None:
                    queue[n + 1].insert(0, node.right)

                if node.left is not None:
                    queue[n + 1].insert(0, node.left)

            # print('queue after - ', queue)

            k = k + 2
            # print('k - ', k)
            # print('total n - ', pow(2, n))

            if k >= pow(2, n + 1):
                n = n + 1
                queue.append([])
                k = 0
                order *= -1

    def zig_zag_simpler(self):
        current_stack = [self.head]
        next_stack = []

        order = 1

        while current_stack:

            node = current_stack.pop(0)
            print(node.value)

            if order == 1:
                if node.left is not None:
                    next_stack.insert(0, node.left)

                if node.right is not None:
                    next_stack.insert(0, node.right)
            else:
                if node.right is not None:
                    next_stack.insert(0, node.right)

                if node.left is not None:
                    next_stack.insert(0, node.left)

            if len(current_stack) == 0:
                current_stack = next_stack
                next_stack = []

                order *= -1


class BST(BT):

    def __init__(self):

        super(BST, self).__init__()

    def add_node(self, value):
        node = Node(value, None, None)

        if self.head is None:
            self.head = node
        else:
            traversal = self.head
            prev = None

            while traversal is not None:

                prev = traversal

                if traversal.value < value:
                    traversal = traversal.right

                else:
                    traversal = traversal.left

            if prev.value < value:
                prev.right = node
            else:
                prev.left = node


if __name__ == '__main__':
    bt = BT()
    # num = list(range(1, 16))
    bt.add_nodes([1, 2, 3, 4, 5, 6, 7])
    # bt.add_nodes(num)
    # bt.post_order()

    bt.zig_zag_simpler()
    # for each in bt:
    #     print(each.value)
    # print(bt.head.left.value)
    # print(bt.head.right.value)

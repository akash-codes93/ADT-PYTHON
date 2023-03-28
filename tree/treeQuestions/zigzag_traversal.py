class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Traversal:

    def __init__(self, root):
        self.root = root
        self.queue = [root]
        self.next_queue = []
        self.order = 1

    def __iter__(self):
        return self

    def run(self):

        while self.queue:
            node = self.queue.pop(0)
            print(node.value, end=', ')
            # yield node.value

            if self.order == 1:
                if node.left:
                    self.next_queue.insert(0, node.left)

                if node.right:
                    self.next_queue.insert(0, node.right)

            else:
                if node.right:
                    self.next_queue.insert(0, node.right)

                if node.left:
                    self.next_queue.insert(0, node.left)

            if not self.queue:
                self.queue = self.next_queue
                self.next_queue = []
                self.order *= -1

        # if not (self.queue and self.next_queue):
        #     raise StopIteration

    def traverse_breadth_first_search(self):
        while self.queue:
            node = self.queue.pop(0)
            print(node.value, end=', ')

            if node.left:
                self.queue.append(node.left)

            if node.right:
                self.queue.append(node.right)

    def traverse_dfs(self, root_node):
        node = root_node
        print(node.value, end=', ')

        if node.left:
            self.traverse_dfs(node.left)

        if node.right:
            self.traverse_dfs(node.right)

        return

    def depth_first_search(self):
        return self.traverse_dfs(self.root)


root = Node(1,
            Node(2,
                 Node(4), Node(5)),
            Node(3,
                 Node(6), Node(7))
            )

traversal = Traversal(root)

# traversal.run()
# traversal.traverse_breadth_first_search()
traversal.depth_first_search()

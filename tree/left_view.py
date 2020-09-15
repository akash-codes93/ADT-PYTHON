class Node:

    def __init__(self, value, left=None, right=None):

        for pointer in [left, right]:

            if not isinstance(pointer, Node):

                if pointer is not None:
                    raise ValueError("Left and right can be Node/None type")

        self.value = value
        self.right = right
        self.left = left


class BT:

    def __init__(self):
        self.head = None

    def add_node(self, value):

        if isinstance(value, Node):
            node = value
        else:
            node = Node(value)

        if self.head is  None:
            self.head = node

        else:

            for each_node in self:

                if each_node.left is None:
                    each_node.left = node

                    break

                elif each_node.right is None:
                    each_node.right = node

                    break

    def add_nodes(self, values):

        if not isinstance(values, list):
            raise ValueError("values must a list type")

        for value in values:
            self.add_node(value)

    def __iter__(self):

        self.queue = [self.head]
        return self

    def __next__(self):

        if self.queue:

            node = self.queue.pop(0)

            if node.left is not None:
                self.queue.append(node.left)

            if node.right is not None:
                self.queue.append(node.right)

            return node

        else:
            raise StopIteration


def left_view(head: Node):

    queue1 = []
    queue2 = []

    queue1.append(head)
    print("Left view: ", head.value, end=" -> ")

    while queue1:

        node = queue1.pop(0)

        if node.left is not None:
            queue2.append(node.left)

        if node.right is not None:
            queue2.append(node.right)

        if len(queue1) == 0:

            queue1 = queue2
            queue2 = []

            if queue1:
                print(queue1[0].value, end=" -> ")


def driver():
    bt = BT()
    bt.add_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print("Level order traversal: ", end=" ")
    for node in bt:
        print(node.value, end=" -> ")

    print()
    left_view(bt.head)


if __name__ == '__main__':
    driver()

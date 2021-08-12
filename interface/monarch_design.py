class Person:

    def __init__(self, val):
        self.val = val
        self.children = []
        self.is_alive = True


class Monarchy:

    def __init__(self):
        self.root = None
        self.monarch = {}

    def birth(self, child, parent):
        child_obj = Person(child)

        if parent is None:
            self.root = child_obj
        else:
            self.monarch[parent].children.append(child_obj)

        self.monarch[child] = child_obj

    def death(self, person):
        self.monarch[person].is_alive = False

    def succession(self, node, output):

        if node.is_alive:
            output.append(node.val)

        children = self.monarch[node.val].children

        for child in children:
            self.succession(child, output)

        return output

    def order_of_succession(self):
        order = self.succession(self.root, [])
        print(order)


if __name__ == '__main__':
    monarch = Monarchy()

    monarch.birth('A', None)
    monarch.birth('B', 'A')
    monarch.birth('C', 'A')
    monarch.birth('D', 'A')
    monarch.birth('E', 'B')
    monarch.birth('F', 'B')
    monarch.birth('H', 'E')
    monarch.birth('I', 'D')

    monarch.order_of_succession()

    monarch.death('A')
    monarch.order_of_succession()

    monarch.death('B')
    monarch.death('F')
    monarch.order_of_succession()

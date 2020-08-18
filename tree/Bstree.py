from Btree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self, value):
        self.value = value
        super().__init__(self.value)
        # self.value = value
        # self.left_child = None
        # self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)

        elif value <= self.value:
            self.left_child = BinarySearchTree(value)

        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)

        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

    def ind_maximum_value(self):
        if self.right_child:
            return self.right_child.find_maximum_value()
        else:
            return self.value

    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True


if __name__ == '__main__':
    a_node = BinarySearchTree(50)
    a_node.insert_node(21)
    b_node = a_node.left_child
    b_node.insert_node(76)
    a_node.insert_node(4)
    a_node.insert_node(32)
    a_node.insert_node(64)
    a_node.insert_node(100)
    a_node.insert_node(52)

    # print("Pre order is : ----------- ")
    # a_node.pre_order()

    elem = a_node.find_node(101)

    print(elem)

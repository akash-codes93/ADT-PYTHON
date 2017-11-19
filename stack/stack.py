class Stack:

    EMPTY_STACK = None

    def __init__(self, *args, **kwargs):
        self.items = []
        self.items = list(args)

    def peek(self):
        try:
            return self.items[len(self.items) - 1]
        except IndexError:
            return Stack.EMPTY_STACK

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return item

    def pop(self):
        try:
            top_element = self.items[len(self.items) - 1]
            self.items.pop()
            return top_element
        except IndexError:
            return Stack.EMPTY_STACK

    # def size(self):
    #     return len(self.items)

    def search(self):
        pass

    # def print_stack(self):
    #     print(self.items)


if __name__ == '__main__':

    stack = Stack(1)
    print(stack.pop())
    print(stack.pop())
    #stack.peek()
    #stack.print_stack()
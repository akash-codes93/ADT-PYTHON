class Queue:
    EMPTY_STACK = None
    def __init__(self, *args, **kwargs):
        self.items = []
        self.items = list(args)

    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            return Queue.EMPTY_STACK

    def empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
        return item

    def dequeue(self):
        try:
            top_element = self.items[0]
            del self.items[0]
            return top_element
        except IndexError:
            return Queue.EMPTY_STACK

    # def size(self):
    #     return len(self.items)

    def search(self):
        pass

        # def print_stack(self):
        #     print(self.items)


if __name__ == '__main__':
    stack = Queue(1)
    print(stack.dequeue())
    print(stack.dequeue())
    # stack.peek()
    # stack.print_stack()

        
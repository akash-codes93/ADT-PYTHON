from linkedList import ListNode


class SingleLinkedList:

    def __init__(self):
        # initialize list with
        self.head = None
        self.tail = None

        return

    # adding an object to the list
    def add_list_item(self, item):

        if not isinstance(item, ListNode) :
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    # returning an iterator object
    def __iter__(self):
        self.current_node = self.head
        return self

    # returning the next element
    def __next__(self):

        if self.current_node is not None:
            node = self.current_node
            self.current_node = self.current_node.next

            return node
        else:
            raise StopIteration

    # to find the length of the linked list
    def __len__(self):
        count = 0
        i = iter(self)

        while 1:
            try:
                next(i)
                count += 1
            except StopIteration:
                break

        return count

    # returning the entire list
    def output_list(self):
        i = iter(self)
        while 1:
            try:
                print(next(i).data)
            except StopIteration:
                break
        return

    # search the linked list which returns list of position where it is found
    def __getitem__(self, item):

        pos = 1
        position = []

        i = iter(self)

        while 1:
            try:
                if next(i).has_value(item) is True:
                    position.append(pos)
                pos = pos+1

            except StopIteration:
                break
        return position

    # delete an item in the linked list
    def __delitem__(self, key):
        previous_node = None
        i = iter(self)

        while 1:
            try:
                node = next(i)
                if node.data == key:
                    # if this is the first node (head)
                    if previous_node is not None:
                        previous_node.next = node.next
                    else:
                        self.head = node.next
                        # we don't have to look any further
                        return

                # needed for the next iteration
                previous_node = node

            except StopIteration:
                break

        return


if __name__ == '__main__':

    node1 = ListNode(15)
    node2 = ListNode(8.2)
    item3 = "Berlin"
    node4 = ListNode(15)

    track = SingleLinkedList()

    for current_item in [node1, node2, item3, node4]:
        track.add_list_item(current_item)

    i = iter(track)

    while 1:
        try:
            print(next(i).data)
        except StopIteration:
            break
    print(len(track))

    print(track[15])

    del track[8.2]

    track.output_list()
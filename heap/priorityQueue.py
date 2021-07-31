import math

"""
Max Heap: child nodes are smaller than parent
- Root node is the greatest node
Property:
Fill array using bfs
parent of any node: floor((index-1)/2)
left: (index*2) + 1
right: (index*2) + 2

Insertion:
####################
insert the node at the next available position.
Then start comparing it with its parent if parent is smaller swap.
do this step till you reach the end.

Deletion:
####################
Swap the last value with the missing value.
then compare the value with its two children.
out of the larger value replace the the value
or if not possible then its ok

"""


class PriorityQueue:

    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.heap == 0

    def peek(self):
        try:
            return self.heap[0]
        except IndexError:
            return None

    def _parent(self, index):
        if index == 0:
            return None
        else:
            return math.floor((index - 1) / 2)

    def _left_child(self, index):
        _len = len(self.heap)

        child = index * 2 + 1
        if child >= _len:
            return None
        return child

    def _right_child(self, index):
        _len = len(self.heap)

        child = index * 2 + 2
        if child >= _len:
            return None
        return child

    def push(self, value):
        self.heap.append(value)

        self.shiftup()

        return len(self.heap)

    def swap(self, i, j):
        k = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = k

    def shiftup(self):
        index = len(self.heap) - 1

        while index == 0 or self.heap[index] >= self.heap[self._parent(index)]:
            parent_index = self._parent(index)
            self.swap(index, parent_index)

            index = parent_index

    def pop(self):
        last_value = self.heap.pop()
        self.heap[0] = last_value

        self.shiftdown()

        return len(self.heap)

    def shiftdown(self):
        index = 0
        while self.heap[index] > self.heap[self._left_child(index)] and self.heap[index] > self.heap[
              self._right_child(index)] and index > len(self.heap) - 2:
            left_child = self._left_child(index)
            right_child = self._right_child(index)
            if self.heap[left_child] > self.heap[right_child]:
                self.swap(left_child, index)
                index = left_child
            else:
                self.swap(right_child, index)
                index = right_child

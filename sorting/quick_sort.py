"""
in-place sort
partition_index = all the left elements are smaller and right elements are greater.
pivot element : last element of the array (can be median also)
i, j at the start pos
move j till it is greater than pivot if less is found swap with i : in case of swap move i by 1
if j reaches pivot
swap i and pivot
"""

from typing import List


class QuickSort:

    @staticmethod
    def swap(a: List, i: int, j: int):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def _get_partition_index(self, a: List, left: int, right: int):
        pivot = a[right]
        i = left

        for j in range(left, right):

            if a[j] < pivot:
                self.swap(a, i, j)
                i = i + 1

        self.swap(a, i, right)

        return i

    def sort(self, a: List, left: int, right: int):
        if left < right:
            partition_index = self._get_partition_index(a, left, right)
            # print(a, partition_index)
            self.sort(a, left, partition_index - 1)
            self.sort(a, partition_index + 1, right)


arr = [5, 3, 1, 6, 4, 2]
QuickSort().sort(arr, 0, 5)
print(arr)

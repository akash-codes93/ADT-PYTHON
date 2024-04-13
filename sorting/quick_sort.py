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


class QuickSelect:

    @staticmethod
    def swap(a: List, i: int, j: int):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    def _get_partition_index(self, a: List, left: int, right: int):
        pivot = a[right]
        i = left

        for j in range(left, right):

            if a[j] > pivot:
                self.swap(a, i, j)
                i = i + 1

        self.swap(a, i, right)
        return i

    def select(self, a: List, left: int, right: int, k: int):
        if left < right:
            partition_index = self._get_partition_index(a, left, right)
            if partition_index == (left + k - 1):
                return arr[partition_index]
            elif partition_index > (left + k - 1):
                return self.select(a, left, partition_index - 1, k)
            else:
                return self.select(a, partition_index + 1, right, left + k - partition_index - 1)

    def select_k(self, a: List, left: int, right: int, k: int):
        if left < right:
            partition_index = self._get_partition_index(a, left, right)
            if partition_index > (left + k - 1):
                self.select_k(a, left, partition_index - 1, k)
            elif partition_index < (left + k - 1):
                self.select_k(a, partition_index + 1, right, left + k - partition_index - 1)


arr = [5, 1, 3, 6, 4, 0]
# QuickSort().sort(arr, 0, 5)

# val = QuickSelect().select(arr, 0, 5, 3)
QuickSelect().select_k(arr, 0, 5, 3)  # 3 largest
print(arr)
# print(val)

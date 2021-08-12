"""
@url: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List


class Solution:

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

    def quickselect(self, nums, left, right, index_to_find):

        # if left < right:
        partition_index = self._get_partition_index(nums, left, right)

        if partition_index == index_to_find:
            return nums[partition_index]
        elif index_to_find < partition_index:
            return self.quickselect(nums, left, partition_index - 1, index_to_find)
        else:
            return self.quickselect(nums, partition_index + 1, right, index_to_find)

    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return nums[0]

        index_to_find = len(nums) - k

        # return self.quickselect(nums, 0, len(nums)-1, index_to_find)
        nums.sort()
        return nums[index_to_find]

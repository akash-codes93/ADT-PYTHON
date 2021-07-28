from typing import List


class Solution:

    def binarySearch(self, nums, left, right, target):

        if len(nums) == 0:
            return -1

        while left <= right:
            mid = (left + right) // 2
            var = nums[mid]

            if var == target:
                return mid

            elif target > var:
                left = mid + 1

            else:
                right = mid - 1

            print(left, right)

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        first = self.binarySearch(nums, 0, len(nums) - 1, target)
        print(first)

        if first == -1:
            return [-1, -1]

        start = temp = first
        end = first

        while start != -1:
            temp = start
            start = self.binarySearch(nums, 0, start - 1, target)

        start = temp

        while end != -1:
            temp = end
            end = self.binarySearch(nums, end + 1, len(nums) - 1, target)

        end = temp

        return [start, end]


Solution().searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 5)


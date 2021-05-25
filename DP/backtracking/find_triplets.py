"""
Print all triplets in an array with a sum less than or equal to a given number
Input:

A = [ 2, 7, 4, 9, 5, 1, 3 ]
sum = 10

Output: Triplets are

(1, 2, 3) --
(1, 2, 4) --
(1, 2, 5) --
(1, 2, 7) --
(1, 3, 4) --
(1, 3, 5) --
(1, 4, 5) --
(2, 3, 4) --
(2, 3, 5) --
"""


class Solution:

    def find_triplets(self, a, nums, num_index, a_index, sum_so_far, k):

        if a_index == len(a):
            print(a)
            return

        for i in range(num_index, len(nums)):

            if a[a_index] == -1 and (sum_so_far + nums[i]) <= k:
                a[a_index] = nums[i]
                sum_so_far += nums[i]

                self.find_triplets(a, nums, i + 1, a_index + 1, sum_so_far, k)

                a[a_index] = -1
                sum_so_far -= nums[i]

    def trigger(self, nums, k):

        a = [-1] * 3
        self.find_triplets(a, nums, 0, 0, 0, k)


Solution().trigger([2, 7, 4, 9, 5, 1, 3], 10)

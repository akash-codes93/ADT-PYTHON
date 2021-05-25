"""
At most k swaps
Input:  S = 934651, k = 1
Output: 134659

Input:  S = 934651, k = 2
Output: 134569

in-case of minimum maintain min_so_far
"""


class Solution:

    @staticmethod
    def swap_digits(nums, i, j):
        p = nums[i]
        nums[i] = nums[j]
        nums[j] = p

    # def swap(self, num, i, n):
    #     if i >= len(str(num)):
    #         return num
    #
    #     if str(num)[i] < str(num)[n - i - 1]:
    #         return self.swap(num, i + 1, n)
    #     else:
    #         rev_num = self.swap_digits(num, i, n)
    #         return min(rev_num, self.swap(num, i + 1, n))

    def swaps(self, nums, k, min_so_far):

        num = int("".join(nums))
        if min_so_far > num:
            min_so_far = num

        if k < 1:
            return min_so_far

        for i in range(0, len(nums) - 1):

            for j in range(i + 1, len(nums)):
                self.swap_digits(nums, i, j)

                min_so_far = self.swaps(nums, k - 1, min_so_far)

                self.swap_digits(nums, i, j)

        return min_so_far

    def k_swaps(self, num, k):

        nums = list(str(num))
        min_so_far = num

        min_so_far = self.swaps(nums, k, min_so_far)

        print(min_so_far)


Solution().k_swaps(934651, 2)
# output = Solution().k_swaps(134659, 2)

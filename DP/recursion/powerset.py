"""
@url: https://leetcode.com/problems/subsets/
Generate the power set of a given set

S{{}, {x}, {y}, {z}, {x, y}, {x, z}, {y, z}, {x, y, z}}
"""


class Solution:

    def powerset(self, nums, p, output):
        if len(nums) == p:
            print(output)
            return

        for choice in [0, 1]:
            if choice == 0:
                output.append(nums[p])
                self.powerset(nums, p + 1, output)
                output.pop()
            else:
                self.powerset(nums, p + 1, output)

    def driver(self, nums):
        self.powerset(nums, 0, [])


Solution().driver(['x', 'y', 'Z'])

"""
@url: https://leetcode.com/problems/subsets/
Generate the power set of a given set

S{{}, {x}, {y}, {z}, {x, y}, {x, z}, {y, z}, {x, y, z}}
"""


# class Solution:
#
#     def powerset(self, nums, p, output):
#         if len(nums) == p:
#             print(output)
#             return
#
#         for choice in [0, 1]:
#             if choice == 0:
#                 output.append(nums[p])
#                 self.powerset(nums, p + 1, output)
#                 output.pop()
#             else:
#                 self.powerset(nums, p + 1, output)
#
#     def driver(self, nums):
#         self.powerset(nums, 0, [])


import copy


class Solution:
    def subsets(self, nums):
        main = []

        def looper(i, output):
            if i == len(nums):
                main.append(copy.copy(output))
                return

            # for j in range(i, len(nums)):
                # print("first", i, j)
            output.append(nums[i])
            looper(i + 1, output)
            output.pop()
            # print("second", i, j)
            looper(i+1, output)

            return

        looper(0, [])
        return main


a = Solution().subsets(['x', 'y'])
print(a)

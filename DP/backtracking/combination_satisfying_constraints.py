"""
n : elements
2n : combination
constraints: gap should be equal to number
Input: n = 3
Output:
3 1 2 1 3 2
2 3 1 2 1 3
"""
from typing import List


class Solution:

    def combinations_given_constraints(self, nums: List[int]) -> List[List[int]]:

        result = []

        if len(nums) == 1:
            return [nums]

        for i in range(0, len(nums)):
            rem_nums = nums[:i] + nums[i + 1:]

            combinations = self.combinations_given_constraints(rem_nums)
            # print(nums, i, combinations)

            if nums.count(nums[i]) > 1:
                for combination in combinations:
                    # print(combination, nums, i)

                    if len(combination) > nums[i] and combination[nums[i]] == nums[i]:
                        d = [nums[i]] + combination
                        if d not in result:
                            result.append(
                                [nums[i]] + combination
                            )
            else:
                for combination in combinations:
                    d = [nums[i]] + combination
                    if d not in result:
                        result.append(
                            [nums[i]] + combination
                        )

        return result

    def findAllCombinations(self, A, x, n):

        # if all elements are filled, print the solution
        if x > n:
            print(A)
            return

        # try all possible combinations for element `x`
        for i in range(2 * n):

            # if position `i` and `i+x+1` are not occupied in the input
            if A[i] == -1 and (i + x + 1) < 2 * n and A[i + x + 1] == -1:
                # place `x` at position `i` and `i+x+1`
                A[i] = x
                A[i + x + 1] = x

                # recur for the next element
                self.findAllCombinations(A, x + 1, n)

                # backtrack (remove `x` from position `i` and `i+x+1`)
                A[i] = -1
                A[i + x + 1] = -1

    def get_combinations(self, n: int):  # -> List[List[int]]:

        # nums_2_n = []
        # for i in range(1, n+1):
        #     nums_2_n.append(i)
        #     nums_2_n.append(i)

        # return self.combinations_given_constraints(nums_2_n)
        A = [-1] * (2 * n)
        x = 1
        return self.findAllCombinations(A, x, n)


output = Solution().get_combinations(3)
print(output)
# print(len(output))

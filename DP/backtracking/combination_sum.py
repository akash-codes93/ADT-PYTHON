"""
@url: https://leetcode.com/problems/combination-sum/
"""

from typing import List


class Solution:

    def combination_sum(self, candidates, target, output, main_output):
        if target == 0:
            # output.sort()
            new_output = [i for i in output]
            new_output.sort()
            if new_output not in main_output:
                main_output.append([i for i in new_output])
            return
        if target < 0:
            return

        for i in range(0, len(candidates)):
            # print(target)
            target = target - candidates[i]
            output.append(candidates[i])
            self.combination_sum(candidates, target, output, main_output)
            output.pop()
            target = target + candidates[i]

        return main_output

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        return self.combination_sum(candidates, target, [], [])


if __name__ == '__main__':
    # print(Solution().combinationSum(candidates=[2, 3, 6, 7], target = 7))
    print(Solution().combinationSum([2,3,5], 8))


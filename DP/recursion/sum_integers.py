"""
Given a number n, generate all distinct ways to write n as the sum of positive integers.
For example, with n = 4, the options are 4, 3 + 1, 2 + 2, 2 + 1 + 1, and 1 + 1 + 1 + 1.
"""
from typing import List


class Solution:
    memoization = {}

    def sum_of_positive_int(self, n: int) -> List[str]:
        if n in self.memoization:
            return self.memoization[n]

        result = []

        if n == 0:
            return []

        result.append(str(n))

        for i in range(1, n):
            sub_res = []

            for sol in self.sum_of_positive_int(n - i):
                sub_res.append(str(i) + '+' + sol)

            result += sub_res

        self.memoization[n] = result

        return result

    def sum_of_positive_int_2(self, arr: List, i: int, n: int) -> None:

        if n == 0:
            sol = " + ".join(arr)
            print(sol)
            return

        for j in range(i, n + 1):
            arr.append(str(j))

            self.sum_of_positive_int_2(arr, j, n - j)

            del arr[-1]


sum_of_positive_int = Solution().sum_of_positive_int_2
print(sum_of_positive_int([], 1, 3))

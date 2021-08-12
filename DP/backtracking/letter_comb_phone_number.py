"""
@url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:

    alpha_comb = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def recursion(self, digits, i, comb, output):

        if i == len(digits):
            output.append(comb)
            return []

        for letter in self.alpha_comb[digits[i]]:

            comb += letter

            self.recursion(digits, i+1, comb, output)

            comb = comb[:-1]

        return output


    def letterCombinations(self, digits: str) -> List[str]:
        return self.recursion(digits, 0, "", [])


if __name__ == '__main__':

    print(Solution().letterCombinations("2"))
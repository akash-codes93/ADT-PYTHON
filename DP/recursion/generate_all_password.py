"""
Given a set of characters generate all possible passwords from them. This means we should generate all possible
permutations of words using the given characters, with repititions and also upto a given length.
Input : arr[] = {a, b},
          len = 2.
Output :
a b aa ab ba bb
"""
from typing import List


class Solution:

    def cal_password(self, values, i, s):

        if i == 0:
            print(s)
            return

        for j in range(0, len(values)):
            password = s + values[j]

            self.cal_password(values, i - 1, password, )
        return

    def password_generator(self, values: List):

        for i in range(1, len(values) + 1):
            self.cal_password(values, i, "")


generate_password = Solution().password_generator
generate_password(['a', 'b'])

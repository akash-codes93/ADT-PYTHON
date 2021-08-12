"""
all combination of n using 1's and 2's
n = 3
[1,1,1], [1,2], [2,1]
n=4
[1,1,1,1], [1,1,2]*3, [2,2]
Solved
"""


class Solution:

    def combination_using_one_n_twos(self, n, output):
        if n == 0:
            print(output)
            return

        elif n < 0:
            return

        for i in [1, 2]:
            output.append(i)
            # print(n - i)
            self.combination_using_one_n_twos(n - i, output)
            # print("d - ", output)
            output.pop()

        return


Solution().combination_using_one_n_twos(5, [])
print("#" * 30)
Solution().combination_using_one_n_twos(4, [])

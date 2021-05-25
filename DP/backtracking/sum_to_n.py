"""
Print all combinations of numbers from 1 to n having sum n

For n = 5, the following combinations are possible:

{ 5 }
{ 1, 4 }
{ 2, 3 }
{ 1, 1, 3 }
{ 1, 2, 2 }
{ 1, 1, 1, 2 }
{ 1, 1, 1, 1, 1 }
"""
"""
Not implemented
"""

a: list
class Solution:

    def sum_to_n_(self, a, n):

        if n == 0:
            print(a)
            return

        if n < 0:
            return

        for i in range(n, 0, -1):
            a.append(i)
            a.sort()
            self.sum_to_n_(a, n - i)
            a.remove(i)

    def sum_to_n(self, n, p, ones):
        if n == 0:
            return

        current = [p] * ones
        current.append(n)
        print(current)
        self.sum_to_n(n - 1, p, ones + 1)

    def trigger(self, n):

        for i in range(0, n // 2 + 1):
            self.sum_to_n(n-i, i, 0)


# Solution().trigger(4)
Solution().sum_to_n_([], 4)

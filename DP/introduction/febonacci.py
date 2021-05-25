class Solution:
    """
    Top Down approach: Memoization
    """
    memoization = {}

    def fibonacci(self, n):

        if n in self.memoization:
            print("Memoization used: ", n)
            return self.memoization[n]

        if n == 0:
            return 0

        if n == 1:
            return 1

        output = self.fibonacci(n - 1) + self.fibonacci(n - 2)

        self.memoization[n] = output
        return output


# print(Solution().fibonacci(10))


class Solution2:
    """
    Bottom Up approach: Tabulation
    """

    def fibonacci(self, n):
        a = 0
        b = 1
        c = 0
        for i in range(2, n + 1):
            c = a + b

            a = b
            b = c

        print(c)


Solution2().fibonacci(10000000)

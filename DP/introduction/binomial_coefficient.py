class Solution:
    memoization = {}

    def combinations(self, n, k):
        if (n, k) in self.memoization:
            print("memoization used: ", (n, k))
            return self.memoization[(n, k)]

        if n == k or k == 0:
            return 1

        out = self.combinations(n - 1, k - 1) + self.combinations(n - 1, k)
        self.memoization[(n, k)] = out

        return out


class Solution2:

    def combinations(self, n, k):
        # n x k
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        # print(dp)
        for i in range(0, n + 1):
            dp[i][0] = 1
            if i <= k:
                dp[i][i] = 1
        print(dp)
        for i in range(n):
            for j in range(k):
                # if dp[i][j] == 0:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        print(dp)
        print(dp[n - 1][k - 1])


output = Solution2().combinations(5, 3)
print(output)
# 5!/3!*2

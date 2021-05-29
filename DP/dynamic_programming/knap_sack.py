"""
Inputs:
val = [60, 100, 120]
wt = [1, 2, 3]
W = 5
"""


class Solution:
    """
    This solution is using backtracking
    """

    def knapsack(self, wt, val, bag_wt, wt_till_now, val_till_now, max_value):

        if wt_till_now >= bag_wt:
            if val_till_now > max_value:
                max_value = val_till_now

            return max_value

        for i in range(0, len(wt)):
            value = val[i]
            weight = wt[i]

            if wt_till_now + weight <= bag_wt:
                rem_wt = wt[:i] + wt[i + 1:]
                rem_val = val[:i] + val[i + 1:]

                max_value = self.knapsack(rem_wt, rem_val, bag_wt, wt_till_now + weight, val_till_now + value,
                                          max_value)

        return max_value

    def driver(self, val, wt, bag_wt):

        return self.knapsack(wt, val, bag_wt, 0, 0, 0)


def knapsack_DP(W, weights, values):
    dp = [[0 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    dp[W][0] = 0
    for i in range(1, len(weights) + 1):
        for w in range(0, W + 1):
            if weights[i - 1] <= w:
                dp[w][i] = max(dp[w][i - 1], dp[w - weights[i - 1]][i - 1] + values[i - 1])
            else:
                dp[w][i] = dp[w][i - 1]
    return dp[W][len(weights)]


# print(Solution().driver([60, 100, 120], [10, 20, 30], 50))

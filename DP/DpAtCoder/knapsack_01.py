"""
https://atcoder.jp/contests/dp/tasks/dp_d
"""

n, w = [int(i) for i in input().split(' ')]

wt = []
v = []

for i in range(0, n):
    wti, vi = [int(i) for i in input().split(' ')]
    wt.append(wti)
    v.append(vi)

dp = [[0] * (w + 1) for i in range(0, n + 1)]  # because dp table w+1, n+1


for i in range(0, n + 1):
    for j in range(0, w + 1):

        if i == 0 or w == 0:
            dp[i][j] = 0

        elif wt[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v[i-1] + dp[i-1][j-wt[i-1]])
print(dp[n][w])

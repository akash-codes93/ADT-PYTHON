def frog1(heights, k):
    dp = [0, abs(heights[1] - heights[0])]

    for p in range(2, len(heights)):
        dp.append(float('inf'))

        for t in range(1, k + 1):

            if p - t >= 0:
                dp[p] = min(
                    dp[p],
                    dp[p - t] + abs(heights[p] - heights[p - t])
                )

    return dp[-1]


num, jp = [int(j) for j in input().split(' ')]

heights = [int(i) for i in input().split(' ')]

p = frog1(heights, jp)
print(p)
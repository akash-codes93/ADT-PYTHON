n, m = [int(i) for i in input().split(' ')]

dp = [[0] * m for i in range(n)]
matrix = [[0] * m for i in range(n)]

for i in range(n):

    s = input()
    for j in range(len(s)):
        matrix[i][j] = s[j]

for i in range(len(dp)):
    for j in range(len(dp[i])):

        if i == 0 and j == 0:
            dp[i][j] = 1
        elif matrix[i][j] == "#":
            dp[i][j] = 0
        elif i==0:
            dp[i][j] = dp[i][j-1]
        elif j==0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


# print(dp)
print(dp[-1][-1]%((10**9)+7))



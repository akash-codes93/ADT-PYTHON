s1 = str(input())
s2 = str(input())

if s1 == 0 or s2 == 0:
    print("")
else:

    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # print(dp)

    s = ""
    i = len(dp) - 1
    j = len(dp[0]) - 1

    while i != 0 and j != 0:

        if dp[i][j] > dp[i-1][j-1] and dp[i-1][j-1] >= dp[i][j-1] and dp[i-1][j-1] >= dp[i-1][j]:
            s += s1[i-1]
            i = i-1
            j = j-1

        else:
            if dp[i-1][j]> dp[i][j-1]:
                i = i-1
            else:
                j=j-1

    print(s[::-1])


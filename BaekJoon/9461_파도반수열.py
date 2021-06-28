import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * (100000)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    if n < 4:
        print(dp[n-1])
    else:
        for i in range(4,n):
            dp[i] = dp[i-1] + dp[i-5]
        print(max(dp))
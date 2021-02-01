import sys
n = int(sys.stdin.readline())


rgb = [[0]*3 for i in range(n)]

for i in range(n):
    rgb[i][0], rgb[i][1], rgb[i][2] = map(int, sys.stdin.readline().split())

dp = [[0]*3 for i in range(n)]

for i in range(n):
    if i ==0:
        dp[i] = rgb[i]
    else:
        dp[i][0] = rgb[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = rgb[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = rgb[i][2] + min(dp[i-1][0],dp[i-1][1])

print(min(dp[n-1]))

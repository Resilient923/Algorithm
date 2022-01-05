import sys
input = sys.stdin.readline

n,k = map(int,input().split())
w = [0 for _ in range(n+1)]
v = [0 for _ in range(n+1)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n):
    a,b = map(int,input().split())
    w[i] = a
    v[i] = b

for i in range(n+1):
    for j in range(k+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
print(dp[n][k])
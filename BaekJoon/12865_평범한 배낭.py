import sys
input = sys.stdin.readline

n,k = map(int,input().split())

weight = [0 for _ in range(n+1)]
value = [0 for _ in range(n+1)]

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(n):
    weight[i],value[i] = map(int,input().split())
 
for i in range(n+1):
    for j in range(k+1):
        if j < weight[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
print(dp[n][k])
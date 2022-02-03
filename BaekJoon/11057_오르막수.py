import sys
input = sys.stdin.readline

# dp 문제이다.
# 규칙을 찾으면 된다.

n = int(input())
dp = [[0]*11 for _ in range(n+1)]

for i in range(11):
    dp[0][i] = i
    
for i in range(1,n+1):
    for j in range(1,11):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007



print(dp[n-1][-1])


# dp를 이용하는 문제

import sys
input = sys.stdin.readline


n = int(input())
dp = [0 for _ in range(n+1)]

T = [0 for _ in range(n+1)]
P = [0 for _ in range(n+1)]

for i in range(n):
    t,p = map(int,input().split())
    T[i] = t
    P[i] = p

for i in range((n+1)-2,-1,-1):
    if T[i] + i <= n:
        dp[i] = max(dp[i+1],P[i]+dp[i+T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])
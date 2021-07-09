import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+2)

dp[2] = 3
for i in range(4,n+2):
    if i % 2 == 0:
        dp[i] += dp[i-2]*3
        for j in range(4,i):
            dp[i] += dp[i-j] * 2
        dp[i] += 2
    else:
        continue

print(dp[n])
#100 436252889

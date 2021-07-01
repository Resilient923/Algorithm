import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
dp = [0]*n
data.sort()
dp[0] = data[0]
for i in range(1,n):
    dp[i] = dp[i-1]+data[i]
print(sum(dp))
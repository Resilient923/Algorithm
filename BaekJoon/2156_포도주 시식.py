#이문제는 dp...?
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

dp =[0 for _ in range(n)]

dp[0] = data[0]
if n == 1:
    dp[0] = data[0]
elif n == 2:
    dp[1] = data[0]+data[1]
elif n == 3:
    dp[1] = data[0]+data[1]
    dp[2] = max(dp[1], data[0]+data[2], data[1]+data[2])
else:
    dp[1] = data[0]+data[1]
    dp[2] = max(dp[1], data[0]+data[2], data[1]+data[2])
    for i in range(3,n):
        dp[i] = max(data[i]+dp[i-3]+data[i-1], data[i]+dp[i-2], dp[i-1])

print(max(dp))

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
dp = [100000 for i in range(k+1)]
coin = 0

for i in coins:
    coin += k // i
    dp[i] = coin
    k %= i


print(dp)

if k ==0:
    print(min(dp))
else:
    print(-1)
###################################################


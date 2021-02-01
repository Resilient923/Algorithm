import sys
n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))
dp =[0 for i in range(n+1)]
for i in range(n):
    for j in range(i):
        if m[i] > m[j] and dp[i] < dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))

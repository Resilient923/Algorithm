import sys
input = sys.stdin.readline

# 이문제는 dp문제이다.
n = int(input())
# 인덱스를 맞춰주기 위해 앞에 0을 둔다.
data = [0] + list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
# dp[n] 은 n개를 살 때 최대 가격으로 정의한다.
# 인덱스 해결을 위해 n+1까지, 0은 신경쓰지 않는다.
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],data[j]+dp[i-j])
print(dp)
print(dp[n])

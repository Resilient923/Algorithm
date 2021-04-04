""" 틀린코드 #이코드는 음수를 고려하지못한다.

n = int(input()) 
m = []
for i in range(n):
    m.append(int(input()))
num = m[0]
for i in range(1,len(m)):
    num = max(num,m[i-1]+m[i])
print(num)
-----------------------------------------------------------------------

두번째 코드 #런타임 에러 발생

n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

dp = [0 for _ in range(n)]
dp[0] = m[0]
for i in range(1,len(m)):
    dp[i] = max(m[i],dp[i-1]+m[i])
print(max(dp))
-------------------------------------------------------------------------------
정답코드

n = int(input())
m = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp[0] = m[0]
for i in range(1,n):
    dp[i] = max(m[i],dp[i-1]+m[i])
print(max(dp)) """

# dp문제이다. 제곱수 항의 최소 개수
# n일 경우 1부터 n까지의 수들을 사용할 때 각각의 경우의 개수를 넣어주면될꺼같다.
import sys
input = sys.stdin.readline

n = int(input())
    
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    dp[i] = i
    for j in range(1,i):
        if(j**2)>i:
            break
        if dp[i] > dp[i-j**2]+1:
            dp[i] = dp[i-j**2]+1
print(dp[n])

#그리디인줄알았지만 틀린코드..
""" ans = []
for i in range(1,int((n+1)**0.5)+1):
    ans.append(i**2)
cnt = 0
ans.sort(reverse=True)
for i in ans:
    cnt += n//i
    n = n%i
print(cnt) """
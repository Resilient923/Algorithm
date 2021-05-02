import sys
from itertools import combinations
input = sys.stdin.readline

#dp 보텀업방식 사용
n,k = map(int,input().split())
numbers = []
dp = [0 for _ in range(k+1)]
for _ in range(n):  
    numbers.append(int(input()))
dp[0] = 1
for i in numbers:
    for j in range(i,k+1):
            dp[j] += dp[j-i]

print(dp[k])
import sys
input = sys.stdin.readline
# 이문제는 그리디쓰면 안된다.
n,k = map(int,input().split())
numbers = []
#dp를 만들어준다.
dp = [10001 for _ in range(k+1)]
#0원 만드는건 0개이다.
dp[0] = 0

for _ in range(n):
    numbers.append(int(input()))
numbers.sort()
for i in range(len(numbers)):
    for j in range(numbers[i],k+1):
        dp[j] = min(dp[j],dp[j-numbers[i]]+1) #핵심코드
        #이전 동전으로만 i원을 만들때 랑 지금 동전까지 써서 만들 때
print(dp[-1] if dp[-1] != 10001 else -1)
        
    
# 이문제는 dp문제이다.

def solution(n):
    answer = 0
    dp =[[0]*2000 for _ in range(2)]
    ans = [0 for _ in range(2000)]
    dp[0][0] = 1
    dp[1][0] = 0
    dp[0][1] = 1
    dp[1][1] = 1
    for i in range(2,n+1):
        dp[0][i] = 1
        dp[1][i] = dp[1][i-1]+dp[1][i-2] + 1
    
    return (dp[0][n-1] + dp[1][n-1]) % 1234567


print(solution(5))
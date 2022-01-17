# 규칙을 찾아야한다.
# dp 문제이다.

import sys
input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31) ]
#i 는 w의 개수, j는 h의 개수로 dp[i][j] 는 w i 개 h j개로 만들 수 있는 경우의 수

#w가 없고 h 만 남아있다면 어차피 경우의 수는 h를 선택하는 방법 밖에 없기 때문에
#dp[0][h] 를 1로 초기화 해준다.
for j in range(1,31):
    dp[0][j] = 1

for i in range(1,31):
    for j in range(30):
        # h가 하나도 없을 때 w를 하나먹으면 h가 하나 무조건 생긴다.
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
            # 반쪽 자리 j 가 하나라도 있으면 h 를 먹을 때와  w 를 먹을 때 두가지 경우를 구해서 더해준다.
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i][j-1]

while 1:
    n = int(input())
    # 이 입력되면 입력을 멈춘다.
    if n == 0:
        break
    print(dp[n][0])
###################################3
n = int(input())
for j in range(1,31):
    dp[0][j] = 1

for i in range(1,31):
    for j in range(i,31):
        dp[i][j] += dp[i-1][j] + dp[i][j-1]

while 1:
    n = int(input())
    if n == 0:
        break
    print(dp[n][n])





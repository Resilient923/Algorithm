# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int,input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))
# dp = [[0] * (n+1) for _ in range(n+1)]
        

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         dp[i][j] = dp[i][j-1] + dp[i-1][j] + graph[i-1][j-1] - dp[i-1][j-1]
# print(dp)
# for _ in range(m):
#     i,j,x,y = map(int,input().split())
#     print(dp[x][y]-dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1])


#시간초과코드
# while q:
#     x1,y1,x2,y2 = q.popleft()
#     cnt = 0
#     for i in range(x1-1,x2):
#         for j in range(y1-1,y2):
#             cnt += graph[i][j]
#     print(cnt)

import sys

n,m = map(int,input().split())

dp = [[0]*(n+1) for _ in range(n+1)]

graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = graph[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(dp[x2][y2] - dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])


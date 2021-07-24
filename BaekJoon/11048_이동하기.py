#이문제는 dfs문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dp =[[0]*(m+1) for _ in range(n+1)]

#dp[0][0] = graph[0][0]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+graph[i-1][j-1]
print(dp[n][m])


# #################################################
# def dfs(x,y,candy,visited):
#     global Max
#     if x == n-1 and y == m-1:
#         candy += graph[x][y]
#         if Max<candy:
#             Max = candy
#         return 
#     if 0 <= x < n and 0 <= y < m and visited[x][y] == 0:
#         visited[x][y] = 1
#         dfs(x+1,y,candy+graph[x][y],visited)
#         dfs(x,y+1,candy+graph[x][y],visited)
#         dfs(x+1,y+1,candy+graph[x][y],visited)

# Max = 0
# candy = 0
# visited = [[0]*m for _ in range(n)]
# #dfs(0,0,candy,visited)
# print(Max)
import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
#dp풀이
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            break
        nx = i + graph[i][j]
        ny = j + graph[i][j]
        if 0 <= nx < n:
            dp[nx][j] += dp[i][j]
        if 0 <= ny < n:
            dp[i][ny] += dp[i][j]
print(dp[n-1][n-1])

""" def dfs(x,y):
    global cnt
    if x==n-1 and y==n-1:
        cnt+=1
        return 
    length = graph[x][y]
    dx = [0,length]
    dy = [length,0]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<n:
            dfs(nx,ny)


            
cnt = 0
dfs(0,0)
print(cnt) """

""" def bfs(x,y):
    global cnt
    if x==n-1 and y==n-1:
        cnt+=1
        return 
    length = graph[x][y]
    q = deque()
    q.append((x,y)) 
    while q:
        a,b = q.popleft()
        dx = [0,length]
        dy = [length,0]
        for i in range(2):
            nx = a + dx[i]
            ny = b + dy[i]
            if -1<nx<n and -1<ny<n:
                q.append((nx,ny)) """
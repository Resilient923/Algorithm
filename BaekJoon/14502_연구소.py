import sys,copy
from collections import deque

input = sys.stdin.readline


dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1 #처음0의개수
max_result = 0
# dfs함수안에서 퍼지는 바이러스의 수를 구할 bfs함수
def virus():
    visited = [[0] * m for _ in range(n)]
    global max_result
    # print(graph)
    # graph = copy.deepcopy(graph)
    result = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                visited[i][j] = 1
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <=ny < m and visited[nx][ny]==0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    # graph[nx][ny] = 2
                    result += 1
                    q.append((nx,ny))
    # for i in range(n):
    #     for j in range(m):
    #         if graph[i][j] == 0:
    #             result += 1
    # dfs함수안에서는 안전영역 max 값( 2의 개수 최솟값)을 갱신해야한다.             
    max_result = max(max_result,cnt-result)

# 1 3개로 벽을 세우는 경우의 수를 구하는 dfs 함수
def wall_dfs(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall_dfs(cnt+1)
                graph[i][j] = 0
wall_dfs(0)
print(max_result-3)



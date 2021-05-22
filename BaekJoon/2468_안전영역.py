import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<n and visited[nx][ny] == 0 and graph[nx][ny]>h:
            visited[nx][ny] = 1
            dfs(nx,ny,h)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

high = 0
for i in range(len(graph)):
    for j in graph[i]:
        if j > high:
            high = j

num = 1
for i in range(high):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j,k,i)
    num = max(num,cnt)

print(num)
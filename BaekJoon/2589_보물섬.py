import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(2500)
n,m = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y,cnt))
    visited[x][y] = 1 #방문처리
    while q:
        x,y,cnt= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and visited[nx][ny]==0 and graph[nx][ny]=='L':
                visited[nx][ny] = 1
                # 한칸이동할떄마다 값을 갱신해주기위해서 cnt+1을 해준다.
                q.append((nx,ny,cnt+1))
    return cnt
               

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            # bfs는 최단거리로 움직이기 때문
            # 각각 i,j 마다 bfs를 실행시켜준다.
            visited = [[0]*m for _ in range(n)]
            ans = max(ans,bfs(i,j,0))

print(ans)
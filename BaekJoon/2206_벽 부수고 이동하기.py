import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph  = []
for _ in range(n):
    graph.append(list(input().rstrip()))
# print(graph)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = [[0]* m for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][wall] == 0:
                if graph[nx][ny] == '0':
                    q.append((nx,ny,wall))
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                if wall == 0 and graph[nx][ny] == '1':
                    q.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][wall] + 1
        print(q)

                #  if wall == '0':
                #     q.append((graph[nx][ny],nx,ny))
                #     cnt[nx][ny] = cnt[x][y] + 1
                #     visited[nx][ny] = 1
                #  elif  wall == '1' and graph[nx][ny] == '0' and flag == 0:
                #     cnt[nx][ny] = cnt[x][y] + 1
                #     visited[nx][ny] = 1
                #     q.append(('0',nx,ny))
                #     flag = 1
        # print(q)
    return -1

# print(visited)
# print(cnt)
# if visited[n-1][m-1] == 0:
#     print(-1)
# else:
#     print(cnt[n-1][m-1])
print(bfs())
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
data = []
data = [input().rstrip() for _ in range(m)]
# print(data)
visited = [[0]*n for _ in range(m)]
count = [[0]*n for _ in range(m)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()

# print(data)
def bfs():
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                # print(nx,ny)
                if data[nx][ny] == '0':
                    # 순서를 1보다 0 일경우를 더먼저 고려하기위해
                    # appendleft를 사용한다.
                    q.appendleft((nx,ny))
                    count[nx][ny] = count[x][y]
                elif data[nx][ny] == '1':
                    q.append((nx,ny))
                    count[nx][ny] = count[x][y] + 1

bfs()
print(count[m-1][n-1])


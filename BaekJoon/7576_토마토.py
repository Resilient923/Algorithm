import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int,input().split())

data = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    data.append(list(map(int,input().split())))

queue = deque()
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>-1 and nx<n and ny>-1 and ny<m:
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y]+1
                    queue.append((nx,ny))
            
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append((i,j))
bfs()
flag = 0
result = -2
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            flag = 1
        result = max(result,data[i][j])
if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
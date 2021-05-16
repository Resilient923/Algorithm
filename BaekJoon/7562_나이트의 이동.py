import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(start_x,start_y,final_x,final_y):
    q = deque()
    q.append([start_x,start_y])
    visited[start_x][start_y]  = 1
    while q:
        x,y = q.popleft()
        if x==final_x and y==final_y:
            print(visited[x][y]-1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y]+1


    
loop = int(input())
for i in range(loop):
    n = int(input())
    start_x,start_y = map(int,input().split())
    final_x,final_y = map(int,input().split())
    visited = [[0]*n for _ in range(n)]
    bfs(start_x,start_y,final_x,final_y)

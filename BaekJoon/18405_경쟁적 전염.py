import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
s,x,y = map(int,input().split())

#bfs 문제
# 상,하,좌,우 번호가 낮은 종류의 바이러스부터 증식.
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                virus.append((graph[i][j],0,i,j))
    virus.sort(key=lambda x: x[0])
    q = deque(virus)
    while q:
        num,time,x,y = q.popleft()
        if time == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = num
                q.append((num,time+1,nx,ny))

bfs()
print(graph[x-1][y-1])




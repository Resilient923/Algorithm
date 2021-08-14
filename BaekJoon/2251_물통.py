import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())
Max = max(A,B,C)
c_check = [0 for _ in range(Max+1)]
visited = [[0]*201 for _ in range(Max+1)]
q = deque()
q.append([0,0,C])
def bfs():
    while q:
        a,b,c = q.popleft()
        if visited[a][c] == 1:
            continue
        else:
            visited[a][c] = 1
        if a == 0:
            c_check[c] = 1
        if a + b > B: 
            q.append([a + b - B, B, c])
        else: 
            q.append([0, a + b, c])
        if a + c > C: 
            q.append([a + c - C, b, C])
        else: 
            q.append([0, b, a + c])
        if b + a > A: 
            q.append([A, b + a - A, c])
        else: 
            q.append([b + a, 0, c])
        if b + c > C: 
            q.append([a, b + c - C, C])
        else: 
            q.append([a, 0, b + c])
        if c + a > A: 
            q.append([A, b, c + a - A])
        else: 
            q.append([c + a, b, 0])
        if c + b > B: 
            q.append([a, B, c + b - B])
        else: 
            q.append([a, c + b, 0])

bfs()
for i in range(Max+1):
    if c_check[i] == 1:
        print(i,end=" ")

import sys
input = sys.stdin.readline
from collections import deque
f,s,g,u,d = map(int,input().split())

visited =  [0 for _ in range(f)]
result = [0 for _ in range(f)]
# result[s-1] = 0
dfloor = [u,-d]

def bfs():
    q= deque()
    visited[s-1] = 1
    q.append(s-1)
    while q:
        floor = q.popleft()
        for i in range(2):
            next_floor = floor + dfloor[i]
            if 0<=next_floor<f and visited[next_floor]==0:
                result[next_floor] = result[floor]+1
                q.append(next_floor)
                visited[next_floor] =1
bfs()
print(result[g-1] if result[g-1] != 0 else "use the stairs")

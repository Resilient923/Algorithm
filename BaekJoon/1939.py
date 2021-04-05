import sys
input = sys.stdin.readline
from heapq import heappop,heappush
from collections import deque

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append([b,cost])
    graph[b].append([a,cost])
start,end = map(int,input().split())

MIN,MAX = 1,1000000000

def bfs(weight):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        a = queue.popleft()
        for x,y in graph[a]:
            if not visited[x] and y >=weight:
                visited[x] = True
                queue.append(x)
    if visited[end]==True:
        return True
    else:
        return False    


ans = 0
while MIN<=MAX:
    visited = [False] * (n+1)
    mid = (MIN+MAX)//2
    if bfs(mid):
        ans = mid
        MIN = mid + 1
    else:
        MAX = mid -1
print(ans)




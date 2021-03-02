from collections import deque
import sys

def bfs(graph, start, visited) :
    q = deque()
    q.append(start)
    while q :
        start = q.popleft()
        visited[start] = True
        for x in graph[start]:
            if visited[x] is False and q.__contains__(x) is False:
                q.append(x)

n,m = map(int,input().split())

graph = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

result = 0
for i in range(1,n+1) :
    if visited[i] is False :
        result = result + 1
        bfs(graph, i, visited)
print(result)
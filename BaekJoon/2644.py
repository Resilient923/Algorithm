from collections import deque

n = int(input())
a,b = map(int,input().split())
lines = int(input())
graph = [[] for i in range(n+1)]
for _ in range(lines):
    node, connected = map(int,input().split())
    graph[node].append(connected)
    graph[connected].append(node)


result=[0 for i in range(n+1)]
def bfs(start):
    queue = deque()
    queue.append(start)
    visited_bfs = [0 for i in range(n+1)]
    visited_bfs[start]=1
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if visited_bfs[i]==0:
                visited_bfs[i]=1
                result[i] = result[q]+1
                queue.append(i)
bfs(a)        
print(result[b] if result[b] !=0 else -1)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited= [False] * (n+1)
def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i]==False:
            dfs(i)


for _ in range(m):
    node1,node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

cnt = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        cnt +=1
print(cnt)
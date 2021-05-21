import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
data = []
graph = [[] for _ in range(n)]
answer = [[0]*n for _ in range(n)]
for _ in range(n):
    data.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            graph[i].append(j)
#dfs사용
def dfs(start,graph,visited):
    for i in graph[start]:
        if visited[i]==0:
            visited[i] = 1
            dfs(i,graph,visited)
    
    return visited

for i in range(n):
    visited = [0] * n 
    answer[i] = dfs(i,graph,visited)
    print(answer[i])
for i in range(n):
    for j in range(n):
        print(answer[i][j],end=" ")
    print()
    

#bfs사용
""" for i in range(n):
    stack = [i]
    visited = []
    while stack:
        cur = stack.pop()
        for j in graph[cur]:
            if j not in visited:
                answer[i][j] += 1
                stack.append(j)
                visited.append(j)

for i in answer:
    print(' '.join(map(str,i))) """

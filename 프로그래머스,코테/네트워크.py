n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]



import sys
sys.setrecursionlimit(10000)

def solution(n, computers):
    visited = [False]*(n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i != j:
                if computers[i][j] == 1:
                    graph[i+1].append(j+1)
                    
    def dfs(start):
        visited[start] = True
        for i in graph[start]:
            if visited[i]==False:
                dfs(i)
    answer = 0
    for i in range(1,n+1):
        if visited[i] == False:
            dfs(i)
            answer += 1
    return answer

print(solution(n,computers))
import sys
input = sys.stdin.readline

cnt = 0
#dfs
def dfs(x, y, way):# way를 flag 처리
    global cnt
    
    if way == 0:
        if y + 1 < n and graph[x][y + 1] == 0: 
            dfs(x, y + 1, 0)
        if x + 1 < n and y + 1 < n:
            if graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0 and graph[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
    elif way == 1:
        if x + 1 < n and graph[x + 1][y] == 0: 
            dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n:
            if graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0 and graph[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
    elif way == 2:
        if y + 1 < n and graph[x][y + 1] == 0: 
            dfs(x, y + 1, 0)
        if x + 1 < n and graph[x + 1][y] == 0: 
            dfs(x + 1, y, 1)
        if x + 1 < n and y + 1 < n:
            if graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0 and graph[x + 1][y] == 0:
                dfs(x + 1, y + 1, 2)
    if x == n - 1 and y == n - 1: 
        cnt += 1
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dfs(0, 1, 0)
print(cnt)




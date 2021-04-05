import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(i, j):
    global minLength
    if i <= -1 or i > n-1 or j <= -1 or j > n-1:
        return    
    if graph[i][j] == 0:
        return
    
    for pre in range(0, num): # 1~(num-1)번 
        for x,y in island[pre]:
            distance = abs(i-x) + abs(j-y) - 1
            if distance < minLength:
                minLength = distance
    graph[i][j] = 0  
    island[num].append((i,j)) #좌표들을 섬의 번호에 맞게 리스트로 만들어준다.
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

num = 0
island = [[] for _ in range(100000)]
minLength = 10000
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            num += 1 
            dfs(i,j)


print(minLength)

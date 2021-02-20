INF = int(1e9)
n = int(input())
graph = [[INF]*n for i in range(n)]
distance = []
result = 0
for i in range(n):
    distance.append(list(map(int,input().split())))
for a in range(n):
    for b in range(n): #시작노드
        for c in range(n): #도착노드
            if a==b or b==c or a==c:
                continue
            elif distance[b][c]==distance[b][a]+distance[a][c]:
                graph[b][c] = 1
            elif distance[b][c] > distance[b][a] + distance[a][c]:
                result = -1
if result!=-1:
    for i in range(n):
        for j in range(i,n):
            if graph[i][j] == INF:
                result += distance[i][j]
print(result)

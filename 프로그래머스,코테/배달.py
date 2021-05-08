import sys
sys.setrecursionlimit(100000)

road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
def solution(N, road, K):
    answer= 0 
    INF = int(1e9)
    graph = [[INF]*N for _ in range(N)]
    for i in range(N):
         graph[i][i] = 0
    for r in road:
        a,b,c = r
        if graph[a-1][b-1] > c:
            graph[a-1][b-1] = graph[b-1][a-1] = c
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
    for i in range(N):
        if graph[0][i] <= K:
            answer +=1 
    return answer
print(solution(6,road,4))



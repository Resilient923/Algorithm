n = 6
s = 4
a = 6
b = 2
#최단거리 플로이드워셜
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for fare in fares:
        i,j,k = fare
        graph[i-1][j-1] = graph[j-1][i-1] = k
    for i in range(n):
        for j in range(n):
            for k in range(n):
                """ graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])  """
                # min들어가면 무조건 시간초과. for 3번에 min이면....
                if graph[j][k] > graph[j][i]+graph[i][k]:
                    graph[j][k] = graph[j][i]+graph[i][k]
    answer = INF
    for i in range(n):
        answer = min(answer,graph[s-1][i]+graph[i][a-1]+graph[i][b-1])

    return answer

print(solution(n,s,a,b,fares))
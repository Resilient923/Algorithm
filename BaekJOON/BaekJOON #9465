n = int(input())

for i in range(n):
    graph = []
    m= int(input())
    for j in range(2): #시작을 이렇게 한다.
        graph.append(list(map(int, input().split())))
    graph[0][1] += graph[1][0]
    graph[1][1] += graph[0][0]
    for k in range(2, m):
        graph[0][k] += max(graph[1][k - 1], graph[1][k - 2])
        graph[1][k] += max(graph[0][k - 1], graph[0][k - 2])
    print(max(graph[0][m - 1], graph[1][m - 1]))

import sys

# 도시의개수
n = int(input())
# 버스의 개수
m = int(input())
INF = 987654321
# 최소비용을 구하기 위한 문제이기 때문에
# INF로 초기화 해주고 갱신해준다.
graph = [[INF] *n for i in range(n)]
# print(graph)

# 시작 도시와 도착 도시를 연결하는 노선은 여러개다
# 이중에 최소비용만 담고 있으면 되기 때문에 갱신이 필요하다.
for _ in range(m):
    start,end,dis = map(int,input().split())
    # 가장 짧은거만 판단하면 되는거아닌가..? 작은걸로 갱신해서 값 넣어주기
    if graph[start-1][end-1] > dis:
        graph[start-1][end-1] = dis

# 플로이드 워셜 구현
# j에서 k로 갈 때 i를 거쳐서 가는경우와 바로 가는 경우를 비교해서
# 더 작은 값을 갱신해준다.
for i in range(n):
    for j in range(n):
        for k in range(n):
                if graph[j][k] > graph[j][i]  + graph[i][k] and  j != k:
                    graph[j][k]  = graph[j][i]  + graph[i][k]
         
# 만약 INF가 담겨있다면 방문을 하지 않은 것이기 때문에 0으로 바꿔준다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 987654321:
            graph[i][j] =0

# 출력
for i in range(n):
    print(*graph[i])
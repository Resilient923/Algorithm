import sys
input = sys.stdin.readline

INF = 1e9

#노드의 개수와 간선의 개수 입력받기
n,m = map(int,input())
#시작노드 입력받기
start = int(input())
#노드들 정보 받기
graph = [[]for _ in range(n+1)]

def smallest_node_number():
    min_number = INF
    node_idx = 0
    for i in range(1,n+1):
        if distance[i] < min_number and not visited[i]:
            min_number = distance[i]
            node_idx = i
    return node_idx
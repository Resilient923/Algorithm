import sys
sys.setrecursionlimit(300000)
a= [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
# a = [0,1,0]
# edges = [[0,1],[1,2]]
answer = 0
def dfs(graph, a, visited,start):
        global answer
        # 현재 노드를 방문 처리
        visited[start] = True
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for next_node in graph[start]:
            if not visited[next_node]:
                node_num = dfs(graph, a, visited,next_node)
                a[start] += node_num
                answer += abs(node_num)
        return a[start]

def solution(a, edges):
    if sum(a) != 0:
        return -1
    visited = [False for _ in range(len(a)+1)]
    graph = [[] for _ in range(len(edges)+1)]
    for i in edges:
        node1,node2 = i
        graph[node1].append(node2)
        graph[node2].append(node1)
    dfs(graph,a,visited,0)
    return answer

print(solution(a,edges))
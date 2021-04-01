import sys
from heapq import heappop,heappush
input = sys.stdin.readline

inf = 987654321
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dp = [inf for _ in range(n+1)]
for i in range(m):
    a,b,cost = map(int,input().split())
    graph[a].append([b,cost])
start,end = map(int,input().split())

def dijkstra(start):
    dp[start] = 0
    heap=[]
    heappush(heap,[0,start])
    while heap:
        cost, node = heappop(heap)
        if dp[node] < cost:
            continue
        for n_node, weight in graph[node]:
            dp_cost = cost + weight
            if dp[n_node] > dp_cost:
                dp[n_node] = dp_cost
                heappush(heap, [dp_cost, n_node])
dijkstra(start)
print(dp[end])
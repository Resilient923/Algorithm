import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


min_diff = 1e9

team = [i for i in range(n)]

member = list(combinations(team,n//2))


for start in member:

    link = [x for x in team if x not in start]

    start_score = 0
    link_score = 0

    for a,b in list(combinations(start,2)):
        start_score += (graph[a][b] + graph[b][a])

    for a,b in list(combinations(link,2)):
        link_score += (graph[a][b] + graph[b][a])

    min_diff = min(min_diff, abs(start_score - link_score))

print(min_diff)
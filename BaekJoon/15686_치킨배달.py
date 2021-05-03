import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

pick_chicken = list(combinations(chicken,m))

ans = []
for i in pick_chicken:
    total = 0
    for j in house:
        Min = 10001
        for k in i:
            dist = abs(k[0]-j[0])+abs(k[1]-j[1])
            Min = min(Min,dist)
        total += Min
    ans.append(total)
print(min(ans))



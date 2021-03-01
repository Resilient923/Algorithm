""" n =int(input())

data = []
dp = [[0]*n for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        dp[i][j] = graph[i][j] + graph[j][i]
        dp[j][i] = dp[i][j]
        data.append(dp[j][i])
result = [data[i * n:(i + 1) * n] for i in range((len(data) - 1 + n) // n )] #list comprehension
print(result)
dp2 = []
for i in result:
    for j in i:
        if i.index(j) > i.index(0):
            dp2.append(j)
print(dp2)
ans = []
for i in range(len(dp2)):
    for j in range(len(dp2)):
        if i == j:
            continue
        if int(dp2[i]-dp2[j]) >=0:
            ans.append(int(dp2[i]-dp2[j]))
print(min(ans)) """

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
ans = 10000000
team = [i for i in range(n)]

members = list(combinations(team, n // 2))

for team1 in members:
    
    team2 = [x for x in team if x not in team1]
    
    team1_score = 0
    team2_score = 0
    for x, y in list(combinations(team1, 2)):
        
        team1_score += graph[x][y] + graph[y][x]
    for x, y in list(combinations(team2, 2)):
        team2_score += graph[x][y] + graph[y][x]
    ans = min(ans, abs(team1_score - team2_score))

print(ans)





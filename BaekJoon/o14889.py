n =int(input())

ans = []
dp = [[0]*n for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
print(graph)
for i in range(n):
    for j in range(n):
        dp[i][j] = graph[i][j] + graph[j][i]
        dp[j][i] = dp[i][j]
        ans.append(dp[j][i])
print(set(ans))
dp2 = []
for i in set(ans):
    for j in set(ans):
        if i == j:
            continue 
        if(i-j)>=0:
            dp2.append(i-j)

print(min(dp2))

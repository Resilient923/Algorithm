import sys
sys.setrecursionlimit(10000)


tc = int(input())
for _ in range(tc):
    n,m,cab= map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    for _ in range(cab):
        r,c = map(int,input().split())
        graph[r][c] = 1

    def dfs(x,y):
        if x<= -1 or x>=n or y<=-1 or y>=m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    print(result)

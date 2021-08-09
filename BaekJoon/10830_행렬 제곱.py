import sys
input = sys.stdin.readline

n,b = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

def dfs(List,b):
    temp = [[0]*n for _ in range(n)]
    if b == 1:
        for i in range(n):
            for j in range(n):
                List[i][j] %= 1000
        return List
    elif b % 2 == 1:
        divide_matrix = dfs(List,b-1)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp[i][j] += divide_matrix[i][k] * List[k][j]
                temp[i][j] %= 1000
        return temp
    elif b % 2 == 0:
        divide_matrix = dfs(List, b // 2)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp[i][j] += divide_matrix[i][k] * divide_matrix[k][j]
                temp[i][j] %= 1000
        return temp

ans = dfs(data,b)

for i in ans:
    for j in i :
        print(j,end=" ")
    print()

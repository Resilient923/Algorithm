import sys
input = sys.stdin.readline

n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

check = [[0]*101 for _ in range(101)]

for _ in range(n):
    x,y,d,g = map(int,input().split())
    check[x][y] = 1

    moving = [d]

    for i in range(g):
        temp = []
        for j in range(len(moving)):
            temp.append((moving[-j-1]+1) % 4)
        moving.extend(temp)
    
    for i in moving:
        nx = x + dx[i]
        ny = y + dy[i]
        check[nx][ny] = 1
        x = nx
        y = ny
result = 0
for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
            result += 1
print(result)
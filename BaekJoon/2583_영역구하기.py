import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global num
    num += 1
    """  graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > -1 and nx < m and ny > -1 and ny < n:
            if graph[nx][ny] == 0:
                dfs(nx,ny) """
    
    if x <= -1 or x > m-1 or y <= -1 or y > n-1:
        return
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1) 
        dfs(x, y-1)
        
    

m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]
data = []
# 아래 코드가 그래프를 우리가 아는 그래프로 변환하는 과정
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    data.append([m-y2,x1,n-y1-(n-m),x2]) #이 코드로 바꿔서 변환해준다.
for i in range(len(data)):
    for j in range(data[i][0],data[i][2]):
        for k in range(data[i][1],data[i][3]):
            graph[j][k] = 1
""" for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range((m-y2),(m-y1),1):
        for x in range(x1,x2,1):
            graph[y][x] = 1 """

#분리된영역의 개수들을 담을 list
numlist = []


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            num = 0
            dfs(i,j)
            numlist.append(num)
print(len(numlist))
for i in sorted(numlist):
    print(i,end=' ')

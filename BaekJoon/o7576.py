import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
data =[]
for i in range(n):
    data.append(list(map(int,input().split())))
queue = deque()
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and data[nx][ny]==0:
                data[nx][ny] = data[x][y] + 1
                queue.append([nx,ny])
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append([i,j])
#bfs함수실행
bfs()
isTrue = 0
result = -2
for i in data:
    for j in i:
        if j==0:
            isTrue = 1
        result = max(result,j) 
#bfs 함수를 실행하고나서도 0이 있으면 -1을 출력
if isTrue == 1:
    print(-1)
#가장큰값이 -1이면 0을 출력
elif result == -1:
    print(0)
#둘다아니면 제일 큰값에 -1을 한 값을 출력
else:
    print(result-1)
             
""" for i in range(n):
    for j in range(m):
        if (data[i][j]==1):
            tomato.append((j,i))
def bfs(x,y):
    ans =0
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                
            if data[nx][ny]==-1:
                continue
            if data[nx][ny]==0:
                data[nx][ny] = data[x][y] +1
                queue.append((nx,ny))
                ans +=1
    return ans
result = 0
for i in tomato:
    result += bfs(i[0],i[1])
print(result)


for i in tomato:
    print(i[0],i[1])
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if data[x][y]==0:
        data[x][y]==1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    elif data[x][y] == -1:
        return False
    return False

ans = 0
for i in tomato:
    if dfs(i[0],i[1]) ==True:
        ans +=1
print(ans) """



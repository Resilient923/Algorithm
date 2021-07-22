import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)
n = int(input())
data = [list(input().rstrip()) for _ in range(n)]
temp_data = data
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#색맹아님
def not_cb_dfs(x,y):
    not_cb_visited[x][y] = 1 # 방문처리하고
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < n:
            if data[nx][ny] == data[x][y] and not_cb_visited[nx][ny] == 0:
                not_cb_dfs(nx,ny)

#색맹임
def cb_dfs(x,y):
    cb_visited[x][y] = 1 # 방문처리하고
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < n:
            if temp_data[nx][ny] == temp_data[x][y] and cb_visited[nx][ny] == 0:
                cb_dfs(nx,ny)
 
###############
#색맹아닌사람
not_cb_visited = [[0]*n for _ in range(n)]
not_cb_cnt = 0

for i in range(n):
    for j in range(n):
        if not_cb_visited[i][j]==0:
            not_cb_dfs(i,j)
            not_cb_cnt += 1
################################################################
#색맹인사람
for i in range(n):
    for j in range(n):
        if temp_data[i][j]=='G':
            temp_data[i][j] = 'R'

cb_visited =[[0]*n for _ in range(n)]
cb_cnt = 0
for i in range(n):
    for j in range(n):
        if cb_visited[i][j]==0:
            cb_dfs(i,j)
            cb_cnt += 1

print(not_cb_cnt,cb_cnt)
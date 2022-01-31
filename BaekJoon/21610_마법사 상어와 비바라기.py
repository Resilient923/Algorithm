import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)]

move_list = []
for i in range(m):
    move_way,move_cnt = list(map(int,input().split()))
    move_list.append([move_way-1,move_cnt])

clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
copy_dx = [-1,-1,1,1]
copy_dy = [-1,1,-1,1]

for i in range(m):
    move_way,move_cnt = move_list[i]
    #1.이동한구름위치를 nextclouds에 넣어준다.
    nextcloud = []
    for cloud_x,cloud_y in clouds:
        nx = (cloud_x + dx[move_way] * move_cnt) % n
        ny = (cloud_y + dy[move_way] * move_cnt) % n 
        nextcloud.append([nx,ny])
   
    visited = [[0]*n for _ in range(n)]
    for cloud_x,cloud_y in nextcloud:
        # 지금 칸에 비를 뿌린다.
        graph[cloud_x][cloud_y] += 1
         #방문처리 
        visited[cloud_x][cloud_y] = 1
    #3.구름이 모두사라진다
    clouds = []

    # 물복사버그 대각선으로 퍼진다
    for _x,_y in nextcloud:
        cnt = 0
        for i in range(4):
            nx = _x+ copy_dx[i]
            ny = _y+ copy_dy[i]
            if 0<= nx <n and 0<= ny <n and graph[nx][ny]: # 물이 있을 때 개수를 세서 
                cnt += 1
        graph[_x][_y] += cnt # 더해준다.

    # 4. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2 and visited[i][j] == 0:
                graph[i][j] -= 2
                clouds.append([i,j])
total = 0
for i in range(n):
    total += sum(graph[i])
print(total)
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
move_list = []
for i in range(m):
    temp = list(map(int,input().split()))
    move_list.append([temp[0]-1,temp[1]])

clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for i in range(m):
    move = move_list[i]
    #1.이동한구름위치
    nextcloud = []
    for cloud in clouds:
        #이게맞나ㅅㅂ...
        nx = (cloud[0] + dx[move[0]] * move[1]) % n
        ny = (cloud[1] + dy[move[0]] * move[1]) % n 
        nextcloud.append([nx,ny])
    #방문처리 및 저장된 물의 양의 1증가한다.
    visited = [[False]*n for _ in range(n)]
    for cloud in nextcloud:
        A[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = True
    #3.구름이 모두사라진다
    clouds = []

    # 물복사버그 대각선으로 퍼진다
    dx2 = [-1,-1,1,1]
    dy2 = [-1,1,-1,1]
    for cloud in nextcloud:
        cnt = 0
        for i in range(4):
            nx = cloud[0] + dx2[i]
            ny = cloud[1] + dy2[i]
            if 0<= nx <n and 0<= ny <n and A[nx][ny]:
                cnt += 1
        A[cloud[0]][cloud[1]] += cnt
    # 4. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for i in range(n):
        for j in range(n):
            if A[i][j] >= 2 and visited[i][j] == False:
                A[i][j] -= 2
                clouds.append([i,j])
total = 0
for i in range(n):
    total += sum(A[i])
print(total)



""" def move(move_list,cloud):
    if move_list[0] == 1:
        for i in range(len(cloud)):
            cloud[i][1] = (n+cloud[i][1]+move_list[1]) % n
    elif move_list[0] == 2:
        for i in range(len(cloud)):
            cloud[i][0] = (n+cloud[i][0]-move_list[1]) % n
            cloud[i][1] = (n+cloud[i][1]+move_list[1]) % n
    elif move_list[0] == 3:
        for i in range(len(cloud)):
            cloud[i][0] = (n+cloud[i][0]-move_list[1]) % n
    elif move_list[0] == 4:
        for i in range(len(cloud)):
            cloud[i][0] = (n+cloud[i][0]-move_list[1]) % n
            cloud[i][1] = (n+cloud[i][1]+move_list[1]) % n
    elif move_list[0] == 5:
        for i in range(len(cloud)):
            cloud[i][1] = (n+cloud[i][1]+move_list[1]) % n
    elif move_list[0] == 6:
        for i in range(len(cloud)):
            cloud[i][0] = (n+cloud[i][0]+move_list[1]) % n
            cloud[i][1] = (n+cloud[i][1]+move_list[1]) % n
    elif move_list[0] == 7:
        for i in range(len(cloud)):
            cloud[i][0] = (n+cloud[i][0]+move_list[1]) % n
    elif move_list[0] == 8:
        for i in range(len(cloud)):
            cloud[i][0] = (n+cloud[i][0]+move_list[1]) % n
            cloud[i][1] = (n+cloud[i][1]-move_list[1]) % n
    return cloud """

   
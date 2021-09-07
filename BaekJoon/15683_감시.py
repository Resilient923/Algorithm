import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(cnt):
    global check, ans
    if cnt == cctv_n: # 모든 CCTV 탐색했다면 사각지대 개수 세주기
        tmp = 0
        for i in range(n):
            for j in range(m):
                if not data[i][j] and not check[i][j]:
                    tmp += 1
        return tmp

    x = cctv[cnt][0]
    y = cctv[cnt][1]

    for i in range(4): 
        # CCTV 의 4방향 확인
        way = []
        if data[x][y] == 1: 
            # 1번 CCTV : 현재 방향
            way.append(i)
        elif data[x][y] == 2: 
            # 2번 CCTV : 현재 방향 + 반대 방향
            way.append(i)
            way.append((i + 2) % 4)
        elif data[x][y] == 3: 
            # 3번 CCTV : 현재 방향 + 왼쪽 90도 방향
            way.append(i)
            way.append((i - 1) % 4)
        elif data[x][y] == 4: 
            # 4번 CCTV : 현재 방향 + 반대 방향 + 왼쪽 90도 방향
            way.append(i)
            way.append((i - 1) % 4)
            way.append((i + 2) % 4)
        elif data[x][y] == 5: 
            # 5번 CCTV : 4방향
            way.append(i)
            way.append((i - 1) % 4)
            way.append((i + 1) % 4)
            way.append((i + 2) % 4)
        q = deque()

        for j in way: # CCTV 방향 개수 만큼 이동
            nx = x + dx[j]
            ny = y + dy[j]
            while 0 <= nx < n and 0 <= ny < m: # 특정 방향으로 끝까지 이동
                if not check[nx][ny] and data[nx][ny] != 6: # 방문하지 않았으며 벽이 아니면
                    check[nx][ny] = 1 # 방문
                    q.append((nx, ny))
                elif data[nx][ny] == 6: 
                    break # 벽이면 중단
                nx += dx[j]
                ny += dy[j]
        # 다음 CCTV 호출
        ans = min(ans, dfs(cnt + 1))
        # 방문했던 곳 되돌려주기
        while q:
            qx, qy = q.popleft()
            if not data[qx][qy]:
                check[qx][qy] = 0
        # 5번 CCTV 는 회전할 필요 없으므로 바로 break
        if data[x][y] == 5: 
            break
    return ans


cctv = []
cctv_n = 0 # 전체 CCTV 개수
ans = 0 # 사각지대
check = [[0] * m for _ in range(n)] # 방문 여부 확인
for i in range(n):
    for j in range(m):
        if data[i][j] and data[i][j] != 6:
            cctv.append((i, j))
            check[i][j] = 1
            cctv_n += 1
        if not data[i][j]:
            ans += 1 # 최대 사각지대 구하기
dfs(0)
print(ans)

from copy import deepcopy
import sys
input = sys.stdin.readline
def fill(x, y, arr, d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 6:
                    break
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = "#"
            else:
                break
def dfs(arr, cnt):
    global result
    temp = deepcopy(arr)
    if cnt == cctv_cnt:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        return
    x, y, cctv = q[cnt]
    for i in direction[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt + 1)
        temp = deepcopy(arr)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]], 
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
n, m = map(int, input().split())
s = []
q = []
cctv_cnt = 0
result = 100000000
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(len(a)):
        if a[j] != 0 and a[j] != 6:
            q.append([i, j, a[j]])
            cctv_cnt += 1
dfs(s, 0)
print(result)
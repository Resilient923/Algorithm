import sys
input = sys.stdin.readline
from collections import deque

#way = 1:오른쪽   2:아래    3:왼쪽    4:위쪽
def direction(way):
    if way == 'L':
        if cur_way == [1,0]:
            return [0,1]
        elif cur_way == [0,1]:
            return [-1,0]
        elif cur_way == [-1,0]:
            return [0,-1]
        elif cur_way == [0,-1]:
            return [1,0]
    elif way == 'D':
        if cur_way == [1,0]:
            return [0,-1]
        elif cur_way == [0,-1]:
            return [-1,0]
        elif cur_way == [-1,0]:
            return [0,1]
        elif cur_way == [0,1]:
            return [1,0]

def if_snake_body(x,y):
    if (x,y) in snake:
        return 0
    return 1

n = int(input())
k = int(input())

graph =[[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    i,j = map(int,input().split())
    # 사과 위치 표시
    graph[i][j] = 1

# 방향 정보들을 dir_data deque에 넣어준다.
l = int(input())
dir_data = deque()
for _ in range(l):
    i,j = input().split()
    dir_data.append((int(i),j))

# 첫 시작은 오른쪽으로 간다.   
cur_way = [0,1]

# 뱀이 있는 x,y 좌표를 저정해줄 deque
snake = deque()
# 뱀은 무조건 1,1 에서 시작
snake.append((1,1))
# result는 걸리는 시간
result = 0

while 1:
    # 뱀의 머리 부분을 뽑아낸다 (가장 최근에 넣은 부분이 머리 부분이다.)
    snake_x,snake_y = snake[-1][0],snake[-1][1]
    snake_x += cur_way[0]
    snake_y += cur_way[1]
    # 벽에 안 부딪히고 뱀 몸하고 안 부딪히면 앞으로 한칸을 먹어준다.
    if 0 < snake_x <= n and 0 < snake_y <= n:
        if if_snake_body(snake_x,snake_y) == 0:
            break
        snake.append((snake_x,snake_y))
        # 만약에 사과가 있으면 한칸 먹어준 그대로 간다 (길이는 1개 증가)
        if graph[snake_x][snake_y] == 1:
            graph[snake_x][snake_y] = 0
        else:
            # 만약에 사과가 없으면 이미 한칸을 먹어줬으므로 뱀 꼬리를 잘라준다.
            snake.popleft()
    else:
        break
    # 걸리는 시간을 측정해준다.
    result += 1
    # 만약에 방향정보가 남아있고, 방향정보에서 시간을 다썼다면,
    if dir_data and result == dir_data[0][0]:
        #방향을 바꿔준다.
        cur_way = direction(dir_data[0][1])
        # 방향을 바꿔주고 나서는 dir_data에서 제외해준다.
        dir_data.popleft()

print(result + 1)
""" import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dice = [0,0,0,0,0,0]
order = list(map(int, sys.stdin.readline().split()))

def east(dice): 
    new_dice = [0,0,0,0,0,0]
    new_dice[0] = dice[3]
    new_dice[1] = dice[1]
    new_dice[2] = dice[0]
    new_dice[3] = dice[5]
    new_dice[4] = dice[4]
    new_dice[5] = dice[2]
    return new_dice
def west(dice):   
    new_dice = [0,0,0,0,0,0]
    new_dice[0] = dice[2]
    new_dice[1] = dice[1]
    new_dice[2] = dice[5]
    new_dice[3] = dice[0]
    new_dice[4] = dice[4]
    new_dice[5] = dice[3]
    return new_dice
def north(dice):   
    new_dice = [0,0,0,0,0,0]
    new_dice[0] = dice[4]
    new_dice[1] = dice[0]
    new_dice[2] = dice[2]
    new_dice[3] = dice[3]
    new_dice[4] = dice[5]
    new_dice[5] = dice[1]
    return new_dice
def south(dice):  
    new_dice = [0,0,0,0,0,0]
    new_dice[0] = dice[1]
    new_dice[1] = dice[5]
    new_dice[4] = dice[0]
    new_dice[5] = dice[4]
    new_dice[2] = dice[2]
    new_dice[3] = dice[3]
    return new_dice


# k번만큼 명령 수행
for i in order:
    if i == 1:      # 동쪽
        if y+1 < m:
            dice = east(dice)
            if graph[x][y+1] == 0:
                graph[x][y+1] = dice[5]
            else:
                dice[5] = graph[x][y+1]
                graph[x][y+1] = 0
            y += 1
            print(dice[0])

    elif i == 2:    # 서쪽
        if y-1 >= 0:
            dice = west(dice)
            if graph[x][y-1] == 0:
                graph[x][y-1] = dice[5]
            else:
                dice[5] = graph[x][y-1]
                graph[x][y-1] = 0
            y -= 1
            print(dice[0])

    elif i == 3:    # 북쪽
        if x-1 >= 0:
            dice = north(dice)
            if graph[x-1][y] == 0:
                graph[x-1][y] = dice[5]
            else: 
                dice[5] = graph[x-1][y]
                graph[x-1][y] = 0
            x -= 1
            print(dice[0])


        elif i == 4:    # 남쪽
            if x+1 < n:
                dice = south(dice)
                if graph[x+1][y] == 0:
                    graph[x+1][y] = dice[5]
                else:
                    dice[5] = graph[x+1][y]
                    graph[x+1][y] = 0
                x += 1
                print(dice[0]) """
#######################################################
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0,0,0,0,0,0]

for i in range(k):
    way = order[i] - 1
    nx = x + dx[way]
    ny = y + dy[way]
    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    if way == 0: # 동쪽
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif way == 1: # 서쪽
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif way == 2: # 북쪽
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif way == 3: # 남쪽
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])
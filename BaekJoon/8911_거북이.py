import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    data = input().rstrip()
    x = 0
    y = 0
    way = 1 # 처음 방향 1 : 위 2: 오른쪽 3: 아래 4 : 왼쪽
    point = []
    for i in data:
        # 방향이 1일 때
        if i == 'F' and way == 1:
            x -= 1
            point.append([x,y])
        elif i == 'B' and way == 1:
            x += 1
            point.append([x,y])
        elif i == 'R' and way == 1:
            way = 2
        elif i == 'L' and way == 1:
            way = 4
        elif i == 'F' and way == 2:
            y += 1
            point.append([x,y])
        elif i == 'B' and way == 2:
            y -= 1
            point.append([x,y])
        elif i == 'R' and way == 2:
            way = 3
        elif i == 'L' and way == 2:
            way = 1
        elif i == 'F' and way == 3:
            x += 1
            point.append([x,y])
        elif i == 'B' and way == 3:
            x -= 1
            point.append([x,y])
        elif i == 'R' and way == 3:
            way = 4
        elif i == 'L' and way == 3:
            way = 2
        elif i == 'F' and way == 4:
            y -= 1
            point.append([x,y])
        elif i == 'B' and way == 4:
            y += 1
            point.append([x,y])
        elif i == 'R' and way == 4:
            way = 1
        elif i == 'L' and way == 4:
            way = 3


    Max_x,Max_y = 0,0
    Min_x,Min_y = 0,0

    for i in range(len(point)):
        Max_x = max(Max_x,point[i][0])
        Min_x = min(Min_x,point[i][0])
        Max_y = max(Max_y,point[i][1])
        Min_y = min(Min_y,point[i][1])
    result = (Max_x-Min_x) * (Max_y-Min_y)

    sum_x = 0
    sum_y = 0
    x_zero_cnt = 0
    y_zero_cnt = 0
    for i in range(len(point)):
        if point[i][0] == 0:
            x_zero_cnt += 1
        if point[i][1] == 0:
            y_zero_cnt += 1
    if x_zero_cnt == len(point) or y_zero_cnt == len(point):
        print(0)
    else:
        print(result)

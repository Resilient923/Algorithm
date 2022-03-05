import sys
from collections import defaultdict
input = sys.stdin.readline

a,b = map(int,input().split())
n,m = map(int,input().split())

# 동,서,남,북 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 위치랑 처음 시작 방향 담는 리스트
data = defaultdict(tuple)

for idx in range(n):
    x,y,way = map(str,input().split())
    if way == 'E':
        save_way = 0
    elif way == 'S':
        save_way = 1
    elif way == 'W':
        save_way = 2
    elif way == 'N':
        save_way = 3
    # x,y 좌표 방향을 구하기 쉽게 바꿔서 저장한다.
    data[idx+1] = (b-int(y),int(x)-1,save_way)

#예외처리가 한번이라도 됐는지 체크하는 flag
flag = 0

# 로봇번호, 명령종류, 명령 횟수
for idx in range(m):
    Id, cmd, num = map(str,input().split())
    Id,num = int(Id),int(num)

    # 현재 비교할 로봇 데이터 pop 하기
    robot_x,robot_y,robot_way = data.pop(Id)
    
    if cmd == 'R':
        # 4번 다돌면 방향은 같으니까 나머지로만 구해줘도 된다.
        num = num % 4
        robot_way += (1 * num) % 4
        # 4번 다돌면 방향은 같으니까 나머지로만 구해줘도 된다.
    elif cmd == 'L':
        num = num % 4
        robot_way += (3 * num) % 4
    elif cmd == 'F':
        # 현재 방향만큼 앞으로 전진
        for i in range(num):
            robot_x += dx[robot_way]
            robot_y += dy[robot_way]
            # 여기서 로봇이 벽에 충돌할때 예외처리
            if not 0<= robot_x < b or not 0<= robot_y < a:
                    print('Robot {} crashes into the wall'.format(Id))
                    flag = 1
                    break
            # 여기서 이미 들어있는 로봇이라면 로봇끼리 충돌하니까
            # 예외처리 해준다.
            for key,value in data.items():
                # value중에 x,y 좌표만 확인하면된다.
                dif_x,dif_y,ignore_way = value
                if robot_x == dif_x and robot_y == dif_y:
                    print('Robot {} crashes into robot {}'.format(Id, key))
                    flag = 1
                    break
            # 예외처리 당했으면 루프 끝내서 다음 명령으로 넘어간다.
            if flag == 1:
                break
    # 예외처리 당했으면 루프 끝내서 다음 명령으로 넘어간다.
    if flag == 1:
        break
    # 예외처리 안당했으면, 로봇이 끝까지 명령에 따라 이동했기 때문에
    # 움직인 좌표로 갱신해준다.
    data[Id] = (robot_x, robot_y, robot_way)

# 만약에 예외처리가 한번도 이루어지지않았다면
# OK출력
if flag == 0:
    print("OK")


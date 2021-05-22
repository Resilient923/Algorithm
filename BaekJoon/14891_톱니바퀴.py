import sys
input = sys.stdin.readline

graph = [None]*4
for i in range(4):
    graph[i] = list(input().strip())

def dfs(x,y): # x는 바퀴번호 y는 방향  
    #인덱스 2, 인덱스 6 맞닿는다
    global visited
    if visited[x] == False:
        visited[x] = True
        left = graph[x][6]
        right = graph[x][2]
        if y == 1:
            flag = graph[x][7] #flag 처리
            for i in range(6,-1,-1):
                graph[x][i+1] = graph[x][i]
            graph[x][0] = flag
        else:
            flag  = graph[x][0]
            for i in range(7):
                graph[x][i] = graph[x][i+1]
            graph[x][7] = flag
        if x-1 >= 0 and left != graph[x-1][2]:
            dfs(x-1,-y)
        if x+1 <=3 and right != graph[x+1][6]:
            dfs(x+1,-y)


k = int(input())
for _ in range(k):
    a,b = map(int,input().split())
    visited = [False]*4
    dfs(a-1,b)

cnt = 0
for i in range(4):
    if graph[i][0] =='1':
        cnt += (2**i)
print(cnt)

##########################################
#성현풀이

""" import sys

def show(circle):
    for i in range(len(circle)):
        for s in circle[i]:
            print(s, end = ' ')
        print()


def rotateRight(array):             
    temp = array[:-1]
    temp.insert(0,array[-1])
    return temp

def rotateLeft(array):
    temp = array[1:]
    temp.append(array[0])
    return temp

if __name__ == "__main__":
    circle = []
    for _ in range(4):
        circle.append(list(map(int, sys.stdin.readline().rstrip())))
    # 양 옆, 인덱스를 맞춰주기 위해 처음 마지막에 톱니바퀴 추가
    circle.append([0,0,0,0,0,0,0,0]) 
    circle.insert(0,[0,0,0,0,0,0,0,0])

    
    k = int(input())
    # k번 회전
    for _ in range(k):
        idx, direction = map(int, input().split())
        left, right = idx, idx

        # 시계 방향 회전
        if direction == 1:          
            # 자기 자신 회전
            circle[idx] = rotateRight(circle[idx])
            
            # 반대 극이면 반시계 방향 회전
            rotate = True
          # 1 = 시계방향
            while rotate == True and left > 0:
                rotate = False
                if circle[left-1][2] != circle[left][6]:    
                    if direction == 1:
                        circle[left-1] = rotateLeft(circle[left-1]) # 반시계
                        direction = -1
                    elif direction == -1:
                        circle[left-1] = rotateRight(circle[left-1]) # 시계 방향
                        direction = 1
                    rotate = True
                    left -= 1

            rotate = True
            direction = 1
            while rotate == True and right < 5:
                rotate = False
                if circle[right+1][6] != circle[right][2]:
                    if direction == 1:
                        circle[right+1] = rotateLeft(circle[right+1])
                        direction = -1
                    elif direction == -1:
                        circle[right+1] = rotateRight(circle[right+1])
                        direction = 1
                    rotate = True
                    right += 1
    

        # 반시계 방향 회전
        elif direction == -1:
            # 자기 자신 회전
            circle[idx] = rotateLeft(circle[idx])
            # 반대 극이면 반시계 방향 회전
            rotate = True
           
            while rotate == True and left > 0:
                rotate = False
                if circle[left-1][2] != circle[left][6]:
                    if direction == -1:
                        circle[left-1] = rotateRight(circle[left-1])
                        direction = 1
                    elif direction == 1:
                        circle[left-1] = rotateLeft(circle[left-1])
                        direction = -1
                    rotate = True
                    left -= 1

            rotate = True
            while rotate == True and right < 5:
                rotate = False
                if circle[right+1][6] != circle[right][2]:
                    if direction == -1:
                        circle[right+1] = rotateRight(circle[right+1])
                        direction = 1
                    elif direction == 1:
                        circle[right+1] = rotateLeft(circle[right+1])
                        direction = -1
                    rotate = True
                    right += 1
                    
            
    answer = 0
    for i in range(4):
        if circle[i][0] == 1:
            answer += (2**(i-1))
    print(answer) """
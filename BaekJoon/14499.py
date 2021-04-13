import sys
input = sys.stdin.readline

Input = list(map(int,input().split()))
_map = [list(map(int,input().split())) for _ in range(Input[0])]
order = list(map(int,input().split()))
x = Input[2]
y = Input[3]

        
#############################################

import sys
def goRight(rect):  # 오른쪽으로 굴리기
    newRect = [0,0,0,0,0,0]
    newRect[0] = rect[3]
    newRect[1] = rect[1]
    newRect[2] = rect[0]
    newRect[3] = rect[5]
    newRect[4] = rect[4]
    newRect[5] = rect[2]
    return newRect

def goLeft(rect):   # 서쪽으로 굴리기
    newRect = [0,0,0,0,0,0]
    newRect[0] = rect[2]
    newRect[1] = rect[1]
    newRect[2] = rect[5]
    newRect[3] = rect[0]
    newRect[4] = rect[4]
    newRect[5] = rect[3]
    return newRect

def goUp(rect):     # 북쪽으로 굴리기
    newRect = [0,0,0,0,0,0]
    newRect[0] = rect[4]
    newRect[1] = rect[0]
    newRect[2] = rect[2]
    newRect[3] = rect[3]
    newRect[4] = rect[5]
    newRect[5] = rect[1]
    return newRect


def goDown(rect):   # 남쪽으로 굴리기
    newRect = [0,0,0,0,0,0]
    newRect[0] = rect[1]
    newRect[1] = rect[5]
    newRect[4] = rect[0]
    newRect[5] = rect[4]
    newRect[2] = rect[2]
    newRect[3] = rect[3]
    return newRect





if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    # 주사위 0으로 초기화
    rect = [0,0,0,0,0,0]
    orders = list(map(int, sys.stdin.readline().split()))
    # k번만큼 명령 수행
    for order in orders:
        if order == 1:      # 동쪽
            if y+1 < m:
                rect = goRight(rect)
                if graph[x][y+1] == 0:
                    graph[x][y+1] = rect[5]
                else:
                    rect[5] = graph[x][y+1]
                    graph[x][y+1] = 0
                y += 1
                print(rect[0])

        elif order == 2:    # 서쪽
            if y-1 >= 0:
                rect = goLeft(rect)
                if graph[x][y-1] == 0:
                    graph[x][y-1] = rect[5]
                else:
                    rect[5] = graph[x][y-1]
                    graph[x][y-1] = 0
                y -= 1
                print(rect[0])

        elif order == 3:    # 북쪽
            if x-1 >= 0:
                rect = goUp(rect)
                if graph[x-1][y] == 0:
                    graph[x-1][y] = rect[5]
                else: 
                    rect[5] = graph[x-1][y]
                    graph[x-1][y] = 0
                x -= 1
                print(rect[0])


        elif order == 4:    # 남쪽
            if x+1 < n:
                rect = goDown(rect)
                if graph[x+1][y] == 0:
                    graph[x+1][y] = rect[5]
                else:
                    rect[5] = graph[x+1][y]
                    graph[x+1][y] = 0
                x += 1
                print(rect[0])

        
        
        
        
        

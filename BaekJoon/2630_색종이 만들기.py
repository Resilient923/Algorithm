import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
#하얀색 이 0 파란색이 1
white_cnt = 0
blue_cnt = 0

def functinon(x,y,length):
    global white_cnt,blue_cnt
    start = graph[x][y]
    for i in range(x,x+length):
        for j in range(y,y+length):
            if start != graph[i][j]:
                # 4개로 쪼갠다.
                for a in range(2):
                    for b in range(2):
                        functinon(x+length//2*a,y+length//2*b,length//2)
                return
    print(x,y)
    if graph[x][y] == 0:
        white_cnt += 1
    elif graph[x][y] == 1:
        blue_cnt += 1

functinon(0,0,n)
print(white_cnt)
print(blue_cnt)



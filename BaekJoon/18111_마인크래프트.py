import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))


#중간값을 구성
Min = min(map(min,graph))
Max = max(map(max,graph))
leastTime = 1e9

for i in range(Min,Max+1):
    pluscnt = 0
    minuscnt = 0
    for j in range(n):
        for k in range(m):
            h = graph[j][k] - i
            if h>0:
                #minuscnt = 1번 작업 수
                minuscnt += h
            elif h<0:
                #h가 음수니까 -를 취해줌으로써 더하기로 바꿔준다.
                #pluscnt = 2번 작업 수
                pluscnt -= h
    if minuscnt+b>=pluscnt:
        time = minuscnt*2 + pluscnt
        #계속 비교해주면서 최솟값을 찾는다.
        if leastTime >= time:
            leastTime = time
            resultHeight = i
print(leastTime,resultHeight)

""" while low<=high:
    pluscnt = 0
    minuscnt = 0
    mid = (low+high)//2
    for i in range(n):
        for j in range(m):
            if graph[i][j] > mid:
                minuscnt += graph[i][j]-mid
            elif graph[i][j] <= mid:
                pluscnt+= mid - graph[i][j]
    if b>=pluscnt:
        totaltime = minuscnt*2+pluscnt
    else: """
    




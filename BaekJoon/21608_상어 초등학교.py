import sys
from collections import defaultdict 
input = sys.stdin.readline

# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

n = int(input())
dict = defaultdict(list)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n*n):
    a = list(map(int,input().rstrip().split()))
    student = a[0]
    like = a[1:]
    dict[student] = like
    
# 모든 학생들 탐색
for student, like in dict.items():
    tmp= []
    #각 학생들에 대해서 board를 탐색하면서 자리 정보 tmp에 저장
    for i in range(n):
        for j in range(n):
            empty = 0
            cnt=0
            if graph[i][j] != 0:
                continue
            for k in range(4):
                nx, ny = i+ dx[k], j+dy[k]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if graph[nx][ny] == 0:
                    empty += 1
                if graph[nx][ny] in like:
                    cnt += 1
            tmp.append([cnt, empty, i, j])
    # 자리정보 정렬
    print('---------------------------------')
    print(tmp)
    tmp.sort(key = lambda x: (-x[0],-x[1], x[2],x[3]))
    # 가장 앞에 있는 자리가 베스트.
    print(tmp)
    graph[tmp[0][2]][tmp[0][3]] = student
    # print('---------------------------------')
    # for i in range(n):
    #     for j in range(n):
    #         print(graph[i][j],end=" ")
    #     print()
    # print('---------------------------------')
result = 0
for i in range(n):
    for j in range(n):
        amount = 0
        for k in range(4):
            nx, ny = i+ dx[k], j+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] in dict[graph[i][j]]:
                amount += 1
        # print(amount)
        if amount == 0:
            result += 0
        elif amount == 1:
            result += 1
        else:
            result += 10 ** (amount-1)
print(result)


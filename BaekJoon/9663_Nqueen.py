import sys
input = sys.stdin.readline

n = int(input())

#먼저 dfs 를 사용한다
#완전탐색으로 퀸을 배치하고, 그 이후에 가능 한 지점들을 제외하고, 놓을 수 있는 방법들을 dfs로 구한다.
# def check(x,y):
#     for i in range(n):
#         visited[i][y] = 1
#         visited[x][i] = 1
#         for j in range(n):   #대각선 체크
#             if i == x + y - j or i == j + abs(x-y):
#                 visited[i][j] = 1
#     return visited
# def back(x,y):
#     for i in range(n):
#         visited[i][y] = 0
#         visited[x][i] = 0
#         for j in range(n):   #대각선 체크
#             if i == x + y - j or i == j + (x-y):
#                 visited[i][j] = 0
#     return visited
# #카운트를 하면서 8개를 놓을 수 있는 방법을 찾는다.
# #대각선으로 쭉, 좌우로 쭉 안된다.
# def dfs(x,y,cnt):
#     global result
#     visited[x][y] = 1
#     cnt += 1
#     check(x,y)
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] == 0:
#                 cnt += 1
#                 dfs(i,j,cnt)
#                 back(i,j)
#                 #백트래킹이 필요하겠다
#             if cnt == n:
#                 result += 1
#                 cnt = 0
#                 return
# result = 0
# for i in range(n):
#     for j in range(n):
#         visited = [[0]*n for _ in range(n)]
#         cnt = 0
#         dfs(i,j,cnt)

# print(result)
# result = 0
# def check(num):
#     for i in range(num):
#         if graph[num] == graph[i] or abs(graph[num]-graph[i]) == num - i:
#             return 0
#     return 1

# def dfs(num):
#     print('-----')
#     global result
#     if num == n:
#         result += 1
#     else:
#         for i in range(n):
#             print(graph)
#             graph[num] = i
#             if check(num):
#                 dfs(num+1)
# graph = [0] * n
# dfs(0)
# print(result)



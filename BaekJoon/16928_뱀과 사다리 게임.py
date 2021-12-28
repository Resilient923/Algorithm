# import sys
# input = sys.stdin.readline
# from collections import defaultdict
# # dp[i][j] = i 번째 칸에 j 번의 주사위를 굴려서 올 수 있나? → T,f

# dp = [0] * 101
# INF = 1000000000
# snakeDict, ladderDict = defaultdict(), defaultdict()

# n, m = map(int, input().split())

# for i in range(n):
#     start, end = map(int , input().split())
#     ladderDict[start] = end
# for i in range(m):
#     start, end = map(int , input().split())
#     snakeDict[start] = end
# re_ladder = {v:k for k,v in ladderDict.items()}
# re_snake = {v:k for k,v in snakeDict.items()}
# dp[1] = 0
# dp[2], dp[3], dp[4], dp[5], dp[6], dp[7] = 1,1,1,1,1,1

# print(re_snake)
# for i in range(8, 101): 
#     dp[i] = INF
# for i in range(8, 101):
#     # 뱀이 현 위치에서 내려가는 것
#     if i in re_ladder:
#     # 사다리는 현 위치에서 올라가는 것
#         dp[i] = min(dp[i-6]+1,dp[i-5]+1, dp[i-4]+1, dp[i-3]+1, dp[i-2]+1 , dp[i-1]+1, dp[re_ladder[i]])
#     else:
#         dp[i] = min(dp[i-6]+1,dp[i-5]+1, dp[i-4]+1, dp[i-3]+1, dp[i-2]+1 , dp[i-1]+1)
# for i in range(8,101):
#     if i in re_snake:
#         dp[i] = min(dp[i],dp[re_snake[i]])
#     if i in re_ladder:
#     # 사다리는 현 위치에서 올라가는 것
#         dp[i] = min(dp[i],dp[i-6]+1,dp[i-5]+1, dp[i-4]+1, dp[i-3]+1, dp[i-2]+1 , dp[i-1]+1, dp[re_ladder[i]])
#     else:
#         dp[i] = min(dp[i], dp[i-6]+1,dp[i-5]+1, dp[i-4]+1, dp[i-3]+1, dp[i-2]+1 , dp[i-1]+1)
# print(dp)
# print(dp[100])
import sys
from collections import deque

input  = sys.stdin.readline

n,m = map(int,input().split())
graph = [i for i in range(101)]
for _ in range(n):
    a,b = map(int,input().split())
    graph[a] = b
for _ in range(m):
    a,b = map(int,input().split())
    graph[a] = b
visited  = [0 for _ in range(101)]


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in range(1,7):
            nx = x + i
            if nx > 100:
                continue
            kan = graph[nx]
            if visited[kan] == 0:
                q.append(kan)
                visited[kan] = visited[x] + 1
                if kan == 100:
                    return

bfs()
print(visited[100]-1)


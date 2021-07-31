import sys
input = sys.stdin.readline
from itertools import combinations

n,s = map(int,input().split())
data = list(map(int,input().split()))
com_data = []
for i in range(len(data)):
    com_data.append(list(combinations(data,i+1)))

cnt = 0
for i in range(len(com_data)):
    for j in range(len(com_data[i])):
        if sum(com_data[i][j]) == s:
            cnt += 1
print(cnt)
#############################dfs로 백트래킹 구현
import sys
input = sys.stdin.readline
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += data[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - data[idx])
    dfs(idx + 1, sum)
n, s = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0
for _ in range(n):
    pos, height = map(int,input().split())
    # 현재 건물이 밀집한 구간에서(0으로 잘라지는 구간) 최소 높이인 건물을 기록해나간다.
    while stack and height < stack[-1]:
        stack.pop()
        answer += 1
    if stack and height == stack[-1]: continue
    stack.append(height)
while stack:
    if stack[-1] > 0:
        answer += 1
    stack.pop()
print(answer)                
#     if stack[-1] > y:
#         total += 1
#     stack.append(y)
#     # print(stack)
# total += 1
# print(total)

# 1 2 1 3 1   0    2 3 2 1
# o o x o x         o o x o

# [1, 1, 1]     [1]
# 2, 3          3 1
#     xx
# xxxxxx
# xxxxxxxxx
# xxxxxxxxxxx x
# x x 

#    x    
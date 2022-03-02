import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

# ans = [0 for _ in range(n)]
# 시간초과
# for i in range(n):
#     stack = []
#     for idx, tall in enumerate(data[i:]):
#         if not stack:
#             stack.append((idx,tall))
#         else:
#             if stack[-1][1] > tall:
#                 ans[i] += 1
#             else:
#                 break
# print(sum(ans))
ans = 0
stack = []
for i in range(n):
    while stack and stack[-1] < data[i]:
        stack.pop()
    stack.append(data[i])
    # print(len(stack)-1)
    # print(stack)
    ans += len(stack) - 1
print(ans)
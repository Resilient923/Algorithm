
import  sys

input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))

answer = [ 0 for _ in range(n)]
stack = []
# 아무리 루프를 오래 돌리려고 해도 안쪽 루프가 N번보다 많이 돌 수는 없다.
# 언젠가 많이 돈 때가 있다면, 다른 때는 많이 안 돌았어야만 하고 총 횟수 역시 O(N)밖에 안된다.
for idx, top in enumerate(data):
    # print(idx,top)
    while stack:
        if stack[-1][1] >  top:
            answer[idx] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((idx,top))
    # print(stack)
print(*answer)

# for idx, top in reversed(list(enumerate(data))):
#     if len(stack) == 0:
#         stack.append((idx+1,top))
#     else:
#         while stack and stack[-1][1] < top:
#             for _ in range(len(stack)):
#                 answer[stack[-1][0]-1] = idx+1
#                 stack.pop()
#         stack.append((idx+1,top))
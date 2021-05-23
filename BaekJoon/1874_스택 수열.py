import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

stack = []
result = []
idx = 1
for i in range(n):
    if idx<=data[i]:
        while idx<=data[i]:
            stack.append(idx)
            result.append('+')
            idx += 1
        stack.pop()
        result.append('-')
    else:
        if len(stack)!=0 and stack[-1] == data[i]:
            stack.pop()
            result.append('-')
if len(stack)!=0:
    print("NO")
else:
    for i in result:
        print(i)

    
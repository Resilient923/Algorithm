import sys
input = sys.stdin.readline

stack = []
n = int(input())
for i in range(n):
    Input = list(input().split())
    if Input[0] == 'push':
        stack.append(Input[1])
    elif Input[0] == 'pop':
        if (len(stack)==0):
            print(-1)
        else:
            print(stack.pop())
    elif Input[0] == 'size':
        print(len(stack))
    elif Input[0] == 'empty':
        if (len(stack)==0):
            print(1)
        else:
            print(0)
    elif Input[0] == 'top':
        if (len(stack)==0):
            print(-1)
        else:
            print(stack[len(stack)-1])

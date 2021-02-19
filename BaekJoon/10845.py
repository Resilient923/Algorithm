import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    Input = sys.stdin.readline().split()
    if Input[0] == 'push':
        data.insert(0,Input[1])
    elif Input[0] == 'front':    
        if len(data) == 0:
            print(-1)
        else:     
            print(data[len(data)-1])
    elif Input[0] == 'back':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
    elif Input[0] == 'empty':    
        if len(data) ==0:
            print(1)
        else:
            print(0)
    elif Input[0] == 'size':
        print(len(data))
    elif Input[0] == 'pop':
        if len(data) == 0:
            print(-1)
        else:
            print(data.pop())
           
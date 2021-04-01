import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque()
for i in range(n):
    a = list(input().split())
    if a[0] == 'push_back':
        deq.append(a[1])
    elif a[0] == 'push_front':
        deq.appendleft(a[1])
    elif a[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif a[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif a[0] == 'empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif a[0] == 'size':
        print(len(deq))
    elif a[0] =='front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif a[0] == 'back':
        if not deq:
            print(-1)
        else:
            print(deq[len(deq)-1])

 
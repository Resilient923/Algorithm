import sys,heapq
input = sys.stdin.readline

n = int(input())
number = []
for i in range(n):
    a = int(input())
    if a == 0:
        if len(number)>0:
            print(heapq.heappop(number))
        else:
            print(0)
    else:
        heapq.heappush(number,a)

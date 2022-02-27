import sys,heapq
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    graph = list(map(int,input().split()))

    if not stack:
        for num in graph:
            heapq.heappush(stack,num)
 
    else:
        for num in graph:
            if num > stack[0]:
                heapq.heappush(stack,num)
                heapq.heappop(stack)
print(stack[0])
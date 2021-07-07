import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

h = []
result = []
for i in data:
    if i == 0:
        if len(h)>0:
            result.append(heapq.heappop(h))
        else:
            result.append(0)
    else:
        heapq.heappush(h,(i,abs(i)))
print(result)
for i in result:
    if i == 0:
        print(0)
    else:
        print(i[1])


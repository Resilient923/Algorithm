import sys
import heapq
input = sys.stdin.readline

#시간초과 코드(어쩐지 너무쉬웠다)
n = int(input())
number = []
""" for i in range(n):
    a = int(input())
    number.append(a)
    if a == 0:
        print(max(number))
        del number[number.index(max(number))] """


for i in range(n):
    a = int(input())
    heapq.heappush(number,(-a,a))
    if a == 0:
        print(heapq.heappop(number)[1])
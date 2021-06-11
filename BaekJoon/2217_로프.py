import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort(reverse=True)
Max = 0
for i in range(1,n+1):
    if data[i-1]*(i)>Max:
        Max = data[i-1]*i
print(Max)
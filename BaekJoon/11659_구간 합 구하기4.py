import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

num = 0
prefix_sum = [0]
for i in data:
    num += i
    prefix_sum.append(num)

def function(start,end,prefix_sum):
    return prefix_sum[end] - prefix_sum[start-1]
    

for _ in range(m):
    a,b = map(int,input().split())
    print(function(a,b,prefix_sum))

    


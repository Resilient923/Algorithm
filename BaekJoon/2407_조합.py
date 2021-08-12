import sys
input = sys.stdin.readline

n,m = map(int,input().split())

data = [i for i in range(1,n+1)]

ans1 = 1
ans2 = 1
for i in data[-m:]:
    ans1 *= i
for i in data[:m]:
    ans2 *= i

print(ans1//ans2)


import sys
input = sys.stdin.readline

n = int(input())
total = 1
t = []
cnt = 0
for i in range(1,n+1):        
    total *= i

while total>0:
    a = total % 10
    t.append(a)
    total = total // 10
for i in t:
    if i != 0:
        print(cnt)
        break
    if i == 0:
        cnt+=1

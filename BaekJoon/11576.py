import sys
input = sys.stdin.readline

a,b = map(int,input().split())
m = int(input())
num = list(map(int,input().split()))
number = 0
# 17진법 8진법
#17진법 2, 16 을 8진법 a,b로
for i in range(len(num)):
    number += num[i]*(a**(m-1-i))
ans = []
while number>=0:
    ans.insert(0,number%b)
    number = number // b
    if number ==0:
        break
for i in ans:
    print(i)
# (시간초과)
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
m = int(input())
result=0
mid = m//n
ans = 0
while(result<=m):
    result = 0
    mid +=1
    for i in data:
        if(mid-i>=0):
            result += i
        else:
            result += mid
print(mid-1)

#맞는코드
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
m = int(input())
start = 0
end = max(data)
while(start<=end):
    mid = (start+end)//2
    ans = 0
    for i in data:
        if i>=mid:
            ans += mid
        else:
            ans += i
    if ans<=m:
        start = mid+1
    else:
        end = mid -1
print(end)



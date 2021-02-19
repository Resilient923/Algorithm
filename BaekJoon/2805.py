import sys
k,n= map(int,sys.stdin.readline().split())

lans=(list(map(int,input().split())))
result = 0
start = 0
end = max(lans)
while(start<=end):
    result=0
    mid = ((start+end)//2)
    for i in lans:
        if(i>mid):
             result += (i-mid)
    if(result<n):
        end = mid-1
    else:
        total = mid
        start = mid+1   
print(total)

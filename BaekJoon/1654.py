import sys
k,n= map(int,sys.stdin.readline().split())
lans=[]
for i in range(k):
    lans.append((int(sys.stdin.readline())))
end = max(lans)
start = 1

while(start<=end):
    mid = (start + end) // 2
    lines = 0
    for i in lans:
        lines  += (i//mid)
        
    if lines >=n:
        start = mid + 1
    else:
        end = mid-1
print(end)
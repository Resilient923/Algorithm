import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
data = list(map(int,input().split()))

data.append(0)
data.append(l-1)
data.sort()


start = 0
end = data[-1]
while start <= end:
    cnt = 0
    mid  = (start+end) // 2
    for i in range(1,len(data)):
        if (data[i]-data[i-1]) > mid:
            cnt += (data[i]-data[i-1] - 1)//mid
    
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)

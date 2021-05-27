#이분탐색
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = [int(input()) for _ in range(n)]

start = 1
end = m*max(data)
# m명을 심사할 수 있는지 없는지를 파악하는 문제이다.
# 1561과는 이점에서 다르다.
while start<=end:
    mid = (start+end)//2
    print(mid)
    cnt =  0 
    for i in range(n):
        cnt += mid//data[i]
    if cnt>=m: 
        time = mid
        end = mid-1
    else:
        start = mid+1
print(time)


import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

start,end = 0,60000000000
time = 0
if n<m:
    print(n)
else:
    while start<=end:
        mid = (start+end)//2
        cnt =  m #t가 0초에는 다타고시작
        for i in range(m):
            cnt += mid//data[i]
        if cnt>=n: #애들많을때
            time = mid
            end = mid-1
        else:#애들 늘릴때
            start = mid+1
    #time 보다 1분전 탄애들수
    ans = m
    for i in range(m):
        ans += (time-1)//data[i]
    #time에 탄 애들cnt
    for i in range(m):
        if time % data[i] == 0:
            ans +=1
        if ans == n:
            print(i+1)
            break

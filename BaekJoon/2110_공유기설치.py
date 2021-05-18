import sys
input = sys.stdin.readline

n,c = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))
data.sort()

start = 1
# start = data[1]- data[0] 이경우에 5,3, 1,7,8,910 이렇게 넣으면 반례가생긴다.
end = data[-1] - data[0]
ans = 0
while start<=end:
    #while문 한바퀴돌때마다 data[0]값으로 시작하고
    flag = data[0]
    cnt = 1
    # mid는 간격이다.
    mid = (start+end)//2
    for i in range(1,len(data)):
        # while문을 통해 정해진 mid값을 각각 집 좌표마다 for문으로 돌려서 가능한지 가능하지 않은지 확인한다.
        if data[i]>=flag+mid:
            # 다음집을 검색한다.
            flag = data[i]
            # 집 카운트해준다 (카운트가 주어진다.)
            cnt+=1
    if cnt<c:
        end = mid-1
    else:
        start = mid+1
        ans = mid
print(ans)


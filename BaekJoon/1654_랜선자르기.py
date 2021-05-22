import sys
input = sys.stdin.readline

k, n = map(int,input().split())
data = []
for _ in range(k):
    data.append(int(input()))
#구하려는 값은 랜선 최대길이
start = 1
end = max(data)

while start<=end:
    cnt = 0 
    mid = (start+end)//2
    for i in data:
        cnt += i//mid
    if cnt <n:
        end = mid - 1
        
    elif cnt >= n:
        start = mid + 1
        result = mid
print(result)
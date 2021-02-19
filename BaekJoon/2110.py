import math

n , c = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))

sorted(data)
start = min(data)
end = max(data)
while(start<end):
    mid = data[math.floor(len(data)//2)-1]
    one = mid - start
    two = end - mid
    if one >two:
        result = mid - data[0]
        break
    else:
        result = data[n] - mid
        break
print(result)

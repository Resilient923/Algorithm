import sys
input = sys.stdin.readline
""" # 시간초과
n = int(input())
data = list(map(int,input().split()))
# 시간초과
setdata = list(set(data))
answer = [0 for i in range(n)]
for i in setdata:
    for j in range(len(data)):
        if data[j]>i:
            answer[j] += 1
answer = (" ".join(map(str,answer)))
print(answer)
# 시간초과 """

n = int(input())
data = list(map(int,input().split()))
data_ = data
data = list(sorted(set(data)))
data = {data[i]:i for i in range(len(data))}
print(*[data[i] for i in data_])


    
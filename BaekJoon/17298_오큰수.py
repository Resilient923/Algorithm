import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
stack = [0]
ans = [-1 for _ in range(n)] # 오큰수 없으면 -1
cnt = 1
while cnt<n:
    while stack and data[stack[-1]] < data[cnt]:
        ans[stack[-1]] = data[cnt]
        stack.pop()
    stack.append(cnt)
    cnt+=1

for i in ans:
    print(i,end=' ')

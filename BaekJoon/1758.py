import sys
input = sys.stdin.readline

n = int(input())

tips = []
for _ in range(n):
    tips.append(int(input()))

ans = 0
tips.sort(reverse=True)

for i in range(n):
    if tips[i]-((i+1)-1) > 0:
        ans += tips[i]-((i+1)-1) 
print(ans)
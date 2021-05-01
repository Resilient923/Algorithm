import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())
ans = []
def dfs(plus,minus,mul,div,cnt,total):
    if cnt == n-1:
        ans.append(total)
    if plus>0:
        dfs(plus-1,minus,mul,div,cnt+1,total+numbers[cnt+1])
    if minus>0:
        dfs(plus,minus-1,mul,div,cnt+1,total-numbers[cnt+1])
    if mul>0:
        dfs(plus,minus,mul-1,div,cnt+1,total*numbers[cnt+1])
    if div>0:
        dfs(plus,minus,mul,div-1,cnt+1,int(total/numbers[cnt+1])) #나눗셈할때 -를
    
dfs(plus,minus,mul,div,0,numbers[0])
print(max(ans))
print(min(ans))

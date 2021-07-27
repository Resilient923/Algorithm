# 이문제는 DFS


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
data = list(map(int,input().split()))

def dfs(num):
    global Max
    if len(data)==2:
        if Max < num:
            Max = num
            return
    for i in range(1,len(data)-1):
        num += data[i-1]*data[i+1]
        temp = data[i]
        del data[i]
        dfs(num)
        # dfs함수 실행시켜주고 다른 dfs에 영향을 미치지 않기위해
        # 원상복구 시켜준다.
        data.insert(i,temp)
        num -= data[i-1]*data[i+1]
 
Max = 0
dfs(0)
print(Max)
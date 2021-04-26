#######################################dfs안되는문제
import sys
input = sys.stdin.readline

""" ans =[]
time = 0
def function(start,k):
    global time
    if start == k:
        ans.append(time)
    else:    
        function(2*start,k)
        function(start+1,k)
        function(start-1,k)
        time +=1

print(min(ans)) """
from collections import deque

Max = 100001
cnt = [0]*Max
n,k = map(int,input().split())
def function():#bfs사용
    q = deque()
    q.append(n) #현재위치 n을 q에 삽입
    while q:
        now = q.popleft() #현재위치
        if now == k: #현재위치가 동생위치랑 같으면 현재위치까지오는데 걸린 카운트 출력
            print(cnt[now])
            return
        for _next in (now+1,now-1,now*2): #순서가 바뀌면 답이 틀리다.
            if 0<= _next <Max and not cnt[_next]:
                cnt[_next] = cnt[now]+1
                q.append(_next)
function()
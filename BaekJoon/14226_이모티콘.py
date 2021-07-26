import collections
import sys
from collections import deque
input = sys.stdin.readline

# 최단시간이면 BFS 문제이다.  
s = int(input())
# 숫자로 생각해서 계산해야한다.
dp = [[-1]*(s+1) for _ in range(s+1)]

#dp 스러운 bfs문제
def bfs():
    q = deque()
    q.append((1,0))
    dp[1][0] = 0

    while q:
        #현재 화면 이모티콘 개수, 클립보드 이모티콘 개수
        window,clipboard = q.popleft()

        # 1번 연산
        if dp[window][window] == -1:
            dp[window][window] = dp[window][clipboard] + 1
            q.append((window,window))
        # 2번 연산
        if window+clipboard <= s and dp[window+clipboard][clipboard] == -1:
            dp[window+clipboard][clipboard] = dp[window][clipboard] + 1
            q.append((window+clipboard,clipboard))
        # 3번 연산
        if window - 1 >=0 and dp[window-1][clipboard] == -1:
            dp[window-1][clipboard] = dp[window][clipboard] + 1
            q.append((window-1,clipboard))

bfs()
ans = dp[s][1]

for i in range(1,s):
    if dp[s][i] != -1:
        ans = min(dp[s][i],ans)
print(ans)

        

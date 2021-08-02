from collections import deque
import sys
input = sys.stdin.readline

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
        # if now == 0:
        for _next in (now+1,now-1,now*2): 
            if _next == now*2 and now != 0:
                if 0<= _next <Max and not cnt[_next]:
                    cnt[_next] = cnt[now]
            # X*2 를 할 때의 순서가 앞에와야 최솟값이 되기 때문에
            # q의 가장맨앞에서 처리해줄수있도록 appendleft를 사용        
                    q.appendleft(_next)
            else:
                if 0<= _next <Max and not cnt[_next]:
                    cnt[_next] = cnt[now]+1
                    q.append(_next)
        # else:
        #     for _next in (now*2,now+1,now-1): 
        #         if _next == now*2:
        #             if 0<= _next <Max and not cnt[_next]:
        #                 cnt[_next] = cnt[now]
        #                 q.append(_next)
        #         else:
        #             if 0<= _next <Max and not cnt[_next]:
        #                 cnt[_next] = cnt[now]+1
        #                 q.append(_next)

function()
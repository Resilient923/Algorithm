import sys
from collections import deque
input = sys.stdin.readline

# f층, 스타트링크가 g층, 강호는 s층 u만큼가고 d만큼 내려가고
f,s,g,u,d = map(int,input().split())

move = [u,-d]

visited = [0 for _ in range(f+1)]
floor = [0 for _ in range(f+1)]
# def bfs():
q = deque()
q.append((s,0))
visited[s] = 1
while q:
    now,cnt = q.popleft()
    # print(now,cnt)
    if now == g:
        print(cnt)
        break
    for i in range(2):
        next_ = now + move[i]
        if 0 <  next_ <= f and visited[next_] == 0:
            q.append((next_,cnt+1))
            visited[next_] = 1
    # print(visited)
if visited[g] == 0:
    print("use the stairs")
# print(visited)
# bfs()





from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

q = [i for i in range(1, n + 1)]
cnt = 0
for i in range(m):
    q_len = len(q)
    now_idx = q.index(data[i])
    if now_idx < q_len - now_idx:
        while 1:
            if q[0] == data[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                cnt += 1
    else:
        while 1:
            if q[0] == data[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                cnt += 1
print(cnt)
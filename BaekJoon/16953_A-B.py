# 이문제는 그리디로 풀면된다.
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
cnt = 0
while b>0:
    # 맨 마지막자리수가 짝수일때 2를 나눌수있다.
    if b % 2 == 0:
        b //= 2
        cnt +=1
    # 맨 마지막 수가 1이면 1을 뺄수 있다.
    elif b%10 == 1:
        b //= 10
        cnt += 1
    # 둘다 아니면 b는 a가 될 수 없다.
    else:
        print(-1)
        break
    # 위에 계산과정을 거쳐서 만약에 b가 a 이면 cnt에다가 1을 더한값출력
    if b == a:
        print(cnt+1)
        break
    # 위에 계산을 하긴했는데 4, 41과 같은 반례가 생기면 
    elif b < a:
        print(-1)
        break
    
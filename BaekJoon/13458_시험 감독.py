import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))

first,second = map(int,input().split())

ans = 0
for i in people:
    i -= first
    # 총 감독관은 한명씩은 있어야한다.
    cnt = 1
    # 총감독관이 1명씩 들어가는데 그 1명이 혼자 감시가능하면
    # 부감독관은 없어도된다. 1명이 감당이 안되면,
    if i>0:
        # 몇명필요한지 그리디로 생각해서 계산하고 시험장별로 부감독관수를 cnt에 더해주고
        cnt += i//second
        # 0으로 나누어떨어지지 않으면 1을 더해준다.
        # 왜냐하면 0으로 나누어떨어지면 딱 그 감독관만 있으면되는데
        # 0으로 안나누어떨어지면 1명이라도 있으면 그 사람을 감독하러 들어가야 하기 때문.
        if i%second !=0:
            cnt += 1
    # 시험장별로 계산해서 전체 감독수 (총+부)에 더해준다.
    ans += cnt
print(ans)
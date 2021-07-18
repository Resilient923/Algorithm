import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m,n,x,y = map(int,input().split())
    ans = -1
    while x <= m*n:
        if (x-y) % n == 0:
            ans = x
            break
        x += m
    print(ans)   

    ######################################시간초과
    # while True:
    #     cnt += 1
    #     if _m % m == x and _n % n == y:
    #         print(cnt)
    #         break
    #     elif _m % m == 0 and _n % n == 0:
    #         print(-1)
    #         break
    #     _m += 1
    #     _n += 1
    # print(cnt)




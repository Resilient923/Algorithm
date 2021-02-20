def fac(n):
    num = 1
    for i in range(1,n):
        num *= i
    return num

t= int(input())
for i in range(t):
    n,m = map(int,input().split())
    bridge = fac(m)//(fac(n)*fac(m-n))
    print(bridge)

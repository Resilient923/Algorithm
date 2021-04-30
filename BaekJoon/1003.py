import sys
input = sys.stdin.readline

n = int(input())


for i in range(n):
    a = int(input())
    one_cnt = 0 
    zero_cnt = 1
    tmp = 0
    for _ in range(a):
        tmp = one_cnt
        one_cnt = one_cnt + zero_cnt
        zero_cnt = tmp
    print(zero_cnt,one_cnt)
import sys
input = sys.stdin.readline

n = int(input())

print(2**n-1)
def hanoi(n,start,end,via):
    if n == 1:
        print(start,end)
    else:
        # 1에서 3으로 가기위해서 2로 다 옮겨놓는다.
        hanoi(n-1,start,via,end)
        # 1에서 3으로 간다.
        print(start,end)
        # 2 에 있던걸 모두 3으로 옮긴다.
        hanoi(n-1,via,end,start)
hanoi(n,1,3,2)
import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
#r,c를 주어진 큰 정사각형중에서 x,y좌표로 생각한다.
num = 0
while n > 0:
    # 사분면 한 변의 길이
    square = (2 ** n) // 2
    if n > 1:
        if square > r and square <= c:
            num += square ** 2
            c -= square
        elif square <= r and square > c:
            num += (square ** 2) * 2
            r -= square
        elif square <= r and square <= c:
            num += (square ** 2) * 3
            r -= square
            c -= square
    #3개로 쪼갠이유는 0,0일때는 이미 square에서 처리한값을 num에 더해주었기때문이다.
    elif n == 1:
        if r == 0 and c == 1:
            num += 1
        elif r == 1 and c == 0:
            num += 2
        elif r == 1 and c == 1:
            num += 3
    n -= 1
print(num)


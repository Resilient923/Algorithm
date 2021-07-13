import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
graph = [[0]*m for _ in range(n)]


def straight(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x][y+1]
    ans += data[x][y+2]
    ans += data[x][y+3]
    return ans

def straight_rotate(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x+1][y]
    ans += data[x+2][y]
    ans += data[x+3][y]
    return ans

def square(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x][y+1]
    ans += data[x+1][y]
    ans += data[x+1][y+1]
    return ans

def zigzag(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x+1][y]
    ans += data[x+1][y+1]
    ans += data[x+2][y+1]
    return ans

def zigzag_rotate(x,y):
    ans = 0
    ans += data[x+1][y]
    ans += data[x+1][y+1]
    ans += data[x][y+1]
    ans += data[x][y+2]
    return ans

def zigzag_rev(x,y):
    ans = 0
    ans += data[x+1][y]
    ans += data[x+2][y]
    ans += data[x+1][y+1]
    ans += data[x][y+1]
    return ans

def zigzag_rev_rotate(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x][y+1]
    ans += data[x+1][y+1]
    ans += data[x+1][y+2]
    return ans

def t(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x][y+1]
    ans += data[x][y+2]
    ans += data[x+1][y+1]
    return ans

def t_rotate1(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x+1][y]
    ans += data[x+2][y]
    ans += data[x+1][y+1]
    return ans

def t_rotate2(x,y):
    ans = 0
    ans += data[x][y+1]
    ans += data[x+1][y]
    ans += data[x+1][y+1]
    ans += data[x+1][y+2]
    return ans

def t_rotate3(x,y):
    ans = 0
    ans += data[x+1][y]
    ans += data[x+1][y+1]
    ans += data[x][y+1]
    ans += data[x+2][y+1]
    return ans

def others1(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x+1][y]
    ans += data[x+2][y]
    ans += data[x+2][y+1]
    return ans

def others2(x,y):
    ans = 0
    ans += data[x+2][y]
    ans += data[x+2][y+1]
    ans += data[x+1][y+1]
    ans += data[x][y+1]
    return ans

def others3(x,y):
    ans = 0
    ans += data[x][y+2]
    ans += data[x+1][y+2]
    ans += data[x+1][y+1]
    ans += data[x+1][y]
    return ans

def others4(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x][y+1]
    ans += data[x][y+2]
    ans += data[x+1][y+2]
    return ans

def others5(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x][y+1]
    ans += data[x+1][y+1]
    ans += data[x+2][y+1]
    return ans

def others6(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x][y+1]
    ans += data[x+1][y]
    ans += data[x+2][y]
    return ans

def others7(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x+1][y]
    ans += data[x][y+1]
    ans += data[x][y+2]
    return ans

def others8(x,y):
    ans = 0
    ans += data[x][y]
    ans += data[x+1][y]
    ans += data[x+1][y+1]
    ans += data[x+1][y+2]
    return ans

result = 0
for i in range(n):
    for j in range(m):
        if 0<= i <n-3 and 0 <= j <m:
            result = max(result,straight_rotate(i,j))
for i in range(n):
    for j in range(m):
        if 0<= i <n and 0<= j <m-3:
           result = max(result,straight(i,j))
for i in range(n):
    for j in range(m):
        if 0<= i <n-1 and 0<= j <m-1:
            result = max(result,square(i,j))
for i in range(n):
    for j in range(m):
        if 0<= i <n-1 and 0<= j <m-2:
            result = max(result,
            zigzag_rev_rotate(i,j),zigzag_rotate(i,j),
            t(i,j),t_rotate2(i,j),
            others3(i,j),others4(i,j),others7(i,j),others8(i,j)
            )
for i in range(n):
    for j in range(m):
        if 0<= i <n-2 and 0<= j <m-1:
            result = max(result,
            zigzag_rev(i,j),zigzag(i,j),
            t_rotate1(i,j),t_rotate3(i,j),
            others1(i,j),others2(i,j),others5(i,j),others6(i,j)
            )

print(result)


###############################################

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]


def function(x, y):
    global answer
    for i in range(19):
        result = 0
        for j in range(4):
            try:
                dx = x + tetromino[i][j][0] # x 좌표
                dy = y + tetromino[i][j][1] # y 좌표
                result += board[dx][dy]
            except IndexError:
                continue
        answer = max(answer, result)
            
answer = 0
for i in range (n):
    for j in range(m):
        function(i, j)
print(answer)

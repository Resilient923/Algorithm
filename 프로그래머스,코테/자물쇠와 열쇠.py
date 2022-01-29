# 회전하고
def rotate(key_list,m):
    result = [[0]* m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m-i-1] = key_list[i][j]
    return result
# key를 넣어보는 함수
def in_key(x,y,key,m,graph):
    for i in range(m):
        for j in range(m):
            graph[x+i][y+j] += key[i][j]
# 다 1인지 확인하는 함수
def check(m,n,graph):
    for i in range(n):
        for j in range(n):
            if graph[m+i][m+j] != 1:
                return 0
    return 1

# key를 빼는 함수
def out_key(x,y,key,m,graph):
    for i in range(m):
        for j in range(m):
            graph[x+i][y+j] -= key[i][j]

def solution(key, lock):
    # 완탐이다.
    # 회전 할 때 4 가지 경우 * 자물쇠 왼쪽 끝이랑 키 오른쪽 아래 맞춰준다.
    # 회전하고
    # key를 넣어보는 함수
    # 확인해보고
    # key를 다시 뺀다
    m,n = len(key), len(lock)
    graph = [[0] * (m*2+n-1) for _ in range((m*2+n-1))]
    
    # 자물쇠를 graph 한가운데에 배치 해놓는다.
    for i in range(n):
        for j in range(n):
            graph[m+i][m+j] = lock[i][j]
    rotate_key = key
    # 4번회전
    for _ in range(4):
        rotate_key = rotate(rotate_key,m)
        for i in range(1,m+n-1):
            for j in range(1,m+n-1):
                in_key(i,j,rotate_key,m,graph)
                if check(m,n,graph) == 1:
                    return True
                out_key(i,j,rotate_key,m,graph)

    return False

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])
""" def solution(n, k, cmd):
    answer = ''
    return answer

def U(cur,x):
    return cur-x
def D(cur,x):
    return cur+x
def C(cur,list):
    del list[cur]
    cur = list[cur]
    return cur """
""" def Z(cur,list): """


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

""" graph = []
delete= []
for i in range(n):
    graph.append(i)
cur = k

for i in cmd:
    if (list(i)[0]) == 'D':
        D(cur,list(i)[2])
    elif (list(i)[0]) == 'U':
        U(cur,list(i)[2])
    elif (list(i)[0]) == 'C':
        C(cur,graph)
    elif (list(i)[0]) == 'Z': """

def solution(n, k, cmd):
    answer = ""

    # 현재 커서 위치와 행들의 삭제 여부를 초기화
    # True: 삭제되지 않은 행
    current = k
    rowInfo = [[i, True] for i in range(n)]

    # 가장 최근에 삭제한 행 정보를 기록하기 위한 스택
    deleted = []
    # # cmd parsing
    total = 0
    for c in cmd:
        if len(c) > 1:
            move = int(c[2:])
            if c[0] == "U":
                total -= move
            if c[0] == "D":
                total += move
        else:
            if total > 0:
                while total > 0:
                    if rowInfo[current+1][1] == True:
                        total -= 1
                    current += 1
            else:
                while total < 0:
                    if rowInfo[current-1][1] == True:
                        total += 1
                    current -= 1
        
            if c == "C":
                
                rowInfo[current][1] = False
                deleted.append(current)
                temp = [[rowInfo[i][1],i] for i in range(current+1, n) if rowInfo[i][1]]
                if temp:
                    current = temp[0][1]
                else:
                    temp = [[rowInfo[i][1],i] for i in range(current) if rowInfo[i][1]]
                    current = temp[-1][1]
            elif c == "Z":
                back = deleted.pop()
                rowInfo[back][1] = True
            total = 0
    
    for i in range(n):
        answer += "O" if rowInfo[i][1] else "X"
    return answer
rows = 100
columns = 97
queries = [[1,1,100,97]]

def solution(rows, columns, queries):
    data = [[0]*columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            data[i][j] += cnt
            cnt += 1
    answer = []
    for a,b,c,d in queries:
        x1,y1,x2,y2 = a-1,b-1,c-1,d-1
        temp = data[x1][y1]
        Min = temp

        # 왼쪽 아래서 왼쪽 위로 끌어오기
        for i in range(x1,x2):
            flag = data[i+1][y1]
            data[i][y1] = flag
            Min = min(Min,flag)

        # 오른쪽 아래에서 왼쪽 아래로 끌어오기
        for i in range(y1,y2):
            flag = data[x2][i+1]
            data[x2][i] = flag
            Min = min(Min,flag)

        # 오른쪽 위에서 오른쪽 아래로 끌어오기
        for i in range(x2,x1,-1):
            flag = data[i-1][y2]
            data[i][y2] = flag
            Min = min(Min,flag)

        # 왼쪽 위에서 오른쪽 위로 끌어오기
        for i in range(y2,y1,-1):
            flag = data[x1][i-1]
            data[x1][i] = flag
            Min = min(Min,flag)

        # 처음에 시작할 때 빼뒀던 temp 값 위치 시키기
        data[x1][y1+1] = temp
        answer.append(Min)
    return answer
print(solution(rows,columns,queries))
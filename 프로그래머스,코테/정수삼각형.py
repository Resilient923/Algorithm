def solution(data):
    n = len(data)
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                data[i][j] = data[i][j]+data[i-1][j]
            elif i == j:
                data[i][j] = data[i][j]+data[i-1][j-1]
            else:
                data[i][j] = max(data[i-1][j-1],data[i-1][j])+data[i][j]
            
    answer = (max(data[-1]))
    return answer
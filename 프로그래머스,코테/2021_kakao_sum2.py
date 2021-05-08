places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

""" person = [[]for _ in range(5)]
X = [[]for _ in range(5)]
flag = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            if places[i][j][k] == "P":
                person[i].append([j,k])
            elif places[i][j][k] == "X":
                X[i].append([j,k])
for i in range(len(person)):
    print(person[i])
    print(X[i])
temp = []
for List in person:
    for i in range(len(List)):
        for j in range(len(List)):
            if abs(List[i][0] - List[j][0]) + abs(List[i][1] - List[j][1]) <= 2:
                temp.append(List[j])
print(temp) """
#############################
def isValidArea(i, j):
    if 0 <= i < 5 and 0 <= j < 5:
        return True
    return False


def solution(places):
    answer = []

    for room in places:
        isSafe = True
        # 자신을 기준으로 오른쪽, 아래쪽, 대각선 아래쪽만 관찰
        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    if isValidArea(i+1,j) and room[i+1][j] == "P":
                        isSafe = False
                    if isValidArea(i+2,j) and room[i+2][j] == "P" and room[i+1][j] != "X":
                        isSafe = False
                    if isValidArea(i,j+1) and room[i][j+1] == "P":
                        isSafe = False
                    if isValidArea(i,j+2) and room[i][j+2] == "P" and room[i][j+1] != "X":
                        isSafe = False

                    if isValidArea(i+1, j+1) and room[i+1][j+1] == "P" and (room[i+1][j] != "X" or room[i][j+1] != "X"):
                        isSafe = False
                        
                    if isValidArea(i+1, j-1) and room[i+1][j-1] == "P" and (room[i][j-1] != "X" or room[i+1][j] != "X"):
                        isSafe = False
        if isSafe:
            answer.append(1)
        else:
            answer.append(0)   
                
    return answer
print(solution(places))


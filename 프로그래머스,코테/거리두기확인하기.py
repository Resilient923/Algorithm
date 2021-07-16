places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def solution(places):
    def validRange(x, y):
        if 0 <= x < 5 and 0 <= y < 5:
            return True
        return False
    answer = []
    for room in places:
        flag = 0
        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    if validRange(i+1,j) and room[i+1][j] == "P":
                        flag = 1
                    if validRange(i+2,j) and room[i+2][j] == "P" and room[i+1][j] != "X":
                        flag = 1
                    if validRange(i,j+1) and room[i][j+1] == "P":
                        flag = 1
                    if validRange(i,j+2) and room[i][j+2] == "P" and room[i][j+1] != "X":
                        flag = 1

                    if validRange(i+1, j+1) and room[i+1][j+1] == "P" and (room[i+1][j] != "X" or room[i][j+1] != "X"):
                        flag = 1
                        
                    if validRange(i+1, j-1) and room[i+1][j-1] == "P" and (room[i][j-1] != "X" or room[i+1][j] != "X"):
                        flag = 1
        if flag == 0:
            answer.append(1)
        else:
            answer.append(0)   
    return answer
print(solution(places))


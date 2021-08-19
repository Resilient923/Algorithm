def solution(scores):
    answer = ''
    length = len(scores)
    for i in range(length):
        score = 0
        cnt = 0
        temp = []
        for j in range(length):
            temp.append(scores[j][i])
        # i는 0,1,2,3,4 순서대로 자기꺼만 확인하면 된다.
        # 자기자 측정한 자기 점수가 젤 크거나 작을 때 유일한 값이면 지운다.
        if temp[i] == min(temp) and temp.count(temp[i]) == 1:
            del temp[i]
        elif temp[i] == max(temp) and temp.count(temp[i]) == 1:
            del temp[i]
      
        average = sum(temp) // len(temp)
        if average >= 90:
            answer += 'A'
        elif 80 <= average < 90:
            answer += 'B'
        elif 70 <= average < 80:
            answer += 'C'
        elif 50 <= average < 70:
            answer += 'D'
        elif average < 50:
            answer += 'F'

               
    return answer
















scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores))
def solution(brown, yellow):
    answer = []
    total = brown+yellow
    totallist = []
    for i in range(1,total+1):
        if total % i == 0:
            totallist.append(i)
    for i in totallist:
        for j in totallist:
            if (i-2)*(j-2) == yellow: #이게 핵심이다 
                a = i
                b = j
    if totallist[len(totallist)//2]**2==total: # 정사각형 모양의 카펫일때
        answer.append(totallist[len(totallist)//2])
        answer.append(totallist[len(totallist)//2])
    else:
        answer.append(a)
        answer.append(b)

    return answer

if __name__ == "__main__": 
    #인터프리터에서 직접실행했을때만 코드를 실행해라
    brown = 24
    yellow = 24
    print(solution(brown,yellow))
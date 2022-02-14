def getWinner(rsp):
    rspSet = set(rsp)
    answer = []
    if len(rspSet) == 1 or len(rspSet) == 3:
        return -1;
    if 'R' in rspSet and 'S' in rspSet:
        for i in range(3):
            if rsp[i] == 'R': answer.append(i)
    if 'R' in rspSet and 'P' in rspSet:
        for i in range(3):
            if rsp[i] == 'P': answer.append(i)
    if 'S' in rspSet and 'P' in rspSet:
        for i in range(3):
            if rsp[i] == 'S': answer.append(i)
    return answer


def solution(rsp3):
    answer = [0, 0, 0]
    for rsp in rsp3:
        winner = getWinner(rsp);
        if winner == -1: continue
        if len(winner) == 1:
            answer[winner[0]] += 2  
        else:
            a, b = winner[0], winner[1]
            if answer[a] == answer[b]:
                answer[a] += 1
                answer[b] += 1
            else:
                if answer[a] < answer[b]:
                    answer[a] += 2
                else:
                    answer[b] += 2
    return answer

print(solution(["SPR","PPR","PSS","RSS","RRR"]))
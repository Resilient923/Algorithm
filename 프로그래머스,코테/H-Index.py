def solution(citations):

    citations.sort()
    Max = len(citations)
    flag = 0
    for i in range(Max):
        if citations[i]>=Max-i:# len(citations[i:])
            flag = 1
            return Max-i
    if flag == 0:
        return 0


""" def solution(citations):

    citations.sort()
    Max = len(citations)
    for i in range(1,Max+1):
        cnt = 0
        for j in citations:
            if i<=j:
                cnt += 1
        if cnt > 0:
            if cnt >= i:
                return cnt
        else:
            return 0 """




citations = [0,0,0,0,0,2,2]
print(solution(citations))
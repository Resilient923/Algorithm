from itertools import permutations as pt

def solution(k, dungeons):
    # [최소 필요 피로도, 소모피로도]
    # dp,... 아니면 완탐
    length = len(dungeons)
    data = list(pt(dungeons,length))
    Max = 0
    for case in data:
        k_tmp = k
        i = 0
        cnt = 0
        print(case)
        while k_tmp >= 0:
            if i == length:
                    break
            if k_tmp >= case[i][0]:
                k_tmp -= case[i][1]
                cnt += 1
                i += 1
            else:
                break
        if Max < cnt:
            Max = cnt
    print(Max)

print(solution(80,[[80,20],[50,40],[30,10]]	))
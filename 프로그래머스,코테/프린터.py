import sys
input = sys.stdin.readline

def solution(priorities, location):
    check = [0 for _ in range(len(priorities))]
    check[location] = 1
    cnt = 0 
    while True:
        if priorities[0] == max(priorities):
            cnt+=1
            if check[0]==1:
                answer = cnt
                break
            else:
                priorities.pop(0)
                check.pop(0)
        else:
            priorities.append(priorities.pop(0))
            check.append(check.pop(0))

    answer = 0
    return answer

solution([1, 1, 9, 1, 1, 1],0)
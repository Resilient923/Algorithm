import sys
from collections import deque
from collections import defaultdict
tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]




def solution(tickets):
    answer = []
    # key가 출발지, value에 목적지들 담아놓은 딕셔너리
    dict = defaultdict(list)

    for start,end in tickets:
        dict[start].append(end)
    # 알파벳 순서대로 정렬
    for key,value in dict.items():
        dict[key] = sorted(value)
    # print(dict)
    stack = ["ICN"]
    while stack:
        now = stack[-1]
        # print(answer)
        if len(dict[now])==0 or now not in dict:
            # return stack
            answer.append(stack.pop())
        else:
            stack.append(dict[now].pop(0))
                
    return answer[::-1]
    
print(solution(tickets))
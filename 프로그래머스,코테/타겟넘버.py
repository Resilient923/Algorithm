from collections import deque

numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    q = deque()
    q.append(0)
    while numbers:
        temp = []
        while q:
            num = q.popleft()
            temp.append(num+numbers[0])
            temp.append(num-numbers[0])
        numbers.pop(0)
        q.extend(temp)
    
    answer = q.count(target)
    return answer
    
print(solution(numbers,target))
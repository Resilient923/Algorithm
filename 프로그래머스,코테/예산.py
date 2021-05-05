def solution(d, budget):
    d.sort()
    cnt = 0
    answer = 0
    for i in d:
        cnt += i
        if cnt <= budget:
            
            answer += 1

    
        
    return answer

print(solution([1,3,2,5,4],9))
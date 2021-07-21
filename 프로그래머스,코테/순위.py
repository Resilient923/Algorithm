n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
def solution(n, results):
    answer = 0
    winner = {i:set() for i in range(1,n+1)}
    loser = {i:set() for i in range(1,n+1)}
    for win, lose in results:
        winner[win].add(lose)
        loser[lose].add(win)
    for i in range(1,n+1):
        for lose in winner[i]:
            loser[lose].update(loser[i])
        for win in loser[i]:
            winner[win].update(winner[i])
    for i in range(1,n+1):
        if len(loser[i]) + len(winner[i]) == n-1:
            answer += 1
    return answer

print(solution(n,results))
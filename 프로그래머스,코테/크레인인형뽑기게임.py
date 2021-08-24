def solution(board, moves):
    answer = 0
    data = []
    def pick_up(number,data):
        for i in range(len(data)):
            if board[i][number-1] !=0:
                data.append(board[i][number-1])
                board[i][number-1] = 0
                break
    for i in moves:
        pick_up(i,data)
        print(data)
        if len(data) > 1:
            if data[-1] == data[-2]:
                answer += 2
                del data[-1]
                del data[-1]

            

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))
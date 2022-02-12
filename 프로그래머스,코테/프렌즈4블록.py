def solution(m, n, board):
    answer = 0
    # 4개 모이는지 확인하는 함수
    def check(board):
        block = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    block.update({(i,j),(i+1,j),(i+1,j+1),(i,j+1)})
        return block

    # 없앤 블록들 0으로 처리하는 함수    
    def remove(block,board):
        board = [list(r) for r in board]
        for blo in block:
            x,y = blo
            board[x][y] = ''
        return board
    
    # 내려보내는 함수
    def down(board):
        cnt = 0 
        # 처음에는 아래서 부터 고려했지만 
        # 다음과 같은 방법으로 서로 자리를 바꿔주면 아래로 내려보낼 수 있다.
        for i in range(m-1): 
            for j in range(n): 
                if board[i][j] and not board[i+1][j]: 
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j] 
                    cnt += 1 
        return cnt, board
    
    while 1:
        # 여기서 4개짜리 묶음이 하나도 없는지 체크해서 41번째줄에 전달
        block = check(board)
        answer += len(block)
        # 삭제
        board = remove(block,board)
        #while문을 돌리기위한 cnt = 1
        print(board)
        cnt = 1
        while cnt:
            # 내려보낸 결과 board 와 하나라도 내려갔는지 cnt를 return 받는다.
            cnt,board = down(board)
        if not cnt and not len(block):
            break
            
    return answer
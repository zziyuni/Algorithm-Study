def solution(board, moves):
    answer = 0
    basket = []
    while moves:
        pos= moves.pop(0)
        for i in range(len(board)):
            if board[i][pos-1] != 0:
                if basket and board[i][pos-1] == basket[-1]:
                    basket.pop()
                    answer+=2
                else:
                    basket.append(board[i][pos-1])
                board[i][pos-1] = 0
                break
    return answer

def solution(board, moves):
    answer = 0
    '''
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
                break'''
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            if basket and basket[-1] == board[j][i-1]:
                answer+=2
                basket.pop()
            else:
                basket.append(board[j][i-1])
            board[j][i-1] = 0
            break

    return answer

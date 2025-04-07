import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

board = [[0] * C for _ in range(R)]


def move(di, x, y, s):
    if di == 1:
        period = 2 * (R - 1)
        new_val = ((R - 1 - x) + s) % period
        if new_val < R:
            return 1, R - 1 - new_val, y
        else:
            return 2, new_val - (R - 1), y
    if di == 2:
        period = 2 * (R - 1)
        new_val = (x + s) % period
        if new_val < R:
            return 2, new_val, y
        else:
            return 1, period - new_val, y
    elif di == 3:
        period = 2 * (C - 1)
        new_val = (y + s) % period
        if new_val < C:
            return 3, x, new_val
        else:
            return 4, x, period - new_val
    if di == 4:
        period = 2 * (C - 1)
        new_val = ((C - 1 - y) + s) % period
        if new_val < C:
            return 4, x, C - 1 - new_val
        else:
            return 3, x, new_val - (C - 1)


for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = (s, d, z)

ans = 0
for col in range(C):
    for row in range(R):
        if board[row][col] != 0:
            ans += board[row][col][2]
            board[row][col] = 0
            break
    new_board = [[0] * C for _ in range(R)]
    for i in range(C):
        for j in range(R):
            if board[j][i] != 0:
                direction, x, y = move(board[j][i][1], j, i, board[j][i][0])
                if new_board[x][y] == 0:
                    new_board[x][y] = (board[j][i][0], direction, board[j][i][2])
                else:
                    if new_board[x][y][2] < board[j][i][2]:
                        new_board[x][y] = (board[j][i][0], direction, board[j][i][2])

    board = new_board

print(ans)

import sys

input = sys.stdin.readline

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, M, x, y, K = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
dice = [0] * 6  # 상단 북 둥 서 남 하단
moves = list(map(int, input().split()))


def move_dice(d):
    global dice, board, x, y
    nx = x + direction[d - 1][0]
    ny = y + direction[d - 1][1]
    if 0 <= nx < N and 0 <= ny < M:
        new_dice = dice[:]
        if d == 1:
            new_dice[5] = dice[2]
            new_dice[2] = dice[0]
            new_dice[0] = dice[3]
            new_dice[3] = dice[5]
        elif d == 2:
            new_dice[2] = dice[5]
            new_dice[0] = dice[2]
            new_dice[3] = dice[0]
            new_dice[5] = dice[3]
        elif d == 3:
            new_dice[5] = dice[1]
            new_dice[1] = dice[0]
            new_dice[0] = dice[4]
            new_dice[4] = dice[5]
        elif d == 4:
            new_dice[1] = dice[5]
            new_dice[0] = dice[1]
            new_dice[4] = dice[0]
            new_dice[5] = dice[4]
        dice = new_dice
        x, y = nx, ny
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[0])


for k in moves:
    move_dice(k)

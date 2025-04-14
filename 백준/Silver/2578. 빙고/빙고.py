import sys

input = sys.stdin.readline

bingo_board = list(list(map(int, input().split())) for _ in range(5))
nums = list(list(map(int, input().split())) for _ in range(5))
bingo = [[False] * 5 for _ in range(5)]

pos = {}
for i in range(5):
    for j in range(5):
        pos[bingo_board[i][j]] = (i, j)


def check_bingo():
    cnt = 0
    for i in range(5):
        if all(bingo[i]):
            cnt += 1
        if all(bingo[j][i] for j in range(5)):
            cnt += 1
    if all(bingo[i][i] for i in range(5)):
        cnt += 1
    if all(bingo[i][4 - i] for i in range(5)):
        cnt += 1
    return cnt


ans = 0

for i in range(5):
    for j in range(5):
        ans += 1
        x, y = pos[nums[i][j]]
        bingo[x][y] = True
        if check_bingo() >= 3:
            print(ans)
            exit(0)

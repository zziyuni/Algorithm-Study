import sys

input = sys.stdin.readline

bingo_board = list(list(map(int, input().split())) for _ in range(5))
nums = list(list(map(int, input().split())) for _ in range(5))
bingo = [[False] * 5 for _ in range(5)]


def check_bingo():
    cnt = 0
    for i in range(5):
        flag = False
        for j in range(5):
            if not bingo[i][j]:
                flag = True
                break
        if not flag:
            cnt += 1
    for i in range(5):
        flag = False
        for j in range(5):
            if not bingo[j][i]:
                flag = True
                break
        if not flag:
            cnt += 1
    for i in range(5):
        flag = False
        if not bingo[i][i]:
            flag = True
            break
    if not flag:
        cnt += 1
    for i in range(5):
        flag = False
        if not bingo[i][4 - i]:
            flag = True
            break
    if not flag:
        cnt += 1
    return cnt


def remove_num(n):
    global bingo
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == n:
                bingo[i][j] = True
                return check_bingo()


ans = 0

for i in range(5):
    for j in range(5):
        ans += 1
        if remove_num(nums[i][j]) >= 3:
            print(ans)
            exit(0)

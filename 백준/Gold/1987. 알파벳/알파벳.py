import sys

input = sys.stdin.readline


def convert_with_ord(char):
    return ord(char) - ord('A')


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue
        if alphabet[convert_with_ord(board[nx][ny])]:
            alphabet[convert_with_ord(board[nx][ny])] = False
            dfs(nx, ny, cnt + 1)
            alphabet[convert_with_ord(board[nx][ny])] = True


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, input().split())
board = list(list(input().strip()) for _ in range(R))

alphabet = [True] * 26
alphabet[convert_with_ord(board[0][0])] = False

ans = 1
dfs(0, 0, 1)

print(ans)

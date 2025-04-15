import sys

input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def robot(r, c):
    global clean, x, y, d, answer
    if not clean[r][c]:
        clean[r][c] = True
        answer += 1
    flag = False
    for i in range(4):
        nr = r + directions[i][0]
        nc = c + directions[i][1]
        if 0 <= nr < N and 0 <= nc < M and rooms[nr][nc] == 0 and not clean[nr][nc]:
            flag = True  # 청소안한 칸이 있음
    if flag:
        d = (d - 1) % 4
        nr = r + directions[d][0]
        nc = c + directions[d][1]
        if 0 <= nr < N and 0 <= nc < M and rooms[nr][nc] == 0 and not clean[nr][nc]:
            x = nr
            y = nc
    else:
        nr = r - directions[d][0]
        nc = c - directions[d][1]
        if 0 <= nr < N and 0 <= nc < M and rooms[nr][nc] == 0:
            x = nr
            y = nc
        else:
            return False
    return True


N, M = map(int, input().split())
x, y, d = map(int, input().split())
rooms = list(list(map(int, input().split())) for _ in range(N))
clean = [[False] * M for _ in range(N)]
answer = 0
while True:

    res = robot(x, y)
    if not res:
        break

print(answer)

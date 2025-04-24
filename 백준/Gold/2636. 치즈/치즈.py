import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check_melt(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if outer[nx][ny]:
            return True
    return False


def make_outer(a, b, outer):
    stack = [(a, b)]
    outer[a][b] = True
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if cheese[nx][ny] == 0 and not outer[nx][ny]:
                stack.append((nx, ny))
                outer[nx][ny] = True


cheese = list(list(map(int, input().split())) for _ in range(n))
outer = [[False] * m for _ in range(n)]
make_outer(0, 0, outer)

melted = []

time = 0
answer = 0
cnt = 0
while True:
    flag = True
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                flag = False
                cnt += 1
                if check_melt(i, j):
                    melted.append((i, j))
    if flag:
        break
    for me in melted:
        x, y = me
        cheese[x][y] = 0
        outer[x][y] = True
        make_outer(x, y, outer)
    time += 1
    answer = cnt
    cnt = 0

print(time, answer, sep='\n')

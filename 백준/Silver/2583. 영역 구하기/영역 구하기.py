import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n, k = map(int, input().split())
square = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            square[i][j] = 1

cnt = 0


def dfs(x, y):
    global cnt
    if x < 0 or x >= m or y < 0 or y >= n:
        return 0
    if square[x][y] == 1:
        return 0

    square[x][y] = 1
    cnt += 1
    for i in range(4):
        dfs(x + dx[i], y + dy[i])

    return cnt


area = []
for i in range(m):
    for j in range(n):
        cnt = dfs(i, j)
        if cnt:
            area.append(cnt)
            cnt = 0

area.sort()
print(len(area))
for i in area:
    print(i, end=' ')

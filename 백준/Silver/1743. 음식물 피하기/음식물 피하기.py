import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, k = map(int, input().split())

food = [[False for _ in range(m + 1)] for _ in range(n + 1)]

for _ in range(k):
    r, c = map(int, input().split())
    food[r][c] = True


def find_food(x, y):
    global area

    if x < 1 or y < 1 or x > n or y > m:
        return False
    if food[x][y]:
        food[x][y] = False
        area += 1
        for i in range(4):
            find_food(x + dx[i], y + dy[i])
    return True


ans = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if food[i][j]:
            area = 0
            if find_food(i, j):
                ans = max(ans, area)

print(ans)

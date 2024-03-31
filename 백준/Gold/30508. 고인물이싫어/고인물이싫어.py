import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
h, w = map(int, input().split())

street = []

for _ in range(n):
    street.append(list(map(int, input().split())))

rain = [[1 for _ in range(m)] for _ in range(n)]
k = int(input())

for _ in range(k):
    r, c = map(int, input().split())
    rain[r - 1][c - 1] = 0


def check():
    while drain:
        x, y = drain.popleft()
        for i in range(4):
            if x + dx[i] < 0 or y + dy[i] < 0 or x + dx[i] >= n or y + dy[i] >= m:
                continue
            if street[x][y] <= street[x + dx[i]][y + dy[i]] and rain[x + dx[i]][y + dy[i]] != 0:
                rain[x + dx[i]][y + dy[i]] = 0
                drain.append((x + dx[i], y + dy[i]))


def bfs(x, y):
    if x < 0 or y < 0 or x + h > n or y + w > m:
        return False
    for i in range(x, x + h):
        for j in range(y, y + w):
            if rain[i][j] == 1:
                return False
    return True


ans = 0

drain = deque()

for i in range(n):
    for j in range(m):
        if rain[i][j] == 0:
            drain.append((i, j))
            check()

DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

# 누적합 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        DP[i][j] = DP[i][j - 1] + DP[i - 1][j] - DP[i - 1][j - 1] + rain[i - 1][j - 1]

ans = 0

for i in range(n - h + 1):
    for j in range(m - w + 1):
        if rain[i][j] == 0:
            if DP[i + h][j + w] - DP[i][j + w] - DP[i + h][j] + DP[i][j] == 0:
                ans += 1

print(ans)


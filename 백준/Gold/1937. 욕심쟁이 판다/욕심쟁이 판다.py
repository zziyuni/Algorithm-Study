import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
bamboo = list(list(map(int, input().split())) for _ in range(n))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dp = [[0] * n for _ in range(n)]


def dfs(x, y):
    if dp[x][y] != 0:
        return dp[x][y]
    tmp = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or ny >= n or nx >= n:
            continue
        if bamboo[nx][ny] < bamboo[x][y]:
            tmp = max(tmp, dfs(nx, ny) + 1)
    dp[x][y] = tmp
    return tmp


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
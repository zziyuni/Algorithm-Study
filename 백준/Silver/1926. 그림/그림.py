import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

painting = []
for _ in range(n):
    painting.append(list(map(int, input().split())))


def bfs(x, y):
    global r
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if painting[x][y] == 1:
        r += 1
        painting[x][y] = 0
        for i in range(4):
            bfs(x + dx[i], y + dy[i])
        return True
    return False


ans = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if painting[i][j] == 1:
            r = 0
            if bfs(i, j):
                cnt += 1
                ans = max(ans, r)

print(cnt, ans, sep='\n')

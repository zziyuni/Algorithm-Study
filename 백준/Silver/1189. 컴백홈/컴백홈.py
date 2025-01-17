import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, dis):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if nx == 0 and ny == C - 1:
            if dis == K-1:
                ans += 1
            continue
        if not visited[nx][ny] and maps[nx][ny] != 'T':
            visited[nx][ny] = True
            dfs(nx, ny, dis + 1)
            visited[nx][ny] = False


R, C, K = map(int, input().split())
maps = list(list(input().strip()) for _ in range(R))

visited = [[False] * C for _ in range(R)]
visited[R - 1][0] = True
ans = 0
dfs(R - 1, 0, 1)

print(ans)
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maps = list(list(map(int, input().split())) for _ in range(N))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0


def find_virus(m):
    q = deque()
    for i in range(N):
        for j in range(M):
            if m[i][j] == 2:
                q.append([i, j])
    return q


queue = find_virus(maps)


def dfs():
    global maps
    maps_copy = [arr[:] for arr in maps]
    q = deque([arr[:] for arr in queue])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue
            if maps_copy[nx][ny] == 0:
                maps_copy[nx][ny] = 2
                q.append([nx, ny])

    safe_count = sum(row.count(0) for row in maps_copy)

    return safe_count


def wall(n):
    global ans
    if n == 3:
        ans = max(ans, dfs())
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall(n + 1)
                maps[i][j] = 0


wall(0)
print(ans)

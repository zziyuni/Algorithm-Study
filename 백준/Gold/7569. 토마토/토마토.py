import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def ripe_tomatoes():
    queue = deque()
    max_day = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    queue.append((i, j, k, 0))
    while queue:
        x, y, z, day = queue.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if tomato[nx][ny][nz] == 0:
                    tomato[nx][ny][nz] = 1
                    queue.append((nx, ny, nz, day + 1))
                    max_day = max(max_day, day + 1)
    return max_day


M, N, H = map(int, input().split())

tomato = list(list(list(map(int, input().split())) for _ in range(N)) for _ in range(H))

if not any(0 in row for layer in tomato for row in layer):
    print(0)
    exit()

ans = ripe_tomatoes()

if any(0 in row for layer in tomato for row in layer):
    print(-1)
else:
    print(ans)

import sys
from collections import deque

input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
rooms = list(list(map(int, input().split())) for _ in range(N))


def bfs(a, b):
    global route_len, ends
    queue = deque([(a, b, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[a][b] = True
    while queue:
        x, y, depth = queue.popleft()
        if depth > route_len:
            ends = [(a, b, x, y)]
            route_len = depth
        elif depth == route_len:
            ends.append((a, b, x, y))
        for i in range(4):
            nx = x + directions[i][0]
            ny = y + directions[i][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not visited[nx][ny] and rooms[nx][ny] != 0:
                queue.append((nx, ny, depth + 1))
                visited[nx][ny] = True


answer = 0
route_len = 0
ends = []
for i in range(N):
    for j in range(M):
        if rooms[i][j] == 0:
            continue
        bfs(i, j)
for e in ends:
    answer = max(rooms[e[0]][e[1]] + rooms[e[2]][e[3]], answer)

print(answer)

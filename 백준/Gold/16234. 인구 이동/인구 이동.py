import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, L, R = map(int, input().split())

population = []
for _ in range(N):
    population.append(list(map(int, input().split())))


def bfs(a, b):
    section = [[a, b]]
    while country:
        x, y = country.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if L <= abs(population[x][y] - population[nx][ny]) <= R and not visited[nx][ny]:
                visited[nx][ny] = True
                country.append((nx, ny))
                section.append([nx, ny])
    return section


day = 0

country = deque()

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                country.append((i, j))
                section = bfs(i, j)
                if len(section) > 1:
                    ans += 1
                    divided = sum(population[x][y] for x, y in section) // len(section)
                    for x, y in section:
                        population[x][y] = divided
    if ans == 0:
        break

    day += 1

print(day)

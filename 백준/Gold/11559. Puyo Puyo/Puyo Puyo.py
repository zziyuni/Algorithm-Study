import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

puyo = []

for _ in range(12):
    puyo.append(list(input().strip()))


def break_puyo():
    for pos in check:
        puyo[pos[0]][pos[1]] = '.'


def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if puyo[j][i] != "." and puyo[k][i] == ".":
                    puyo[k][i] = puyo[j][i]
                    puyo[j][i] = "."
                    break


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                continue
            if puyo[nx][ny] == puyo[x][y] and not visited[nx][ny]:
                visited[nx][ny] = True
                check.append([nx, ny])
                q.append((nx, ny))


ans = 0

q = deque()
while True:
    visited = [[False] * 6 for _ in range(12)]
    breaking = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and not visited[i][j]:
                q.append((i, j))
                check = [[i, j]]
                visited[i][j] = True
                bfs()
                if len(check) >= 4:
                    breaking += 1
                    break_puyo()
    if breaking == 0:
        break
    down()
    ans += 1

print(ans)

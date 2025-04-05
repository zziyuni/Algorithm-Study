import sys
from collections import deque

input = sys.stdin.readline

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_empty(x, y):
    for direction in directions:
        nx = x + direction[0]
        ny = y + direction[1]
        if 0 <= nx < N and 0 <= ny < M:
            if rooms[nx][ny] == 0:
                return True
    return False


def back(x, y, di):
    if di == 0:
        return x + 1, y
    if di == 1:
        return x, y - 1
    if di == 2:
        return x - 1, y
    if di == 3:
        return x, y + 1


def rotate_90(x, y, di):
    if di == 0:
        if y - 1 >= 0 and rooms[x][y - 1] == 0:
            return x, y - 1, 3
        else:
            return x, y, 3

    if di == 1:
        if x - 1 >= 0 and rooms[x - 1][y] == 0:
            return x - 1, y, 0
        else:
            return x, y, 0
    if di == 2:
        if y + 1 < M and rooms[x][y + 1] == 0:
            return x, y + 1, 1
        else:
            return x, y, 1
    if di == 3:
        if x + 1 < N and rooms[x + 1][y] == 0:
            return x + 1, y, 2
        else:
            return x, y, 2


def clean_room(a, b, di):
    queue = deque([(a, b, di)])
    cnt = 0
    while queue:
        x, y, direction = queue.popleft()
        if rooms[x][y] == 0:
            cnt += 1
            rooms[x][y] = 2
        if not is_empty(x, y):
            nx, ny = back(x, y, direction)
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                return cnt
            if rooms[nx][ny] == 1:
                return cnt
            queue.append((nx, ny, direction))
        else:
            nx, ny, direction = rotate_90(x, y, direction)
            queue.append((nx, ny, direction))


N, M = map(int, input().split())
r, c, d = map(int, input().split())
rooms = list(list(map(int, input().split())) for _ in range(N))

print(clean_room(r, c, d))

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

pipe = list(list(input().strip()) for _ in range(R))

dx = [1, 0, -1]
dy = [1, 1, 1]


def find_route(a, b):
    stack = [(a, b)]
    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        if y == C - 1:
            return True
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and pipe[nx][ny] == '.':
                stack.append((nx, ny))
    return False


ans = 0
visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    if find_route(i, 0):
        ans += 1

print(ans)

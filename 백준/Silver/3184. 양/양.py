import sys

input = sys.stdin.readline

R, C = map(int, input().split())
yard = list(list(input().strip()) for _ in range(R))

visited = [[False] * C for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(a, b):
    stack = [(a, b)]
    wolf = 0
    sheep = 0
    if yard[a][b] == 'o':
        sheep += 1
    elif yard[a][b] == 'v':
        wolf += 1
    visited[a][b] = True
    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx >= R or ny >= C or yard[nx][ny] == '#':
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if yard[nx][ny] == 'o':
                    sheep += 1
                if yard[nx][ny] == 'v':
                    wolf += 1
                stack.append((nx, ny))
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf


ans_s = 0
ans_w = 0
for i in range(R):
    for j in range(C):
        if not visited[i][j] and yard[i][j] != '#':
            s, w = dfs(i, j)

            ans_s += s
            ans_w += w

print(ans_s, ans_w)

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    queue = deque([(a, b)])
    cnt = 0
    doc[a][b] = -1
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and doc[nx][ny] == 1:
                queue.append((nx, ny))
                doc[nx][ny] = -1
    return cnt


N = int(input())
doc = list(list(map(int, input().strip())) for _ in range(N))
ans = []
for i in range(N):
    for j in range(N):
        if doc[i][j] == 1:
            ans.append(bfs(i, j))

print(len(ans))
for c in sorted(ans):
    print(c)

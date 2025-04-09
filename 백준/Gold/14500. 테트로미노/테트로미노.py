import sys

input = sys.stdin.readline

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())

paper = list(list(map(int, input().split())) for _ in range(N))


def check_T(cx, cy):
    val = paper[cx][cy]
    plus = 0
    if cy < M - 1 and 0 < cx < N - 1:  # 오
        plus = max(paper[cx - 1][cy + 1] + paper[cx + 1][cy + 1] + paper[cx][cy + 1], plus)
    if 0 < cy < M - 1 and cx < N - 1:  # 아래
        plus = max(paper[cx + 1][cy - 1] + paper[cx + 1][cy + 1] + paper[cx + 1][cy], plus)
    if cy > 0 and 0 < cx < N - 1:  # 왼
        plus = max(paper[cx + 1][cy - 1] + paper[cx][cy - 1] + paper[cx - 1][cy - 1], plus)
    if 0 < cy < M - 1 and cx > 0:  # 위
        plus = max(paper[cx - 1][cy - 1] + paper[cx - 1][cy + 1] + paper[cx - 1][cy], plus)
    return val + plus


def find_max(cx, cy, path, val):
    global ans
    if len(path) == 4:
        ans = max(ans, val)
        return
    for i in range(4):
        nx = cx + directions[i][0]
        ny = cy + directions[i][1]
        if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in path:
            path.add((nx, ny))
            find_max(nx, ny, path, val + paper[nx][ny])
            path.remove((nx, ny))


ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, check_T(i, j))
        find_max(i, j, {(i, j)}, paper[i][j])


print(ans)

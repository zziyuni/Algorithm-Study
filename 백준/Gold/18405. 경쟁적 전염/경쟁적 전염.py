import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, K = map(int, input().split())
virus = []
cube = list(list(map(int, input().split())) for _ in range(N))

for i in range(N):
    for j in range(N):
        if cube[i][j] != 0:
            virus.append((cube[i][j], i, j, 0))  # 바이러스 종류(cube[i][j]), 바이러스에 걸린 좌표(i,j), 감염된 시간(0) queue에 넣기
virus.sort()
virus = deque(virus)
S, pos_x, pos_y = map(int, input().split())

while virus:
    v = virus.popleft()
    if v[3] >= S:  # S초 후의 상황에서 스탑하므로 S초 이상일 경우는 보지 않아도 됨
        break
    for i in range(4):
        x = v[1] + dx[i]
        y = v[2] + dy[i]
        if x >= N or y >= N or x < 0 or y < 0:
            continue
        if cube[x][y] == 0:  # 감염이 안됐다면
            cube[x][y] = v[0]
            virus.append((v[0], x, y, v[3] + 1))

print(cube[pos_x - 1][pos_y - 1])

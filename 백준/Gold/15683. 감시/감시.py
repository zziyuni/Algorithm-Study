import sys

input = sys.stdin.readline

N, M = map(int, input().split())
office = list(list(map(int, input().split())) for _ in range(N))
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cctv_directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}
answer = int(1e9)
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv.append(((i, j), office[i][j]))


def backtracking(cnt, office_info):
    global answer
    if cnt == len(cctv):
        zero_cnt = sum(row.count(0) for row in office_info)
        answer = min(zero_cnt, answer)
        return

    pos, t = cctv[cnt]
    x, y = pos
    for dirs in cctv_directions[t]:
        office_copy = [row[:] for row in office_info]
        for d in dirs:
            nx, ny = x, y
            while True:
                nx += directions[d][0]
                ny += directions[d][1]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                if office_copy[nx][ny] == 6:
                    break
                if office_copy[nx][ny] == 0:
                    office_copy[nx][ny] = -1
        backtracking(cnt + 1, office_copy)


backtracking(0, office)
print(answer)

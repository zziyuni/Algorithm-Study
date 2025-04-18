import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
space = list(list(map(int, input().split())) for _ in range(N))

dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    for j in range(3):
        dp[0][i][j] = space[0][i]

for i in range(1, N):
    for j in range(M):
        if j + 1 < M:
            dp[i][j][0] = min(dp[i][j][0], dp[i - 1][j + 1][2] + space[i][j], dp[i - 1][j + 1][1] + space[i][j])

        dp[i][j][1] = min(
            dp[i][j][1],
            dp[i - 1][j][0] + space[i][j],
            dp[i - 1][j][2] + space[i][j]
        )
        if j - 1 >= 0:
            dp[i][j][2] = min(dp[i][j][2], dp[i - 1][j - 1][0] + space[i][j], dp[i - 1][j - 1][1] + space[i][j])

answer = INF

for j in range(M):
    answer = min(answer, min(dp[N - 1][j]))

print(answer)

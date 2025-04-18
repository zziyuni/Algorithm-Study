import sys

input = sys.stdin.readline

INF = int(1e9)
N = int(input())

matrix = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[INF] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        for k in range(i, j):
            cost = matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)

print(dp[0][N - 1])

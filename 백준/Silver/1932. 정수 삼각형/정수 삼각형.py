import sys

input = sys.stdin.readline

n = int(input())

triangle = list(list(map(int, input().split())) for _ in range(n))

DP = [[0] * n for _ in range(n)]

DP[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(len(triangle[i])):
        DP[i][j] = max(DP[i][j], DP[i - 1][j] + triangle[i][j], DP[i - 1][j - 1] + triangle[i][j] if j - 1 >= 0 else 0)

print(max(max(DP)))

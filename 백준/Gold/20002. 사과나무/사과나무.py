import sys

input = sys.stdin.readline

N = int(input())

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

profit = list(list(map(int, input().split())) for _ in range(N))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + profit[i - 1][j - 1]

ans = -int(1e9)
for i in range(N):
    for j in range(1, N + 1 - i):
        for k in range(1, N + 1 - i):
            ans = max(ans, prefix_sum[j + i][k + i] - prefix_sum[j - 1][k + i] - prefix_sum[j + i][k - 1] +
                      prefix_sum[j - 1][k - 1])

print(ans)

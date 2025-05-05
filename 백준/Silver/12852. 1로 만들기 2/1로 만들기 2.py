import sys

input = sys.stdin.readline

N = int(input())
dp = [1e9] * (N + 1)
dp[N] = 0
prev = [0] * (N + 1)
for i in range(N, -1, -1):

    if i % 3 == 0:
        if dp[i // 3] > dp[i] + 1:
            dp[i // 3] = dp[i] + 1
            prev[i // 3] = i

    if i % 2 == 0:
        if dp[i // 2] > dp[i] + 1:
            dp[i // 2] = dp[i] + 1
            prev[i // 2] = i

    if i - 1 >= 0:
        if dp[i - 1] > dp[i] + 1:
            dp[i - 1] = dp[i] + 1
            prev[i - 1] = i

print(dp[1])
path = []
now = 1
while now != 0:
    path.append(now)
    now = prev[now]

print(*reversed(path))

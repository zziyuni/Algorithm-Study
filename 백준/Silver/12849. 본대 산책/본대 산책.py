import sys
from collections import deque

input = sys.stdin.readline

D = int(input())

route = [[] for _ in range(8)]

for x, y in [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 6), (5, 7), (6, 7)]:
    route[x].append(y)
    route[y].append(x)

dp = [[0] * 8 for _ in range(D + 1)]
dp[0][0] = 1
for i in range(1, D + 1):
    for j in range(8):
        for k in route[j]:
            dp[i][j] += dp[i - 1][k]
            dp[i][j] %= int(1e9 + 7)

print(dp[D][0])
import sys

input = sys.stdin.readline

INF = int(1e9)
n, k = map(int, input().split())

DP = [INF] * (k + 1)
coins = []
for _ in range(n):
    cost = int(input())
    coins.append(cost)

DP[0] = 0
for i in range(k + 1):
    for j in coins:
        if i - j < 0:
            continue
        DP[i] = min(DP[i - j] + 1, DP[i])
if DP[k] == INF:
    print(-1)
else:
    print(DP[k])

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
DP = [0 for _ in range(k + 1)]

for i in coin:
    for j in range(i, k + 1):
        if j - i != 0 and DP[j - i] == 0:
            continue
        if DP[j] == 0:
            DP[j] = DP[j - i] + 1
            continue
        DP[j] = min(DP[j], DP[j - i] + 1)

print(DP[k] if DP[k] != 0 else -1)

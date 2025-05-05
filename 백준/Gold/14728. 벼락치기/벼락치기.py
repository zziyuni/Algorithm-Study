import sys

input = sys.stdin.readline

N, T = map(int, input().split())

score = list(list(map(int, input().split())) for _ in range(N))

dp = [0] * (T+1)

for t, s in score:
    for j in range(T, t - 1, -1):
        dp[j] = max(dp[j], dp[j - t] + s)

print(max(dp))

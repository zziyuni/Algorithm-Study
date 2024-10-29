import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 2 or i == 5:
        dp[i] = 1
        continue
    if i == 1 or i == 3:
        continue
    if i < 5:
        dp[i] = dp[i - 2]
    else:
        if dp[i - 2] != 0 and dp[i - 5] != 0:
            dp[i] = min(dp[i - 2], dp[i - 5])
        elif dp[i - 2] == 0:
            dp[i] = dp[i - 5]
        else:
            dp[i] = dp[i - 2]

    if dp[i] > 0:
        dp[i] += 1

print(dp[n] if dp[n] != 0 else -1)

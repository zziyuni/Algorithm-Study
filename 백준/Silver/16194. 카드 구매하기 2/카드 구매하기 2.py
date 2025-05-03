import sys

input = sys.stdin.readline

N = int(input())
price = list(map(int, input().split()))
dp = [int(1e9)] * (N + 1)
dp[0] = 0
for i in range(N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + price[j - 1])

print(dp[N])

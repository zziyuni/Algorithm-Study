N = int(input())

dp = [0] * (N // 2 + 1)
dp[0] = 1
for i in range(1, N // 2 + 1):
    for j in range(i):
        dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % 987654321

print(dp[N // 2])
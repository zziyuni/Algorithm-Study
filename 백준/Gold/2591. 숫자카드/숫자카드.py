card = input().strip()

n = len(card)

dp = [0] * (n)
# DP로 조합 계산
dp[0] = 1
for i in range(1, n):
    if card[i] != '0':
        dp[i] += dp[i - 1]
    if int(card[i - 1:i + 1]) <= 34 and card[i - 1] != '0':
        if i == 1:
            dp[i] += 1
            continue
        dp[i] += dp[i - 2]

print(dp[n - 1])
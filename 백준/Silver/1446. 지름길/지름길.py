import sys

input = sys.stdin.readline

N, D = map(int, input().split())
route = list(list(map(int, input().split())) for _ in range(N))
route.sort()
dp = [i for i in range(10001)]

for j in range(N):
    s, e, distance = route[j]
    for i in range(D + 1):
        if e == i:
            dp[i] = min(dp[i], dp[s] + distance)
        dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[D])
import sys

input = sys.stdin.readline

MOD = 2 ** 64
M, N = map(int, input().split())

candy = list(int(input()) for _ in range(N))

extra = sum(candy) - M

candy.sort()
ans = 0
for i in range(N):
    tmp = min(candy[i], extra // (N - i))
    ans = (ans + tmp ** 2) % MOD
    extra -= tmp

print(ans)

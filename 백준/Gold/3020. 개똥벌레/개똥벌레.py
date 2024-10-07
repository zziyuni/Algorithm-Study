import sys

input = sys.stdin.readline

N, H = map(int, input().split())
A = list(int(input()) for _ in range(N))
up = [0] * (H + 1)
down = [0] * (H + 1)
for i in range(0, N, 2):
    up[A[i]] += 1
for i in range(1, N, 2):
    down[A[i]] += 1

for i in range(H - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]

ans = [0] * (H+1)
for i in range(1, H + 1):
    ans[i] = up[i] + down[H - i + 1]

ans = ans[1:]
print(min(ans), ans.count(min(ans)))

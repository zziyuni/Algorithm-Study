import sys
import math

input = sys.stdin.readline

N, M, L = map(int, input().split())

pos = list(map(int, input().split())) if N > 0 else []
pos = [0] + pos + [L]
pos.sort()

ans = 0
left = 1
right = 0
for i in range(N + 1):
    right = max(right, pos[i + 1] - pos[i])

while left <= right:
    mid = (left + right) // 2
    installed = 0
    for i in range(N + 1):
        if pos[i + 1] - pos[i] > mid:
            installed += (pos[i + 1] - pos[i] - 1) // mid

    if installed > M:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

print(ans)

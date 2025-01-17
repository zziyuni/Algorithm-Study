import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
pair = [[False] * (N + 1) for _ in range(N + 1)]
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    pair[a][b] = True
    pair[b][a] = True

for c in combinations(range(1, N + 1), 3):
    c1 = c[0]
    c2 = c[1]
    c3 = c[2]
    if pair[c1][c2] or pair[c1][c3] or pair[c2][c3]:
        continue
    ans += 1

print(ans)
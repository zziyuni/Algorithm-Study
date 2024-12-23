import sys

input = sys.stdin.readline

N = int(input())
points = list(list(map(int, input().split())) for _ in range(N))
plus = []
minus = []

for p in points:
    plus.append(p[0] + p[1])
    minus.append(p[0] - p[1])

plus.sort()
minus.sort()
ans = max(plus[-1] - plus[0], minus[-1] - minus[0])

print(ans)

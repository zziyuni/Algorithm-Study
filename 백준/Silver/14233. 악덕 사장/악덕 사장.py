import sys

input = sys.stdin.readline

n = int(input())

Ai = list(map(int, input().split()))

Ai = sorted(Ai)

ans = Ai[0]

for i in range(1, n):
    ans = min(int(Ai[i] / (i + 1)), ans)

print(ans)

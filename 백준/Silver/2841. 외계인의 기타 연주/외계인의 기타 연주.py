import sys

input = sys.stdin.readline

N, P = map(int, input().split())

fingers = [[] for _ in range(N)]
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    if len(fingers) == 0:
        fingers[a - 1].append(b)
        ans += 1
        continue
    while len(fingers[a - 1]) > 0 and fingers[a - 1][-1] > b:
        ans += 1
        fingers[a - 1].pop()
    if len(fingers[a - 1]) == 0 or fingers[a - 1][-1] != b:
        fingers[a - 1].append(b)
        ans += 1
print(ans)

import sys

input = sys.stdin.readline

n = int(input())
straw = list(int(input()) for _ in range(n))

straw = sorted(straw, reverse=True)

for i in range(n - 2):
    if straw[i] < straw[i + 1] + straw[i + 2]:
        print(straw[i] + straw[i + 1] + straw[i + 2])
        exit()
    else:
        continue

print(-1)

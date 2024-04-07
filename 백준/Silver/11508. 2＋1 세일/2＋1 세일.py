import sys

input = sys.stdin.readline

n = int(input())

price = []
for _ in range(n):
    p = int(input())
    price.append(p)

price = sorted(price, reverse=True)

ans = 0
for i in range(n):
    if (i + 1) % 3 == 0:
        continue
    ans += price[i]

print(ans)

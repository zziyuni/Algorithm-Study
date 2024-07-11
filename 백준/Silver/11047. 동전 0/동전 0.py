import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
result = 0
for c in coins:
    result += k // c
    k %= c

    if k == 0:
        break

print(result)

import sys

input = sys.stdin.readline

N, K, A, B = map(int, input().split())
water = [K] * N

ans = 0
while water.count(0) == 0:
    ans += 1
    min_water = min(water)
    min_index = water.index(min_water)
    for i in range(min_index, min_index + A):
        water[i] += B

    for i in range(N):
        water[i] -= 1

print(ans)
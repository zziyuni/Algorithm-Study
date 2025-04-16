import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
city = list(list(map(int, input().split())) for _ in range(N))


def find_shortest_chicken(hx, hy, cx, cy):
    return abs(hx - cx) + abs(hy - cy)


homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        if city[i][j] == 2:
            chickens.append((i, j))
pairs = list(combinations(chickens, M))

answer = int(1e9)

for pair in pairs:
    min_sum = 0
    for h in homes:
        min_val = int(1e9)
        for p in pair:
            min_val = min(min_val, find_shortest_chicken(h[0], h[1], p[0], p[1]))
        min_sum += min_val
    answer = min(min_sum, answer)

print(answer)

import sys
from itertools import combinations

input = sys.stdin.readline
N, L, R, X = map(int, input().split())
level = list(map(int, input().split()))

answer = 0
for i in range(2, N + 1):
    for comb in combinations(level, i):
        total = sum(comb)
        if L <= total <= R and max(comb) - min(comb) >= X:
            answer += 1

print(answer)

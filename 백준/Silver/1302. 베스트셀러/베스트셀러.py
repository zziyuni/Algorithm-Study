import sys

best = {}
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    book = input().strip()
    if book in best:
        best[book] += 1
    else:
        best[book] = 1

sorted_map = dict(sorted(best.items(), key=lambda item: (-item[1], item[0]), reverse=False))

ans = next(iter(sorted_map.keys()))
print(ans)

import sys
from itertools import accumulate

input = sys.stdin.readline

n, q = map(int, input().split())

nums = list(map(int, input().split()))

nums = sorted(nums)
sums = list(accumulate(nums))
for _ in range(q):
    a, b = map(int, input().split())

    if a - 2 < 0:
        print(sums[b - 1])
    else:
        print(sums[b - 1] - sums[a - 2])

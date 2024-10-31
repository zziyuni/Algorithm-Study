import sys
import heapq
import copy

input = sys.stdin.readline
K, N = map(int, input().split())
nums = list(map(int, input().split()))

primeNum = copy.deepcopy(nums)

cur = 0
for i in range(N):
    cur = heapq.heappop(nums)
    for p in primeNum:
        if p * cur >= 2 ** 31:
            break
        heapq.heappush(nums, p * cur)
        if cur % p == 0:
            break

print(cur)

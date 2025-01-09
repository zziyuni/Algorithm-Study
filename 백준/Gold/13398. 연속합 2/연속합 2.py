import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

DP = [-1e9] * n
E = [-1e9] * n
DP[0] = nums[0]

for i in range(1, n):
    DP[i] = max(nums[i], nums[i] + DP[i - 1])
    if i >= 2:
        E[i] = max(E[i - 1] + nums[i], DP[i - 2] + nums[i])

print(max(max(E), max(DP)))
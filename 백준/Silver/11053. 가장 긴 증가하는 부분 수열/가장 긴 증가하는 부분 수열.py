import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

DP = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[n] for n in nums]

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j] and len(dp[i]) < len(dp[j]) + 1:
            dp[i] = dp[j] + [nums[i]]

max_seq = max(dp, key=len)
print(len(max_seq))
print(*max_seq)

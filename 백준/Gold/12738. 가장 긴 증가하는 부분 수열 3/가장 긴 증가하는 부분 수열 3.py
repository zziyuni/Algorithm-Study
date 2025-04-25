import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


def binary_search(dp, target):
    left, right = 0, len(dp)
    while left < right:
        mid = (left + right) // 2
        if dp[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


dp = []
for n in nums:
    idx = binary_search(dp, n)
    if idx == len(dp):
        dp.append(n)
    else:
        dp[idx] = n

print(len(dp))

import sys

n = int(input())
input = sys.stdin.readline

nums = list(int(input()) for _ in range(n))

nums = sorted(nums,reverse=True)

for i in nums:
    print(i)

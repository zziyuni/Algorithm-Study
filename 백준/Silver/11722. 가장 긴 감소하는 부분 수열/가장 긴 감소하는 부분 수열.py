import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dsc_nums = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if nums[i] < nums[j]:
            dsc_nums[i] = max(dsc_nums[i], dsc_nums[j] + 1)

print(max(dsc_nums))

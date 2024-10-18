import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

start = 0
end = 0

sum_num = nums[0]
ans = 0
while True:
    if sum_num == M:
        ans += 1
    if sum_num < M:
        if end == N - 1:
            break
        end += 1
        sum_num += nums[end]
    else:
        sum_num -= nums[start]
        start += 1

print(ans)

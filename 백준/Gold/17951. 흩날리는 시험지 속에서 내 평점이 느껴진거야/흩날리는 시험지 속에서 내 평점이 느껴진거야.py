import sys

input = sys.stdin.readline

n, k = map(int, input().split())

score = list(map(int, input().split()))

start = 0
end = sum(score)

while start <= end:
    mid = (start + end) // 2
    sum_score = 0
    cnt = 0
    for s in score:
        sum_score += s
        if sum_score >= mid:
            sum_score = 0
            cnt += 1
    if cnt >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)

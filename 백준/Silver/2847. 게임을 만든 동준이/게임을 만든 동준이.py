import sys

input = sys.stdin.readline

n = int(input())
score = list(int(input()) for _ in range(n))

cnt = 0
for i in range(1, n):
    if score[n - i] <= score[n - (i + 1)]:
        cnt += score[n - (i + 1)] - score[n - i] + 1
        score[n - (i + 1)] = score[n - i] - 1

print(cnt)

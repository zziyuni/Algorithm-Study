import sys

input = sys.stdin.readline

n = int(input())

score = list(int(input()) for _ in range(n))

DP = [0] * n
DP[0] = score[0]
for i in range(1, n):
    if i == 1:
        DP[i] = score[0] + score[1]
    elif i == 2:
        DP[i] = max(score[0]+score[2],score[1]+score[2])
    else:
        DP[i] = max(DP[i-2]+score[i], DP[i-3]+score[i-1]+score[i])

print(DP[-1])
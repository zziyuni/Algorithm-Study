import sys

input = sys.stdin.readline

T = int(input())
DP = [0] * 10001
DP[1] = 1
DP[2] = 2
DP[3] = 3

DP_3_2 = [0] * 10001

DP_3_2[2] = 1
DP_3_2[3] = 1

for i in range(4, 10001):
    DP_3_2[i] = DP_3_2[i - 2]
    if i % 3 == 0:
        DP_3_2[i] += 1

    DP[i] = DP[i - 1] + DP_3_2[i]

for _ in range(T):
    n = int(input())
    print(DP[n])

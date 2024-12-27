import sys

input = sys.stdin.readline

N = int(input())
A = list((map(int, input().split())))
DP = [10e9] * N
DP[0] = 0
for i in range(N):
    a = A[i]
    for j in range(1, min(a + 1, N - i)):
        DP[i + j] = min(DP[i + j], DP[i] + 1)

if DP[N-1] == 10e9:
    print(-1)
else:
    print(DP[N-1])
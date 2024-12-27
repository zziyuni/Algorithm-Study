N = int(input())

DP = [False] * 1001
DP[1] = True
DP[3] = True
DP[4] = True

for i in range(5, N+1):
    DP[i] = not DP[i - 1] or not DP[i - 3] or not DP[i - 4]

if DP[N]:
    print('SK')
else:
    print('CY')

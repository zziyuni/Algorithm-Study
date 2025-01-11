import sys

input = sys.stdin.readline

N, M = map(int, input().split())
distance = [0]
condition = [0]
for _ in range(N):
    d = int(input())
    distance.append(d)
for _ in range(M):
    c = int(input())
    condition.append(c)

tiredness = [[1e9] * (M + 1) for _ in range(N + 1)]

for i in range(M + 1):
    tiredness[0][i] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        tiredness[i][j] = min(tiredness[i][j - 1], tiredness[i - 1][j - 1] + distance[i] * condition[j])

print(min(tiredness[N]))

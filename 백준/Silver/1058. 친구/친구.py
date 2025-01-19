import sys

input = sys.stdin.readline

N = int(input())

friend = [list(input().strip()) for _ in range(N)]
distance = [[1e9] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if friend[i][j] == 'Y':
            distance[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or k == i or k == j:
                continue
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if distance[i][j] <= 2:
            cnt += 1
    ans = max(ans, cnt)
print(ans)

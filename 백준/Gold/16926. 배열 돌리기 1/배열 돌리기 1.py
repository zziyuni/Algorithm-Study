import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = list((list(map(int, input().split()))) for _ in range(N))

layer = min(N, M) // 2

queue = deque()
new_arr = [[0] * M for _ in range(N)]
for i in range(layer):
    queue.clear()
    queue.extend(arr[i][i:M - i])
    queue.extend(row[M - 1 - i] for row in arr[i + 1:N - i - 1])
    queue.extend(arr[N - i - 1][i:M - i][::-1])

    queue.extend(row[i] for row in arr[i + 1:N - i - 1][::-1])

    queue.rotate(-R)

    for j in range(i, M - i):
        new_arr[i][j] = queue.popleft()
    for j in range(i + 1, N - 1 - i):
        new_arr[j][M - i - 1] = queue.popleft()
    for j in range(M - i - 1, i - 1, -1):
        new_arr[N - i - 1][j] = queue.popleft()

    for j in range(N - 2 - i, i, -1):
        new_arr[j][i] = queue.popleft()

for a in new_arr:
    print(*a)

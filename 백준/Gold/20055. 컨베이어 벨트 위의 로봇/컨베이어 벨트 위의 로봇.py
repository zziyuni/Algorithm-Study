import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
top = deque()
bottom = deque()
for i in range(N - 1, -1, -1):
    top.append([A[i], 0])
for i in range(2 * N - 1, N - 1, -1):
    bottom.append([A[i], 0])

step = 0
zero = 0
while True:
    if zero >= K:
        break
    bottom.append(top.popleft())
    top.append(bottom.popleft())
    step += 1
    if top[0][1] == 1:
        top[0][1] = 0
    for i in range(1, N):
        if top[i][1] == 1:
            if top[i - 1][0] >= 1 and top[i - 1][1] == 0:
                top[i - 1][0] -= 1
                if top[i - 1][0] == 0:
                    zero += 1
                top[i - 1][1] = 1
                top[i][1] = 0
            if top[0][1] == 1:
                top[0][1] = 0

    if top[N - 1][1] == 0 and top[N - 1][0] >= 1:
        top[N - 1][0] -= 1
        if top[N - 1][0] == 0:
            zero += 1
        top[N - 1][1] = 1


print(step)

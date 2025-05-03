import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
indegree = [0] * N
order = [[] for _ in range(N)]
delay = [0] * N
time = [0] * N
queue = deque()
for i in range(N):
    a = list(map(int, input().split()))
    delay[i] = a[0]
    pre = a[1:-1]
    indegree[i] = len(pre)
    for j in pre:
        order[j - 1].append(i)
    if indegree[i] == 0:
        queue.append(i)
        time[i] = delay[i]

while queue:
    x = queue.popleft()
    for nxt in order[x]:
        indegree[nxt] -= 1
        time[nxt] = max(time[nxt], time[x] + delay[nxt])
        if indegree[nxt] == 0:
            queue.append(nxt)
print(*time)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

works = [[] for _ in range(N)]
times = []
indegree = []

for i in range(N):
    work = list(map(int, input().split()))
    times.append(work[0])
    indegree.append(work[1])
    for pre in work[2:]:
        works[pre - 1].append(i)

queue = deque()
dp = [0] * N
for i in range(N):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = times[i]

while queue:
    cur = queue.popleft()
    for nxt in works[cur]:
        indegree[nxt] -= 1
        dp[nxt] = max(dp[nxt], dp[cur] + times[nxt])
        if indegree[nxt] == 0:
            queue.append(nxt)

print(max(dp))

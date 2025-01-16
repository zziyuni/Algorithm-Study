import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    delay = list(map(int, input().split()))
    seq = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    for _ in range(K):
        x, y = map(int, input().split())
        seq[x].append(y)
        indegree[y] += 1
    W = int(input())
    ans = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            ans[i] = delay[i - 1]
    while q:
        cur = q.popleft()
        for i in seq[cur]:
            indegree[i] -= 1
            ans[i] = max(ans[cur] + delay[i - 1], ans[i])
            if indegree[i] == 0:
                q.append(i)
    print(ans[W])
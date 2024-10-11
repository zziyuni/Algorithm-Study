import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
visited = [False] * N

nodes = deque()
cnt = 0
for i in range(N):
    if visited[i]:
        continue
    nodes = deque([i])
    visited[i] = True
    cnt += 1
    while len(nodes) != 0:
        k = nodes.popleft()
        for a in graph[k]:
            if not visited[a]:
                nodes.append(a)
                visited[a] = True

print(cnt)

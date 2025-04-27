import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

gender = list(input().split())
path = [[] for _ in range(N)]
for _ in range(M):
    u, v, d = map(int, input().split())
    if gender[u - 1] != gender[v - 1]:
        path[u - 1].append([v - 1, d])
        path[v - 1].append([u - 1, d])

nodes = [(0, 0)]
visited = [False] * N
result = 0
while nodes:
    distance, cur = heapq.heappop(nodes)
    if visited[cur]:
        continue
    visited[cur] = True
    result += distance
    for neighbor, d in path[cur]:
        if not visited[neighbor]:
            heapq.heappush(nodes, (d, neighbor))

if not all(visited):
    print(-1)
else:
    print(result)

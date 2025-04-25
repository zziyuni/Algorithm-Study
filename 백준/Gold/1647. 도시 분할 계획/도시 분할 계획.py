import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

path = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    path[a - 1].append((b - 1, c))
    path[b - 1].append((a - 1, c))

hq = [(0, 0)]

visited = [False] * N
answer = 0
max_cost = 0
while hq:
    cur_cost, x = heapq.heappop(hq)
    if visited[x]:
        continue
    max_cost = max(max_cost, cur_cost)
    answer += cur_cost
    visited[x] = True
    for neighbor, cost in path[x]:
        if not visited[neighbor]:
            heapq.heappush(hq, (cost, neighbor))

print(answer - max_cost)

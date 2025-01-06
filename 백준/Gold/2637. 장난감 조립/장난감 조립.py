import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
in_degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    in_degree[b] += 1
    graph[a].append([b, c])

answer = [0] * (N + 1)
answer[N] = 1
queue = deque()

for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

total_cnt = 0
base = 0
while queue:
    cur = queue.popleft()
    for i, cnt in graph[cur]:
        answer[i] += answer[cur] * cnt
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)

for i in range(1, N + 1):
    if len(graph[i]) == 0:
        print(i, answer[i])

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

relation = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

visited = [False] * N


def dfs(a, depth):
    if depth == 4:
        print(1)
        sys.exit(0)
    visited[a] = True
    for i in relation[a]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[a] = False


for i in range(N):
    dfs(i, 0)
print(0)

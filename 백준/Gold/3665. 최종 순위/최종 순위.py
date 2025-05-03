import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    pre_ranking = list(map(int, input().split()))

    m = int(input())
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n):
            graph[pre_ranking[i]][pre_ranking[j]] = True
            indegree[pre_ranking[j]] += 1

    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            indegree[b] -= 1
            indegree[a] += 1
            graph[b][a] = True
        elif graph[b][a]:
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
            graph[a][b] = True

    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    cycle = False
    many = False
    result = []
    for _ in range(n):
        if len(queue) == 0:
            cycle = True
            break
        elif len(queue) > 1:
            many = True
            break
        x = queue.popleft()
        result.append(x)
        for i in range(1, n + 1):
            if graph[x][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
    if cycle:
        print("IMPOSSIBLE")
    elif many:
        print("?")
    else:
        print(*result)

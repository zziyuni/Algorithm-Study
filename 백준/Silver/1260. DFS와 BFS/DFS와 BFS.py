from collections import deque

N, M, V = map(int, input().split())
route = [[] for _ in range(N + 1)]


def dfs(s):
    visited = [False] * (N + 1)
    ans = []
    stack = [s]
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            ans.append(cur)
            visited[cur] = True
            for x in reversed(route[cur]):
                stack.append(x)
    return ans


def bfs(s):
    visited = [False] * (N + 1)
    queue = deque([s])
    ans = []
    visited[s] = True
    while queue:
        cur = queue.popleft()
        ans.append(cur)
        for x in route[cur]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)
    return ans


for _ in range(M):
    a, b = map(int, input().split())
    route[a].append(b)
    route[b].append(a)
for r in route:
    r.sort()

print(*dfs(V))
print(*bfs(V))

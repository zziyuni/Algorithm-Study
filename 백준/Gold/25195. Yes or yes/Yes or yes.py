import sys

input = sys.stdin.readline

n, m = map(int, input().split())

path = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    path[x].append(y)

s = int(input())

exist = list(map(int, input().split()))
visited = [False] * (n + 1)

for e in exist:
    visited[e] = True


def dfs(start):
    stack = []
    if visited[start]:
        return False
    stack.append(start)
    visited[start] = True
    while len(stack) != 0:
        cur = stack.pop()
        if len(path[cur]) == 0:
            return True
        for node in path[cur]:
            if not visited[node]:
                visited[node] = True
                stack.append(node)

    return False


if dfs(1):
    print("yes")
else:
    print("Yes")

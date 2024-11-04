import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
island = [None] * (N + 1)
route = [[] for _ in range(N + 1)]

for i in range(N - 1):
    t, a, p = input().split()
    island[i + 2] = [t, int(a)]
    route[int(p)].append(i + 2)


def dfs(node):
    ans = 0
    for child in route[node]:
        ans += dfs(child)
    if island[node] is not None:
        t, a = island[node]
        if t == 'W':
            ans = max(0, ans - a)
        else:
            ans += a
    return ans


print(dfs(1))

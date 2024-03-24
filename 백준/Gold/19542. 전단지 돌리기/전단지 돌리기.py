import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, s, d = map(int, input().split())

path = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    path[x].append(y)
    path[y].append(x)

ans = 0


def dfs(start, p,):
    global ans
    dst = 0
    for i in path[start]:
        if i != p:
            dst = max(dst, dfs(i, start))
    if dst+1 > d:
        ans += 1
    return dst + 1


dfs(s, 0)

print(max(0,2*(ans-1)))

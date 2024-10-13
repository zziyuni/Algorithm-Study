import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

parent = [-1] * N
parent[0] = 0


def bfs(n):
    for i in tree[n]:
        if parent[i] == -1:
            parent[i] = n + 1
            bfs(i)


bfs(0)

for i in range(1,N):
    print(parent[i])

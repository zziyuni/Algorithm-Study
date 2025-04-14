import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
parent = [0] * V
for i in range(V):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append([c, a - 1, b - 1])
graph.sort()

answer = 0
for i in range(E):
    cost, a, b = graph[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(a, b)
        answer += cost
print(answer)

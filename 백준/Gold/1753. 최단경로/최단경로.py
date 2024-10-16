import sys
import heapq

input = sys.stdin.readline

INF = 10e9
V, E = map(int, input().split())
K = int(input()) - 1

graph = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))

distance = [INF] * V


def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    while h:
        length, cur = heapq.heappop(h)
        if distance[cur] < length:
            continue
        for i in graph[cur]:
            if length + i[1] < distance[i[0]]:
                distance[i[0]] = length + i[1]
                heapq.heappush(h, (distance[i[0]], i[0]))


dijkstra(K)

for d in distance:
    if d == INF:
        print('INF')
    else:
        print(d)

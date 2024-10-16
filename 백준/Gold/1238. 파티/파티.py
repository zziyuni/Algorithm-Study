import heapq
import sys

input = sys.stdin.readline
INF = 10e9

N, M, X = map(int, input().split())

road = [[] for _ in range(N)]
reverse_road = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    road[a - 1].append((b - 1, t))
    reverse_road[b - 1].append((a - 1, t))

to_X = [INF] * N
to_home = [INF * N]


def dijkstra(start, roads):
    time = [INF] * N
    time[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    while h:
        cur_t, cur = heapq.heappop(h)
        if time[cur] < cur_t:
            continue
        for r in roads[cur]:
            if time[r[0]] > cur_t + r[1]:
                time[r[0]] = cur_t + r[1]
                heapq.heappush(h, (time[r[0]], r[0]))
    return time


to_X = dijkstra(X - 1, road)
to_home = dijkstra(X - 1, reverse_road)

ans = -1
for i in range(N):
    ans = max(ans, to_X[i] + to_home[i])
print(ans)

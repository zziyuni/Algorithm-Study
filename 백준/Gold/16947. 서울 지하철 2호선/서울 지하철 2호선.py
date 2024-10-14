import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N = int(input())
station = [[] for _ in range(N)]

for _ in range(N):
    a, b = map(int, input().split())
    station[a - 1].append(b - 1)
    station[b - 1].append(a - 1)

distance = [-1] * N
is_cycle = [False] * N


def cycle_check(start, cur, cnt):
    visited[cur] = True
    for j in station[cur]:
        if not visited[j]:
            if cycle_check(start, j, cnt + 1):
                return True
        elif start == j and cnt >= 2:
            return True
    return False


def calc_distance():
    queue = deque()
    for i in range(N):
        if is_cycle[i]:
            distance[i] = 0
            queue.append(i)
    while queue:
        node = queue.popleft()
        for s in station[node]:
            if distance[s] == -1:
                queue.append(s)
                distance[s] = distance[node] + 1


for i in range(N):
    visited = [False] * N
    is_cycle[i] = cycle_check(i, i, 0)

calc_distance()

print(*distance)

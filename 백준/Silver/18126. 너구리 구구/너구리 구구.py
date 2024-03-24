import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())

distance = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    distance[a][b] = c
    distance[b][a] = c
dist = [0 for i in range(n + 1)]


def get_distance(s):
    for i in range(n + 1):
        if distance[s][i] != 0:
            dist[i] = dist[s] + distance[s][i]
            distance[s][i] = 0
            distance[i][s] = 0
            get_distance(i)


get_distance(1)

print(max(dist))

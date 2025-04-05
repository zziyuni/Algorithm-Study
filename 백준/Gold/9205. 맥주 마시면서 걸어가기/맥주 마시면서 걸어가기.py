import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9


def calc_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def go_festival(h, s, f):
    max_distance = 50 * 20
    if calc_distance(h[0], h[1], f[0], f[1]) <= max_distance:
        return True
    queue = deque([h])
    visited = [False] * (len(s))
    while queue:
        cur = queue.popleft()
        if calc_distance(cur[0], cur[1], f[0], f[1]) <= max_distance:
            return True
        for i in range(len(s)):
            if not visited[i] and calc_distance(cur[0], cur[1], s[i][0], s[i][1]) <= max_distance:
                visited[i] = True
                queue.append(s[i])

    return False


t = int(input())

for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = list(list(map(int, input().split())) for _ in range(n))
    festival = list(map(int, input().split()))
    if go_festival(home, store, festival):
        print('happy')
    else:
        print('sad')

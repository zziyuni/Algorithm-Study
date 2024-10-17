import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

order = [[] for _ in range(N)]
pre_cnt = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    order[a - 1].append(b - 1)
    pre_cnt[b - 1] += 1


def topology_sort():
    result = []
    queue = deque()
    for i in range(N):
        if pre_cnt[i] == 0:
            queue.append(i)
    while queue:
        cur = queue.popleft()
        result.append(cur + 1)
        for i in order[cur]:
            pre_cnt[i] -= 1
            if pre_cnt[i] == 0:
                queue.append(i)
    print(*result)


topology_sort()

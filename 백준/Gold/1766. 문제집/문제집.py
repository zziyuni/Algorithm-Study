import sys
import heapq

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
    pre = []
    for i in range(N):
        if pre_cnt[i] == 0:
            heapq.heappush(pre, i)
    while pre:
        cur = heapq.heappop(pre)
        result.append(cur + 1)
        for i in order[cur]:
            pre_cnt[i] -= 1
            if pre_cnt[i] == 0:
                heapq.heappush(pre, i)
    print(*result)


topology_sort()

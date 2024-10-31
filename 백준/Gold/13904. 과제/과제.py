import sys
import heapq

input = sys.stdin.readline

N = int(input())
homework = [[] for _ in range(1001)]
max_day = 0
for _ in range(N):
    d, w = map(int, input().split())
    homework[d].append(w)
    max_day = max(max_day, d)

ans = 0
pq = []
for i in range(max_day, 0, -1):
    for score in homework[i]:
        heapq.heappush(pq, -score)
    if len(pq) == 0:
        continue
    ans += -heapq.heappop(pq)

print(ans)
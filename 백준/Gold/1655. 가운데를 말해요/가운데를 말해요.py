import sys
import heapq

input = sys.stdin.readline

N = int(input())
ans = []
max_hq = []
min_hq = []

for _ in range(N):

    i = int(input())
    if len(max_hq) == 0:
        heapq.heappush(max_hq, -i)
    elif len(min_hq) == 0:
        v = -heapq.heappop(max_hq)
        if i > v:
            heapq.heappush(max_hq, -v)
            heapq.heappush(min_hq, i)
        else:
            heapq.heappush(max_hq, -i)
            heapq.heappush(min_hq, v)
    else:
        if -max_hq[0] < i:
            heapq.heappush(min_hq, i)
        else:
            heapq.heappush(max_hq, -i)
        if len(max_hq) < len(min_hq):
            heapq.heappush(max_hq, -heapq.heappop(min_hq))
        elif len(max_hq) > len(min_hq) + 1:
            heapq.heappush(min_hq, -heapq.heappop(max_hq))

    ans.append(-max_hq[0])

for i in ans:
    print(i)

import sys
import heapq

input = sys.stdin.readline

N = int(input())

classes = []
for _ in range(N):
    S, T = map(int, input().split())
    classes.append((S, T))

classes.sort(key=lambda x: (x[0], x[1]))

ends = []
for s, t in classes:
    if ends:
        earliest = heapq.heappop(ends)
        if s < earliest:
            heapq.heappush(ends, earliest)
    heapq.heappush(ends, t)

print(len(ends))

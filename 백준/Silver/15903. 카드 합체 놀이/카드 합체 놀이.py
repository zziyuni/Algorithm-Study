import sys
from queue import PriorityQueue

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
pq = PriorityQueue()
for a in nums:
    pq.put(a)

for _ in range(m):
    a = pq.get()
    b = pq.get()
    min_sum = a+b
    pq.put(min_sum)
    pq.put(min_sum)


ans = 0
while pq.qsize() != 0:
    ans += pq.get()


print(ans)
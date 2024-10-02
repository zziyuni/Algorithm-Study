import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for i in range(n):
    p = int(input())
    pq.put(p)

ans = 0
cnt = 1
while True:
    if cnt == n:
        break
    first_val = pq.get()
    second_val = pq.get()
    ans += (first_val + second_val)
    cnt += 1
    pq.put(first_val + second_val)

print(ans)

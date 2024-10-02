import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())

pq = PriorityQueue()
for i in range(n):
    vote = int(input())
    if i == 0:
        dasom = vote
    else:
        pq.put(-vote)
ans = 0
while True:
    if pq.empty():
        break
    max_val = -pq.get()
    if max_val < dasom:
        break
    dasom += 1
    max_val -= 1
    ans += 1
    pq.put(-max_val)

print(ans)

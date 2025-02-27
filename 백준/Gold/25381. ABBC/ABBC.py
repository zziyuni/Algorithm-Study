from collections import deque
import sys

input = sys.stdin.readline
S = input().strip()

n = len(S)
ans = 0
A_indices = [i for i in range(n) if S[i] == 'A']
B_indices = deque(i for i in range(n) if S[i] == 'B')
C_indices = [i for i in range(n) if S[i] == 'C']

A_indices.sort(reverse=True)

for a in A_indices:
    if len(B_indices) != 0 and a < B_indices[-1]:
        ans += 1
        B_indices.pop()
for c in C_indices:
    if len(B_indices) != 0 and c > B_indices[0]:
        ans += 1
        B_indices.popleft()

print(ans)

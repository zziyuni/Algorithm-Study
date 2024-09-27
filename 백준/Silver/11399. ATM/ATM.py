import sys

input = sys.stdin.readline
n = int(input())
time = list(map(int, input().split()))
time.sort()
ans = 0
t = 0
for i in range(n):
    t += time[i]
    ans += t

print(ans)

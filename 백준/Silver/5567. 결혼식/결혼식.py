import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

friends = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)

invited = [0] * n
invited[0] = 1
for i in friends[0]:
    invited[i] = 1

for i in range(n):
    if invited[i] == 1:
        for j in friends[i]:
            if invited[j] == 0:
                invited[j] = 2

print(invited.count(1)-1+invited.count(2))

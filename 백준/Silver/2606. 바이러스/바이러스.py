import sys

input = sys.stdin.readline

n = int(input())
n_pair = int(input())
pairs = [[] for _ in range(n)]
for _ in range(n_pair):
    a, b = map(int, input().split())
    pairs[a - 1].append(b - 1)
    pairs[b - 1].append(a - 1)

virus = [0] * n
virus[0] = 1
while True:
    flag = False
    for i in range(n):
        if virus[i] == 0:
            continue
        for j in pairs[i]:
            if virus[j] == 0:
                virus[j] = 1
                flag = True
    if not flag:
        break

print(virus.count(1)-1)

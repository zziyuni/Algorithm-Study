import sys

input = sys.stdin.readline

N = int(input())
T = int(input())
recommend = list(map(int, input().split()))
rank = []

for r in recommend:
    index = -1
    for i in range(len(rank)):
        if rank[i][0] == r:
            index = i
    if index == -1:
        if len(rank) >= N:
            tmp_rank = rank[:]
            tmp_rank.sort(key=lambda x: x[1])
            rank.remove(tmp_rank[0])
        rank.append([r, 1])
    else:
        rank[index][1] += 1

rank.sort()
for r in rank:
    print(r[0], end=' ')

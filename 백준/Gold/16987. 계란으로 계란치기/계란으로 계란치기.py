import sys

input = sys.stdin.readline

n = int(input())
egg = list(list(map(int, input().split())) for _ in range(n))
ans = 0


def egg_break(pos, cnt):
    global ans
    global egg
    if pos == n:
        ans = max(ans, cnt)
        return
    if egg[pos][0] <= 0 or cnt == n-1:
        egg_break(pos + 1, cnt)
        return
    tmp = cnt
    for i in range(0, n):
        if i == pos:
            continue
        if egg[i][0] > 0:
            egg[i][0] -= egg[pos][1]
            egg[pos][0] -= egg[i][1]
            if egg[i][0] <= 0:
                cnt += 1
            if egg[pos][0] <= 0:
                cnt += 1
            egg_break(pos+1, cnt)
            egg[i][0] += egg[pos][1]
            egg[pos][0] += egg[i][1]

            cnt = tmp


egg_break(0, 0)

print(ans)

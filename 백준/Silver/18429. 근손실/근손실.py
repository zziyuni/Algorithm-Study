import sys

input = sys.stdin.readline

n, k = map(int, input().split())
weight = list(map(int, input().split()))
isUsed = [False] * n
ans = 0


def exercise(w, j):
    global ans
    if w < 500:
        return
    if j == n:
        if w >= 500:
            ans += 1
        return
    for i in range(n):
        if not isUsed[i]:
            isUsed[i] = True
            exercise(w - k + weight[i], j + 1)
            isUsed[i] = False


exercise(500, 0)
print(ans)

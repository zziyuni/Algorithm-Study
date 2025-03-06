import sys

input = sys.stdin.readline

N = int(input())
route = list(list(map(int, input().split())) for _ in range(N))
check = [[False for _ in range(N)] for _ in range(N)]
ans = 0

for i in range(N):
    check[i][i] = True
for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if k == i or k == j:
                continue
            if route[i][j] > route[i][k] + route[k][j]:
                print(-1)
                sys.exit()
            if route[i][j] == route[i][k] + route[k][j]:
                check[i][j] = True
                check[j][i] = True

for i in range(N):
    for j in range(i + 1, N):
        if not check[i][j]:
            ans += route[i][j]

print(ans)

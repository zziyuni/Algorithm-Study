import sys

input =sys.stdin.readline

N, K = map(int,input().split())
items = [list(map(int, input().split())) for _ in range(N)]

values = [[0] * (K+1) for _ in range(N+1)]


for i in range(1,N+1):
    weight = items[i-1][0]
    value = items[i-1][1]
    for j in range(1,K+1):
        if weight > j:
            values[i][j] = values[i-1][j]
        else:
            values[i][j] = max(values[i-1][j-weight] + value, values[i-1][j])


print(values[N][K])
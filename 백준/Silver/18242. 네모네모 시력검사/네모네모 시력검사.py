import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = list(list(input().strip()) for _ in range(N))

ans = 'DOWN'
start = M
for i in range(N):
    cnt = grid[i].count('#')
    if cnt != 0 and start == M:
        start = grid[i].index('#')
        if ''.join(grid[i]).count('#.#') > 0:
            ans = 'UP'
            break
    if cnt == 1:
        if grid[i].index('#') == start:
            ans = 'RIGHT'
            break
        else:
            ans = 'LEFT'
            break

print(ans)
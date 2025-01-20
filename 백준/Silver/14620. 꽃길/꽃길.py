import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N = int(input())
price = list(list(map(int, input().split())) for _ in range(N))

visited = [[False] * N for _ in range(N)]
ans = 1e9


def is_valid(x, y):
    if visited[x][y]:
        return False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
            return False
    return True


def backtracking(cnt, cost):
    global ans
    if cnt == 3:
        ans = min(ans, cost)
        return
    for x in range(N):
        for y in range(N):
            if visited[x][y]:
                continue
            if is_valid(x, y):
                visited[x][y] = True
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    visited[nx][ny] = True
                new_cost = price[x][y]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    new_cost += price[nx][ny]
                backtracking(cnt + 1, cost + new_cost)
                visited[x][y] = False
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    visited[nx][ny] = False


backtracking(0, 0)
print(ans)
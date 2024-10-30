from collections import deque

N, K = map(int, input().split())
INF = 10e9
time = [INF] * 200000

time[N] = 0
queue = deque([N])
visited = [False] * 200000
visited[N] = True
while queue:
    if N >= K:
        time[K] = N - K
        break
    cur = queue.pop()
    if cur == K:
        break
    if 2 * cur < 200000 and not visited[2 * cur]:
        time[2 * cur] = time[cur]
        queue.appendleft(cur * 2)
        visited[2 * cur] = True
    if cur - 1 >= 0 and not visited[cur - 1]:
        time[cur - 1] = time[cur] + 1
        queue.appendleft(cur - 1)
        visited[cur - 1] = True
    if cur + 1 < 200000 and not visited[cur + 1]:
        time[cur + 1] = time[cur] + 1
        queue.appendleft(cur + 1)
        visited[cur + 1] = True

print(time[K])

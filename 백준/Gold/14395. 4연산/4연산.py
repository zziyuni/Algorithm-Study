from collections import deque

s, t = map(int, input().split())


def find_method(n):
    queue = deque([[n, []]])
    visited = set([])
    while queue:
        cur, path = queue.popleft()
        if cur == t:
            return path
        if cur * cur not in visited and cur * cur <= t:
            queue.append([cur * cur, path + ['*']])
            visited.add(cur * cur)
        if cur + cur not in visited and cur + cur <= t:
            queue.append([cur + cur, path + ['+']])
            visited.add(cur + cur)
        if 0 not in visited:
            queue.append([0, path + ['-']])
            visited.add(0)
        if 1 not in visited:
            queue.append([1, path + ['/']])
            visited.add(1)
    return -1


ans = find_method(s)
if ans == -1:
    print(-1)
elif len(ans) == 0:
    print(0)
else:
    print(''.join(ans))

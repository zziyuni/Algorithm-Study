import sys

input = sys.stdin.readline

N, L = map(int, input().split())

info = list(list(map(int, input().split())) for _ in range(N))


def find_route(line, direction):
    used = [False] * N
    j = 1
    while j < N:
        pre = get_value(line, j - 1, direction)
        cur = get_value(line, j, direction)
        if pre - cur > 1:
            return False
        elif pre - 1 == cur:
            if j + L > N:
                return False
            for i in range(j, j + L):
                if used[i] or get_value(line, i, direction) != cur:
                    return False
            for i in range(j, j + L):
                used[i] = True
            j += L
        elif pre == cur:
            j += 1
        elif pre + 1 == cur:
            if j < L:
                return False
            else:
                for i in range(j - L, j):
                    if used[i] or get_value(line, i, direction) != pre:
                        return False
                for i in range(j - L, j):
                    used[i] = True
                j += 1
        else:
            return False

    return True


def get_value(i, j, dir):
    return info[i][j] if dir == 0 else info[j][i]


ans = 0
for i in range(N):
    if find_route(i, 0):
        ans += 1
    if find_route(i, 1):
        ans += 1

print(ans)

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(node, cur_m):
    visited[node] = True
    types, money, rooms = room_info[node]
    if types == 'L' and cur_m < money:
        cur_m = money
    elif types == 'T':
        cur_m -= money
        if cur_m < 0:
            return False
    if node == N - 1:
        return True
    for r in rooms:
        if not visited[r - 1]:
            if dfs(r - 1, cur_m):
                return True
            visited[r-1] = False
    return False


while True:
    N = int(input())
    if N == 0:
        break
    room_info = []
    for i in range(N):
        cur_money = 0
        info = list(input().split())
        t = info[0]
        m = int(info[1])
        r = list(map(int, info[2:-1]))
        room_info.append((t, m, r))
    visited = [False] * N
    if dfs(0, cur_money):
        print('Yes')
    else:
        print('No')

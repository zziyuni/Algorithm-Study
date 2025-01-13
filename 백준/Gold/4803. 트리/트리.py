import sys

input = sys.stdin.readline


def find_tree(x, e):
    global visited

    visited[x] = True
    stack = [(x, -1)]
    node_cnt = 0
    edge_cnt = 0
    while stack:
        cur, parent = stack.pop()
        node_cnt += 1
        for i in e[cur]:
            edge_cnt += 1
            if not visited[i]:
                stack.append((i, cur))
                visited[i] = True
            else:
                if parent != i:
                    return False
    if node_cnt - 1 != edge_cnt // 2:
        return False
    return True


case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    edge = [[] for _ in range(n + 1)]
    ans = 0
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    for i in range(1, n + 1):
        if not visited[i] and find_tree(i, edge):
            ans += 1
    print(f"Case {case}: ", end="")
    if n == 0 or ans == 0:
        print('No trees.')
    elif ans > 1:
        print('A forest of', ans, 'trees.')
    elif ans == 1:
        print('There is one tree.')
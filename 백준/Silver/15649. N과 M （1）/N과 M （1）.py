def backtracking(n, pos, arr):
    if pos == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            backtracking(n, pos + 1, arr)
            arr.pop()


n, m = map(int, input().split())

backtracking(n, 0, [])

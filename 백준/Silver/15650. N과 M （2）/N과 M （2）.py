def backtracking(arr):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(arr[-1] if arr else 1, n + 1):
        if i not in arr:
            arr.append(i)
            backtracking(arr)
            arr.pop()


n, m = map(int, input().split())
backtracking([])

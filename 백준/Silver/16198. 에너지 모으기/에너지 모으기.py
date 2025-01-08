import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
weights = list(map(int, input().split()))


def backtracking(arr, w):
    ans = 0
    if len(arr) == 2:
        return w
    for i in range(1, len(arr) - 1):
        removed = arr[:i] + arr[i + 1:]
        ans = max(ans, backtracking(removed, w + arr[i - 1] * arr[i + 1]))
    return ans


print(backtracking(weights, 0))

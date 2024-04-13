import sys

input = sys.stdin.readline
n, k = map(int, input().split())

ml = []
for _ in range(n):
    m = int(input())
    ml.append(m)


def binary_search(start, end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for mak in ml:
            cnt += mak // mid
        if cnt < k:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    return res


ans = binary_search(1, max(ml))

print(ans)

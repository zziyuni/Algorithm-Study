import sys

input = sys.stdin.readline

t = int(input())


def find_pair(target):
    start = 0
    end = len(b) - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if b[mid] == target:
            end = mid - 1
        elif b[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            res = mid
    return res + 1


while True:
    if t == 0:
        break
    ans = 0
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    for c in a:
        pos = find_pair(c)
        ans += pos
    print(ans)
    t -= 1

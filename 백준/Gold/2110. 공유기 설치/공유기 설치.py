import sys

input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

left = 1
right = house[-1] - house[0]
ans = 0
while left <= right:
    mid = (left + right) // 2
    cur = 0
    installed = 1
    for i in range(n):
        if house[cur] + mid <= house[i]:
            installed += 1
            cur = i
    if installed >= c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1


print(ans)

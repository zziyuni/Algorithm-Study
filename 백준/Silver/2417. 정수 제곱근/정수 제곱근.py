n = int(input())

start = 1
end = n
ans = 0
while start <= end:
    mid = (start + end) // 2
    if mid * mid >= n:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1


print(ans)
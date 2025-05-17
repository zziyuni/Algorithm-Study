def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    while left <=right:
        mid = (left+right) // 2 
        cnt = 0
        for t in times:
            cnt += mid//t
        if cnt >= n:
            answer = mid
            right = mid-1
        else:
            left = mid + 1
    return answer
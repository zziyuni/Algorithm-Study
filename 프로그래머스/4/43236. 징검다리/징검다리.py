def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.sort()
    rocks.append(distance)
    while left<= right:
        mid = (left+right) // 2
        cnt = 0
        pre = 0
        for i in range(len(rocks)):
            if rocks[i] - pre < mid:
                cnt += 1
            else:
                pre = rocks[i]
        if cnt <= n:
            answer = mid
            left = mid + 1
            
        else:
            right = mid - 1
                    
            
            
    return answer
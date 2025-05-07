def solution(diffs, times, limit):
    answer = 0
    left = min(diffs)
    right = max(diffs)
    def calc_time(level):
        time = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                time += times[i]
            else:
                if i == 0:
                    time += (diffs[i] - level) * (times[i])
                else:
                    time += (diffs[i] - level) * (times[i] + times[i-1])
                time +=times[i]
        return time   
                
        
    while left<=right:
        mid = (left+right) // 2
        if calc_time(mid) <= limit:
            right = mid-1
            answer = mid
        else:
            left = mid+1

    return answer
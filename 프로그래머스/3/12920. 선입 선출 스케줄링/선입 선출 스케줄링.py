def solution(n, cores):
    answer = 0
    
    if n <= len(cores):
        return n
    left = 0
    right = max(cores) * n
    time = 0
    while left<=right:
        mid = (left+right) //2
        cnt = len(cores)
        for c in cores:
            cnt += mid//c
        if cnt >= n:
            time = mid
            right = mid-1
        else:
            left = mid+1
    processed = len(cores)  
    for c in cores:
        processed += (time - 1) // c
    remain = n - processed

    for idx, c in enumerate(cores):
        if time % c == 0:
            remain -= 1
            if remain == 0:
                return idx + 1 

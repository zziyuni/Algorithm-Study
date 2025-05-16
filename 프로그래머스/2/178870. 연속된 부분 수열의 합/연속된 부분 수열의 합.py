def solution(sequence, k):
    answer = []
    left = 0
    right =0
    total = sequence[0]
    while left<=right and right < len(sequence):
        if total < k:
            right +=1
            if right == len(sequence):
                break
            total += sequence[right]
        elif total > k:
            total -= sequence[left]
            left += 1
        else:
            if len(answer) == 0 or answer[1] - answer[0] > right - left:
                answer = [left,right]
            total -= sequence[left]
            left += 1
        
    
    return answer
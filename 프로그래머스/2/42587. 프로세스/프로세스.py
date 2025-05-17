from collections import deque

def solution(priorities, location):
    answer = 0
    order = [[idx,val]for idx,val in enumerate(priorities)]
    
    p_queue = deque(order)
    priorities.sort(reverse = True)
    max_idx = 0

    while p_queue:
        idx,cur = p_queue.popleft()
        if priorities[max_idx] > cur:
            p_queue.append([idx,cur])
        else:
            answer += 1
            if idx == location:
                break
            max_idx +=1

        
    return answer
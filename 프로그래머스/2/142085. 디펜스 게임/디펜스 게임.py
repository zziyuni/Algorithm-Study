import heapq
def solution(n, k, enemy):
    answer = 0
    stages = []
    for i in range(len(enemy)):
        heapq.heappush(stages,-enemy[i])
        n -= enemy[i]
        if n < 0:
            if k == 0:
                break
            skill = heapq.heappop(stages)
            n += -skill 
            k-=1
        answer = i+1
    
    return answer
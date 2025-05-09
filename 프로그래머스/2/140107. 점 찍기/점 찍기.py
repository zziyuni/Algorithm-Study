import math
def solution(k, d):
    answer = 0
    
    for i in range(d+1):
        if d**2 - (i*k)**2 <0:
            break
        answer +=1
        answer += math.floor((d**2 - (i*k)**2) ** (1/2) // k)
        
    return answer
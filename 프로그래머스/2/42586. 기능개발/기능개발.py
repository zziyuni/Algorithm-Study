import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    funcs = deque([])
    for i in range(len(progresses)):
        funcs.append(math.ceil((100-progresses[i]) / speeds[i]))
    pre = funcs.popleft()
    print(funcs)
    cnt = 1
    while funcs:
        cur = funcs.popleft()
        if cur <= pre:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            pre = cur
    answer.append(cnt)
        
    return answer
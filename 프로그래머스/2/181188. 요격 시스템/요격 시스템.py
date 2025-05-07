def solution(targets):
    answer = 1
    targets.sort(key = lambda x:(x[1]))
    pre = targets[0][1] - 0.5
    for i in range(1,len(targets)):
        if pre < targets[i][0]:
            answer+=1
            pre = targets[i][1] - 0.5
        else:
            pre = min(targets[i][1]-0.5,pre)
        
    return answer
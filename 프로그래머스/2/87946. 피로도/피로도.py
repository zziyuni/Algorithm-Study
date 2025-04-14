def backtracking(cur, visited,dungeons):
    global answer
    updated = False
    for i in range(len(dungeons)):
        min_fatigue, use_fatigue = dungeons[i]
        if cur >= min_fatigue and i not in visited :
            updated = True
            backtracking(cur-use_fatigue,visited|{i},dungeons)
    if not updated:
        answer = max(answer,len(visited))
        
answer = -1    
def solution(k, dungeons):
    global answer
    answer = -1
    backtracking(k,set(),dungeons)
    return answer
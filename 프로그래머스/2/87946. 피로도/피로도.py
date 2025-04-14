from itertools import permutations

def solution(k, dungeons):
    answer = -1
    pairs = permutations(dungeons,len(dungeons))
    for p in pairs:
        cnt = 0
        cur = k
        for f in p:
            min_fatigue, use_fatigue = f
            if cur < min_fatigue:
                continue
            else:
                cur -= use_fatigue
                cnt += 1
        answer = max(answer,cnt)
    
    return answer
def solution(clothes):
    answer = 1
    clothes_hash = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_hash:
            clothes_hash[clothes[i][1]].append(clothes[i][0])
        else:
            clothes_hash[clothes[i][1]] = [clothes[i][0]]
    
    for key in clothes_hash:
        answer *= (len(clothes_hash[key]) +1)
    answer -=1
    return answer
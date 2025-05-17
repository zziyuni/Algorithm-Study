def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    for i in range(len(answers)):
        if one[i%5] == answers[i]:
            cnt_1 +=1
        if two[i%8] == answers[i]:
            cnt_2 +=1
        if three[i%10] == answers[i]:
            cnt_3 += 1
    if cnt_1 > cnt_2:
        if cnt_1 > cnt_3:
            answer.append(1)
        elif cnt_1 < cnt_3:
            answer.append(3)
        else:
            answer= [1,3]
    elif cnt_1 <cnt_2:
        if cnt_2 > cnt_3:
            answer.append(2)
        elif cnt_2 < cnt_3:
            answer.append(3)
        else:
            answer= [2,3]
    else:
        if cnt_1 == cnt_3:
            answer = [1,2,3]
        else:
            answer =[1,2]
            
        
            
        
    return answer
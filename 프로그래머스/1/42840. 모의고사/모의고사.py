def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    cnts = [0,0,0]
    for i in range(len(answers)):
        if one[i%5] == answers[i]:
            cnts[0] +=1
        if two[i%8] == answers[i]:
            cnts[1] +=1
        if three[i%10] == answers[i]:
            cnts[2] += 1
    max_score = max(cnts)
    for i in range(3):
        if cnts[i] == max_score:
            answer.append(i+1)
            
        
            
        
    return answer
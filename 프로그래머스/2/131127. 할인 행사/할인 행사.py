def solution(want, number, discount):
    answer = 0
    needs = []
    for i in range(len(want)):
        needs.append((want[i],number[i]))
    
    for i in range(len(discount)-9):
        discount_dict = dict()
        for j in range(i,i+10):
            if discount[j] not in discount_dict:
                discount_dict[discount[j]] = 1
            else:
                discount_dict[discount[j]] += 1
        flag = False
        for j in range(len(needs)):
            name,cnt = needs[j]
            if name not in discount_dict:
                flag = True
                break
            if discount_dict[name] >= cnt:
                continue
            else:
                flag =True
                break
        if not flag:
            answer +=1
    return answer
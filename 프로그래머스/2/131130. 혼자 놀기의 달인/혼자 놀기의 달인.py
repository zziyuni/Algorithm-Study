def solution(cards):
    answer = 0
    
    
    def back(c,cnt,opened,cnts):
        if opened[cards[c-1]]:
            cnts.append(cnt)
            return
        opened[cards[c-1]] = True
        back(cards[c-1],cnt + 1,opened,cnts)
        
    for i in range(len(cards)):
        opened = [False] * (len(cards) + 1)
        cnts = []
        opened[cards[i]] = True
        back(cards[i],1,opened,cnts)
        for j in range(len(cards)):
            if opened[cards[j]]:
                continue
            opened[cards[j]] = True
            back(cards[j],1,opened,cnts)
        cnts.sort()
        if len(cnts) == 1:
            answer = max(0,answer)
        else:
            answer = max(cnts[-1]*cnts[-2],answer)
            

    return answer
import math

def solution(picks, minerals):
    answer = 0
    f = [[1,1,1],[5,1,1],[25,5,1]] #다이아,철,돌
    count =[]
    for i in range(0,len(minerals),5):
        dia = 0
        iron = 0
        stone = 0
        for j in range(i,min(i+5, len(minerals))):
            if minerals[j] == "diamond":
                dia +=1
            if minerals[j] == "iron":
                iron+=1
            if minerals[j] == "stone":
                stone+=1
        count.append([dia,iron,stone])
    count = count[:sum(picks)]
    count.sort( key = lambda x:(-x[0],-x[1],-x[2]))
    for c in count:
        for i in range(3):
            if picks[i] == 0:
                continue
            picks[i] -=1
            for j in range(3):
                answer += f[i][j] * c[j]
            break

    
    return answer
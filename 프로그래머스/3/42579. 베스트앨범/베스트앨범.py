def solution(genres, plays):
    answer = []
    song = {}
    count = []
    for i in range(len(genres)):
        if genres[i] in song:
            song[genres[i]].append((i,plays[i]))
        else:
            song[genres[i]] = [(i,plays[i])]
    for key in song:
        song[key].sort(key = lambda x:(-x[1],x[0]))
        count.append(song[key])
    print(count)
    count.sort(key = lambda x:-sum(k[1] for k in x))
    for c in count:
        for i in range(min(2,len(c))):
            answer.append(c[i][0])
    
    return answer
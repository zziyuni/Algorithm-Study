def solution(n, words):
    answer = [0,0]
    history = set()
    
    for i in range(len(words)):

        if words[i] in history or (i != 0 and words[i][0] != words[i-1][-1]) or len(words[i]) == 0:
            answer = [i%n + 1 ,(i//n)+1]
            break
        history.add(words[i])
            

    return answer
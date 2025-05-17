def solution(begin, target, words):
    answer = 0
    stack = [(begin,0)]
    used = set()
    len_word = len(begin)
    while stack:
        cur,cnt = stack.pop()
        used.add(cur)
        if cur == target:
            answer = cnt
            break
        for w in words:
            if w not in used:
                diff_count = 0
                for j in range(len_word):
                    if cur[j] != w[j]:
                        diff_count += 1
                    if diff_count >1:
                        break
                if diff_count == 1:
                    
                    stack.append((w,cnt+1))
                
        
    return answer
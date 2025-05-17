def solution(numbers, hand):
    answer = ''
    left = set([1,4,7])
    right = set([3,6,9])
    l_pos = 10
    r_pos = 12
    for n in numbers:
        if n == 0:
            n = 11
        if n in left:
            answer+='L'
            l_pos = n
        elif n in right:
            answer+='R'
            r_pos = n
        else:
            r_step = abs(n-r_pos)//3 + abs(n-r_pos)%3
            l_step = abs(n-l_pos)//3 + abs(n-l_pos)%3
            if l_step < r_step:
                l_pos = n
                answer+='L'
            elif l_step > r_step:
                r_pos = n
                answer+='R'
                
            else:
                if hand == 'right':
                    r_pos = n
                    answer+='R'
                else:
                    l_pos = n
                    answer+='L'
                    
                    
            
        
    return answer
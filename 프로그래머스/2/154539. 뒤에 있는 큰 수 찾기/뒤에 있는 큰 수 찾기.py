def solution(numbers):
    stack = []
        
    answer = [-1] * len(numbers)
    for i in range(len(numbers)-1,-1,-1):
        while stack and numbers[stack[-1]] <= numbers[i]:
            stack.pop()
        if stack:
            answer[i] = numbers[stack[-1]]
        stack.append(i)
        
    return answer
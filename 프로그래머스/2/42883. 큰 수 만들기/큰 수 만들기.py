def solution(number, k):
    stack = [number[0]]
    for i in range(1,len(number)):
        while stack and k >0 and number[i] > stack[-1]:
            stack.pop()
            k-=1
        stack.append(number[i])
    if k > 0:
        stack = stack[:-k]
            
    return ''.join(stack)
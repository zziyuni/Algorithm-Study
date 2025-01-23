s = list(input().strip())

s.reverse()

stack = []

while s:
    cur = s.pop()
    stack.append(cur)
    if len(stack) >= 4 and ''.join(stack[-4:]) == 'PPAP':
        for _ in range(3):
            stack.pop()

if ''.join(stack) == 'P':
    print('PPAP')
else:
    print('NP')
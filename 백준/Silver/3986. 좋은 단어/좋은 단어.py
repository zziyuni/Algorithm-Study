import sys

input = sys.stdin.readline

N = int(input())
words = list(input().strip() for _ in range(N))

ans = 0

for w in words:
    stack = []
    for i in w:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        ans += 1

print(ans)

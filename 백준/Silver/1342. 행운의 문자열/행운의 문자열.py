import sys
import math

input = sys.stdin.readline


def find_lucky(n, a):
    global ans
    if n == length:
        ans += 1
        return
    for i in range(0, length):
        if not isUsed[i] and a != characters[i]:
            isUsed[i] = True

            find_lucky(n + 1, characters[i])
            isUsed[i] = False


characters = list(input().strip())
length = len(characters)
isUsed = [False] * length

count = {}
for i in characters:
    try:
        count[i] += 1
    except:
        count[i] = 1
values = list(count.values())
result = math.prod(math.factorial(val) for val in values)

ans = 0
find_lucky(0, ' ')
print(ans // result)

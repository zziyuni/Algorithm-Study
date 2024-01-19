import math
S = input().strip()

ans = 0

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        ans += 1


print(min(math.ceil(ans / 2), len(S) - math.ceil(ans / 2)))

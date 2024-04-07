import sys
import math

input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))

crane = sorted(crane, reverse=True)

m = int(input())
box = list(map(int, input().split()))

box = sorted(box, reverse=True)

if crane[0] < box[0]:
    print(-1)
    exit()

ans = 0
while len(box) != 0:
    for i in range(len(crane)):
        for j in range(len(box)):
            if crane[i] >= box[j]:
                del box[j]
                break
    ans += 1

print(ans)

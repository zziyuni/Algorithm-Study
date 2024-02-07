import sys

input = sys.stdin.readline

n = int(input())
tips = []
for _ in range(n):
    tip = int(input())
    tips.append(tip)

tips = sorted(tips, reverse=True)

for i in range(n):
    tips[i] -= i if tips[i] - i > 0 else tips[i]

print(sum(tips))

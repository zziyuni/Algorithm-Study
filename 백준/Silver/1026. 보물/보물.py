import sys

input = sys.stdin.readline
n = int(input());
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b = sorted(b)
a = sorted(a, reverse=True)

sum = 0
for i in range(n):
    sum += (a[i] * b[i])

print(sum)

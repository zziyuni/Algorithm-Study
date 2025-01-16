N = int(input())

even = 0
five = 0
for i in range(1, N + 1):
    n = i
    while n % 2 == 0:
        n //= 2
        even += 1
    while n % 5 == 0:
        n //= 5
        five += 1

print(min(five, even))
import sys

input = sys.stdin.readline


def is_lucky(n):
    while n:
        digit = n % 10
        if digit != 5 and digit != 8:
            return False
        n //= 10
    return True


def check_lucky(a, b, c):
    ab_sums = {i + j for i in a for j in b}
    lucky_numbers = {s + k for s in ab_sums for k in c if is_lucky(s + k)}
    return len(lucky_numbers)


t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    k = int(input())
    C = list(map(int, input().split()))
    print(check_lucky(A, B, C))

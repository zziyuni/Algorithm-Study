import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())


def factorial_mod(n, m):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % m
    return result


if N >= M:
    print(0)
else:
    print(factorial_mod(N,M))

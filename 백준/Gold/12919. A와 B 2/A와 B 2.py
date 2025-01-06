import sys

sys.setrecursionlimit(10 ** 6)

S = input().strip()
T = input().strip()


def reverse_remove(s):
    s = list(s)
    s.reverse()
    s = s[:-1]
    return ''.join(s)


def check(a, b):
    if len(str(a)) > len(str(b)):
        return False
    if a == b:
        return True
    if b[0] == 'B':
        if check(a, reverse_remove(b)):
            return True
    if b[-1] == 'A':
        if check(a, b[:-1]):
            return True
    return False


if check(S, T):
    print(1)
else:
    print(0)

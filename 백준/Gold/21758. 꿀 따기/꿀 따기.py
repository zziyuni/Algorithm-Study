import sys
from itertools import accumulate

input = sys.stdin.readline

n = int(input())

honey = list(map(int, input().split()))

honey_sum = list(accumulate(honey))


def left_pot():
    ans = honey_sum[n - 1] - honey[n - 1]
    pot = 0
    bee = n - 1
    tmp = honey_sum[n - 1] - honey[n - 1]
    for i in range(pot + 1, bee):
        ans = max(ans, tmp + honey_sum[i - 1] - honey[i])
    return ans


def right_pot():
    ans = honey_sum[n - 1] - honey[0]
    pot = n - 1
    bee = 0
    tmp = honey_sum[n - 1] - honey[0]
    for i in range(bee + 1, pot):
        ans = max(ans, tmp + honey_sum[pot] - honey_sum[i]-honey[i])
    return ans


def middle_pot():
    bee1 = 0
    bee2 = n - 1
    ans = 0
    tmp = 0
    if bee1 + 1 == bee2 - 1:
        return honey[bee1 + 1] * 2
    for i in range(bee1 + 1, bee2):
        ans = max(tmp + honey_sum[i] - honey[0] + honey_sum[bee2 - 1] - honey_sum[i - 1], ans)
    return ans


a = left_pot()
b = right_pot()
c = middle_pot()

print(max(a, b, c))

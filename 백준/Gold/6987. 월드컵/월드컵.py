import sys
from itertools import combinations

input = sys.stdin.readline


def check_possible(cnt, case):
    if cnt == 15:
        return all(x == 0 for x in case)

    c1, c2 = pairs[cnt]
    if case[3 * (c1 - 1)] > 0 and case[3 * (c2 - 1) + 2] > 0:
        case[3 * (c1 - 1)] -= 1
        case[3 * (c2 - 1) + 2] -= 1
        if check_possible(cnt + 1, case):
            return True
        case[3 * (c1 - 1)] += 1
        case[3 * (c2 - 1) + 2] += 1
    if case[3 * (c1 - 1) + 2] > 0 and case[3 * (c2 - 1)] > 0:
        case[3 * (c1 - 1) + 2] -= 1
        case[3 * (c2 - 1)] -= 1
        if check_possible(cnt + 1, case):
            return True
        case[3 * (c1 - 1) + 2] += 1
        case[3 * (c2 - 1)] += 1
    if case[3 * (c1 - 1) + 1] > 0 and case[3 * (c2 - 1) + 1] > 0:
        case[3 * (c1 - 1) + 1] -= 1
        case[3 * (c2 - 1) + 1] -= 1
        if check_possible(cnt + 1, case):
            return True
        case[3 * (c1 - 1) + 1] += 1
        case[3 * (c2 - 1) + 1] += 1
    return False


answer = []
cases = list(list(map(int, input().split())) for _ in range(4))
pairs = list(combinations(range(6), 2))
for case in cases:
    if sum(case) != 30:
        answer.append(0)
        continue
    answer.append(1 if check_possible(0, case[:]) else 0)

print(*answer)

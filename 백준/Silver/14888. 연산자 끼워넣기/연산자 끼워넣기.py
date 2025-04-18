import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

min_val = int(1e9)
max_val = -int(1e9)


def backtracking(val, cnt, opr):
    global min_val, max_val
    if cnt == N - 1:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    if opr[0] > 0:
        opr[0] -= 1
        backtracking(val + A[cnt + 1], cnt + 1, opr)
        opr[0] += 1
    if opr[1] > 0:
        opr[1] -= 1
        backtracking(val - A[cnt + 1], cnt + 1, opr)
        opr[1] += 1
    if opr[2] > 0:
        opr[2] -= 1
        backtracking(val * A[cnt + 1], cnt + 1, opr)
        opr[2] += 1
    if opr[3] > 0:
        opr[3] -= 1
        if val < 0:
            backtracking(-(-val // A[cnt + 1]), cnt + 1, opr)
        else:
            backtracking(val // A[cnt + 1], cnt + 1, opr)
        opr[3] += 1


N = int(input())
A = list(map(int, input().split()))
operations = list(map(int, input().split()))
backtracking(A[0], 0, operations)
print(max_val)
print(min_val)

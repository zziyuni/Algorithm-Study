import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)


def backtracking(pos, selected, ability):
    global answer
    if pos == 11:
        answer = max(ability, answer)
        return
    for player in range(11):
        if not selected[player] and s[player][pos] != 0:
            selected[player] = True
            backtracking(pos + 1, selected, ability + s[player][pos])
            selected[player] = False


C = int(input())

for _ in range(C):
    answer = 0
    s = list(list(map(int, input().split())) for _ in range(11))
    positions = [False] * 11
    backtracking(0, positions, 0)
    print(answer)

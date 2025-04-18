import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, k = map(int, input().split())

subjects = list(list(map(int, input().split())) for _ in range(n))


def backtracking(s, total_hour):
    global answer
    if total_hour == k:
        answer += 1
        return
    for i in range(s, n):
        weekdays, start, end = subjects[i]
        flag = False
        if weekdays == 5 or total_hour + end - start + 1 > k:
            continue
        for j in range(start, end + 1):
            if time_table[weekdays][j] != 0:
                flag = True
                break
        if flag:
            continue
        for j in range(start, end + 1):
            time_table[weekdays][j] = 1
        backtracking(i + 1, total_hour + end - start + 1)
        for j in range(start, end + 1):
            time_table[weekdays][j] = 0


answer = 0

time_table = [[0] * 11 for _ in range(6)]
backtracking(0, 0)
print(answer)

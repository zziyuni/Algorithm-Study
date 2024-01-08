import sys

input = sys.stdin.readline

k = int(input())

for i in range(k):
    arr = []
    score = list(map(int, input().split()))
    n = score.pop(0)
    score.sort()

    for j in range(n - 1):
        arr.append(score[j + 1] - score[j])

    print("Class", i + 1)
    print("Max ", max(score), ", Min ", min(score), ", Largest gap ", max(arr), sep='')

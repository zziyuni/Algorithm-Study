import sys

input = sys.stdin.readline

N = int(input())
count_scores = dict()

for _ in range(N):
    s = int(input())
    if s not in count_scores:
        count_scores[s] = 1
    else:
        count_scores[s] += 1

scores = list(count_scores.keys())
scores.sort()
answer = 0
max_val = scores[-1] + 1

minus = 0
for i in range(len(scores) - 1, -1, -1):
    if scores[i] + N >= max_val:
        answer += count_scores[scores[i]]
    else:
        break
    minus += count_scores[scores[i]]
    max_val = max(max_val, scores[i] + minus)

print(answer)

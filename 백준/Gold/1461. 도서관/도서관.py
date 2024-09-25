import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pos = list(map(int, input().split()))
positives = [x for x in pos if x > 0]
negatives = [abs(x) for x in pos if x < 0]
positives.sort(reverse=True)
negatives.sort(reverse=True)


ans = 0

for i in range(0, len(positives), M):
    ans += positives[i]*2
for i in range(0, len(negatives), M):
    ans += negatives[i]*2


print(ans-max(max(positives) if positives else 0, max(negatives) if negatives else 0))
